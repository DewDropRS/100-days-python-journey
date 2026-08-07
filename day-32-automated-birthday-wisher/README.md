# Automated Birthday Wisher
### 100 Days of Python | Day 32

A script that checks a CSV of birthdays against today's date and emails a personalized birthday letter to anyone celebrating that day, picking a random letter template and merging in their name. Built around Python's `smtplib` for sending mail over Gmail's SMTP server.

---

## What I Learned

- Connecting to Gmail's SMTP server with `smtplib.SMTP_SSL("smtp.gmail.com", 465)` for an implicitly encrypted connection
- Authenticating with `connection.login()` using a Gmail **app password**, which requires 2-Step Verification to be enabled on the account
- Sending mail with `connection.sendmail(from_addr, to_addrs, msg)`, and manually including a `Subject:` line in the message string since `smtplib` does not add one automatically
- Using `with smtplib.SMTP_SSL(...) as connection:` so the connection always closes, even if `login()` or `sendmail()` raises an error
- Loading structured data from `.csv` into Python with `csv.DictReader`, which turns each row into a dictionary keyed by column header (`name`, `email`, `year`, `month`, `day`)
- Filtering a list of dictionaries with a list comprehension to find rows matching today's month and day
- Merging real data into a text template with `str.replace()`, swapping a `[name]` placeholder for the actual recipient's name
- Picking a random letter template from a set of `.txt` files with `random.choice()`
- Keeping credentials out of version control using `python-dotenv`: storing real values in a local `.env` file, loading them with `load_dotenv()`, and excluding `.env` from git via `.gitignore`

---

## Debugging Notes

**`AttributeError: 'WindowsPath' object has no attribute 'read'`** — tried calling `.read()` directly on a `Path` object returned by `random.choice()`. `Path` objects aren't file handles; either open them first with `open(path)` or use the built-in `.read_text(encoding="utf-8")` method.

**Empty `todays_birthdays` list during testing** — the date-matching filter was correct, but `birthdays.csv` hadn't been updated to include an entry for the test date, so nothing matched. Confirmed the logic by temporarily hardcoding `today` to a known date in the CSV.

**`SyntaxError` risk from nested quotes in an f-string** — `f"...{person["name"]}..."` uses double quotes inside a double-quoted f-string. This only works on Python 3.12+ (PEP 701); on earlier versions it raises a `SyntaxError`. Fixed by using single quotes for the dict key: `f"...{person['name']}..."`.

---

## smtplib Reference

```python
import smtplib

with smtplib.SMTP_SSL("smtp.gmail.com", 465) as connection:
    connection.login(user=my_email, password=app_password)
    connection.sendmail(
        from_addr=my_email,
        to_addrs=recipient_email,
        msg=f"Subject:Happy Birthday!\n\n{personalized_letter}"
    )
```

### `SMTP_SSL` vs `SMTP` + `starttls()`

| Approach | Port | How it works |
|---|---|---|
| `smtplib.SMTP_SSL(host, 465)` | 465 | Connection is encrypted from the start |
| `smtplib.SMTP(host, 587)` then `.starttls()` | 587 | Connection starts unencrypted, then upgrades to encrypted |

### Common `smtplib` errors

| Exception | Cause |
|---|---|
| `TimeoutError` | No port specified, or the wrong port (25) — connection never reaches the server |
| `smtplib.SMTPAuthenticationError` | Wrong email/password, or a regular password used instead of an app password |
| `smtplib.SMTPServerDisconnected` | Connection closed before `sendmail()` finished — often from not using `with` |

---

## Exception Handling Coverage

| Exception | Where | What it handles |
|---|---|---|
| `FileNotFoundError` | `load_birthdays_csv()` | `birthdays.csv` missing at the expected path |

---

## Tech Stack

| Tool | Purpose |
|---|---|
| Python 3 | Core language |
| `smtplib` | Sending email over SMTP |
| `csv` | Reading `birthdays.csv` into dictionaries |
| `pathlib` | Cross-platform file path handling |
| `random` | Picking a random letter template |
| `datetime` | Checking today's date against each record |
| `python-dotenv` | Loading credentials from a local `.env` file instead of hardcoding them |

`python-dotenv` is the only external dependency; everything else is standard library.

---

## Installation

```bash
git clone https://github.com/yourusername/automated-birthday-wisher.git
cd automated-birthday-wisher
pip install python-dotenv
```

Requires a Gmail account with 2-Step Verification enabled and an app password generated at [myaccount.google.com/apppasswords](https://myaccount.google.com/apppasswords).

Credentials are kept out of the codebase using a `.env` file, which is excluded from git via `.gitignore` and never committed. Create a `.env` file in the project root:

```
MY_EMAIL=youraccount@gmail.com
MY_APP_PASSWORD=your16charapppassword
RECIPIENT_EMAIL=someone@yahoo.com
```

`config.py` loads these with `load_dotenv()` and `os.getenv()` rather than hardcoding real values.

---

## How to Run

```bash
python main.py
```

---

## Project Structure

```
project/
├── .env                # real credentials, excluded from git
├── .gitignore           # excludes .env from version control
├── config.py
├── main.py
├── src/
│   └── data_loader.py
└── data/
    ├── birthdays.csv
    └── letter_templates/
        ├── letter_1.txt
        ├── letter_2.txt
        └── letter_3.txt
```

---

## Sample Data Format

`birthdays.csv`:

```
name,email,year,month,day
Mom,someone@yahoo.com,1955,8,6
```

`letter_templates/letter_1.txt`:

```
Dear [name],

Happy birthday! Wishing you a wonderful year ahead.
```

---

## Author

Built by Rocio Segura as part of the [100 Days of Code: Python](https://www.udemy.com/course/100-days-of-code/) curriculum.