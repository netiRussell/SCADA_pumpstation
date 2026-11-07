import csv
from pathlib import Path
import pytest

DATA_FILE = (
    Path(__file__).resolve().parents[1]
    / "data"
    / "tank_level_history.csv"
)

@pytest.fixture(scope="module")
def samples():
    if not DATA_FILE.exists():
        pytest.fail("Export historian CSV before testing")

    with DATA_FILE.open(newline="") as file:
        return list(csv.DictReader(file))


def test_historian_contains_data(samples):
    assert len(samples) > 0, "No historian samples found"


def test_tank_levels_within_limits(samples):
    for sample in samples:
        level = float(sample["level_pct"])
        assert 0 <= level <= 100


def test_all_samples_have_good_quality(samples):
    for sample in samples:
        assert int(sample["quality_code"]) == 192


def test_timestamps_are_ordered(samples):
    times = [int(row["timestamp_ms"]) for row in samples]
    assert times == sorted(times)
