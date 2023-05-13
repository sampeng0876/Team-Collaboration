import tkinter as tk
from tkcalendar import DateEntry

# Define the options for the dropdown menu
#date_list = ['1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20','21','22','23','24','25','26','27','28','29','30','31']
time_slots_list_1 = ['00:00','01:00','02:00','03:00','04:00','05:00','06:00','07:00','08:00','09:00','10:00','11:00','12:00','13:00','14:00','15:00','16:00','17:00','18:00','19:00','20:00','21:00','22:00','23:00']
time_slots_list_2 = ['00:00','01:00','02:00','03:00','04:00','05:00','06:00','07:00','08:00','09:00','10:00','11:00','12:00','13:00','14:00','15:00','16:00','17:00','18:00','19:00','20:00','21:00','22:00','23:00']
available_time_slots = ['02','03','04','05','06','07','08','10']

# Create a function to get the selected value and close the window
def on_select():
    global date_picker, time_picker_1,time_picker_2
    date_picker = cal.get_date().strftime('%Y-%m-%d')
    time_picker_1 = var1.get()
    time_picker_2 = var2.get()
    
    root.destroy()

# Create the window
root = tk.Tk()

# Create a variable to store the selected option
var1 = tk.StringVar(root)
var2 = tk.StringVar(root)
# Set the default value of the dropdown
var1.set(time_slots_list_1[0])
var2.set(time_slots_list_2[0])

# Create the dropdown and add the options
dropdown1 = tk.OptionMenu(root, var1, *time_slots_list_1)
dropdown1.pack(padx=10, pady=10)
dropdown2 = tk.OptionMenu(root, var2, *time_slots_list_2)
dropdown2.pack(padx=10, pady=10)

# Create a calendar widget
cal = DateEntry(root)
cal.pack(padx=10, pady=10)

# Create a button to submit the selection and close the window
submit_button = tk.Button(root, text="Submit", command=on_select)
submit_button.pack(padx=10, pady=10)

# Start the mainloop to display the window
root.mainloop()

print(type(date_picker))
print("Selected " + date_picker)
print("Selected " + time_picker_1 + " to "+ time_picker_2)
appt_date = '9'
print(type(appt_date))
print("Available Times: " + str(available_time_slots))
for i in available_time_slots:
    # print([i], end=' ')
    # print(i, end=' ')
    # print(time_picker)   
    if i in range(0,23):
        print(i)
        print(time_picker_1[:2])
        print(time_picker_2[:2])
        print("Successfully Booked " + str(date_picker) + ' at ' + i  + ":00")
        break        
else: print("No Available Times from " + time_picker_1 + " to "+ time_picker_2)
    

    
