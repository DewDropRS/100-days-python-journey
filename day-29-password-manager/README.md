# MyPass — Password Manager
### 100 Days of Python | Days 29 & 30

A personal password manager built with Python and Tkinter, combining GUI development with secure password and passphrase generation, JSON-based storage, and robust exception handling. This project spans two days of learning: **Day 29** focused on Tkinter GUI development, and **Day 30** introduced exception handling with try/except and working with JSON data.

---

## Preview

![MyPass Password Manager](screen-capture.png)

---

## What I Learned

### Day 29 — Tkinter GUI Development
- Building a desktop GUI application using `Tkinter`
- Laying out widgets using the **grid system** (rows, columns, sticky alignment, columnspan)
- Working with `Entry`, `Label`, `Button`, and `Radiobutton` widgets
- Using `StringVar` to link radio buttons to a shared variable for mutually exclusive selection
- Triggering functions from widget interactions via `command=`
- Clearing and pre-filling entry fields programmatically
- Customizing fonts per widget type — `Segoe UI` for labels, `Consolas` for password fields

### Day 30 — Exception Handling and JSON
- Writing `try/except/else/finally` blocks
- Catching specific exceptions: `ValueError`, `FileNotFoundError`, `json.JSONDecodeError`, `KeyError`
- Using early `return` to exit functions cleanly on validation failure
- Understanding the difference between `except`, `else`, and `finally`
- Why bare `except:` and `except: pass` are considered bad practice
- Why read and write operations require separate `with open()` blocks
- Using `json.load()` to read JSON data into a Python dictionary
- Using `json.dump()` to write a Python dictionary back to a JSON file
- Working with nested dictionaries as a data structure for storing credentials

---

## Features

### Core Features (Day 29 & 30 Requirements)
- Add website, email/username, and password entries
- Search for a saved entry by website name
- Password generator producing a 16-character password with letters, digits, and symbols
- Generated password automatically copied to clipboard using `pyperclip`
- Data persisted to a local `data.json` file
- Confirmation dialog before saving any entry
- Error popups for missing fields and file not found

### My Enhancements (Above and Beyond)

**Dual Generation Mode with Radio Buttons**
Replaced the single generate password button with two radio buttons — one for traditional passwords and one for passphrases. Both share a `StringVar` which makes them mutually exclusive. Clicking either one immediately generates and inserts the result into the password field.

**Cryptographically Secure Random Generation**
Swapped Python's `random` module for the built-in `secrets` module throughout all generation functions. Unlike `random`, `secrets` draws from the operating system's secure random source making it suitable for real password generation.

```python
secrets.choice(chars)            # pick a character
secrets.choice(words)            # pick a word
secrets.randbelow(100)           # pick a number
secrets.SystemRandom().shuffle   # shuffle the result
```

**EFF Wordlist Passphrase Generator**
Fetches the [Electronic Frontier Foundation's large wordlist](https://www.eff.org/files/2016/07/18/eff_large_wordlist.txt) — the same list used by tools like 1Password and Bitwarden — using Python's built-in `urllib.request`. No third-party HTTP library needed.

Passphrases are strengthened with three unpredictable elements inserted at random positions:
- One randomly chosen word is capitalized
- A random number is inserted at a random index
- A random symbol is inserted at a random index

```
Example output: crisp-Globe-43-flown-!-amber
```

**Duplicate Entry Detection**
Before saving, checks whether the website already exists in `data.json`. If it does, the user is prompted to confirm the update or cancel — preventing accidental overwrites.

**Resized Logo with PIL (Personal Enhancement)**
Uses Pillow to load and resize the app logo at runtime with high-quality `LANCZOS` resampling. This was not covered in the Day 29 lectures and was added independently using the `PIL` library.

---

## Tech Stack

| Tool | Purpose |
|---|---|
| Python 3 | Core language |
| Tkinter | GUI framework |
| `json` | Data storage and retrieval |
| `secrets` | Cryptographically secure random generation |
| `string` | Pre-built character constants (letters, digits) |
| `urllib.request` | Fetching EFF wordlist from the web |
| Pillow (PIL) | Image loading and resizing |
| `pyperclip` | Copy generated password to clipboard |

---

## Installation

```bash
# Clone the repo
git clone https://github.com/yourusername/mypass-password-manager.git
cd mypass-password-manager

# Install dependencies
pip install pillow pyperclip
```

> `json`, `secrets`, `string`, and `urllib` are all part of Python's standard library — no install needed.

---

## How to Run

```bash
python main.py
```

On first run, `data.json` is created automatically when you save your first entry. An internet connection is required the first time you generate a passphrase so the EFF wordlist can be fetched.

---

## Exception Handling Coverage

| Exception | Where | What it handles |
|---|---|---|
| `ValueError` | `save_password()` | Any entry field left blank before saving |
| `FileNotFoundError` | `save_password()` | `data.json` does not exist yet — creates it |
| `FileNotFoundError` | `search()` | `data.json` does not exist yet |
| `json.JSONDecodeError` | `save_password()` | File exists but contains invalid JSON |
| `KeyError` | `search()` | Website key not found in data |
| `urllib.error.URLError` | `load_eff_words()` | EFF wordlist unreachable — no internet |

---

## Exception Handling Reference

The `try/except/else/finally` structure controls what happens when something goes wrong. Each block has a distinct role.

```python
try:
    # Code that might fail goes here

except ValueError as e:
    # Runs only if a ValueError was raised
    print(f"Invalid value: {e}")

except FileNotFoundError:
    # Runs only if a FileNotFoundError was raised
    print("File not found.")

else:
    # Runs only if NO exception was raised in the try block

finally:
    # Always runs — error or not
    # Useful for cleanup like closing connections
```

### When to use each block

| Block | When it runs | Common use |
|---|---|---|
| `try` | Always | Wrap the risky code |
| `except` | Only if an exception was raised | Show error message, log the error |
| `else` | Only if no exception was raised | Continue with the happy path |
| `finally` | Always, after everything else | Cleanup — closing files, connections |

### Most common exceptions

| Exception | When it triggers |
|---|---|
| `ValueError` | Wrong value type or format, or manually raised for validation |
| `FileNotFoundError` | Trying to open a file that does not exist |
| `json.JSONDecodeError` | File exists but contains invalid or corrupted JSON |
| `KeyError` | Accessing a dictionary key that does not exist |
| `TypeError` | Wrong data type used in an operation |
| `IndexError` | Accessing a list index that is out of range |
| `OSError` | File read/write failure or permissions issue |
| `urllib.error.URLError` | Network request failed or URL is unreachable |

### Catching multiple exceptions

```python
# Handle each exception differently
try:
    with open("data.json", "r") as file:
        data = json.load(file)

except FileNotFoundError:
    data = {}                          # start fresh if file missing

except json.JSONDecodeError:
    messagebox.showerror("File corrupted.")   # warn user if file is broken

else:
    process(data)                      # only runs if file loaded successfully
```

```python
# Handle multiple exceptions the same way
except (ValueError, TypeError) as e:
    messagebox.showerror(title="Input Error", message=str(e))
```

### Using raise for manual validation

`raise` lets you trigger an exception yourself when a condition fails, so `except` can catch and handle it in one place.

```python
try:
    if not website:
        raise ValueError("Website field cannot be blank.")

except ValueError as e:
    messagebox.showerror(title="Missing Field", message=str(e))
```

### Early return vs else

Use `return` inside `except` to exit a function early when there is nothing left to do:

```python
except FileNotFoundError:
    messagebox.showerror("File not found.")
    return    # exit the function, skip everything below
```

---

## JSON Quick Reference

The `json` module converts between Python dictionaries and JSON files. It is part of Python's standard library — no install needed.

### Reading from a JSON file

`json.load()` reads a JSON file and returns a Python dictionary.

```python
import json

with open("data.json", "r") as file:
    data = json.load(file)    # data is now a Python dict

# Access values like any dictionary
email = data["google.com"]["email"]
```

### Writing to a JSON file

`json.dump()` converts a Python dictionary and writes it to a file.

```python
with open("data.json", "w") as file:
    json.dump(data, file, indent=4)    # indent=4 makes the file human-readable
```

### Converting between JSON and strings (without files)

```python
# dict → JSON string
json_string = json.dumps(data)

# JSON string → dict
data = json.loads(json_string)
```

### Updating existing data

Read first, update the dictionary in memory, then write the whole thing back:

```python
# Read
with open("data.json", "r") as file:
    data = json.load(file)

# Update in memory
data.update(new_entry)       # adds or overwrites keys

# Write back
with open("data.json", "w") as file:
    json.dump(data, file, indent=4)
```

> Read and write always require separate `with open()` blocks. The `with` statement closes the file the moment its indented block ends.

### JSON data structure used in this project

JSON stores data as key-value pairs. This project uses a nested structure where the website is the outer key and credentials are the inner dictionary.

```json
{
    "google.com": {
        "email": "user@example.com",
        "password": "abc123"
    },
    "github.com": {
        "email": "user@example.com",
        "password": "xyz789"
    }
}
```

In Python this becomes a dictionary of dictionaries:

```python
data["google.com"]              # → {"email": "...", "password": "..."}
data["google.com"]["email"]     # → "user@example.com"
"google.com" in data            # → True  (check if key exists)
```

---

## Project Structure

```
mypass-password-manager/
│
├── main.py        # Main application
├── logo.png       # App logo
├── data.json      # Password data (excluded from version control via .gitignore)
├── .gitignore     # Excludes data.json from version control
└── README.md      # This file
```

---

## Sample Data Format

```json
{
    "example.com": {
        "email": "user@example.com",
        "password": "your-password-here"
    }
}
```

---

## What's Next

- [ ] Master password protection with Fernet encryption (`cryptography` library) 
https://cryptography.io/en/latest/fernet/
- [ ] Store `secret.key` separately from encrypted data file https://www.geeksforgeeks.org/fernet-symmetric-encryption-using-cryptography-module-in-python/
- [ ] Delete entry option
- [ ] Password strength indicator

---

## Author

Built by Rocio Segura as part of the [100 Days of Code: Python](https://www.udemy.com/course/100-days-of-code/) curriculum.