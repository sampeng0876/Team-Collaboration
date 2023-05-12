from tkinter import *

root = Tk()
root.title("Data Entry")

# Get the screen width and height
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

# Calculate the x and y coordinates for the window to be centered
x = (screen_width - 500) // 2
y = (screen_height - 500) // 2

# Set the position of the window
root.geometry(f"500x500+{x}+{y}")

# List to store container data
container_list = []

# Function to handle button click and retrieve the entered data
def retrieve_data():
    data = container_entry.get("1.0", "end-1c")
    lines = data.split("\n")
    container_list.extend(lines)
    container_entry.delete("1.0", "end")
    print(type(container_list))
    print(type(container_list[0]))
    a = "type"
    print(type(a))
    print("Container List:")
    print(container_list)
    root.destroy()

# Create a label for data entry
Label(root, text="Enter Data:").pack(pady=10)

# Create a Text widget for data entry
container_entry = Text(root, height=10, width=40)
container_entry.pack(pady=5)

# Create a button to retrieve the entered data
button = Button(root, text="Retrieve Data", command=retrieve_data)
button.pack(pady=10)

root.mainloop()
