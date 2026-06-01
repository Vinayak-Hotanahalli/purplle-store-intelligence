import json

from event_generator import create_event

event = create_event(
    visitor_id="VIS_0001",
    event_type="ENTRY"
)

with open(
    "outputs/events.jsonl",
    "a"
) as f:

    f.write(
        json.dumps(event)
        + "\n"
    )

print(event)