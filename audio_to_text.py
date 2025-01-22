import speech_recognition as sr

def main():
    recognizer = sr.Recognizer()
    mic = sr.Microphone()
    combined_text = ""  # To store the entire recognized text

    try:
        print("Listening... Speak into the microphone. Press Ctrl+C to stop.")
        with mic as source:
            recognizer.adjust_for_ambient_noise(source)
            while True:
                audio = recognizer.listen(source)
                try:
                    recognized_text = recognizer.recognize_google(audio, language="ur")
                    combined_text += recognized_text + " "  # Append text with a space
                    print(f"\r{combined_text}", end="")  # Display the combined text
                except sr.UnknownValueError:
                    print("\rSpeech was unclear. Could not recognize.", end="")
                except sr.RequestError as e:
                    print(f"\rError with the recognition service: {e}", end="")
    except KeyboardInterrupt:
        print("\nProgram terminated by user.")
        print("\nFinal Text:")
        print(combined_text)

if __name__ == "__main__":
    main()
