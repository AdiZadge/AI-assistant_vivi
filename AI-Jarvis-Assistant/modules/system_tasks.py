"""
system_tasks.py
---------------
Handles opening apps and sending WhatsApp messages.
"""

import os
import webbrowser
import pywhatkit as kit
import datetime


def open_app(app_name: str) -> bool:
    """
    Try to open applications or websites.
    If app is not found locally, open web version if available.
    """
    app_name = app_name.lower()

    try:
        # --- LOCAL APPS (update paths if you have desktop apps installed) ---
        if "chrome" in app_name:
            os.startfile("C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe")

        elif "vs code" in app_name or "visual studio code" in app_name:
            os.startfile("C:\\Users\\Aditya\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe")

        elif "explorer" in app_name:
            os.startfile("explorer")

        elif "notepad" in app_name:
            os.system("notepad")

        # --- WHATSAPP FIX: Open WhatsApp Web ---
        elif "whatsapp" in app_name:
            webbrowser.open("https://web.whatsapp.com")

        # --- WEBSITES ---
        elif "youtube" in app_name:
            webbrowser.open("https://www.youtube.com")

        elif "google" in app_name:
            webbrowser.open("https://www.google.com")

        else:
            return False  # Not found

        return True

    except Exception as e:
        print(f"Error opening {app_name}: {e}")
        return False



def send_whatsapp_message(phone_no: str, message: str) -> bool:
    """
    Send a WhatsApp message using pywhatkit (opens WhatsApp Web).
    """
    try:
        now = datetime.datetime.now()
        hour = now.hour
        minute = now.minute + 2

        if minute >= 60:
            minute = minute - 60
            hour = (hour + 1) % 24

        kit.sendwhatmsg(phone_no, message, hour, minute)
        return True

    except Exception as e:
        print(f"Error sending WhatsApp message: {e}")
        return False
