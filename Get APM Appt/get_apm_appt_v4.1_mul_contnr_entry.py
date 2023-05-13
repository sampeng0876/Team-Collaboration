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
import sv_ttk
import tkinter
from tkinter import ttk
import customtkinter


# Create a function to get the selected value and close the window
def on_submit():
    global date_picker, start_time, end_time, check_days, appt_dates, appt_type, container_entry, username
    # date_picker = cal.get_date().strftime('%Y-%m-%d')
    # date_picker = cal.get_date()  # Assuming cal.get_date() returns the date string '5/9/23'
    # date_string = cal.get_date()  # Assuming cal.get_date() returns the date string '5/9/23'
    # date_object = datetime.strptime(date_string, '%m/%d/%y')
    # date_picker = date_object.strftime('%Y-%m-%d')
    # print(type(date_picker))
    # print(date_picker)

    # Get the calendar values
    formatted_date = cal.get_date()
    date_picker = datetime.strptime(formatted_date, '%m/%d/%y').date()
    # Get the check_days values from dropdowns
    check_days = check_day_var.get()
    appt_dates = [date_picker + timedelta(days=i) for i in range(int(check_days))]
    # print(appt_dates)
    
    # Get the selected time values from the dropdowns
    start_time_1 = start_time_var.get()
    end_time_2 = end_time_var.get()

    # Get the values of appointment type
    appt_type = appt_type_var.get()

    # # Get the values of container
    # container = container_var.get()

    # Check if the selected time range is available
    start_time = start_time_1
    end_time = end_time_2
    
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
username_info = ['20','yuna','p1']

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
username_dropdown = ttk.OptionMenu(root, username_var, '20', *username_info)
username_dropdown.config(width=5)
username_dropdown.grid(column=1, row=6, padx=10, pady=5)

# Create submit button
# style = ttk.Style()
# style.configure('Blue.TButton', foreground='blue', background='white')
submit_button = customtkinter.CTkButton(root, width=60, text="OK", command=on_submit)
submit_button.grid(column=1, row=7, padx=10, pady=5)

# Start the mainloop to display the window
root.mainloop()


# chrome_options = Options()
# # #chrome_options.add_argument("--disable-extensions")
# # #chrome_options.add_argument("--disable-gpu")
# chrome_options.add_argument("--headless")

# # Set the options to run the browser in headless mode
# chrome_options.headless = True

# driver = webdriver.Chrome(options=chrome_options)
chrome_options = webdriver.ChromeOptions()
# chrome_options.add_argument('--headless')


driver = webdriver.Chrome(options=chrome_options)

driver.maximize_window()
wait = WebDriverWait(driver, 10)
driver.get("https://termpoint.apmterminals.com")
# Container Number
# ctnrno = 'TGHU6723051'

# print(date_picker)
# print(type(date_picker))
# appt_date = date_picker

# print(apptdate)
# print(type(apptdate))
# appt_date = date.today()
# print(appt_date)
# print(type(appt_date))

if username == 'p1':
    driver.find_element(By.XPATH, '//*[@id="Login_form"]/div[1]/div/div/input').send_keys("P1logistics")

    driver.find_element(By.XPATH, '//*[@id="Login_form"]/div[2]/div/div/input').send_keys("P1log5418")

elif username == '20':
    driver.find_element(By.XPATH, '//*[@id="Login_form"]/div[1]/div/div/input').send_keys("twenty")
    driver.find_element(By.XPATH, '//*[@id="Login_form"]/div[2]/div/div/input').send_keys("20Trans!")

elif username == 'yuna':
    driver.find_element(By.XPATH, '//*[@id="Login_form"]/div[1]/div/div/input').send_keys("wcofreightinc@gmail.com")

    driver.find_element(By.XPATH, '//*[@id="Login_form"]/div[2]/div/div/input').send_keys("Seawolf321!")

driver.find_element(By.XPATH, '//*[@id="Login_form"]/div[3]/div/button').click()

####################################################################################################################
check_container = 0
while True:
    
    if check_container < len(container_list) :
    # Wait for the page to load Wait schedule
        WebDriverWait(driver, 15).until( 
            EC.presence_of_all_elements_located((By.XPATH, '//*[@id="menu-sec"]/a[3]'))
        )
        # Schedule a new appointment
        driver.find_element(By.XPATH,'//*[@id="menu-sec"]/a[3]').click() 
        # driver.find_element(By.XPATH,'//*[@id="main-container"]/div/div/div/div/div[1]/div[1]/div[1]/button').click() 
        sleep(1)

        #Appt Type
        driver.find_element(By.XPATH,'//*[@id="ApptTypeDdDv"]').click() 
        sleep(1)


        if appt_type == 'IMPORT PICKUP':
            # IMPORT PICKUP
            driver.find_element(By.XPATH,'//*[@id="ApptTypeDdDv"]/div/div[2]/div[1]').click() 

        elif appt_type =='EMPTY DROPOFF':
            # EMPTY DROPOFF
            driver.find_element(By.XPATH,'//*[@id="ApptTypeDdDv"]/div/div[2]/div[4]').click()
        sleep(1)
        
        # Empty Container#
        driver.find_element(By.XPATH,'//*[@id="containerName"]').send_keys(container_list[check_container]) 
        container_number = container_list[check_container]

        # Submit
        driver.find_element(By.XPATH,'//*[@id="formcontent"]/form/div[2]/div[2]/button').click() 
        sleep(2)

        #OWN CHASSIS?
        driver.find_element(By.XPATH,'//*[@id="ipgrid_0_own_chassis?"]/i').click()
        sleep(1)

        #NO
        driver.find_element(By.XPATH,'//*[@id="ipgrid_0_own_chassis?"]/div[2]/div[2]/span').click()
        sleep(1)

        # Call out multi_date_checker
        multi_date_checker (appt_dates, wait, start_time, end_time, driver, check_days, container_number)

        # if date_check_method == 'Check Single Date':
        #     # Sinle Date Checker
        #     single_date_checker(appt_dates, wait, start_time, end_time, driver, date_picker)
        # elif date_check_method == 'Check Multi Dates':
        #     # Multiple Dates Checker
        #     multi_date_checker (appt_dates, wait, start_time, end_time, driver)        
        #print(check_container)          
    if check_container == len(container_list):
        break
    else: check_container+=1
        

print("Done")


# Close the browser
driver.quit()