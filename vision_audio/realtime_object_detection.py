# import tensorflow as tf
# import cv2
# import numpy as np

# model = tf.saved_model.load("ssd_mobilenet_v2/saved_model")

# def detect_objects(frame):
#     input_tensor = tf.convert_to_tensor(frame)
#     input_tensor = input_tensor[tf.newaxis, ...]
#     detections = model(input_tensor)
#     return detections



import os
import tensorflow as tf
import cv2
import numpy as np

# Disable GPU for TensorFlow
os.environ['CUDA_VISIBLE_DEVICES'] = '-1'

# Load the pre-trained model
model_path = "ssd_mobilenet_v2_fpnlite_320x320_coco17_tpu-8/saved_model"
model = tf.saved_model.load(model_path)

# Function to detect objects and draw bounding boxes
def detect_objects(frame):
    height, width, _ = frame.shape
    input_tensor = tf.convert_to_tensor(frame)
    input_tensor = input_tensor[tf.newaxis, ...]
    detections = model(input_tensor)

    boxes = detections['detection_boxes'][0].numpy()
    classes = detections['detection_classes'][0].numpy().astype(int)
    scores = detections['detection_scores'][0].numpy()

    for i in range(len(scores)):
        if scores[i] > 0.5:  # Confidence threshold
            box = boxes[i] * [height, width, height, width]
            y_min, x_min, y_max, x_max = box.astype(int)
            label = f"Class {classes[i]}: {scores[i]:.2f}"
            cv2.rectangle(frame, (x_min, y_min), (x_max, y_max), (0, 255, 0), 2)
            cv2.putText(frame, label, (x_min, y_min - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
    return frame

# Open webcam
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Error: Cannot access the camera.")
    exit()

while True:
    ret, frame = cap.read()
    if not ret:
        print("Error: Cannot read frame from the camera.")
        break

    # Detect objects in the frame
    frame = detect_objects(frame)

    # Display the frame
    cv2.imshow("Object Detection", frame)

    # Break the loop on 'q' key press
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
