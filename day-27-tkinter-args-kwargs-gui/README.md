# Day 27 – Tkinter, *args, **kwargs & GUI Programming

## Topics Covered

- Tcl/Tk GUI toolkit and how `tkinter` wraps it
- `*args` and `**kwargs` — flexible function parameters
- Building a GUI app with tkinter widgets and grid layout

---

## What is Tcl/Tk?

**Tcl** (Tool Command Language) and **Tk** are two paired technologies that form the foundation of Python's `tkinter` module.

- **Tcl** — a lightweight scripting language created by John Ousterhout at UC Berkeley in **1988**
- **Tk** — a GUI toolkit built on top of Tcl, added in **1991**, that provides widgets like buttons, labels, and windows

## How Python Fits In

`tkinter` ("Tk interface") is simply a Python wrapper around the Tcl/Tk C library.

```
Your Python code
      ↓
  tkinter (Python module)
      ↓
  _tkinter (C extension)
      ↓
  Tcl/Tk (C library)
      ↓
  Native OS window system (Windows / macOS / X11)
```

> Tkinter quirks that feel un-Pythonic are inherited from Tcl's original design.

## Key Design Concepts

| Concept | Description |
|---|---|
| **Widget-based** | Everything is a widget with a parent path (e.g. `.window.frame.button`) |
| **Geometry managers** | `pack`, `grid`, and `place` handle layout instead of pixel-positioning |
| **Event loop** | `mainloop()` hands control to Tk to listen for clicks, keypresses, etc. |
| **Cross-platform** | Uses native OS APIs — same code runs on Windows, macOS, and Linux |

## Geometry Managers

| Manager | Description |
|---|---|
| `pack` | Stacks widgets in order. Simple but limited control over positioning. |
| `place` | Positions widgets at exact x/y coordinates. Full control but doesn't scale with resizing. |
| `grid` | Organizes widgets in rows and columns like a table. Best for complex layouts. |

## Why It's Bundled with Python

Tk was chosen as Python's standard GUI toolkit in the early 1990s because it was cross-platform, lightweight, embeddable, and open source. It ships with CPython, so `import tkinter` works with no installation required.

## Tradeoffs

| ✅ Strengths | ❌ Limitations |
|---|---|
| Zero install, ships with Python | Widgets look dated by default |
| Simple API, great for learning | Not ideal for complex/modern UIs |
| Cross-platform | Less actively developed than Qt/wxPython |
| Lightweight | Limited built-in widget variety |

---

## **kwargs Notes

tkinter functions use `**kwargs` internally, which is why IDEs don't show parameter hint popups on hover — the signature just shows `**kw`. Use `print(help(widget))` or the tkinter docs to see available options.

Default values can be set two equivalent ways:

```python
# Option 1 — in the function signature (IDE-friendly)
def __init__(self, color="blue", size=12):
    self.color = color

# Option 2 — in .get() when using **kwargs (more flexible)
def __init__(self, **kwargs):
    self.color = kwargs.get("color", "blue")
```

Option 1 gives IDE autocomplete. Option 2 is why tkinter uses `**kwargs` — widgets have too many optional parameters to list explicitly.

## Useful tkinter Patterns

```python
# Set multiple attributes at once with .config()
button.config(text="Click me", bg="blue", fg="white", font=("Arial", 12))

# IntVar() — links a checkbox state to a Python-trackable variable
is_checked = IntVar()
checkbutton = Checkbutton(root, text="Subscribe", variable=is_checked)
print(is_checked.get())  # 0 = unchecked, 1 = checked
```

---

## Project — Miles to Kilometers Converter

A GUI app that takes a miles input and converts it to kilometers on button click.

**Conversion formula:** `km = miles × 1.60934`

**Layout (3-column grid):**

| Column 0 | Column 1 | Column 2 |
|---|---|---|
| | Entry (miles input) | "Miles" label |
| "is equal to" label | km result label | "Km" label |
| | Calculate button | |

### Key Concepts Used
- `Tk()` must be created before any widgets
- `columnconfigure(weight=1)` allows columns to expand on window resize
- `sticky="ew"` stretches widgets to fill their grid cell
- `Entry.get()` returns a string — wrap in `float()` for math, `str()` to display back
- `mainloop()` always goes last