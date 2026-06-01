import uuid
from datetime import datetime


def create_event(
    visitor_id,
    event_type,
    store_id="ST1008",
    camera_id="CAM5"
):

    return {
        "event_id": str(uuid.uuid4()),
        "store_id": store_id,
        "camera_id": camera_id,
        "visitor_id": visitor_id,
        "event_type": event_type,
        "timestamp": datetime.utcnow().isoformat(),
        "zone_id": None,
        "dwell_ms": 0,
        "is_staff": False,
        "confidence": 1.0,
        "metadata": {}
    }