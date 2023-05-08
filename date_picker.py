import tkinter as tk
from tkcalendar import DateEntry

# Define the options for the dropdown menu
#date_list = ['1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20','21','22','23','24','25','26','27','28','29','30','31']
time_slots_list = ['00','01','02','03','04','05','06','07','08','09','10','11','12','13','14','15','16','17','18','19','20','21','22','23']

# Create a function to get the selected value and close the window
def on_select():
    global date_picker, time_picker
    date_picker = cal.get_date().strftime('%Y-%m-%d')
    time_picker = var.get()
    
    root.destroy()

# Create the window
root = tk.Tk()

# Create a variable to store the selected option
var = tk.StringVar(root)

# Set the default value of the dropdown
var.set(time_slots_list[0])

# Create the dropdown and add the options
dropdown = tk.OptionMenu(root, var, *time_slots_list)
dropdown.pack()

# Create a calendar widget
cal = DateEntry(root)
cal.pack()

# Create a button to submit the selection and close the window
submit_button = tk.Button(root, text="Submit", command=on_select)
submit_button.pack()

# Start the mainloop to display the window
root.mainloop()


available_time_slots = ['02','03','04','05','06','07','08']

print(type(date_picker))
print("Selected " + date_picker[-2:])
print("Selected " + time_picker + ":00")
appt_date = '9'
print(type(appt_date))
for i in available_time_slots:
    # print([i], end=' ')
    # print(i, end=' ')
    # print(time_picker)   
    if i == time_picker:
        #print(i)
        print("Successfully Booked " + str(date_picker) + ' at ' + i  + ":00")
        break        
else: print(time_picker + ":00" + " is Not Available")
    

    
