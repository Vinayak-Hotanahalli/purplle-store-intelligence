import cv2
import supervision as sv
from ultralytics import YOLO

VIDEO_PATH = r"D:\PurplleChallenge\data\CAM 5.mp4"

model = YOLO("yolov8n.pt")

tracker = sv.ByteTrack()

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

    if detections.tracker_id is not None:

        for i in range(len(detections)):

            x1, y1, x2, y2 = map(
                int,
                detections.xyxy[i]
            )

            track_id = int(
                detections.tracker_id[i]
            )

            cv2.rectangle(
                frame,
                (x1, y1),
                (x2, y2),
                (0,255,0),
                2
            )

            cv2.putText(
                frame,
                f"ID:{track_id}",
                (x1, y1 - 10),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.7,
                (0,255,255),
                2
            )

    cv2.imshow(
        "Tracking",
        frame
    )

    key = cv2.waitKey(1)

    if key == 27:
        break

cap.release()
cv2.destroyAllWindows()