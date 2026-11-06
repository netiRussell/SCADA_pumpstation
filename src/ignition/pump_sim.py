"""PumpStationSCADA process simulator (Ignition 8.3 / Jython 2.7 compatible).

Only `tick()` depends on Ignition. `advance()` is deterministic and
can be unit-tested with a standard Python interpreter.
No real hardware or safety-rated controls are connected.
"""

CAPACITY_L = 100.0
PUMP_FLOW_LPM = 60.0
DEMAND_FLOW_LPM = 24.0
AUTO_START_PCT = 35.0
AUTO_STOP_PCT = 75.0
HIGH_HIGH_PCT = 95.0
TRIP_RESET_BELOW_PCT = 85.0
TAG_ROOT = '[default]PumpStation/'


def clamp(value, lower, upper):
    return max(lower, min(upper, value))


def advance(level_pct, was_running, auto_mode, manual_demand,
            trip_latched, reset_request, runtime_sec, dt_sec=1.0):
    """Compute one simulated time step; outputs commands AND process state.

    Tank level is a percentage; water flows are in liters per minute.
    A high-high trip is latched and must be explicitly reset below 85%.
    """
    if dt_sec <= 0:
        raise ValueError('dt_sec must be positive')

    level = clamp(float(level_pct), 0.0, 100.0)
    trip = bool(trip_latched) or level >= HIGH_HIGH_PCT
    if bool(reset_request) and level < TRIP_RESET_BELOW_PCT:
        trip = False

    if trip:
        running = False
    elif bool(auto_mode):
        if level <= AUTO_START_PCT:
            running = True
        elif level >= AUTO_STOP_PCT:
            running = False
        else:
            running = bool(was_running)
    else:
        running = bool(manual_demand)

    inlet = PUMP_FLOW_LPM if running else 0.0
    outlet = DEMAND_FLOW_LPM if level > 0.0 else 0.0
    delta_pct = (inlet - outlet) * dt_sec / 60.0 / CAPACITY_L * 100.0
    next_level = clamp(level + delta_pct, 0.0, 100.0)

    # Simulated protective trip on attempted high-high crossing.
    if next_level >= HIGH_HIGH_PCT:
        trip = True
        running = False
        inlet = 0.0
        next_level = clamp(
            level - outlet * dt_sec / 60.0 / CAPACITY_L * 100.0,
            0.0, 100.0)

    return {
        'TankLevelPct': round(next_level, 3),
        'PumpRunning': running,
        'InflowLpm': inlet,
        'OutflowLpm': outlet,
        'HighHighTrip': trip,
        'RuntimeSec': int(runtime_sec) + (int(dt_sec) if running else 0),
    }


def tick():
    """Call from a single Gateway Timer Script every 1000 ms."""
    logger = system.util.getLogger('PumpStationSim')
    names = [
        'Simulation/Enabled', 'Commands/AutoMode',
        'Commands/ManualRunDemand', 'Commands/ResetTrip',
        'Process/TankLevelPct', 'Process/PumpRunning',
        'Status/HighHighTrip', 'Process/RuntimeSec',
        'Status/Heartbeat'
    ]
    try:
        readings = system.tag.readBlocking([TAG_ROOT + name for name in names])
        if not all(value.quality.isGood() for value in readings):
            logger.warn('One or more simulator inputs have bad tag quality')
            return
        vals = [value.value for value in readings]
        if not bool(vals[0]):
            return  # Simulation intentionally paused.

        result = advance(
            level_pct=vals[4], was_running=vals[5],
            auto_mode=vals[1], manual_demand=vals[2],
            trip_latched=vals[6], reset_request=vals[3],
            runtime_sec=vals[7], dt_sec=1.0)

        outputs = [
            ('Process/TankLevelPct', result['TankLevelPct']),
            ('Process/PumpRunning', result['PumpRunning']),
            ('Process/InflowLpm', result['InflowLpm']),
            ('Process/OutflowLpm', result['OutflowLpm']),
            ('Process/RuntimeSec', result['RuntimeSec']),
            ('Status/HighHighTrip', result['HighHighTrip']),
            ('Status/Heartbeat', (int(vals[8]) + 1) % 1000000),
        ]
        if bool(vals[3]):
            outputs.append(('Commands/ResetTrip', False))

        quality = system.tag.writeBlocking(
            [TAG_ROOT + name for name, value in outputs],
            [value for name, value in outputs])
        if not all(status.isGood() for status in quality):
            logger.warn('One or more simulator writes failed')
    except Exception as exc:
        logger.error('Simulation tick failed: %s' % exc)
