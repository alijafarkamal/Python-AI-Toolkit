import whisper

print("Downloading the Whisper model. Please wait...")
model = whisper.load_model("base")  # This will download the model.
print("Model downloaded successfully!")
