from time import time

zone_entry_time = {}

dwell_generated = set()

def check_dwell(
    track_id,
    zone_name
):

    key = (
        track_id,
        zone_name
    )

    if key not in zone_entry_time:

        zone_entry_time[key] = time()

        return

    dwell_seconds = (
        time()
        -
        zone_entry_time[key]
    )

    if (
        dwell_seconds >= 5
        and
        key not in dwell_generated
    ):

        print(
            f"ZONE_DWELL "
            f"ID:{track_id} "
            f"{zone_name}"
        )

        dwell_generated.add(
            key
        )