import json
from pathlib import Path

EVENTS_FILE = Path("outputs/events.jsonl")


def load_events():

    events = []

    if not EVENTS_FILE.exists():

        print("events.jsonl not found")

        return events

    with open(
        EVENTS_FILE,
        "r",
        encoding="utf-8"
    ) as f:

        for line in f:

            line = line.strip()

            if not line:
                continue

            try:

                event = json.loads(line)

                events.append(event)

            except Exception as e:

                print(
                    f"Skipping bad line: {e}"
                )

    return events