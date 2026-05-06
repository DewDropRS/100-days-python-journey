# ============================================================
# flashcard_app.py
# Flash Card App — Main application class for the Flashy
# flash card learning app.
# ============================================================
from tkinter import * #imports only classes
from tkinter import filedialog, simpledialog, messagebox

import pandas as pd
from PIL import Image, ImageTk
import random

from config import(
    DATA_DIR,
    BACKGROUND_COLOR,
    CARD_FRONT_IMAGE,
    CARD_BACK_IMAGE,
    RIGHT_BUTTON_IMAGE,
    WRONG_BUTTON_IMAGE
)
from data_loader import load_flash_card_data


class FlashCardApp:
    """
    Main application class for the Flashy flash card learning app.
    Manages the tkinter UI, card navigation, flip timer, and known word tracking.
    """


    def __init__(self, window):
        self.window = window
        self.current_card = {}
        self.flip_timer = None
        self.flip_delay_ms = 3000 # 3-second default before flipping card
        self.setup_ui()
        self.choose_flip_delay()
        self.choose_language()  # asks user to pick language before cards show


    def setup_ui(self):
        """
        Sets up the user interface for window, front and back of the cards, and buttons.
        """

        self.window.title("Flashy")
        self.window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

        self.canvas = Canvas(width=800, height=526)
        self.card_front_img = PhotoImage(file=CARD_FRONT_IMAGE)
        self.card_back_img = PhotoImage(file=CARD_BACK_IMAGE)
        self.current_image = self.canvas.create_image(400, 263, image=self.card_front_img)
        self.card_title = self.canvas.create_text(400, 150, text="", font=("Ariel", 40, "italic"))
        self.card_word = self.canvas.create_text(400, 263, text="", font=("Ariel", 60, "bold"))
        self.canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)

        # Words remaining label
        self.words_remaining = Label(text="", bg=BACKGROUND_COLOR, fg="white", font=("Ariel", 14, "italic"))

        # Buttons
        self.cross_image = PhotoImage(file=WRONG_BUTTON_IMAGE)
        self.unknown_button = Button(image=self.cross_image
                                , highlightthickness=0
                                , command=self.show_next_card)


        self.check_image = PhotoImage(file=RIGHT_BUTTON_IMAGE)
        self.known_button = Button(image=self.check_image
                              , highlightthickness=0
                              , command=self.word_is_known)

        # Grid
        self.canvas.grid(row=0, column=0, columnspan=2)
        self.unknown_button.grid(row=1, column=0)
        self.known_button.grid(row=1, column=1)
        self.words_remaining.grid(row=2, column=0, columnspan=2)

    def choose_language(self):
        """
        Opens a file picker dialog for the user to select a language learning CSV file.
        Loads the selected file and starts the flash card session.
        """
        filepath = filedialog.askopenfilename(
            title="Choose a language file",
            initialdir=DATA_DIR,  # opens directly to your data folder
            filetypes=[("CSV files", "*.csv")]  # filters to only show CSV files
        )

        # Guard against user closing the dialog without selecting a file
        if filepath:
            self.load_data(filepath)

        else:
            # User closed dialog without selecting a file
            retry = messagebox.askretrycancel(
                title="No File Selected",
                message="No language file was selected.\nRetry to choose a file or Cancel to exit."
            )
            if retry:
                self.choose_language()  # re-prompt
            else:
                self.window.destroy()  # exit the app cleanly

    def choose_flip_delay(self):
        """
        Asks the user how many seconds before the card flips automatically.
        """
        seconds = simpledialog.askinteger(
            title="Flip Speed",
            prompt="How many seconds before the card flips?",
            minvalue=1,
            maxvalue=10,
            initialvalue=3  # default suggestion
        )

        # Guard against user canceling the dialog
        if seconds:
            self.flip_delay_ms = seconds * 1000  # convert to milliseconds


    def update_words_remaining(self):
        """
        Updates the words remaining label with the current count of words left to learn.
        """
        count = len(self.word_translation_dict)
        self.words_remaining.config(text=f"{count} words remaining")


    def load_data(self, filepath):
        """
        Loads the language learning CSV data from the given file path.
        :param filepath: full path to the CSV file (string)
        """
        try:
            df = load_flash_card_data(filepath)
            self.word_translation_dict = df.to_dict(orient="records")

            # Validate that the file has 2 columns exactly
            keys = list(self.word_translation_dict[0].keys())
            if len(keys) != 2:
                messagebox.showerror(
                    title="Invalid File Format",
                    message=f"Expected 2 columns (word, translation) but found {len(keys)}.\nPlease choose a valid language file."
                )
                self.choose_language()
                return

            # Save the language to learn and the translation language
            self.lang_to_learn = keys[0]
            self.translation_lang = keys[1]

            # Show the initial card just after loading flash card data
            self.show_next_card()

        except pd.errors.EmptyDataError:
            # CSV file exists but is empty
            messagebox.showerror(
                title="Empty File",
                message="The selected file is empty.\nPlease choose another file."
            )
            self.choose_language()

        except pd.errors.ParserError:
            # CSV file exists but is malformed/corrupted
            messagebox.showerror(
            title="Invalid File",
            message="The selected file could not be read.\nPlease choose a valid CSV file."
            )
            self.choose_language()

        except Exception as e:
            # Catch-all for anything unexpected
            messagebox.showerror(
            title="Error Loading File",
            message=f"Something went wrong loading the file:\n{e}"
            )
            self.choose_language()


    def show_next_card(self):
        """
        Cancels any existing flip timer, loads a new random card,
        schedules the card flip, and updates the words remaining count.
        """
        # Cancel any existing flip timer so it doesn't fire mid-card
        if self.flip_timer:
            self.window.after_cancel(self.flip_timer)

        # Get a new card
        self.next_card()

        # Schedule flip for this specific card's translation
        self.flip_timer = self.window.after(self.flip_delay_ms,
                                  func=self.flip_card)

        self.update_words_remaining()

    def next_card(self):
        """
        Selects a random card from the deck and updates the canvas with the language label,
        word to learn, and card front image.
        """

        self.current_card = random.choice(self.word_translation_dict)
        # Stored on self so flip_card can access them after the timer fires
        self.word = self.current_card[self.lang_to_learn]
        self.word_translation = self.current_card[self.translation_lang]

        self.canvas.itemconfig(self.card_title, text=self.lang_to_learn, fill='black')
        self.canvas.itemconfig(self.card_word, text=self.word, fill='black')
        self.canvas.itemconfig(self.current_image, image=self.card_front_img)


    def flip_card(self):
        """
        Flips the card to the back image and updates the canvas with the
        translation language label and translated word.
        """
        # card_title, card_word, and current_image are canvas item IDs
        self.canvas.itemconfig(self.card_title, text=self.translation_lang, fill='white')
        self.canvas.itemconfig(self.card_word, text=self.word_translation, fill='white')
        self.canvas.itemconfig(self.current_image, image=self.card_back_img)


    def save_progress(self):
        """
        Saves the remaining words to a progress CSV file named after the language pair.
        File is overwritten each time a word is marked as known.
        """
        filename = f"{self.lang_to_learn}_{self.translation_lang}_to_learn.csv"
        filepath = DATA_DIR / filename

        # Convert dict back to DataFrame and save
        df = pd.DataFrame(self.word_translation_dict)
        df.to_csv(filepath, index=False)


    def word_is_known(self):
        """
        Removes the current card from the deck when the user marks it as known,
        then advances to the next card. Known words will not appear again in the current session.
        """
        self.word_translation_dict.remove(self.current_card)
        self.save_progress()
        self.update_words_remaining()
        self.show_next_card()
