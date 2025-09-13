"""
main.py
-------
Main script for Vivi AI Assistant.
"""

import datetime
import pyjokes

# Import custom modules
from modules.listen import take_command
from modules.speak import speak
from modules.system_tasks import open_app, send_whatsapp_message
from modules.search import google_search, wiki_search
from modules.time_date import tell_time, tell_date
import modules.system_control as system_control


def greet_user():
    """Greet user based on time of day."""
    hour = datetime.datetime.now().hour
    if 5 <= hour < 12:
        speak("Good morning! I am Vivi, your personal assistant.")
    elif 12 <= hour < 18:
        speak("Good afternoon! I am Vivi, your personal assistant.")
    else:
        speak("Good evening! I am Vivi, your personal assistant.")
    speak("How can I help you today?")


def process_command(command: str) -> bool:
    """
    Process user's voice command.
    Returns False if assistant should stop listening, True otherwise.
    """
    if not command:  # ✅ Fix: Prevent NoneType crash
        return True

    command = command.lower()

    # --- SYSTEM CONTROL ---
    if "shutdown" in command:
        speak("Shutting down the system now.")
        system_control.shutdown()

    elif "restart" in command:
        speak("Restarting your computer.")
        system_control.restart()

    elif "sleep" in command:
        speak("Putting your computer to sleep.")
        system_control.sleep()

    # --- TIME & DATE ---
    elif "time" in command:
        speak(f"The current time is {tell_time()}")

    elif "date" in command:
        speak(f"Today's date is {tell_date()}")

    # --- JOKES ---
    elif "joke" in command:
        joke = pyjokes.get_joke()
        speak(joke)

    # --- SEARCH ---
    elif "search google for" in command:
        query = command.replace("search google for", "").strip()
        speak(f"Searching Google for {query}")
        google_search(query)

    elif "wikipedia" in command:
        query = command.replace("wikipedia", "").strip()
        speak(f"Searching Wikipedia for {query}")
        result = wiki_search(query)
        speak(result)

    # --- OPEN APPS ---
    elif "open" in command:
        app_name = command.replace("open", "").strip()
        success = open_app(app_name)
        if success:
            speak(f"Opening {app_name}")
        else:
            speak(f"Sorry, I couldn't find {app_name} installed.")

    # --- WHATSAPP MESSAGE ---
    elif "send whatsapp message" in command:
        try:
            speak("Please tell me the phone number including country code.")
            phone_no = take_command()

            speak("What message should I send?")
            message = take_command()

            if phone_no and message:
                success = send_whatsapp_message(phone_no, message)
                if success:
                    speak("Your message has been scheduled successfully in WhatsApp.")
                else:
                    speak("Sorry, I couldn't schedule the message.")
            else:
                speak("Phone number or message not received.")
        except Exception:
            speak("Something went wrong while sending the message.")

    # --- EXIT ---
    elif "exit" in command or "quit" in command or "stop" in command:
        speak("Goodbye! I am shutting down. Have a great day!")
        return False   # ✅ Tell main loop to stop

    else:
        speak("Sorry, I didn’t understand that. Could you repeat?")

    return True  # ✅ Continue listening


def run_assistant():
    """Run Vivi in a continuous loop."""
    greet_user()
    while True:
        command = take_command()
        if not command or command == "none":
            continue  # ✅ Skip instead of crashing
        keep_running = process_command(command)
        if not keep_running:   # ✅ Exit cleanly
            break


if __name__ == "__main__":
    run_assistant()
