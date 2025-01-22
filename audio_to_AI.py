# import pyaudio
# import librosa
# import numpy as np
# from sklearn.ensemble import RandomForestClassifier
# from sklearn.preprocessing import StandardScaler
# import joblib

# # Audio recording parameters
# FORMAT = pyaudio.paInt16
# CHANNELS = 1
# RATE = 16000  # Audio sampling rate
# CHUNK = 1024  # Audio chunk size

# # Pretrained model path
# MODEL_PATH = "pretrained_audio_classifier.pkl"

# # Class labels for the model
# LABELS = ["Silence", "Talking", "Music", "Typing", "Background Noise"]

# # Load pretrained model
# try:
#     model = joblib.load(MODEL_PATH)
#     print("Model loaded successfully.")
# except FileNotFoundError:
#     print(f"Error: Pretrained model file not found at {MODEL_PATH}.")
#     exit(1)

# def extract_features(waveform, sr):
#     """
#     Extract audio features using librosa.
#     """
#     # Mel-frequency cepstral coefficients (MFCC)
#     mfccs = librosa.feature.mfcc(y=waveform, sr=sr, n_mfcc=13)
#     # Chroma features
#     chroma = librosa.feature.chroma_stft(y=waveform, sr=sr)
#     # Spectral contrast
#     spectral_contrast = librosa.feature.spectral_contrast(y=waveform, sr=sr)

#     # Combine features into a single array
#     features = np.hstack([
#         np.mean(mfccs, axis=1),
#         np.mean(chroma, axis=1),
#         np.mean(spectral_contrast, axis=1)
#     ])
#     return features

# def classify_audio(audio_data):
#     """
#     Classify audio data into categories.
#     """
#     # Convert audio buffer to waveform
#     waveform = np.frombuffer(audio_data, dtype=np.int16).astype(np.float32) / 32768.0
#     features = extract_features(waveform, RATE)
#     features = features.reshape(1, -1)  # Reshape for the model
#     prediction = model.predict(features)
#     return LABELS[prediction[0]]

# def main():
#     """
#     Main function to capture audio and classify in real-time.
#     """
#     # Initialize PyAudio
#     p = pyaudio.PyAudio()
#     stream = p.open(format=FORMAT, channels=CHANNELS, rate=RATE, input=True, frames_per_buffer=CHUNK)

#     print("Listening for sounds... Press Ctrl+C to stop.")
#     try:
#         while True:
#             # Capture audio chunk
#             audio_data = stream.read(CHUNK, exception_on_overflow=False)
#             # Classify the audio
#             sound_description = classify_audio(audio_data)
#             print(f"\rDetected sound: {sound_description}", end="")
#     except KeyboardInterrupt:
#         print("\nStopping...")
#     finally:
#         stream.stop_stream()
#         stream.close()
#         p.terminate()

# if __name__ == "__main__":
# #     main()
# import os
# os.environ['CUDA_VISIBLE_DEVICES'] = '-1'  # Disable GPU
# os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'  # Suppress TensorFlow warnings
# import pyaudio
# import numpy as np
# import tensorflow as tf
# import tensorflow_hub as hub
# import scipy.signal

# # Load the YAMNet model from TensorFlow Hub
# yamnet_model = hub.load('https://tfhub.dev/google/yamnet/1')

# # Initialize PyAudio
# p = pyaudio.PyAudio()

# # Audio recording parameters
# FORMAT = pyaudio.paInt16
# CHANNELS = 1
# RATE = 16000  # Required sampling rate for YAMNet
# CHUNK = 1024  # Audio chunk size

# # Class labels for YAMNet
# yamnet_classes = [line.strip() for line in tf.keras.utils.get_file(
#     'yamnet_class_map.csv',
#     'https://raw.githubusercontent.com/tensorflow/models/master/research/audioset/yamnet/yamnet_class_map.csv'
# ).numpy().decode('utf-8').splitlines()]

# def process_audio(audio_data):
#     # Convert audio data to numpy array
#     waveform = np.frombuffer(audio_data, dtype=np.int16) / 32768.0
#     waveform = waveform.astype(np.float32)

#     # Run the audio through the YAMNet model
#     scores, embeddings, spectrogram = yamnet_model(waveform)
#     scores = scores.numpy()

#     # Get the top classification
#     top_class_index = np.argmax(np.mean(scores, axis=0))
#     top_class_name = yamnet_classes[top_class_index]
#     return top_class_name

# def main():
#     # Open the microphone stream
#     stream = p.open(format=FORMAT, channels=CHANNELS, rate=RATE, input=True, frames_per_buffer=CHUNK)

#     print("Listening for sounds... Press Ctrl+C to stop.")
#     try:
#         while True:
#             # Read audio data from the microphone
#             audio_data = stream.read(CHUNK, exception_on_overflow=False)

#             # Process and classify the audio
#             sound_description = process_audio(audio_data)
#             print(f"\rDetected sound: {sound_description}", end="")
#     except KeyboardInterrupt:
#         print("\nStopping...")
#         stream.stop_stream()
#         stream.close()
#         p.terminate()

# if __name__ == "__main__":
#     main()
# import tensorflow as tf
# import tensorflow_hub as hub
# import numpy as np
# import sounddevice as sd
# import librosa

# # Load the VGGish model
# print("Loading VGGish model...")
# model = hub.load('https://tfhub.dev/google/vggish/1')

# # Audio recording parameters
# SAMPLING_RATE = 16000  # VGGish expects 16kHz audio
# DURATION = 5  # Record 5 seconds of audio

# def record_audio(duration, samplerate):
#     """
#     Record audio from the microphone for a given duration.
#     """
#     print("Recording...")
#     audio = sd.rec(int(duration * samplerate), samplerate=samplerate, channels=1, dtype='float32')
#     sd.wait()  # Wait until recording is finished
#     print("Recording complete.")
#     return audio.flatten()

# def extract_features(audio, samplerate):
#     """
#     Extract features from audio for VGGish input.
#     """
#     # Convert to mono and normalize
#     audio = librosa.resample(audio, orig_sr=samplerate, target_sr=SAMPLING_RATE)
#     audio = np.clip(audio, -1.0, 1.0)
#     # Pad or truncate to 1 second
#     if len(audio) < SAMPLING_RATE:
#         audio = np.pad(audio, (0, SAMPLING_RATE - len(audio)))
#     else:
#         audio = audio[:SAMPLING_RATE]
#     return audio

# def classify_audio(audio):
#     """
#     Classify audio using the VGGish model.
#     """
#     features = extract_features(audio, SAMPLING_RATE)
#     features = np.expand_dims(features, axis=0)  # Add batch dimension
#     embeddings = model(features)
#     print(f"Extracted embeddings: {embeddings}")
#     return embeddings

# def main():
#     """
#     Main function to record and classify sounds.
#     """
#     try:
#         while True:
#             audio = record_audio(DURATION, SAMPLING_RATE)
#             embeddings = classify_audio(audio)
#             print(f"Sound embeddings: {embeddings}")
#     except KeyboardInterrupt:
#         print("\nStopping...")
#     finally:
#         print("Program exited.")

# if __name__ == "__main__":
#     main()

import os
import csv
import pyaudio
import numpy as np
import tensorflow as tf
import tensorflow_hub as hub

# Suppress TensorFlow warnings and disable GPU
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'
os.environ['CUDA_VISIBLE_DEVICES'] = '-1'

# Load the YAMNet model
print("Loading YAMNet model...")
yamnet_model = hub.load('https://tfhub.dev/google/yamnet/1')

# Load class labels correctly
print("Loading class labels...")
yamnet_classes_path = tf.keras.utils.get_file(
    'yamnet_class_map.csv',
    'https://raw.githubusercontent.com/tensorflow/models/master/research/audioset/yamnet/yamnet_class_map.csv'
)

with open(yamnet_classes_path, 'r') as f:
    yamnet_classes = [row[1] for row in csv.reader(f)][1:]  # Skip header and take class names

# Debug: Print the first few class labels
print("First 10 classes:", yamnet_classes[:10])

# Audio recording parameters
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 16000  # Required sampling rate for YAMNet
CHUNK = 16000  # Process 1 second of audio at a time

# Initialize PyAudio
p = pyaudio.PyAudio()

def process_audio(audio_data):
    """
    Process audio data through YAMNet and return the top class description.
    """
    try:
        # Convert audio data to numpy array
        waveform = np.frombuffer(audio_data, dtype=np.int16).astype(np.float32) / 32768.0

        # Run the audio through the YAMNet model
        predictions = yamnet_model(waveform)
        scores = predictions[0].numpy()  # Scores for each class

        # Debug: Print raw scores and shape
        print(f"\nRaw scores (shape: {scores.shape}):", scores)

        # Average scores across time frames
        averaged_scores = np.mean(scores, axis=0)

        # Get the top classification index
        top_class_index = np.argmax(averaged_scores)
        top_class_name = yamnet_classes[top_class_index]
        confidence = averaged_scores[top_class_index]

        return f"{top_class_name} (Confidence: {confidence:.2f})"

    except Exception as e:
        return f"Error processing audio: {str(e)}"

def main():
    """
    Main function to capture audio and classify surroundings in real-time.
    """
    try:
        # Open the microphone stream
        stream = p.open(format=FORMAT, channels=CHANNELS, rate=RATE, input=True, frames_per_buffer=CHUNK)
        print("Listening for sounds... Press Ctrl+C to stop.")

        while True:
            # Read audio data from the microphone
            audio_data = stream.read(CHUNK, exception_on_overflow=False)

            # Process and classify the audio
            sound_description = process_audio(audio_data)
            print(f"\rDetected sound: {sound_description}", end="")

    except KeyboardInterrupt:
        print("\nStopping...")
    finally:
        stream.stop_stream()
        stream.close()
        p.terminate()

if __name__ == "__main__":
    main()
