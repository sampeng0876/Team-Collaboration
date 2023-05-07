import tkinter as tk

# Create a new window
window = tk.Tk()

# Set the window title
window.title("Input")

# Create a label to display instructions to the user
label = tk.Label(window, text="Please enter your input:")
label.pack()

# Create a text box for the user to enter their input
entry = tk.Entry(window)
entry.pack()

# Create a variable to hold the user input
user_input = ""

# Create a function to handle the input submission
def submit_input():
    global user_input  # Use the global keyword to modify the global variable
    user_input = entry.get()  # Get the text entered in the text box
    window.destroy()  # Close the window

# Create a button to submit the input
button = tk.Button(window, text="Submit", command=submit_input)
button.pack()

# Start the main loop to display the window and wait for the user to enter input
window.mainloop()

# Print the user input after the window is closed
print("User input:", user_input)
