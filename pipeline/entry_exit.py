import cv2
import supervision as sv
from ultralytics import YOLO

# -------------------------
# Configuration
# -------------------------

VIDEO_PATH = r"D:\PurplleChallenge\data\CAM 5.mp4"

ENTRY_LINE_Y = 500

# -------------------------
# Models
# -------------------------

model = YOLO("yolov8n.pt")

tracker = sv.ByteTrack()

# -------------------------
# Storage
# -------------------------

previous_positions = {}

entered_ids = set()

exited_ids = set()

# -------------------------
# Video
# -------------------------

cap = cv2.VideoCapture(VIDEO_PATH)

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

    # Draw entry line
    cv2.line(
        frame,
        (0, ENTRY_LINE_Y),
        (1920, ENTRY_LINE_Y),
        (0, 0, 255),
        3
    )

    if detections.tracker_id is not None:

        for i in range(len(detections)):

            x1, y1, x2, y2 = map(
                int,
                detections.xyxy[i]
            )

            track_id = int(
                detections.tracker_id[i]
            )

            # center point
            center_x = int(
                (x1 + x2) / 2
            )

            center_y = int(
                (y1 + y2) / 2
            )

            # draw box
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
                (255, 0, 0),
                -1
            )

            cv2.putText(
                frame,
                f"ID:{track_id}",
                (x1, y1 - 10),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.7,
                (0, 255, 255),
                2
            )

            # first time seen
            if track_id not in previous_positions:

                previous_positions[
                    track_id
                ] = center_y

            previous_y = previous_positions[
                track_id
            ]

            # ENTRY
            if (
                previous_y < ENTRY_LINE_Y
                and
                center_y >= ENTRY_LINE_Y
            ):

                if track_id not in entered_ids:

                    save_event(
                                visitor_id,
                                "ENTRY"
                                )

                    entered_ids.add(
                        track_id
                    )

            # EXIT
            if (
                previous_y > ENTRY_LINE_Y
                and
                center_y <= ENTRY_LINE_Y
            ):

                if track_id not in exited_ids:

                    save_event(
                         visitor_id,
                         "EXIT"
                            )

                    exited_ids.add(
                        track_id
                    )

            # update latest position
            previous_positions[
                track_id
            ] = center_y

    cv2.imshow(
        "Entry Exit Detection",
        frame
    )

    key = cv2.waitKey(1)

    if key == 27:
        break

cap.release()
cv2.destroyAllWindows()