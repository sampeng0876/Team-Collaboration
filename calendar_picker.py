import tkinter as tk
from tkinter import ttk
from tkcalendar import DateEntry

# Create a list of options for the dropdown
options = ["Option 1", "Option 2", "Option 3", "Option 4"]

# Create a function to get the selected value and close the window
def on_select():
    print("Selected option:", var.get())
    print("Selected date:", cal.get_date())
    root.destroy()

# Create the window
root = tk.Tk()

# Create a variable to store the selected option
var = tk.StringVar(root)

# Set the default value of the dropdown
var.set(options[0])

# Create the dropdown and add the options
dropdown = tk.OptionMenu(root, var, *options)
dropdown.pack()

# Create a calendar widget
cal = DateEntry(root)
cal.pack()

# Create a button to submit the selection and close the window
submit_button = tk.Button(root, text="Submit", command=on_select)
submit_button.pack()

# Start the mainloop to display the window
root.mainloop()
