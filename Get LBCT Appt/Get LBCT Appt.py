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

# By Pass reCaptcha
# https://www.youtube.com/watch?v=LDlD5k8S0oQ&ab_channel=ThePyCoach

# # Define the options for the dropdown menu
# #date_list = ['1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20','21','22','23','24','25','26','27','28','29','30','31']
# time_slots_list = ['00:00','01:00','02:00','03:00','04:00','05:00','06:00','07:00','08:00','09:00','10:00','11:00','12:00','13:00','14:00','15:00','16:00','17:00','18:00','19:00','20:00','21:00','22:00','23:00']

# # Create a function to get the selected value and close the window
# def on_select():
#     global date_picker, time_picker
#     date_picker = cal.get_date().strftime('%Y-%m-%d')
#     time_picker = var.get()
#     root.destroy()

# # Create the window
# root = tk.Tk()

# # Create a variable to store the selected option
# var = tk.StringVar(root)

# # Set the default value of the dropdown
# var.set(time_slots_list[0])

# # Create a calendar widget
# cal = DateEntry(root)
# cal.pack()

# # Create the dropdown and add the options
# dropdown = tk.OptionMenu(root, var, *time_slots_list)
# dropdown.pack()

# # Create a button to submit the selection and close the window
# submit_button = tk.Button(root, text="Submit", command=on_select)
# submit_button.pack()

# # Start the mainloop to display the window
# root.mainloop()


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
# Container Number
ctnrno = 'MEDU4918194'

# apptdate = str(int(date_picker[-2:]))
#print(apptdate)
# print(type(apptdate))
# appt_date = apptdate
WebDriverWait(driver, 15).until( 
    EC.presence_of_all_elements_located((By.XPATH, '//*[@id="UserName"]'))
)
driver.find_element(By.XPATH, '//*[@id="UserName"]').send_keys("p1logistics@mail.com")

driver.find_element(By.XPATH, '//*[@id="Password"]').send_keys("8802616")
#driver.get('https://www.lbct.com/Login/Login')

WebDriverWait(driver, 20).until(EC.frame_to_be_available_and_switch_to_it((By.XPATH,"//iframe[@title='reCAPTCHA']")))
WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "div.recaptcha-checkbox-border"))).click()
sleep(20)
#driver.find_element(By.XPATH, '//*[@id="recaptcha-anchor"]/div[1]').click() # Check Box
driver.switch_to.default_content()

# WebDriverWait(driver, 20).until(EC.frame_to_be_available_and_switch_to_it((By.XPATH, '//*[@id="loginBoxLogin"]')))
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH,'//*[@id="loginBoxLogin"]'))).click()
# driver.find_element(By.XPATH, '//*[@id="loginBoxLogin"]').click()

# driver.find_element(By.XPATH, '//*[@id="cookie-bar"]/div/span[2]/button').click() # Click Cookies


driver.find_element(By.XPATH, '//*[@id="sideBarTextarea"]').send_keys('TRHU5383128','CSLU1957155') # Search Box Send Keys
driver.find_element(By.XPATH, '//*[@id="sideBarTextareaSubmitBtn"]').click() # Click Search Button

# Wait schedule
WebDriverWait(driver, 15).until( 
    EC.presence_of_all_elements_located((By.XPATH, '//*[@id="demurrageValue1guarantee_8330843003"]'))
)
#LFD
LFD = driver.find_element(By.XPATH,'//*[@id="demurrageValue1guarantee_8330843003"]').text
print(LFD)
sleep(1)
# #APPT
# driver.find_element(By.XPATH,'//*[@id="ApptTypeDdDv"]').click() 
# sleep(1)
# #EMPTY DROPOFF
# driver.find_element(By.XPATH,'//*[@id="ApptTypeDdDv"]/div/div[2]/div[4]').click() 
# sleep(1)

# #Empty Container#
# driver.find_element(By.XPATH,'//*[@id="containerName"]').send_keys(ctnrno) 

# #Submit
# driver.find_element(By.XPATH,'//*[@id="formcontent"]/form/div[2]/div[2]/button').click() 
# sleep(1)

# #OWN CHASSIS?
# driver.find_element(By.XPATH,'//*[@id="ipgrid_0_own_chassis?"]/i').click()
# sleep(1)

# #NO
# driver.find_element(By.XPATH,'//*[@id="ipgrid_0_own_chassis?"]/div[2]/div[2]/span').click()
# sleep(1)

# # Find the calendar picker element
# calendar_picker = wait.until(EC.presence_of_element_located((By.XPATH,'//*[@id="calendar0"]')))

# # Click the date picker element to open the date picker
# calendar_picker.click()
# # print("Clicked Calendar")
# # sleep(3)

# # Locate the dates of this month
# picker_day_current = driver.find_elements(by="xpath", value='//div[@class="react-flex-view align-content-center justify-content-center react-datepicker-picker day current"]')
# picker_day_current_selected = driver.find_elements(by="xpath", value='//div[@class="react-flex-view align-content-center justify-content-center react-datepicker-picker day current selected"]')

# # Create a for loop to find the Appointment Date
# for date in picker_day_current + picker_day_current_selected:
#     date_text = date.find_element(by="xpath", value='./span').text
#     # print(date_text)
#     if date_text == appt_date:
#         # print("Found it")
#         date.click()        
#         # print("Clicked Date")
#         #sleep(5)
#         break

# # Click Time Slots
# time_clicker = wait.until(EC.presence_of_element_located((By.XPATH,'//*[@id="ipgrid_0_slot"]/i')))
# time_clicker.click()
# # sleep(1)
# # print("Clicked Time Slots")
# # Locate the Appointment Time Slots
# time_slots_container = driver.find_elements(by="xpath", value='//*[@class="visible menu transition"]/div') # //*[@id="ipgrid_0_slot"]/div[2]/div[1] SAME AS //div[@class="visible menu transition"]/div

# # Appointment Date
# print(f"Selected Appt Date: {date_picker}")
# print("Available Time Slots:")

# available_time_slots=[]
# for time in time_slots_container:
#     try:
#         time_slots_text = time.find_element(by="xpath", value='./span').text # Read time slot text        
#         if time_slots_text.strip():# strip is without whitespace       
#             print(time_slots_text)
#             available_time_slots.append(time_slots_text[:2])
#     except:
#         print("No time slot found")
        
# print(available_time_slots)
# #available_time_slots = ['02','03','04','05','06','07','08']

# for time_slot in available_time_slots:
#     # print([i], end=' ')
#     # print(i, end=' ')
#     # print(time_picker)   
#     if time_slot == time_picker[:2]:
#         print(time_slot)
#         print("Successfully Booked " + str(date_picker) + ' at ' + time_picker)        
#         break        
# else: 
#     print(time_picker + " is Not Available")



print("Done")


# Close the browser
driver.quit()