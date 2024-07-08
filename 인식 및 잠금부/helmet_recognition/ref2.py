import torch
import cv2
import numpy as np

# Load the model
model = torch.hub.load('ultralytics/yolov5', 'yolov5s', pretrained=True)

# Initialize the webcam
cap = cv2.VideoCapture(0)  # Use the 0th camera device. Change the index to use a different camera.

# Set the desired frame width and height for faster processing
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 320)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 240)

while cap.isOpened():
    ret, frame = cap.read()  # Capture frame
    if not ret:
        break

    # Resize the frame to a smaller size for faster processing
    resized_frame = cv2.resize(frame, (320, 240))

    # Perform object detection using YOLOv5 model
    results = model(resized_frame)

    # Draw detection results on the image
    for det in results.xyxy[0]:  # Coordinates in xyxy format
        x1, y1, x2, y2, conf, cls = det
        label = f'{results.names[int(cls)]} {conf:.2f}'
        # Draw rectangle
        cv2.rectangle(resized_frame, (int(x1), int(y1)), (int(x2), int(y2)), (255, 0, 0), 2)
        # Draw label
        cv2.putText(resized_frame, label, (int(x1), int(y1) - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (255, 0, 0), 2)

    # Display the result on the screen
    cv2.imshow('YOLOv5 Real-time Object Detection', resized_frame)

    # Press 'q' key to exit the loop
    if cv2.waitKey(100000000) & 0xFF == ord('q'):
        break

# Release the webcam and close all windows
cap.release()
cv2.destroyAllWindows()
