import smart_do_V2_local
import kilroy_do_V2_local
import pcl_do_V2_local
import pg_do_V2_local
import uwe_do_V2_local
import wlg_do_V2_local
import unnyeo_do_V2_local
import qz_do_V2_local
import nypp_do_V2_local
import csn_do_V2_local

from tkinter import *
from tkcalendar import *
import datetime as dt
import sv_ttk
import tkinter
from tkinter import ttk
import customtkinter

def on_submit():
    global extract_do
    
    # Get Username value
    extract_do = extract_do_var.get()

    root.destroy()

# UI settings
####################################################################################################################
root = tkinter.Tk()
# Set theme
# sv_ttk.use_dark_theme()
sv_ttk.use_light_theme()
# root.title("Appointment Scheduler")
# root.geometry("500x500")extract_do

root.title("Appointment Scheduler")

# Get the screen width and height
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

# Calculate the x and y coordinates for the window to be centered
x = (screen_width - 230) // 2
y = (screen_height - 100) // 2

# Set the position of the window
root.geometry(f"230x100+{x}+{y}")

# List of Username
extract_do_info = ['SMART','UWE','PCL','PG','QZ','QZ_ATLANTA','UNNYEO','UNNYEO_2','WLG','4CSN','NYPP','KILROY','EZ']


# Create Username Seclection
Label(root, text="Record Task: ").grid(column=0, row=6, padx=10, pady=5)
extract_do_var = StringVar(root)
# check_day_var.set("1")
extract_do_dropdown = ttk.OptionMenu(root, extract_do_var, 'SMART', *extract_do_info)
extract_do_dropdown.config(width=8)
extract_do_dropdown.grid(column=1, row=6, padx=10, pady=5)

# Create submit button
# style = ttk.Style()
# style.configure('Blue.TButton', foreground='blue', background='white')
submit_button = customtkinter.CTkButton(root, width=60, text="OK", command=on_submit)
submit_button.grid(column=1, row=7, padx=10, pady=5)

# Start the mainloop to display the window
root.mainloop()


if extract_do == 'SMART':
    smart_do_V2_local.scan_and_process_files()
elif extract_do == 'UWE':
    uwe_do_V2_local.scan_and_process_files()
elif extract_do == 'PCL':
    pcl_do_V2_local.scan_and_process_files()
elif extract_do == 'PG':
    pg_do_V2_local.scan_and_process_files()
elif extract_do == 'QZ':
    qz_do_V2_local.scan_and_process_files()
elif extract_do == 'UNNYEO':
    unnyeo_do_V2_local.scan_and_process_files()
elif extract_do == 'NYPP':
    nypp_do_V2_local.scan_and_process_files()
elif extract_do == 'WLG':
    wlg_do_V2_local.scan_and_process_files()
elif extract_do == '4CSN':
    csn_do_V2_local.scan_and_process_files()
else: print(f"{extract_do} Not Exist ! ! !")
