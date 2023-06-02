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



# By Pass reCaptcha
# https://www.youtube.com/watch?v=LDlD5k8S0oQ&ab_channel=ThePyCoach

# Get Cookies
# Video: https://www.youtube.com/watch?v=cVnYod9Fhko&ab_channel=JieJenn
# Cookies Convertor: https://curlconverter.com/


# # Create a function to get the selected value and close the window
# ###################################################################################################################
# def on_submit():
#     global container_entry
    
#     # Get container entries
#     data = container_entry.get("1.0", "end-1c")
#     lines = data.split("\n")
#     container_list.extend(lines)
#     container_entry.delete("1.0", "end")
#     print("Container List:")
#     print(container_list)  
#     root.destroy()


# # UI Window Settings
# ####################################################################################################################
# root = tkinter.Tk()
# # Set theme
# # sv_ttk.use_dark_theme()
# sv_ttk.use_light_theme()
# # root.title("Appointment Scheduler")
# # root.geometry("500x500")

# root.title("Appointment Scheduler")

# # Get the screen width and height
# screen_width = root.winfo_screenwidth()
# screen_height = root.winfo_screenheight()

# # Calculate the x and y coordinates for the window to be centered
# x = (screen_width - 210) // 2
# y = (screen_height - 250) // 2

# # Set the position of the window
# root.geometry(f"210x250+{x}+{y}")

# # List to store container entries
# container_list = []

# # Create a label for data entry
# Label(root, text="Enter Container Number:").grid(column=1, row=1, padx=5, pady=5)
# container_entry = customtkinter.CTkTextbox(root, height=160, width=200, border_width=1 ,border_color="lightgray" )
# container_entry.grid(column=1, row=2, padx=5, pady=5)

# # Create submit button
# # style = ttk.Style()
# # style.configure('Blue.TButton', foreground='blue', background='white')
# submit_button = customtkinter.CTkButton(root, width=60, text="OK", command=on_submit)
# submit_button.grid(column=1, row=7, padx=10, pady=5)

# # Start the mainloop to display the window
# root.mainloop()

# Main
####################################################################################################################

# # Create a new Chrome session
driver = webdriver.Chrome()
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

# containers = ['CCLU7723702',
#               'CSNU8069786',
#               'BMOU5128510',
#               'OOCU8990868',
#               'CCLU7308661',]
containers = ['CCLU7723702']

# Container List
container_list = '\n'.join(containers)

# Appt Release Time 11:10am
# V1 Make Appointment
################################################################
WebDriverWait(driver, 15).until( 
    EC.presence_of_all_elements_located((By.XPATH, '//*[@id="UserName"]'))
)
driver.find_element(By.XPATH, '//*[@id="UserName"]').send_keys("p1logistics@mail.com")

driver.find_element(By.XPATH, '//*[@id="Password"]').send_keys("8802616")
#driver.get('https://www.lbct.com/Login/Login')

WebDriverWait(driver, 20).until(EC.frame_to_be_available_and_switch_to_it((By.XPATH,"//iframe[@title='reCAPTCHA']")))
WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "div.recaptcha-checkbox-border"))).click()
sleep(20)


driver.switch_to.default_content()

# Click cookies Accept Button
driver.find_element(By.XPATH, '//*[@id="cookie-bar"]/div/span[2]/button').click()


# WebDriverWait(driver, 20).until(EC.frame_to_be_available_and_switch_to_it((By.XPATH, '//*[@id="loginBoxLogin"]')))
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH,'//*[@id="loginBoxLogin"]')))
driver.find_element(By.XPATH, '//*[@id="loginBoxLogin"]').click()

# Click Create Appt
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH,'//*[@id="sideBarCreateApptItem"]/div'))).click()

# Click Transaction Type Drop Down 
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH,'//*[@id="CreateApptTable"]/tbody/tr[2]/td[2]/span/span/span/span[2]/span'))).click()

# Click Empty In 
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH,'//*[@id="SelectedType_CreateAppt_listbox"]/li[4]'))).click()

# Click Container Number Input Box
# WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH,'//*[@id="id_CntrId_txt"]'))).click()

# Send Key Container Number Input Box
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH,'//*[@id="id_CntrId_txt"]'))).send_keys(container_list)

# Click Get Time Slots
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH,'//*[@id="id_sub_GetTimeslot"]'))).click()

# Click Date / Time Slots Box
sleep(3)
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH,'//*[@id="id_DateTimeRow_CreateAppt"]/td[2]/span/span/span/span[1]'))).click()

# appt_time = wait.until(EC.presence_of_element_located((By.XPATH,'')))
# 

# Locate the Appointment Time Slots
# WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH,'')))
time_slots_container = driver.find_elements(by="xpath", value='//*[@id="newDateTime_CreateAppt_listbox"]/li')

available_time_slots = []

# Check available time slots
for time in time_slots_container:
    try:
        # Read time slot text
        time_slots_text = time.text  
        if time_slots_text.strip():
            available_time_slots.append(time_slots_text)
        print(time_slots_text)
    except:
        print("No Time Slots Appended")
 
print(available_time_slots)

# ################################################################
# # Expand Tables
# get_expand_icon = WebDriverWait(driver, 10).until(
#     # //*[@class="k-hierarchy-cell"]/a
#     # //*[@class="k-icon k-i-expand"]
#     EC.presence_of_all_elements_located((
#     By.XPATH, '//*[@class="k-hierarchy-cell"]/a')))

# # Click on the expand icon
# for icon in get_expand_icon[1:]:
#     icon.click()
#     sleep(1)



################################################################
# Expand Tables

# WebDriverWait(driver, 10).until(
#     # //*[@class="k-hierarchy-cell"]/a
#     # //*[@class="k-icon k-i-expand"]
#     EC.element_to_be_clickable((
#     By.XPATH, '//*[@class="k-icon k-i-expand"]')))
# get_expand_icon = driver.find_elements(By.XPATH, '//*[@class="k-icon k-i-expand"]')
# # print(get_expand_icon)
# # Click on the expand icon
# for icon in get_expand_icon:
#     icon.click()
#     sleep(1)




print("Finished")


# Close the browser
driver.quit()
