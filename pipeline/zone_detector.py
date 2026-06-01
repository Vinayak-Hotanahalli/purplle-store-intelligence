import cv2
import supervision as sv
from ultralytics import YOLO
from dwell_detector import check_dwell

VIDEO_PATH = r"D:\PurplleChallenge\data\CAM 5.mp4"

# -------------------------
# Load Model & Tracker
# -------------------------

model = YOLO("yolov8n.pt")
tracker = sv.ByteTrack()

# -------------------------
# Video
# -------------------------

cap = cv2.VideoCapture(VIDEO_PATH)

# -------------------------
# Zones
# -------------------------

ZONES = {

    "ENTRANCE": (
        0,
        0,
        350,
        1080
    ),

    "FOH": (
        350,
        250,
        1500,
        900
    ),

    "MAKEUP": (
        700,
        350,
        1200,
        750
    ),

    "SHELF_TOP": (
        250,
        0,
        1700,
        250
    ),

    "BILLING": (
        1500,
        0,
        1920,
        1080
    )
}

# -------------------------
# Storage
# -------------------------

visitor_zone = {}

# -------------------------
# Main Loop
# -------------------------

while True:

    success, frame = cap.read()

    if not success:
        break

    results = model(
        frame,
        conf=0.25,
        verbose=False
    )

    detections = sv.Detections.from_ultralytics(
        results[0]
    )

    detections = tracker.update_with_detections(
        detections
    )

    # -------------------------
    # Draw Zones
    # -------------------------

    for zone_name, (
        x1,
        y1,
        x2,
        y2
    ) in ZONES.items():

        cv2.rectangle(
            frame,
            (x1, y1),
            (x2, y2),
            (255, 0, 0),
            2
        )

        cv2.putText(
            frame,
            zone_name,
            (x1, y1 + 30),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.7,
            (255, 0, 0),
            2
        )

    # -------------------------
    # Process Detections
    # -------------------------

    if detections.tracker_id is not None:

        for i in range(len(detections)):

            x1, y1, x2, y2 = map(
                int,
                detections.xyxy[i]
            )

            track_id = int(
                detections.tracker_id[i]
            )

            center_x = int(
                (x1 + x2) / 2
            )

            center_y = int(
                (y1 + y2) / 2
            )

            current_zone = None

            # -------------------------
            # Find Current Zone
            # -------------------------

            for zone_name, (
                zx1,
                zy1,
                zx2,
                zy2
            ) in ZONES.items():

                if (
                    zx1 <= center_x <= zx2
                    and
                    zy1 <= center_y <= zy2
                ):

                    current_zone = zone_name
                    break

            # -------------------------
            # Dwell Detection
            # -------------------------

            if current_zone:

                check_dwell(
                    track_id,
                    current_zone
                )

            # -------------------------
            # First Time Seen
            # -------------------------

            if track_id not in visitor_zone:

                visitor_zone[
                    track_id
                ] = current_zone

            previous_zone = (
                visitor_zone[
                    track_id
                ]
            )

            # -------------------------
            # Zone Change
            # -------------------------

            if (
                current_zone
                and
                current_zone != previous_zone
            ):

                print(
                    f"ZONE_ENTER "
                    f"ID:{track_id} "
                    f"{current_zone}"
                )

                visitor_zone[
                    track_id
                ] = current_zone

            # -------------------------
            # Draw Detection
            # -------------------------

            cv2.rectangle(
                frame,
                (x1, y1),
                (x2, y2),
                (0, 255, 0),
                2
            )

            cv2.circle(
                frame,
                (center_x, center_y),
                5,
                (0, 0, 255),
                -1
            )

            cv2.putText(
                frame,
                f"ID:{track_id}",
                (x1, y1 - 10),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.6,
                (0, 255, 255),
                2
            )

    # -------------------------
    # Show Frame
    # -------------------------

    cv2.imshow(
        "Zone Detector",
        frame
    )

    key = cv2.waitKey(1)

    if key == 27:
        break

# -------------------------
# Cleanup
# -------------------------

cap.release()
cv2.destroyAllWindows()