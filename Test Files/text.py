from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from datetime import datetime, date, timedelta
from time import sleep
import tkinter as tk
from tkcalendar import DateEntry
from selenium.webdriver.chrome.options import Options
from tkinter import *
from tkcalendar import *
import datetime as dt
from multi_date_checker import multi_date_checker
from login_info import login_info
import sv_ttk
import tkinter
from tkinter import ttk
import customtkinter


# Create a function to get the selected value and close the window
####################################################################################################################
def on_submit():
    global start_time, end_time, check_days, appt_dates_list, appt_type, container_entry, username

    # Get the calendar values
    date_picker= cal.get_date()
    formatted_date = datetime.strptime(date_picker, '%m/%d/%y').date()
    # print(f'Selected Date {formatted_date}')
    
    # Get the check_days values from dropdowns
    check_days = check_day_var.get()
    appt_dates_list = [formatted_date + timedelta(days=i) for i in range(int(check_days))]
    # print(f'appt_dates_list: {appt_dates_list}\nthis is %d: {appt_dates_list[0].strftime("%d")}')

    # Get the selected time values from the dropdowns
    start_time = start_time_var.get()
    end_time = end_time_var.get()

    # Get the values of appointment type
    appt_type = appt_type_var.get()

    # # Get the values of container
    # container = container_var.get()
    
    # Get container entries
    data = container_entry.get("1.0", "end-1c")
    lines = data.split("\n")
    container_list.extend(lines)
    container_entry.delete("1.0", "end")
    print("Container List:")
    print(container_list)
    
    # Get Username value
    username = username_var.get()

    root.destroy()

# UI settings
####################################################################################################################
root = tkinter.Tk()
# Set theme
# sv_ttk.use_dark_theme()
sv_ttk.use_light_theme()
# root.title("Appointment Scheduler")
# root.geometry("500x500")

root.title("Appointment Scheduler")

# Get the screen width and height
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

# Calculate the x and y coordinates for the window to be centered
x = (screen_width - 500) // 2
y = (screen_height - 600) // 2

# Set the position of the window
root.geometry(f"500x600+{x}+{y}")


# Create a list of a times options
choose_time = [f'{i:02}:00' for i in range(24)]

# Create a list of a day options
check_day = [str(i) for i in range(1, 11)]

# Create a list of appointment type options
appt_types = ['IMPORT PICKUP', 'EMPTY DROPOFF']

# List to store container entries
container_list = []

# List of Username
username_info = ['p2','20','yuna','p1']

# # Create a list of date check method
# choose_method = ['Check Single Date', 'Check Multi Dates']

# Create labels and dropdowns for a calendar picker
# Label(root, text="Select The Appt Date:").grid(column=0, row=0, padx=10, pady=5)
cal = Calendar(root, selectmode="day")
cal.grid(column=1, row=0, padx=10, pady=5)

# # Create a label for containers
# Label(root, text="Container Number:").grid(column=0, row=1, padx=10, pady=5)
# container_var = StringVar(root)
# # container_var.set("Enter Container Number")
# container_input = ttk.Entry(root,textvariable=container_var)
# container_input.grid(column=1, row=1, padx=10, pady=5)

# Create a label for data entry
Label(root, text="Enter Container Number:").grid(column=0, row=1, padx=10, pady=5)
container_entry = customtkinter.CTkTextbox(root, height=160, width=200, border_width=1 ,border_color="lightgray" )
container_entry.grid(column=1, row=1, padx=10, pady=5)

# Create labels and dropdowns for APPOINTMENT TYPE
Label(root, text="Appointment Type:").grid(column=0, row=2, padx=10, pady=5)
appt_type_var = StringVar(root)
# appt_type_var.set("IMPORT PICKUP")
appt_type_dropdown = ttk.OptionMenu(root, appt_type_var, 'Appt Type', *appt_types)
#appt_type_dropdown.config(width=5)
appt_type_dropdown.grid(column=1, row=2, padx=10, pady=5)

# Create labels and dropdowns for start and end times
Label(root, text="Start Time: ").grid(column=0, row=3, padx=10, pady=5)
start_time_var = StringVar(root)
# start_time_var.set("From")
start_time_dropdown = ttk.OptionMenu(root, start_time_var, 'From', *choose_time)
start_time_dropdown.config(width=5)
start_time_dropdown.grid(column=1, row=3, padx=10, pady=5)

Label(root, text="End Time: ").grid(column=0, row=4, padx=10, pady=5)
end_time_var = StringVar(root)
# end_time_var.set("To")
end_time_dropdown = ttk.OptionMenu(root, end_time_var, 'To', *choose_time)
end_time_dropdown.config(width=5)
end_time_dropdown.grid(column=1, row=4, padx=10, pady=5)


# Label(root, text="Date Check Method: ").grid(column=0, row=3, padx=10, pady=5)
# date_check_method_var = StringVar(root)
# date_check_method_var.set("Select A Method")
# date_check_method_dropdown = OptionMenu(root, date_check_method_var, *choose_method)
# date_check_method_dropdown.grid(column=1, row=3, padx=10, pady=5)

Label(root, text="Check How Many Days: ").grid(column=0, row=5, padx=10, pady=5)
check_day_var = StringVar(root)
# check_day_var.set("1")
check_day_dropdown = ttk.OptionMenu(root, check_day_var, '1', *check_day)
check_day_dropdown.config(width=5)
check_day_dropdown.grid(column=1, row=5, padx=10, pady=5)

# Create Username Seclection
Label(root, text="Username: ").grid(column=0, row=6, padx=10, pady=5)
username_var = StringVar(root)
# check_day_var.set("1")
username_dropdown = ttk.OptionMenu(root, username_var, 'p2', *username_info)
username_dropdown.config(width=5)
username_dropdown.grid(column=1, row=6, padx=10, pady=5)

# Create submit button
# style = ttk.Style()
# style.configure('Blue.TButton', foreground='blue', background='white')
submit_button = customtkinter.CTkButton(root, width=60, text="OK", command=on_submit)
submit_button.grid(column=1, row=7, padx=10, pady=5)

# Start the mainloop to display the window
root.mainloop()

available_time_slots = [
    "",
    "",
    "07-Jun 09:00-09:29 (Current Openings: 5) (Canceled: 2)",
    "07-Jun 09:30-09:59 (Current Openings: 14)",
    "07-Jun 10:00-10:29 (Current Openings: 13) (Canceled: 2)",
    "07-Jun 10:30-10:59 (Current Openings: 12) (Canceled: 1)",
    "08-Jun 11:00-11:29 (Current Openings: 18) (Canceled: 3)",
    "08-Jun 11:30-11:59 (Current Openings: 25) (Canceled: 1)",
    "08-Jun 12:00-12:29 (Current Openings: 19)",
    "08-Jun 12:30-12:59 (Current Openings: 23)",
    "09-Jun 13:00-13:29 (Current Openings: 14)",
    "09-Jun 13:30-13:59 (Current Openings: 13)",
    "09-Jun 14:00-14:29 (Current Openings: 14)",
    "09-Jun 14:30-14:59 (Current Openings: 17)",
    "09-Jun 15:00-15:29 (Current Openings: 15) (Canceled: 1)"
]

# appt_dates = [appt_date[:2].strip() for appt_date in available_time_slots]
# print(appt_dates)

# # Check available times in selected range from start time to end time
# available_times = [time[6:12].strip() for time in available_time_slots if start_time <= time[6:12].strip() <= end_time]

available_appt_dates = [date[:2].strip() for date in available_time_slots]


# check appte dates
for appt_date in appt_dates_list:
    
    print(f"Checking...")
    print(f"Appt Date: {appt_date}\n") 

    # check if appte dates are in the available_appt_dates
    if appt_date.strftime("%d") in available_appt_dates:

        new_available_time_slots=[]
        
        print(f'****************************')
        print(f'***   Available Appts   ****')
        print(f'****************************')
        for available_date in available_time_slots:
            # Check if available date is available
            if available_date[:2].strip() == appt_date.strftime("%d"):
                new_available_time_slots.append(available_date)              
                print(f'***  {available_date[:19]} ***')
        print(f'****************************')
        # Check available times in selected range from start time to end time
        available_times = [time[6:12].strip() for time in new_available_time_slots if start_time <= time[6:12].strip() <= end_time]

        if available_times:
            print(f"\nSelected Appt Times From {start_time} to {end_time}")
            print(f'Available Times in Selected Range: {available_times}\n')
            print(f'Successful Booked Appt: {available_times[0]}\n')
            break
        else:
            print(f'\nAppt is Available\nBut No Appt Time in Selected Range From {start_time} to {end_time}\n')
    else:
        print(f'No Appt on {appt_date}')


print('Finished')