# https://github.com/rdbende/Sun-Valley-ttk-theme
# import tkinter
# from tkinter import ttk
# import sv_ttk

# root = tkinter.Tk()

# button = ttk.Button(root, text="Button")
# button.pack()

# sv_ttk.use_dark_theme()
# sv_ttk.use_light_theme()

# root.mainloop()

# import tkinter
# from tkinter import ttk
# import sv_ttk

# root = tkinter.Tk()

# button = ttk.Button(root, text="Button")
# button.pack()

# sv_ttk.set_theme("dark")

# root.mainloop()


# import tkinter
# from tkinter import ttk

# import sv_ttk

# root = tkinter.Tk()

# button = ttk.Button(root, text="Toggle theme", command=sv_ttk.toggle_theme)
# button.pack()

# root.mainloop()



import tkinter
from tkinter import ttk
import tkinter as tk
import sv_ttk


root = tk.Tk()

# Pack a big frame so, it behaves like the window background
big_frame = ttk.Frame(root)
big_frame.pack(fill="both", expand=True)



# Set the initial theme
root.tk.call("source", "azure.tcl")
root.tk.call("set_theme", "light")

def change_theme():
    # NOTE: The theme's real name is azure-<mode>
    if root.tk.call("ttk::style", "theme", "use") == "azure-dark":
        # Set light theme
        root.tk.call("set_theme", "light")
    else:
        # Set dark theme
        root.tk.call("set_theme", "dark")

# Remember, you have to use ttk widgets
button = ttk.Button(big_frame, text="Change theme!", command=change_theme)
button.pack()

root.mainloop()