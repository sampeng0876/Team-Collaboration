from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
import tkinter as tk
from selenium.webdriver.chrome.options import Options
from tkinter import *
from tkcalendar import *
import datetime as dt
import sv_ttk
import tkinter
from tkinter import ttk
import customtkinter
from bs4 import BeautifulSoup
from openpyxl import load_workbook
from LBCT_multi_date_checker import multi_date_checker
from datetime import datetime, date, timedelta
import os


# By Pass reCaptcha
# https://www.youtube.com/watch?v=LDlD5k8S0oQ&ab_channel=ThePyCoach

# Get Cookies
# Video: https://www.youtube.com/watch?v=cVnYod9Fhko&ab_channel=JieJenn
# Cookies Convertor: https://curlconverter.com/


def on_submit():
    global start_time, end_time, check_days, appt_dates_list, appt_type, container_entry, username

    # Get the calendar values
    date_picker= cal.get_date()
    formatted_date = datetime.strptime(date_picker, '%m/%d/%y').date()

    
    # Get the check_days values from dropdowns
    check_days = check_day_var.get()
    appt_dates_list = [formatted_date + timedelta(days=i) for i in range(int(check_days))]
    
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
appt_types = ['LOAD OUT', 'EMPTY DROPOFF']

# List to store container entries
container_list = []

# List of Username
username_info = ['p2','20','yuna','p1','jimbo']

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

# Main
####################################################################################################################
# Solved path: https://stackoverflow.com/questions/50443955/how-to-load-extension-within-chrome-driver-in-selenium-with-python
# Get Chrome EXT crx file: https://www.youtube.com/watch?v=Fx1hbZMVS7k&ab_channel=ComputingHUB
chrome_options = webdriver.ChromeOptions()
# extension_path = './Buster'
# chrome_options.add_argument('--load-extension=' + extension_path)
chrome_options.add_extension(r'C:\Users\Grace\Desktop\Manual\SP\Team-Collaboration\Get_LBCT_Appt\Buster.crx')

# # Create a new Chrome session
driver = webdriver.Chrome(options=chrome_options, executable_path=r'C:\Users\Grace\Desktop\Manual\SP\Team-Collaboration\chromedriver.exe')
driver.maximize_window()
wait = WebDriverWait(driver, 10)

driver.get("https://www.lbct.com/Login/Login")


# # Add the cookies
# for cookie_name, cookie_value in cookies.items():
#     cookie = {
#         'name': cookie_name,
#         'value': cookie_value
#     }
#     driver.add_cookie(cookie)

# sleep(10)
# # Refresh the page to apply the cookies
# driver.refresh()


# containers = ['CCLU7723702']

# Container List
# container_list = '\n'.join(container_list)

# Appt Release Time 11:10am
# V1 Make Appointment
################################################################
WebDriverWait(driver, 15).until( 
    EC.presence_of_all_elements_located((By.XPATH, '//*[@id="UserName"]'))
)
driver.find_element(By.XPATH, '//*[@id="UserName"]').send_keys("p1logistics@mail.com")

driver.find_element(By.XPATH, '//*[@id="Password"]').send_keys("8802616")
#driver.get('https://www.lbct.com/Login/Login')

# WebDriverWait(driver, 20).until(EC.frame_to_be_available_and_switch_to_it((By.XPATH,"//iframe[@title='reCAPTCHA']")))

iframe = driver.find_element(By.XPATH,'//*[@id="loginBoxTable"]/tbody/tr[4]/td/div/div/div/iframe') #Change iframe
driver.switch_to.frame(iframe)
# Click Check Box
WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "div.recaptcha-checkbox-border"))).click()

driver.switch_to.default_content()

iframe = driver.find_element(By.XPATH,'/html/body/div[6]/div[4]/iframe') #Change iframe//*[@title="recaptcha challenge expires in two minutes"]
driver.switch_to.frame(iframe)

WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="solver-button"]'))).click()
# sleep(30)
WebDriverWait(driver, 120).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'span.recaptcha-checkbox-checked'))) # #判断绿色打勾

driver.switch_to.default_content()

# Click cookies Accept Button
driver.find_element(By.XPATH, '//*[@id="cookie-bar"]/div/span[2]/button').click()


# WebDriverWait(driver, 20).until(EC.frame_to_be_available_and_switch_to_it((By.XPATH, '//*[@id="loginBoxLogin"]')))
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH,'//*[@id="loginBoxLogin"]')))
driver.find_element(By.XPATH, '//*[@id="loginBoxLogin"]').click()


check_container = 0
check_date = 1
while True:
    
    if check_container < len(container_list) :

        # Click Create Appt
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH,'//*[@id="sideBarCreateApptItem"]/div'))).click()
        sleep(1)
        # Click Transaction Type Drop Down 
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH,'//*[@id="CreateApptTable"]/tbody/tr[2]/td[2]/span/span/span/span[2]/span'))).click()              
        sleep(1)
        if appt_type == 'LOAD OUT':
            # IMPORT PICKUP
            WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH,'//*[@id="SelectedType_CreateAppt_listbox"]/li[7]'))).click()
            sleep(1)
        elif appt_type =='EMPTY DROPOFF':
            # Click Empty In
            WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH,'//*[@id="SelectedType_CreateAppt_listbox"]/li[4]'))).click()
            sleep(1)
        
        
        # Send Key Container Number Input Box
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH,'//*[@id="id_CntrId_txt"]'))).send_keys(container_list[check_container])
        container_number = container_list[check_container]


        # Click Get Time Slots
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH,'//*[@id="id_sub_GetTimeslot"]'))).click()


        # Call out multi_date_checker
        multi_date_checker (appt_dates_list, wait, start_time, end_time, driver, check_days, container_number, container_list, check_date)

    # print(check_container)
    if check_container == len(container_list):
        # If reached the last container start over to check the first container
        check_container = 0
        if len(container_list) == 0:
            break
    elif check_date == len(appt_dates_list):
        break
    else: check_container+=1   



print("Finished")


# Close the browser
driver.quit()
