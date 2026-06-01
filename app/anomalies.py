from app.load_events import load_events

def get_anomalies():

    events = load_events()

    entries = 0
    exits = 0
    dwell_events = 0

    for event in events:

        event_type = event.get(
            "event_type",
            ""
        )

        if event_type == "ENTRY":
            entries += 1

        elif event_type == "EXIT":
            exits += 1

        elif event_type == "ZONE_DWELL":
            dwell_events += 1

    anomalies = []

    if entries == 0:

        anomalies.append({

            "type": "LOW_FOOTFALL",

            "message":
            "No visitors detected"
        })

    if exits > entries:

        anomalies.append({

            "type": "TRACKING_ISSUE",

            "message":
            "Exits exceed entries"
        })

    if dwell_events == 0:

        anomalies.append({

            "type": "LOW_ENGAGEMENT",

            "message":
            "No dwell events detected"
        })

    return anomalies