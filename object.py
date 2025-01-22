# # # import cv2
# # # import numpy as np

# # # # Load YOLO model and the pre-trained weights
# # # config_path = "yolov4.cfg"  # Path to YOLO config file
# # # weights_path = "yolov4.weights"  # Path to YOLO pre-trained weights file
# # # names_path = "coco.names"  # Path to the COCO names file

# # # # Load class names
# # # with open(names_path, "r") as f:
# # #     class_names = f.read().strip().split("\n")

# # # # Load YOLO network
# # # net = cv2.dnn.readNet(weights_path, config_path)
# # # net.setPreferableBackend(cv2.dnn.DNN_BACKEND_CUDA)
# # # net.setPreferableTarget(cv2.dnn.DNN_TARGET_CUDA)

# # # # Define input/output layer
# # # output_layers = net.getUnconnectedOutLayersNames()

# # # # Function to detect objects and draw labels
# # # def detect_objects(frame):
# # #     height, width = frame.shape[:2]
# # #     # Create a blob from the input image
# # #     blob = cv2.dnn.blobFromImage(frame, 1 / 255.0, (416, 416), swapRB=True, crop=False)
# # #     net.setInput(blob)
# # #     detections = net.forward(output_layers)

# # #     boxes, confidences, class_ids = [], [], []

# # #     # Process detections
# # #     for output in detections:
# # #         for detection in output:
# # #             scores = detection[5:]
# # #             class_id = np.argmax(scores)
# # #             confidence = scores[class_id]
# # #             if confidence > 0.5:
# # #                 center_x, center_y, w, h = (detection[0:4] * [width, height, width, height]).astype("int")
# # #                 x = int(center_x - w / 2)
# # #                 y = int(center_y - h / 2)

# # #                 boxes.append([x, y, int(w), int(h)])
# # #                 confidences.append(float(confidence))
# # #                 class_ids.append(class_id)

# # #     # Apply Non-Maximum Suppression (NMS)
# # #     indices = cv2.dnn.NMSBoxes(boxes, confidences, 0.5, 0.4)

# # #     if len(indices) > 0:  # Ensure indices is not empty
# # #         for i in indices.flatten():
# # #             x, y, w, h = boxes[i]
# # #             label = str(class_names[class_ids[i]])
# # #             confidence = confidences[i]

# # #             # Draw bounding box and label on the frame
# # #             cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
# # #             cv2.putText(frame, f"{label}: {confidence:.2f}", (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

# # #     return frame

# # # # Open webcam
# # # cap = cv2.VideoCapture(0)

# # # if not cap.isOpened():
# # #     print("Error: Cannot access the camera.")
# # #     exit()

# # # while True:
# # #     ret, frame = cap.read()
# # #     if not ret:
# # #         print("Error: Cannot read frame from the camera.")
# # #         break

# # #     # Detect objects in the frame
# # #     frame = detect_objects(frame)

# # #     # Display the frame
# # #     cv2.imshow("Object Detection", frame)

# # #     # Break the loop on 'q' key press
# # #     if cv2.waitKey(1) & 0xFF == ord('q'):
# # #         break

# # # cap.release()
# # # cv2.destroyAllWindows()



# # import cv2
# # import numpy as np
# # from threading import Thread

# # # Load YOLO model and the pre-trained weights
# # config_path = "yolov4-tiny.cfg"  # Path to YOLO tiny config file
# # weights_path = "yolov4-tiny.weights"  # Path to YOLO tiny weights file
# # names_path = "coco.names"  # Path to the COCO names file

# # # Load class names
# # with open(names_path, "r") as f:
# #     class_names = f.read().strip().split("\n")

# # # Load YOLO network
# # net = cv2.dnn.readNet(weights_path, config_path)
# # net.setPreferableBackend(cv2.dnn.DNN_BACKEND_OPENCV)
# # net.setPreferableTarget(cv2.dnn.DNN_TARGET_CPU)

# # # Define input/output layer
# # output_layers = net.getUnconnectedOutLayersNames()

# # # Function to detect objects and draw labels
# # def detect_objects(frame):
# #     height, width = frame.shape[:2]
# #     # Create a blob from the input image
# #     blob = cv2.dnn.blobFromImage(frame, 1 / 255.0, (320, 320), swapRB=True, crop=False)
# #     net.setInput(blob)
# #     detections = net.forward(output_layers)

# #     boxes, confidences, class_ids = [], [], []

# #     # Process detections
# #     for output in detections:
# #         for detection in output:
# #             scores = detection[5:]
# #             class_id = np.argmax(scores)
# #             confidence = scores[class_id]
# #             if confidence > 0.3:  # Lower confidence threshold for more detections
# #                 center_x, center_y, w, h = (detection[0:4] * [width, height, width, height]).astype("int")
# #                 x = int(center_x - w / 2)
# #                 y = int(center_y - h / 2)

# #                 boxes.append([x, y, int(w), int(h)])
# #                 confidences.append(float(confidence))
# #                 class_ids.append(class_id)

# #     # Apply Non-Maximum Suppression (NMS)
# #     indices = cv2.dnn.NMSBoxes(boxes, confidences, 0.5, 0.4)

# #     if len(indices) > 0:  # Ensure indices is not empty
# #         for i in indices.flatten():
# #             x, y, w, h = boxes[i]
# #             label = str(class_names[class_ids[i]])
# #             confidence = confidences[i]
    
# #             # Draw bounding box and label on the frame
# #             cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
# #             cv2.putText(frame, f"{label}: {confidence:.2f}", (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

# #     return frame

# # # Threaded video capture class
# # class VideoCaptureAsync:
# #     def __init__(self, src=0):
# #         self.capture = cv2.VideoCapture(src)
# #         self.ret = False
# #         self.frame = None
# #         self.running = True

# #     def start(self):
# #         Thread(target=self.update, daemon=True).start()
# #         return self

# #     def update(self):
# #         while self.running:
# #             self.ret, self.frame = self.capture.read()

# #     def read(self):
# #         return self.ret, self.frame

# #     def stop(self):
# #         self.running = False
# #         self.capture.release()

# # # Open webcam
# # cap = VideoCaptureAsync(0).start()

# # if not cap.capture.isOpened():
# #     print("Error: Cannot access the camera.")
# #     exit()

# # frame_id = 0
# # while True:
# #     ret, frame = cap.read()
# #     if not ret:
# #         print("Error: Cannot read frame from the camera.")
# #         break

# #     # Skip frames for faster processing
# #     if frame_id % 2 == 0:
# #         frame = detect_objects(frame)

# #     # Display the frame
# #     if frame_id % 2 == 0:
# #         cv2.imshow("Object Detection", frame)

# #     frame_id += 1

# #     # Break the loop on 'q' key press
# #     if cv2.waitKey(1) & 0xFF == ord('q'):
# #         break

# # cap.stop()
# # cv2.destroyAllWindows()




# import cv2
# import numpy as np

# # Load YOLO model and the pre-trained weights
# config_path = "yolov4-tiny.cfg"  # Path to YOLO tiny config file
# weights_path = "yolov4-tiny.weights"  # Path to YOLO tiny weights file
# names_path = "coco.names"  # Path to the COCO names file

# # Load class names
# with open(names_path, "r") as f:
#     class_names = f.read().strip().split("\n")

# # Load YOLO network
# net = cv2.dnn.readNet(weights_path, config_path)
# net.setPreferableBackend(cv2.dnn.DNN_BACKEND_OPENCV)
# net.setPreferableTarget(cv2.dnn.DNN_TARGET_CPU)

# # Define input/output layer
# output_layers = net.getUnconnectedOutLayersNames()

# # Function to detect objects and draw labels
# def detect_objects(frame):
#     height, width = frame.shape[:2]
#     # Create a blob from the input image
#     blob = cv2.dnn.blobFromImage(frame, 1 / 255.0, (320, 320), swapRB=True, crop=False)
#     net.setInput(blob)
#     detections = net.forward(output_layers)

#     boxes, confidences, class_ids = [], [], []

#     # Process detections
#     for output in detections:
#         for detection in output:
#             scores = detection[5:]
#             class_id = np.argmax(scores)
#             confidence = scores[class_id]
#             if confidence > 0.3:  # Lower confidence threshold for more detections
#                 center_x, center_y, w, h = (detection[0:4] * [width, height, width, height]).astype("int")
#                 x = int(center_x - w / 2)
#                 y = int(center_y - h / 2)

#                 boxes.append([x, y, int(w), int(h)])
#                 confidences.append(float(confidence))
#                 class_ids.append(class_id)

#     # Apply Non-Maximum Suppression (NMS)
#     indices = cv2.dnn.NMSBoxes(boxes, confidences, 0.5, 0.4)

#     if len(indices) > 0:  # Ensure indices is not empty
#         for i in indices.flatten():
#             x, y, w, h = boxes[i]
#             label = str(class_names[class_ids[i]])
#             confidence = confidences[i]

#             # Draw bounding box and label on the frame
#             cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
#             cv2.putText(frame, f"{label}: {confidence:.2f}", (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

#     return frame

# # Open webcam
# cap = cv2.VideoCapture(0, cv2.CAP_V4L2)  # Explicitly use V4L2 backend

# if not cap.isOpened():
#     print("Error: Cannot access the camera.")
#     exit()

# while True:
#     ret, frame = cap.read()
#     if not ret:
#         print("Error: Cannot read frame from the camera.")
#         break

#     # Detect objects in the frame
#     frame = detect_objects(frame)

#     # Display the frame
#     cv2.imshow("Object Detection", frame)

#     # Break the loop on 'q' key press
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break

# cap.release()
# cv2.destroyAllWindows()




import cv2
import numpy as np

# Load YOLO model and the pre-trained weights
config_path = "yolov4.cfg"  # Path to full YOLO config file
weights_path = "yolov4.weights"  # Path to full YOLO weights file
names_path = "coco.names"  # Path to the COCO names file

# Load class names
with open(names_path, "r") as f:
    class_names = f.read().strip().split("\n")

# Load YOLO network
net = cv2.dnn.readNet(weights_path, config_path)
net.setPreferableBackend(cv2.dnn.DNN_BACKEND_OPENCV)
net.setPreferableTarget(cv2.dnn.DNN_TARGET_CPU)

# Define input/output layer
output_layers = net.getUnconnectedOutLayersNames()

# Function to detect objects and draw labels
def detect_objects(frame):
    height, width = frame.shape[:2]
    # Create a blob from the input image
    blob = cv2.dnn.blobFromImage(frame, 1 / 255.0, (608, 608), swapRB=True, crop=False)
    net.setInput(blob)
    detections = net.forward(output_layers)

    boxes, confidences, class_ids = [], [], []

    # Process detections
    for output in detections:
        for detection in output:
            scores = detection[5:]
            class_id = np.argmax(scores)
            confidence = scores[class_id]
            if confidence > 0.25:  # Lower confidence threshold for more detections
                center_x, center_y, w, h = (detection[0:4] * [width, height, width, height]).astype("int")
                x = int(center_x - w / 2)
                y = int(center_y - h / 2)

                boxes.append([x, y, int(w), int(h)])
                confidences.append(float(confidence))
                class_ids.append(class_id)

    # Apply Non-Maximum Suppression (NMS)
    indices = cv2.dnn.NMSBoxes(boxes, confidences, 0.3, 0.4)

    if len(indices) > 0:  # Ensure indices is not empty
        for i in indices.flatten():
            x, y, w, h = boxes[i]
            label = str(class_names[class_ids[i]])
            confidence = confidences[i]

            # Draw bounding box and label on the frame
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
            cv2.putText(frame, f"{label}: {confidence:.2f}", (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

    return frame

# Open webcam
cap = cv2.VideoCapture(0, cv2.CAP_V4L2)  # Explicitly use V4L2 backend

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
