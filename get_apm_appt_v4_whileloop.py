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
from single_date_checker import single_date_checker
from multi_date_checker import multi_date_checker
# Create a function to get the selected value and close the window
def on_submit():
    global date_picker, start_time, end_time, date_check_method
    # date_picker = cal.get_date().strftime('%Y-%m-%d')
    # date_picker = cal.get_date()  # Assuming cal.get_date() returns the date string '5/9/23'
    # date_string = cal.get_date()  # Assuming cal.get_date() returns the date string '5/9/23'
    # date_object = datetime.strptime(date_string, '%m/%d/%y')
    # date_picker = date_object.strftime('%Y-%m-%d')
    # print(type(date_picker))
    # print(date_picker)
    formatted_date = cal.get_date()
    date_picker = datetime.strptime(formatted_date, '%m/%d/%y').date()
    

    
    # Get the selected values from the dropdowns
    start_time_1 = start_time_var.get()
    end_time_2 = end_time_var.get()

    # Check if the selected time range is available
    start_time = start_time_1
    end_time = end_time_2

    # Get the check time method values from dropdowns
    date_check_method = date_check_method_var.get()
    
    
    root.destroy()

root = Tk()
root.title("Appointment Scheduler")
root.geometry("500x500")

# Create a list of a times options
choose_time = [f'{i:02}:00' for i in range(24)]

# Create a list of date check method
choose_method = ['Check Single Date', 'Check Multi Dates']
# create a calendar picker
cal = Calendar(root, selectmode="day")
cal.grid(column=1, row=0, padx=10, pady=5)

# Create labels and dropdowns for start and end times
Label(root, text="Start Time: ").grid(column=0, row=1, padx=10, pady=5)
start_time_var = StringVar(root)
start_time_var.set("Select Start Time")
start_time_dropdown = OptionMenu(root, start_time_var, *choose_time)
start_time_dropdown.grid(column=1, row=1, padx=10, pady=5)

Label(root, text="End Time: ").grid(column=0, row=2, padx=10, pady=5)
end_time_var = StringVar(root)
end_time_var.set("Select End Time")
end_time_dropdown = OptionMenu(root, end_time_var, *choose_time)
end_time_dropdown.grid(column=1, row=2, padx=10, pady=5)


Label(root, text="Date Check Method: ").grid(column=0, row=3, padx=10, pady=5)
date_check_method_var = StringVar(root)
date_check_method_var.set("Select A Method")
date_check_method_dropdown = OptionMenu(root, date_check_method_var, *choose_method)
date_check_method_dropdown.grid(column=1, row=3, padx=10, pady=5)


# Create submit button
submit_button = Button(root, text="Submit", command=on_submit)
submit_button.grid(column=1, row=4, padx=10, pady=5)

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
ctnrno = 'TGHU6723051'

# print(date_picker)
# print(type(date_picker))
appt_date = date_picker

# print(apptdate)
# print(type(apptdate))
# appt_date = date.today()
# print(appt_date)
# print(type(appt_date))
driver.find_element(By.XPATH, '//*[@id="Login_form"]/div[1]/div/div/input').send_keys("twenty")

driver.find_element(By.XPATH, '//*[@id="Login_form"]/div[2]/div/div/input').send_keys("20Trans!")

# Yuna
# driver.find_element(By.XPATH, '//*[@id="Login_form"]/div[1]/div/div/input').send_keys("wcofreightinc@gmail.com")

# driver.find_element(By.XPATH, '//*[@id="Login_form"]/div[2]/div/div/input').send_keys("Magnolia321!")

driver.find_element(By.XPATH, '//*[@id="Login_form"]/div[3]/div/button').click()

# Wait schedule
WebDriverWait(driver, 15).until( 
    EC.presence_of_all_elements_located((By.XPATH, '//*[@id="main-container"]/div/div/div/div/div[1]/div[1]/div[1]/button'))
)
#Schedule a new appointment
driver.find_element(By.XPATH,'//*[@id="main-container"]/div/div/div/div/div[1]/div[1]/div[1]/button').click() 
sleep(1)
#APPT
driver.find_element(By.XPATH,'//*[@id="ApptTypeDdDv"]').click() 
sleep(1)

# IMPORT PICKUP
driver.find_element(By.XPATH,'//*[@id="ApptTypeDdDv"]/div/div[2]/div[1]').click() 

# EMPTY DROPOFF
# driver.find_element(By.XPATH,'//*[@id="ApptTypeDdDv"]/div/div[2]/div[4]').click()
# empty_dropff = driver.find_element(By.XPATH,'//*[@id="ApptTypeDdDv"]/div/div[2]/div[4]').click() 
sleep(1)

# Empty Container#
driver.find_element(By.XPATH,'//*[@id="containerName"]').send_keys(ctnrno) 

# Submit
driver.find_element(By.XPATH,'//*[@id="formcontent"]/form/div[2]/div[2]/button').click() 
sleep(2)

#OWN CHASSIS?
driver.find_element(By.XPATH,'//*[@id="ipgrid_0_own_chassis?"]/i').click()
sleep(1)

#NO
driver.find_element(By.XPATH,'//*[@id="ipgrid_0_own_chassis?"]/div[2]/div[2]/span').click()
sleep(1)
#
#driver.find_element(By.XPATH,'//*[@id="ipgrid_0"]/div[3]/div[2]/div/div[1]/div').click()

#Select Calendar
# driver.find_element(By.XPATH,'//*[@id="calendar0"]').click()

if date_check_method == 'Check Single Date':
    # Sinle Date Checker
    single_date_checker(appt_date, wait, start_time, end_time, driver, date_picker)
elif date_check_method == 'Check Multi Dates':
    # Multiple Dates Checker
    multi_date_checker (appt_date, wait, start_time, end_time, driver)

print("Done")


# Close the browser
driver.quit()