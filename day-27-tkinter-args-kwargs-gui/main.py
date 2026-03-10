# A good rule of thumb for tkinter structure:
#
#   Tk() — create the window
#   Define functions/callbacks
#   Create widgets
#   Pack/grid widgets
#   mainloop() — start the event loop


# tkinter = "Tk interface" — it's just a Python wrapper around the Tcl/Tk C library.
# Tcl/Tk is the foundation that Python's tkinter module is built on.
# Tcl (Tool Command Language) — a scripting language created by John Ousterhout at UC Berkeley in 1988.
#   Lightweight, string-based, embeddable.
# Tk — a GUI toolkit built on top of Tcl, added in 1991. Provides the actual widgets (buttons, labels, windows, etc.).

# NOTE: tkinter functions often use **kwargs (keyword arguments) internally,
# which means the IDE can't statically inspect the expected parameters.
# This is why hovering over a tkinter function doesn't show the usual
# parameter hint popup — the function signature just shows **kw or **kwargs,
# so the editor has nothing specific to display. You'll need to rely on
# the tkinter docs or print(help(widget)) to see available options.
# https://docs.python.org/3/library/tkinter.html#

from tkinter import *

MIN_WIDTH = 500
MIN_HEIGHT = 500

# Create the window FIRST before any widgets
window = Tk()
window.title("My First GUI Program")
window.minsize(width = MIN_WIDTH, height = MIN_HEIGHT)
window.config(padx = 20, pady = 20)
# Button
def button_clicked():
    my_label.config(text = input.get())

button1 = Button(text = "Button1", command = button_clicked)
button2 = Button(text = "Button2", command = button_clicked)
# Label
my_label = Label(text = "This is the label", font=("Arial", 24, "bold"))
my_label.config(padx = 10, pady = 10)
# Entry
input = Entry(width = 10)
print(input.get())

# pack  — stacks widgets in order (top to bottom or left to right).
#          simple but limited control over exact positioning.

# place — positions widgets at exact x/y coordinates.
#          full control, but tedious and doesn't scale with window resizing.

# grid  — organizes widgets in rows and columns like a table.
#          best for complex layouts, most commonly used in real projects.
# Can't mix pack and grid!

# Pack
# my_label.pack(side = "left")
# button.pack()
# input.pack(side = "left")

# Place (0,0) is in the top left corner
# my_label.place(x = 100, y=200)

# Grid
my_label.grid(column = 0, row = 0)
button1.grid(column=1, row = 1)
button2.grid(column=2, row = 0)
input.grid(column=3, row = 2)

window.mainloop() # always at the end

