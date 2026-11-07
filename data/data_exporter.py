import sqlite3
import csv
import time
from pathlib import Path

DB_PATH = Path("/usr/local/ignition/data/local/quickstart/samplequickstart.db")
OUTPUT = Path("./data/tank_level_history.csv")

# Last 24 hours (Unix milliseconds)
cutoff = int((time.time() - 24 * 3600) * 1000)

query = """
SELECT
    d.t_stamp AS timestamp_ms,
    d.floatvalue AS level_pct,
    d.dataintegrity AS quality_code
FROM sqlt_data_1_2026_11 AS d
JOIN sqlth_te AS t
    ON d.tagid = t.id
WHERE t.tagpath LIKE ?
    AND d.floatvalue IS NOT NULL
    AND d.t_stamp >= ?
ORDER BY d.t_stamp ASC
"""

# Open existing database in read-only mode
db_uri = DB_PATH.resolve().as_uri() + "?mode=ro"

if __name__ == "__main__":
    with sqlite3.connect(db_uri, uri=True, timeout=3) as conn:
        cursor = conn.execute(
            query,
            ("%PumpStation/Process/TankLevelPct", cutoff)
        )

        OUTPUT.parent.mkdir(parents=True, exist_ok=True)

        with OUTPUT.open("w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow([
                "timestamp_ms",
                "level_pct",
                "quality_code"
            ])
            writer.writerows(cursor)

    print("Export completed:", OUTPUT)