# import whisper
# import pyaudio
# import wave
# import tempfile

# # Ensure the "tiny" or "base" Whisper model is used for faster processing on CPU
# model = whisper.load_model("base")

# # Audio recording settings
# FORMAT = pyaudio.paInt16
# CHANNELS = 1
# RATE = 16000  # Preferred sampling rate for speech recognition
# CHUNK = 1024  # Audio chunk size
# RECORD_SECONDS = 5  # Recording duration per chunk
# TEMP_FILE = tempfile.NamedTemporaryFile(suffix=".wav").name

# # Initialize PyAudio
# audio = pyaudio.PyAudio()

# # Open audio stream
# stream = audio.open(format=FORMAT, channels=CHANNELS, rate=RATE, input=True, frames_per_buffer=CHUNK)

# print("Listening... Speak into the microphone (Press Ctrl+C to stop).")

# try:
#     while True:
#         print("Recording...")
#         frames = []

#         # Record audio for the specified duration
#         for _ in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
#             data = stream.read(CHUNK)
#             frames.append(data)

#         # Save recorded audio to a temporary file
#         with wave.open(TEMP_FILE, 'wb') as wf:
#             wf.setnchannels(CHANNELS)
#             wf.setsampwidth(audio.get_sample_size(FORMAT))
#             wf.setframerate(RATE)
#             wf.writeframes(b''.join(frames))

#         # Transcribe the audio using Whisper
#         print("Transcribing...")
#         result = model.transcribe(TEMP_FILE, fp16=False)  # Use fp16=False for CPU processing
#         print("You said:\n" + result["text"])

# except KeyboardInterrupt:
#     print("\nStopping...")
#     stream.stop_stream()
#     stream.close()
#     audio.terminate()

import whisper
import pyaudio
import wave
import tempfile

# Load the Whisper model (use "base" for CPU)
model = whisper.load_model("base")

# Audio recording settings
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 16000
CHUNK = 1024

# Initialize PyAudio
audio = pyaudio.PyAudio()

# Open audio stream
stream = audio.open(format=FORMAT, channels=CHANNELS, rate=RATE, input=True, frames_per_buffer=CHUNK)

print("Listening... Speak into the microphone. Press Ctrl+C to stop.")

try:
    while True:
        frames = []

        # Record audio for 5 seconds
        print("Recording...")
        for _ in range(0, int(RATE / CHUNK * 5)):
            data = stream.read(CHUNK)
            frames.append(data)

        # Save audio to a temporary file
        temp_file = tempfile.NamedTemporaryFile(suffix=".wav", delete=False)
        with wave.open(temp_file.name, 'wb') as wf:
            wf.setnchannels(CHANNELS)
            wf.setsampwidth(audio.get_sample_size(FORMAT))
            wf.setframerate(RATE)
            wf.writeframes(b''.join(frames))

        # Transcribe audio
        print("Transcribing...")
        result = model.transcribe(temp_file.name, fp16=False)
        print("You said:\n" + result["text"])

except KeyboardInterrupt:
    print("\nStopping...")
    stream.stop_stream()
    stream.close()
    audio.terminate()
