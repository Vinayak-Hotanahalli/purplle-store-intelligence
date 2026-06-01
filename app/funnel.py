from app.load_events import load_events

def get_funnel():

    events = load_events()

    entries = 0

    zone_visitors = set()

    billing_visitors = set()

    for event in events:

        event_type = event.get(
            "event_type",
            ""
        )

        visitor_id = event.get(
            "visitor_id",
            ""
        )

        zone_id = event.get(
            "zone_id",
            None
        )

        # Count Entries

        if event_type == "ENTRY":

            entries += 1

        # Zone Visitors

        if event_type in [
            "ZONE_ENTER",
            "ZONE_DWELL"
        ]:

            zone_visitors.add(
                visitor_id
            )

        # Billing Visitors

        if zone_id == "BILLING":

            billing_visitors.add(
                visitor_id
            )

    conversion_rate = 0

    if entries > 0:

        conversion_rate = round(
            (
                len(
                    billing_visitors
                )
                /
                entries
            ) * 100,
            2
        )

    return {

        "entries":
        entries,

        "zone_visitors":
        len(zone_visitors),

        "billing_visitors":
        len(billing_visitors),

        "conversion_rate":
        conversion_rate
    }