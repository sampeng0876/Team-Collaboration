import tkinter as tk
from tkcalendar import DateEntry

def on_submit():
    # Get the selected values from the dropdowns
    start_time_1 = dropdown_var1.get()
    end_time_2 = dropdown_var2.get()

    # Check if the selected time range is available
    start_time = start_time_1
    end_time = end_time_2
    available_times = [time for time in available_time_slots if start_time <= time <= end_time]
    
    # Check if there are any available times
    if available_times:
        # Choose the earliest available time
        chosen_time = available_times[0]
        
        # Print available times
        print(available_time_slots)
        # Print a success message

        print(f"The Earliest is : {chosen_time}")
        root.destroy()
    else:
        print(f"No available times in the selected range {start_time} to {end_time}.")
        root.destroy()
    

# Create two lists with values from '00:00' to '23:00'
hours = [f'{i:02}:00' for i in range(24)]
hours2 = [f'{i:02}:00' for i in range(24)]

# Create a list of available times
available_time_slots = ['00:30','02:00', '03:00', '04:00', '08:00', '10:00']

# Create a root using Tkinter
root = tk.Tk()

# Create two dropdowns and add the values from the lists to them
dropdown_var1 = tk.StringVar(value='00:00')
dropdown1 = tk.OptionMenu(root, dropdown_var1, *hours)
dropdown1.pack()
dropdown_var2 = tk.StringVar(value='00:00')
dropdown2 = tk.OptionMenu(root, dropdown_var2, *hours2)
dropdown2.pack()

# Create a submit button
submit_button = tk.Button(root, text="Submit", command=on_submit)
submit_button.pack()

# Start the main event loop for the root
root.mainloop()
