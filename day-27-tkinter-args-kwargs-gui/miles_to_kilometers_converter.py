from tkinter import *

# Create the window FIRST before any widgets
mtokm_window = Tk()
mtokm_window.title("Miles to Kilometers Converter")
mtokm_window.config(padx = 20, pady = 20)
mtokm_window.columnconfigure(0, weight=1)  # ← here
mtokm_window.columnconfigure(1, weight=1)
mtokm_window.columnconfigure(2, weight=1)

# Button definition
def calculate():
    # km = miles * 1.60934
    if input_miles.get():
        km = round(float(input_miles.get()) * 1.60934, 2)
        km_result.config(text = str(km))

# labels
is_equal_to_label = Label(text = "is equal to", font=("Arial", 14, "normal"), anchor="e")
miles_label = Label(text = "Miles", font=("Arial", 14, "normal"), anchor="w")
km_label = Label(text = "Km", font=("Arial", 14, "normal"), anchor="w")
km_result = Label(text= "0", font=("Arial", 14, "normal"), anchor="center")

# input box
input_miles = Entry(width=10)

# Button
calculate_button = Button(text = "Calculate", command = calculate)

# Grid out the widgets
is_equal_to_label.grid(column=0,row=1, sticky="ew")
input_miles.grid(column=1,row=0, padx = 10, sticky="ew")
km_result.grid(column=1,row=1, padx = 10, sticky="ew")
calculate_button.grid(column=1,row=2, padx = 10, pady = 5)
miles_label.grid(column=2,row=0, sticky="ew")
km_label.grid(column=2,row=1, sticky="ew")

mtokm_window.mainloop() # always at the end

