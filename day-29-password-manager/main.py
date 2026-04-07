import string
from tkinter import * #imports only classes
from tkinter import messagebox
from PIL import Image, ImageTk
import pyperclip
import json
import secrets
import urllib.request # For opening and reading URLs

LABEL_FONT = ("Segoe UI", 11)
ENTRY_FONT = ("Consolas", 11)
BUTTON_FONT = ("Consolas", 8)
BACKGROUND = "white"
FOREGROUND = "black"

# ---------------------------- LOAD LOGO ---------------------------------------- #
def load_logo(width=200, height=200):
    """Load and resize logo image for display in Tkinter using PIL."""
    img = Image.open("logo.png")
    img = img.resize((width, height), Image.Resampling.LANCZOS)    # resize with high quality
    return ImageTk.PhotoImage(img) # convert for Tkinter
# ---------------------------- LOAD EFF WORDS ----------------------------------- #
def load_eff_words():
    """Download EFF's passphrase wordlist. """
    url = "https://www.eff.org/files/2016/07/18/eff_large_wordlist.txt"
    words = []
    with urllib.request.urlopen(url) as response:
        # a raw line looks like this b'11111\tabacus\n'
        # .decode() turns bytes to string
        # .strip() strips whitespace and newline
        # .split("\t") splits the string that is separated by a tab
        # [1] - get second item that is the actual word
        for line in response:
            word = line.decode().strip().split("\t")[1]
            words.append(word)
    return words
# ---------------------------- PASSPHRASE GENERATOR ----------------------------- #
def generate_passphrase(number_of_words = 4):
    """Generate passphrase with added unpredictable elements. """

    # Load words and randomly choose words
    words = load_eff_words()
    chosen_words = [secrets.choice(words) for _ in range(number_of_words)]

    # Make passphrase stronger by adding unpredictable elements
    # Randomly capitalize a word
    capital_index = secrets.randbelow(len(chosen_words))
    chosen_words[capital_index] = chosen_words[capital_index].capitalize()

    # Insert a random number
    number = secrets.randbelow(len(chosen_words) + 1)
    number_index = secrets.randbelow(len(chosen_words) + 1)
    chosen_words.insert(number_index, str(number))

    # Insert a random symbol
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
    symbol = secrets.choice(symbols)
    symbol_index = secrets.randbelow(len(chosen_words) + 1)
    chosen_words.insert(symbol_index, symbol)

    passphrase = '-'.join(chosen_words)
    return passphrase

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password(length = 16):
    """Generate a password using upper case and lower case letters, digits, and symbols.

        :returns: password (Str)
    """

    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    chars = string.ascii_letters + string.digits + "".join(symbols)

    # Password should have at least one letter, one digit, and one symbol
    password = [
        secrets.choice(string.ascii_letters),
        secrets.choice(string.digits),
        secrets.choice(symbols)
    ]
    # Complete the password
    # don't really need the index so just use underscore as a placeholder
    password += [secrets.choice(chars) for _ in range(length - 3)]

    # shuffle it
    secrets.SystemRandom().shuffle(password)
    # turn list into a string. the join() can also be used like the following:
    # '-'.join(password_list) if you want a dash as a separator.
    password = ''.join(password)
    return password


def generate():
    """Generates password/passphrase based on radio button user choice"""
    selection = password_choice.get()
    if selection == "password":
        result = generate_password()
    elif selection == "passphrase":
        result = generate_passphrase()
    # First clear field and insert the returned result
    password_entry.delete(0, END)
    password_entry.insert(0, result)
    pyperclip.copy(result)
# ---------------------------- SAVE PASSWORD ------------------------------- #
# save to data.text (website_entry, email_usrname_entry, password_entry)
# Validates that all fields are filled before prompting to save.
# Raises ValueError if any field is blank, caught by except to show an error popup.
def save_password():
    """
    Saves password entry into data.txt.
    Validates that all fields are filled before prompting the user to save (OK, Cancel)
    Raises ValueError if any field is blank, caught by except to show the error in a popup message box.
    :return:
    """
    # Grab current entry values
    website = website_entry.get()
    email = email_usrname_entry.get()
    password = password_entry.get()
    new_data = {
        website: {
            "email" : email,
            "password" : password,
        }
    }
    # Check for blank fields before asking to save
    try:
        if not website or not email or not password:
            raise ValueError("All fields must be filled in before saving.")

        ok_cancel = messagebox.askokcancel(
            message=f"website: {website}\nemail/username: {email}\npassword: {password}\nGo ahead and save?",
            icon='question',
            title='Save password?'
        )

        if ok_cancel:
            # Day 30 enhancement: json load/update/dump
            try:
                with open("data.json", "r") as file:
                    # file.write(f"{website} | {email} | {password}\n")
                    # Read existing data into a python dictionary called data
                    data = json.load(file)

            except FileNotFoundError:
                # Create the file for the first time
                with open("data.json", "w") as file:
                    json.dump(new_data, file, indent = 4)

            else:
                if website in data:
                # Prompt user if they want to update the password
                    overwrite_password = messagebox.askokcancel(
                        title = ""
                        , message = f"An entry for {website} already exists.\nWould you like to update it?"
                        , icon = "warning"
                    )
                    if not overwrite_password:
                        return # exit without saving password/passphrase
                # Update the existing data with the new data
                data.update(new_data)
                with open("data.json", "w") as file:
                    # Save the updated data back into the json file
                    json.dump(data, file, indent=4)

                # Clear website and password fields, restore default email
                website_entry.delete(0, 'end')
                email_usrname_entry.delete(0, 'end')
                email_usrname_entry.insert(0, "madeup.madeup@gmail.com")
                password_entry.delete(0, 'end')
    except ValueError as e:
        # Show error popup if any field is blank
        messagebox.showerror(title="Missing fields", message=str(e), icon = 'warning')

# ---------------------------- SEARCH ------------------------------- #
def search():
    # This is the key to search on
    website = website_entry.get()

    # Check for website field left empty
    if not website:
        messagebox.showerror(title="Missing Field", message="Please enter a website to search.")
        return #exit function since can't search on empty field

    # Catch if file does not exist
    try:
        with open("data.json", "r") as file:
            # Read existing data into a python dictionary called data
            data = json.load(file)

    except FileNotFoundError as e:
        messagebox.showerror(title="Password file does not yet exist.", message=str(e), icon='warning')
        return # exit function since password file does not exist

    else:
        # If the file exists now try searching on website key
        # entry is a dictionary
        if website in data:
            messagebox.showinfo(title = f"Search {website}",
                message = f"email/username: {data[website]["email"]}\npassword: {data[website]["password"]}")
        else:
            messagebox.showerror(title="Not Found", message=f"No entry found for '{website}'.")

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx = 40
              , pady = 40
              , background = "white")

logo_image = load_logo(width = 300, height = 300)
logo_label = Label(window, image = logo_image, bg = "white") # type: ignore
logo_label.image = logo_image                           # keep reference to prevent garbage collection



# _text = canvas.create_text(100, 130, text = "00:00", fill = "white", font = (FONT_NAME, 40, "bold"))
# -----labels/entries
website_label = Label(text = "Website: "
                      , font = LABEL_FONT
                      , fg = FOREGROUND
                      , bg = BACKGROUND
                      , highlightthickness = 0)
website_entry = Entry(width = 35
                      , font = ENTRY_FONT
                      , bg = "white")
website_entry.focus()

email_usrname_label = Label(text = "Email/Username: "
                            , font = LABEL_FONT
                            , fg = FOREGROUND
                            , bg=BACKGROUND
                            , highlightthickness=0)
email_usrname_entry = Entry(width=35
                            , font=ENTRY_FONT
                            , bg = "white")
email_usrname_entry.insert(0, "madeup.madeup@gmail.com")

password_label = Label(text ="Password/Passphrase: "
                       , font=LABEL_FONT
                       , fg = FOREGROUND
                       , bg=BACKGROUND
                       , highlightthickness=0)
password_entry = Entry(width=35
                       , font=ENTRY_FONT
                       , bg ="white")



# -----Buttons-----
search_button = Button(width = 46
                       , text = "Search website"
                       , command = search
                       , bg = "white"
                       , font = BUTTON_FONT
                       , highlightthickness=0
                       )

add_button = Button(width = 46
                    , text = "Add to MyPass"
                    , command = save_password
                    , bg = "white"
                    , font = BUTTON_FONT
                    , highlightthickness=0
                    )

# -----Radio buttons for selecting traditional password or passphrase
password_choice = StringVar(value = "password")
password_radio = Radiobutton(
    window,
    width = 16,
    text="Gen Password",
    variable=password_choice,     # both radios share the same StringVar
    value="password",           # set value when selected
    command=generate            # call generate function
)
passphrase_radio = Radiobutton(
    window,
    width = 16,
    text="Gen Passphrase",
    variable=password_choice,
    value="passphrase",
    command=generate
)
# -----main grid-----
# 7 rows by 2 columns
logo_label.grid(row=0, column=0, columnspan=2) # logo image
website_label.grid(row = 1, column = 0, sticky = "e")
website_entry.grid(row = 1, column = 1, sticky = "w")

search_button.grid(row = 2, column = 1, sticky = "e")

email_usrname_label.grid(row = 3, column = 0, sticky = "e")
email_usrname_entry.grid(row = 3, column = 1, columnspan=1, sticky = "w")

password_label.grid(row = 4, column = 0, sticky = "e")
password_entry.grid(row = 4, column = 1, columnspan = 1, sticky = "w")
# generate_pw_button.grid(row = 3, column = 2, sticky = "e")
password_radio.grid(row=5, column=1, sticky="W")
passphrase_radio.grid(row=5, column=1, sticky="E")

add_button.grid(row = 6, column = 1, columnspan=1, sticky = "w")


window.update()
window.mainloop()