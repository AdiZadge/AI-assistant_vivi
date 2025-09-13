import speech_recognition as sr
from modules.speak import speak

def take_command():
    """
    Listen for user voice and convert to text.
    Returns: recognized command (str) or None if not understood.
    """
    r = sr.Recognizer()

    try:
        with sr.Microphone() as source:
            print("Listening...")
            r.pause_threshold = 1  # small pause between words
            audio = r.listen(source, phrase_time_limit=5)  # listen max 5 sec

        print("Recognizing...")
        query = r.recognize_google(audio, language="en-in")
        print(f"You said: {query}")
        return query

    except sr.UnknownValueError:
        # Speech not clear
        print("Sorry, I could not understand your voice.")
        speak("Sorry, I could not understand your voice.")
        return None

    except sr.RequestError:
        # API/network error
        print("Speech recognition service not available.")
        speak("Speech recognition service is not available. Switching to text mode.")
        # Fallback to text input
        return input("Type your command: ")

    except Exception as e:
        print(f"Error while listening: {e}")
        speak("I faced an error while listening. Please try again.")
        return None
