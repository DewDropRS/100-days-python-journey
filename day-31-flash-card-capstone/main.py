# ============================================================
# main.py
# Entry point for Flashy, a flash card application for learning
# new concepts and languages. Initializes the tkinter window and
# delegates all UI and functionality to the FlashCardApp class.
# ============================================================
import sys
import os

# Add src/ to path so modules can find each other
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), 'src'))

from tkinter import Tk
from flashcard_app import FlashCardApp

window = Tk()
app = FlashCardApp(window)

window.mainloop()
