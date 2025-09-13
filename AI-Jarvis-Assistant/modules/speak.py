"""
speak.py
--------
This module handles text-to-speech using pyttsx3.
"""

import pyttsx3

# Initialize the speech engine
engine = pyttsx3.init()
engine.setProperty('rate', 170)  # Speed of speech

def speak(text: str):
    """
    Convert text into speech and also print it on console.
    """
    print(f"Jarvis: {text}")
    engine.say(text)
    engine.runAndWait()
