import sys
import os
from math import floor
from tkinter import *
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#CC4D90" # short break
RED = "#F1583F" # long break
GREEN = "#379B46" # work
BROWN = "#6B4825"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
check_marks = ""
reps = 0
timer = None #
# ---------------------------- Resource Path ------------------------------- #
def resource_path(relative_path):
    """Get the correct path to a resource whether running as script or exe."""
    if hasattr(sys, '_MEIPASS'):
        # PyInstaller extracts files here at runtime
        return os.path.join(sys._MEIPASS, relative_path)
    return os.path.join(os.path.abspath("."), relative_path)


# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    global check_marks, timer, reps
    window.after_cancel(timer)  # cancel any pending countdown
    start_button.config(state="normal") # enable start button
    timer_label.config(text="Click Start\nwhen ready\n ", fg=GREEN)
    canvas.itemconfig(timer_text, text="00:00")
    check_marks = ""
    check_label.config(text=check_marks)

    completed = floor(reps / 2)
    progress_label.config(text=f"🍅 {completed} pomodoros completed!", fg=GREEN)

    # lambda wraps the config() call so it's passed as a function reference to window.after()
    # and executes after the 5-second delay, rather than immediately at the time of the call
    window.after(5000, lambda: progress_label.config(text=""))

    # reset reps
    reps = 0

    # reset the entry durations
    work_entry.delete(0, END)
    work_entry.insert(0, "25")
    short_break_entry.delete(0, END)
    short_break_entry.insert(0, "5")
    long_break_entry.delete(0, END)
    long_break_entry.insert(0, "20")

# ---------------------------- TIMER MECHANISM ------------------------------- #


def start_timer():

    global reps, check_marks, WORK_MIN, SHORT_BREAK_MIN, LONG_BREAK_MIN

    # disable button after first click to prevent multiple countdown loops
    start_button.config(state="disabled")

    try:
        WORK_MIN = int(work_entry.get())
    except ValueError:
        WORK_MIN = 25
        work_entry.delete(0, END)
        work_entry.insert(0, "25")

    try:
        SHORT_BREAK_MIN = int(short_break_entry.get())
    except ValueError:
        SHORT_BREAK_MIN = 5
        short_break_entry.delete(0, END)
        short_break_entry.insert(0, "5")

    try:
        LONG_BREAK_MIN = int(short_break_entry.get())
    except ValueError:
        LONG_BREAK_MIN = 20
        long_break_entry.delete(0, END)
        long_break_entry.insert(0, "20")

    work_seconds = WORK_MIN * 60
    short_break_seconds = SHORT_BREAK_MIN * 60
    long_break_seconds = LONG_BREAK_MIN * 60

    reps += 1

    # calculate how many more work rounds until the next Long Break
    rounds_left = str(floor((8-(reps % 8))/2))

    # long break for every 8 reps (long break after 4 work timers and 3 short break timers)
    # w(1),sb(2),w(3),sb(4),w(5),sb(6),w(7),lb(8),w(9),sb(10),...,lb(16)
    if reps % 8 == 0: # 8,16,24,...
        window.lift()
        window.attributes("-topmost", True)
        window.attributes("-topmost", False)

        count_down(long_break_seconds)
        timer_label.config(text="Long Break\nYou earned it!\n ", fg=RED)
    # else if even (but not evenly divisible by 8), start short break timer
    elif reps % 2 == 0:
        window.lift()
        window.attributes("-topmost", True)
        window.attributes("-topmost", False)

        count_down(short_break_seconds)
        timer_label.config(text="Short Break\n \n ", fg=PINK)
    # else odd therefore start work timer
    else:
        count_down(work_seconds)
        timer_label.config(text = f"Work\n({rounds_left} more rounds\nfor a long break!)", fg = GREEN)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
# window.after(delay_ms, function, arg) schedules a function call without freezing the UI.
# Unlike time.sleep(), it works with tkinter's event loop keeping the window responsive.
def count_down(count):
    global check_marks, reps
    count_minute = floor(count/60)
    count_second = count % 60

    # String formatting (format specification)
    # :02d pads single digit numbers with a leading zero (e.g. 5 → "05")
    canvas.itemconfig(timer_text, text = f"{count_minute:02d}:{count_second:02d}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count -1)
    else:
        # Award checkmark only after a completed work round (odd reps). Capped at 4.
        if reps % 2 != 0:
            if len(check_marks) < 4:
                check_marks += "🍅"
            # Reset to one 🍅 (not empty) when cycle completes
            else:
                check_marks = "🍅"

            progress_label.config(text =f"({floor((reps + 1) / 2)} completed)")
            check_label.config(text=f"{check_marks}")
        start_timer()

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx = 10, pady = 15, bg=YELLOW)

# Frame for user input entries
left_frame = Frame(window, bg = YELLOW)
left_frame.grid(row =4, column = 0, columnspan=2, pady=10)

# User custom entries for durations
entry_title_label = Label(left_frame, text="Customize durations: ", font=(FONT_NAME,12, "bold"),  fg = BROWN, bg=YELLOW, highlightthickness=0)
work_entry_label = Label(left_frame, text="work (min): ", font=(FONT_NAME,12, "bold"),  fg = BROWN, bg=YELLOW, highlightthickness=0)
work_entry = Entry(left_frame, width=5, bg = "white")
work_entry.insert(END, string="25") # default value of 25

short_break_entry_label = Label(left_frame, text="short break (min): ", font=(FONT_NAME,12, "bold"),  fg = BROWN, bg=YELLOW, highlightthickness=0)
short_break_entry = Entry(left_frame, width=5, bg = "white")
short_break_entry.insert(END, string="5") # default value of 25

long_break_entry_label = Label(left_frame, text="long break (min): ", font=(FONT_NAME,12, "bold"),  fg = BROWN, bg=YELLOW, highlightthickness=0)
long_break_entry = Entry(left_frame, width=5, bg = "white")
long_break_entry.insert(END, string="20") # default value of 25

# Timer and Check labels
timer_label = Label(width = 15, text = "Click Start\nwhen ready\n ", font=(FONT_NAME,22, "bold"),fg = GREEN, bg=YELLOW, highlightthickness=0)
check_label = Label(text = "", font=(FONT_NAME,22, "bold"),fg = RED, bg=YELLOW, highlightthickness=0)
progress_label = Label(text ="", font=(FONT_NAME, 12, "bold"), fg = GREEN, bg=YELLOW, highlightthickness=0)
# Buttons
start_button = Button(text = "Start", command = start_timer, bg = "white", font = (FONT_NAME, 14, "bold"), highlightthickness=0)
reset_button = Button(text = "Reset", command = reset_timer, bg = "white", font = (FONT_NAME, 14, "bold"), highlightthickness=0)

# Tomato
canvas = Canvas(width=200, height=224, bg = YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file=resource_path("tomato.png"))
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text = "00:00", fill = "white", font = (FONT_NAME, 40, "bold"))


# window.update() + resizable(False, False) freezes at content-calculated size.
window.update() # let tkinter calculate dimensions first
window.resizable(False, False)



# Grid
# left_Frame is anchored to row 1 column 0 of the main grid
# frame has its own grid
entry_title_label.grid(row = 0, column = 0, columnspan=2)
work_entry_label.grid(row = 1, column = 0, sticky = "e")
work_entry.grid(row = 1, column = 1)

short_break_entry_label.grid(row = 2, column = 0, sticky = "e")
short_break_entry.grid(row = 2, column = 1)

long_break_entry_label.grid(row = 3, column = 0, sticky = "e")
long_break_entry.grid(row = 3, column = 1)

# main grid
timer_label.grid(row = 0, rowspan = 2, column = 0, columnspan=2, sticky = "nsew")
canvas.grid(row = 2, column = 0, columnspan=2, padx=50, pady=25,)
start_button.grid(row = 3, column = 0)
reset_button.grid(row = 3, column =1)
check_label.grid(row = 5, column = 0, columnspan=3, sticky = "ew")
progress_label.grid(row = 6, column = 0, columnspan=3, sticky ="ew")

window.mainloop()