from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from datetime import datetime, timedelta
from time import sleep
import tkinter as tk
from tkcalendar import DateEntry
from selenium.webdriver.chrome.options import Options
from tkinter import *
from tkcalendar import *
import datetime as dt
import sv_ttk
import tkinter
from tkinter import ttk
import customtkinter

# By Pass reCaptcha
# https://www.youtube.com/watch?v=LDlD5k8S0oQ&ab_channel=ThePyCoach

# Create a function to get the selected value and close the window
####################################################################################################################
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


chrome_options = Options()
# #chrome_options.add_argument("--disable-extensions")
# #chrome_options.add_argument("--disable-gpu")
chrome_options.add_argument("--headless")

# Set the options to run the browser in headless mode
# chrome_options.headless = True

driver = webdriver.Chrome()
driver.maximize_window()
wait = WebDriverWait(driver, 10)
driver.get("https://www.lbct.com/Login/Login")


containers = ['TRHU5383128',
              'CSLU1957155',
              'FCIU9915913',
              'TGBU9211653',
              'TRHU4303560',
              'TGBU4954255',
              'TXGU5678920',
              'OOCU6881615']

# containers = ['CSLU1957155']

# Container List
container_list = '\n'.join(containers)


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

# driver.find_element(By.XPATH, '//*[@id="cookie-bar"]/div/span[2]/button').click() # Click Cookies

WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH,'//*[@class ="k-textbox sideBarCargoAvailabilityTextArea textareaPlaceholder"]')))
driver.find_element(By.XPATH, '//*[@class ="k-textbox sideBarCargoAvailabilityTextArea textareaPlaceholder"]').click() # Search Box Send Keys
driver.find_element(By.XPATH, '//*[@class ="k-textbox sideBarCargoAvailabilityTextArea textareaPlaceholder"]').send_keys(container_list)
driver.find_element(By.XPATH, '//*[@id="sideBarTextareaSubmitBtn"]').click() # Click Search Button

# Expand Table
get_expand_icon = WebDriverWait(driver, 10).until(
    # //*[@class="k-hierarchy-cell"]/a
    # //*[@class="k-icon k-i-expand"]
    EC.presence_of_all_elements_located((
    By.XPATH, '//*[@class="k-hierarchy-cell"]/a')))

print(get_expand_icon)

# i = 3
# WebDriverWait(driver, 10).until(
# EC.element_to_be_clickable((
# By.XPATH, f'//*[@id="batchCargoSearchGrid"]/tbody/tr[{i}]/td[1]/a')))

for icon in get_expand_icon[1:]:

    icon.click()
    sleep(1)



# Get Details Information
get_details_info = WebDriverWait(driver, 10).until(
    EC.presence_of_all_elements_located((
    By.XPATH, '//*[@class="table-default container-table-horizontal"]/tbody/tr/td/strong')))

details_info_list = []

# Loop through the container_id_elements and extract the text

for info in get_details_info:
    info_text = info.text
    print(info_text)
    details_info_list.append(info_text)
# print(data_list)    

# print(f'this is get_details_info {details_info_list}')

sleep(1)
print("Done")


# Close the browser
driver.quit()