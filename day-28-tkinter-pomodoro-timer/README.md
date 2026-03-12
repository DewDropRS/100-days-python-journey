# Pomodoro Timer — Day 28 of 100 Days of Python

A fully functional Pomodoro Timer built with Python and tkinter. Supports customizable work and break durations, tracks completed rounds with tomato icons, and displays progress toward the next long break.

---

## Features

### Core (Original Project Requirements)
- Automatic cycling through work → short break → work → long break
- Visual progress tracking with 🍅 tomato icons
- Color-coded timer label (green = work, pink = short break, red = long break)
- Start and Reset buttons

### Added Enhancements (Beyond Original Requirements)
- **Customizable durations** — entry fields pre-filled with classic Pomodoro defaults (25/5/20 min) that the user can override before starting
- **Input validation** — non-integer entries revert to default values automatically
- **Rounds feedback** — displays how many work rounds remain until the next long break
- **Cycle-capped tomatoes** — 🍅 icons reset after each cycle of 4, following the classic Pomodoro standard
- **Total pomodoros count** — tracks and displays cumulative completed pomodoros since last reset
- **Completion flash on reset** — briefly shows total completed pomodoros when the timer is reset
- **Prevents stacked timers** — start button is disabled after first click to prevent multiple countdown loops

---

## How It Works

### Timer Sequence
The classic Pomodoro Technique cycles through reps in this order:

```
work(1) → short break(2) → work(3) → short break(4) →
work(5) → short break(6) → work(7) → long break(8) → repeat
```

Odd reps are work rounds, even reps are short breaks, and every 8th rep is a long break.

### Rep Tracking Logic
```python
if reps % 8 == 0:       # long break
elif reps % 2 == 0:     # short break
else:                   # work round
```

### Rounds Until Long Break
```python
rounds_left = floor((8 - (reps % 8)) / 2)
```

| reps | rounds_left |
|------|-------------|
| 1    | 3 ✅        |
| 3    | 2 ✅        |
| 5    | 1 ✅        |
| 7    | 0 ✅        |

---

## Key Concepts

### `window.after()` — Non-Blocking Countdown
```python
# window.after(delay_ms, function, arg) schedules a function call without freezing the UI.
# Unlike time.sleep(), it works with tkinter's event loop keeping the window responsive.
def count_down(count):
    window.after(1000, count_down, count - 1)
```

`time.sleep()` freezes the entire tkinter window. `window.after()` schedules the next call while keeping the UI responsive. Each call to `count_down` schedules the next one, creating a recursive countdown loop.

### `highlightthickness=0` — Removing the Focus Border
```python
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
```

Tkinter draws a highlight border around widgets that have keyboard focus. Setting `highlightthickness=0` removes this border so the canvas renders flush with no extra visual frame — essential for clean drawing surfaces.

### String Formatting with `:02d`
```python
# :02d pads single digit numbers with a leading zero (e.g. 5 → "05")
canvas.itemconfig(timer_text, text=f"{count_minute:02d}:{count_second:02d}")
```

Without `:02d`, a count of 5 seconds would display as `"1:5"` instead of `"01:05"`.

### Disabling the Start Button
```python
# Disable start button on first click to prevent multiple window.after() loops
# from stacking up. Save window.after() return value to cancel on reset.
start_button.config(state="disabled")
```

Every click of Start launches a new countdown loop. Disabling the button after the first click prevents multiple loops from running simultaneously.

### Fixing Window Resize on Dynamic Text
```python
# timer_label.config(width=10) fixes the label width in character units so
# dynamic text changes don't cause the window to resize.
timer_label = Label(width=10, ...)
window.geometry("400x600")  # or lock with a fixed geometry
```

---

## Strong vs Dynamic Typing in Python

These are two separate but related concepts that describe how Python handles data types.

### Dynamic Typing
Variables are **not locked to a type** — they can be reassigned to a different type at runtime.

```python
# Dynamic Typing — same variable, different types
x = 0           # x is an int
print(type(x))  # <class 'int'>

x = "00"        # x is now a string — Python allows this
print(type(x))  # <class 'str'>
```

### Strong Typing
Python **will not silently convert incompatible types** for you. You must convert explicitly.

```python
count = 5

# ❌ raises TypeError — Python won't guess
result = count + "00"

# ✅ must convert explicitly
result = str(count) + "00"   # "500"
result = count + int("10")   # 15
```

Compare to JavaScript (weakly typed), which would silently return `"500"` without error.

### Both Concepts Together — Countdown Timer Example

```python
count_min = math.floor(count / 60)   # int — result of math operation
count_sec = count % 60               # int — result of modulo operation

if count_sec < 10:
    count_sec = f"0{count_sec}"      # str — variable reassigned from int to string

canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
```

- `count_sec` starts as an `int` from the modulo operation, then gets reassigned to a `str` inside the `if` block → **dynamic typing**
- Python would raise a `TypeError` if you tried to do math on `count_sec` after reassignment without converting back → **strong typing**

> **One-line summary:** Python is **dynamically typed** (variables can change type freely) but **strongly typed** (it won't mix incompatible types silently without explicit conversion).

---

## Future Enhancements

### Productivity / Functionality
- Sound alert when a timer ends
- Desktop notification when switching between work and break
- Daily/session statistics (total focus time, total breaks)
- Pause/resume button mid-countdown

### Customization
- Theme switcher — let the user choose from preset color themes via a listbox, radio button, or spinbox widget
- Custom font size or style selector
- Option to toggle the "rounds till long break" blurb on/off

### UX / Polish
- Keyboard shortcut to start/reset (e.g. spacebar)
- Animate the tomato or timer when a round completes
- Window always-on-top toggle so it floats above other apps

---

## Project Structure

```
├── main.py
├── tomato.png
└── README.md
```

---

## Requirements

- Python 3.x
- tkinter (included with standard Python installation)