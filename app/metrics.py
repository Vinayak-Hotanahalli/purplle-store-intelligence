from app.load_events import load_events

def get_metrics():

    events = load_events()

    visitors = set()

    entries = 0
    exits = 0
    dwell_events = 0

    for event in events:

        visitors.add(
            event["visitor_id"]
        )

        if event["event_type"] == "ENTRY":
            entries += 1

        elif event["event_type"] == "EXIT":
            exits += 1

        elif event["event_type"] == "ZONE_DWELL":
            dwell_events += 1

    return {

        "unique_visitors": len(visitors),

        "entries": entries,

        "exits": exits,

        "dwell_events": dwell_events
    }