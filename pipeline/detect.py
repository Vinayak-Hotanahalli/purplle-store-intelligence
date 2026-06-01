import cv2
from ultralytics import YOLO

VIDEO_PATH = r"D:\PurplleChallenge\data\CAM 5.mp4"

model = YOLO("yolov8n.pt")

cap = cv2.VideoCapture(VIDEO_PATH)

while True:

    success, frame = cap.read()

    if not success:
        break

    results = model(frame)

    for result in results:

        for box in result.boxes:

            cls = int(box.cls[0])

            # class 0 = person
            if cls != 0:
                continue

            x1, y1, x2, y2 = map(
                int,
                box.xyxy[0]
            )

            confidence = float(box.conf[0])

            cv2.rectangle(
                frame,
                (x1, y1),
                (x2, y2),
                (0, 255, 0),
                2
            )

            cv2.putText(
                frame,
                f"{confidence:.2f}",
                (x1, y1 - 10),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.6,
                (0, 255, 0),
                2
            )

    cv2.imshow(
        "Purplle Detection",
        frame
    )

    if cv2.waitKey(1) == 27:
        break

cap.release()
cv2.destroyAllWindows()