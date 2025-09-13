# modules/system_control.py
"""
System Control Module
---------------------
Handles system-level commands like shutdown, restart, lock,
volume control, and battery status.
"""

import os
import psutil
import pyautogui
from modules.speak import speak


def shutdown():
    speak("Shutting down your system in 5 seconds. Please save your work.")
    os.system("shutdown /s /t 5")


def restart():
    speak("Restarting your system in 5 seconds.")
    os.system("shutdown /r /t 5")


def lock():
    speak("Locking your system now.")
    os.system("rundll32.exe user32.dll,LockWorkStation")


def battery_status():
    battery = psutil.sensors_battery()
    percent = battery.percent
    speak(f"Your battery is at {percent} percent.")
    if battery.power_plugged:
        speak("Your laptop is charging.")
    else:
        speak("Your laptop is not charging.")


def volume_up():
    speak("Increasing volume.")
    for _ in range(5):
        pyautogui.press("volumeup")


def volume_down():
    speak("Decreasing volume.")
    for _ in range(5):
        pyautogui.press("volumedown")


def mute():
    speak("Muting volume.")
    pyautogui.press("volumemute")
