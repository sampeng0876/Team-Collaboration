# import tkinter as tk
# import customtkinter


# # Theme settings
# customtkinter.set_appearance_mode("default") # mode: dark, light, system, default
# customtkinter.set_default_color_theme("dark-blue") # color: dark-blue, green

# root = customtkinter.CTk()
# # root.geometry("500x350")

# # Get the screen width and height
# screen_width = root.winfo_screenwidth()
# screen_height = root.winfo_screenheight()

# # Calculate the x and y coordinates for the window to be centered
# x = (screen_width - 500) // 2
# y = (screen_height - 600) // 2

# # Set the position of the window
# root.geometry(f"500x350+{x}+{y}")

# def login():
#     global username, password
#     username = username_input.get()
#     password = password_input.get()

#     print (username)
#     print (password)
#     # root.destroy()

# frame = customtkinter.CTkFrame(master=root)
# frame.pack(pady=20, padx=60, fill="both", expand=True)

# label = customtkinter.CTkLabel(master=frame, text="Login System",font=("Roboto", 24,'bold'))
# label.pack(pady=12, padx=10)

# username_input = customtkinter.CTkEntry(master=frame, placeholder_text="Username")
# username_input.pack(pady=12, padx=10)

# password_input = customtkinter.CTkEntry(master=frame, placeholder_text="Password", show="*")
# password_input.pack(pady=12, padx=10)

# button = customtkinter.CTkButton(master=frame, text="Login", command=login)
# button.pack(pady=12, padx=10)

# checkbox = customtkinter.CTkCheckBox(master=frame, text="Remember Me")
# checkbox.pack(pady=12, padx=18)


# root.mainloop()



# # Create a new window
# window = tk.Tk()

# # Set the window title
# window.title("Login")

# # Create a label to display instructions to the user
# label = tk.Label(window, text="User Name:")
# label.pack()

# # Create a text box for the user to enter their input
# entry = tk.Entry(window)
# entry.pack()

# # Create a variable to hold the user input
# user_input = ""

# # Create a function to handle the input submission
# def submit_input():
#     global user_input  # Use the global keyword to modify the global variable
#     user_input = entry.get()  # Get the text entered in the text box
#     window.destroy()  # Close the window

# # Create a button to submit the input
# button = tk.Button(window, text="Submit", command=submit_input)
# button.pack()

# # Start the main loop to display the window and wait for the user to enter input
# window.mainloop()

# # Print the user input after the window is closed
# print("User input:", user_input)

import tkinter as tk
import customtkinter
import random

# Theme settings
customtkinter.set_appearance_mode("default") # mode: dark, light, system, default
customtkinter.set_default_color_theme("dark-blue") # color: dark-blue, green

root = customtkinter.CTk()

# Get the screen width and height
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

# Calculate the x and y coordinates for the window to be centered
x = (screen_width - 500) // 2
y = (screen_height - 600) // 2

# Set the position of the window
root.geometry(f"500x350+{x}+{y}")

def generate_random_data():
    usernames = ['user1', 'user2', 'user3', 'user4', 'user5']
    passwords = ['password1', 'password2', 'password3', 'password4', 'password5']
    return random.choice(usernames), random.choice(passwords)

def validate_login():
    entered_username = username_input.get()
    entered_password = password_input.get()

    valid_username, valid_password = generate_random_data()

    if entered_username == valid_username and entered_password == valid_password:
        print("Login successful!")
        # Perform any desired action for successful login
    else:
        print("Username or password is invalid, please try again")
        password_input.delete(0, tk.END)
        password_input.configure(validate="key", validatecommand=(root.register(show_alert), '%P'))

def show_alert(password):
    if password:
        root.after(0, root.bell)
        root.after(0, lambda: password_input.configure(validate="none"))

frame = customtkinter.CTkFrame(master=root)
frame.pack(pady=20, padx=60, fill="both", expand=True)

label = customtkinter.CTkLabel(master=frame, text="Login System", font=("Roboto", 24, 'bold'))
label.pack(pady=12, padx=10)

username_input = customtkinter.CTkEntry(master=frame, placeholder_text="Username")
username_input.pack(pady=12, padx=10)

password_input = customtkinter.CTkEntry(master=frame, placeholder_text="Password", show="*")
password_input.pack(pady=12, padx=10)

button = customtkinter.CTkButton(master=frame, text="Login", command=validate_login)
button.pack(pady=12, padx=10)

checkbox = customtkinter.CTkCheckBox(master=frame, text="Remember Me")
checkbox.pack(pady=12, padx=18)

root.mainloop()
