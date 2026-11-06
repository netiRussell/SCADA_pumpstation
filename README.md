# PumpStationSCADA

**Industrial pump-station supervisory control and monitoring demo | Ignition 8.1 / Perspective**

## Executive overview
PumpStationSCADA demonstrates a simulated pumping station with a
100-liter tank (TK-101), pump (P-101), operator controls, automatic
level regulation with hysteresis, latched high-high protection,
alarming, and historical trending.

**Simulation only:** No actual PLC, OPC UA field device, electrical
installation, or certified safety system is connected.

## Engineering functions
- Auto start at <=35% and stop at >=75%; state retention between limits.
- Manual pump request, overridden by a latched high-high trip at >=95%.
- Reset interlock requiring level <85%.
- Low (<=20%) and high (>=85%) level alarms, with alarm-status display.
- Live process HMI and time-series historian using Ignition Perspective.
- Deterministic controller model with automated tests.

## Demo
To be added...

## Factory Acceptance Test (FAT)
To be added...

## Validity and Statistics analysis (PyTest and SQL)
To be added...

## Repository map
To be added...
- `path` — description

## Technical limitations
The simulation uses a simplified steady-flow water balance with a
nominal 1-second step. Timer jitter, sensor failure, historian scale,
user permissions, communications-loss response, and actual industrial
PLC integration are not validated. Never connect this code to real
process equipment.
