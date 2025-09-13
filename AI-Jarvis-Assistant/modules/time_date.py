"""
time_date.py
------------
This module provides current time and date.
"""

import datetime
from modules.speak import speak

def tell_time():
    """
    Speak the current system time.
    """
    strTime = datetime.datetime.now().strftime("%H:%M:%S")
    speak(f"The time is {strTime}")

def tell_date():
    """
    Speak the current system date.
    """
    strDate = datetime.datetime.now().strftime("%d %B %Y")
    speak(f"Today’s date is {strDate}")
