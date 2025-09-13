"""
search.py
---------
This module handles Google search and Wikipedia summaries.
"""

import webbrowser
import wikipedia
from modules.speak import speak

def google_search(query: str):
    """
    Perform a Google search in the web browser.
    """
    webbrowser.open(f"https://www.google.com/search?q={query}")
    speak(f"Here are the search results for {query}")

def wiki_search(query: str):
    """
    Fetch a short Wikipedia summary for the given query.
    """
    try:
        results = wikipedia.summary(query, sentences=2)
        speak("According to Wikipedia")
        speak(results)
    except:
        speak("Sorry, I couldn't fetch Wikipedia results.")
