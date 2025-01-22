import tensorflow as tf
from tensorflow.keras.applications import MobileNetV2
from tensorflow.keras.applications.mobilenet_v2 import preprocess_input, decode_predictions
from tensorflow.keras.preprocessing.image import load_img, img_to_array

# Load pre-trained model
model = MobileNetV2(weights="imagenet")

# Load and preprocess image
image_path = "ali.jpg"  # Replace with a local image path
img = load_img(image_path, target_size=(224, 224))
img_array = img_to_array(img)
img_array = preprocess_input(img_array)
img_array = tf.expand_dims(img_array, 0)

# Predict
predictions = model.predict(img_array)
decoded_predictions = decode_predictions(predictions, top=3)[0]

# Print predictions
print("Predictions:")
for pred in decoded_predictions:
    print(f"{pred[1]}: {pred[2]*100:.2f}%")
