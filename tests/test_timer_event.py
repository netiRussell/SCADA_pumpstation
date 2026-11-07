from pathlib import Path

def test_timer_calls_pump_sim_tick():
    timer_file = (
        Path(__file__).resolve().parents[1]
        / "src/ignition/timer_event.py"
    )

    code = timer_file.read_text()

    assert "pump_sim.tick()" in code, (
        "Regression failed: pump_sim.tick() is missing!"
    )
