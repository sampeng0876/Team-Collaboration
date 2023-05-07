from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from datetime import datetime, timedelta
from time import sleep

# import tkinter as tk

# # Create a new window
# window = tk.Tk()

# # Set the window title
# window.title("Input")

# # Create a label to display instructions to the user
# label = tk.Label(window, text="Please enter your input:")
# label.pack()

# # Create a text box for the user to enter their input
# entry = tk.Entry(window)
# entry.pack()

# # Create a variable to hold the user input
# appt_date = ""

# # Create a function to handle the input submission
# def submit_input():
#     global appt_date  # Use the global keyword to modify the global variable
#     appt_date = entry.get()  # Get the text entered in the text box
#     window.destroy()  # Close the window

# # Create a button to submit the input
# button = tk.Button(window, text="Submit", command=submit_input)
# button.pack()

# # Start the main loop to display the window and wait for the user to enter input
# window.mainloop()

# # Print the user input after the window is closed
# print("User input:", appt_date)

# appt_date = input("Please enter your age: ")
driver = webdriver.Chrome()
wait = WebDriverWait(driver, 10)

# Container Number
ctnrno = 'MEDU4918194'

# Appointment Date
appt_date = '8'

driver.get("https://termpoint.apmterminals.com")

driver.find_element(By.XPATH, '//*[@id="Login_form"]/div[1]/div/div/input').send_keys("twenty")

driver.find_element(By.XPATH, '//*[@id="Login_form"]/div[2]/div/div/input').send_keys("20Trans!")

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
#EMPTY DROPOFF
driver.find_element(By.XPATH,'//*[@id="ApptTypeDdDv"]/div/div[2]/div[4]').click() 
sleep(1)

#Empty Container#
driver.find_element(By.XPATH,'//*[@id="containerName"]').send_keys(ctnrno) 
#Submit
driver.find_element(By.XPATH,'//*[@id="formcontent"]/form/div[2]/div[2]/button').click() 
sleep(1)

#OWN CHASSIS?
driver.find_element(By.XPATH,'//*[@id="ipgrid_0_own_chassis?"]/i').click()

#NO
driver.find_element(By.XPATH,'//*[@id="ipgrid_0_own_chassis?"]/div[2]/div[2]/span').click()

#
#driver.find_element(By.XPATH,'//*[@id="ipgrid_0"]/div[3]/div[2]/div/div[1]/div').click()

#Select Calendar
# driver.find_element(By.XPATH,'//*[@id="calendar0"]').click()

# Find the date picker element
date_picker = wait.until(EC.presence_of_element_located((By.XPATH,'//*[@id="calendar0"]')))

# Get today's date
today = datetime.today()

# Calculate the date to select (e.g. 3 days from now)
# date_to_select = today + timedelta(days=3)
date_to_select = today

# Convert the date to a string that matches the date format used by the date picker
date_str = date_to_select.strftime("%m/%d/%Y")

# Click the date picker element to open the date picker
date_picker.click()

# Locate the dates of this month
dates = driver.find_elements(by="xpath", value='//div[@class="react-flex-view align-content-center justify-content-center react-datepicker-picker day current"]')

# Create a for loop to find the Appointment Date
for date in dates:
    date_text = date.find_element(by="xpath", value='./span').text
    print(date_text)
    if date_text == appt_date:
        print("Found it")
        date.click()
        print("Clicked")
        # sleep(5)
        break


# Clieck Time Slots
time_picker = wait.until(EC.presence_of_element_located((By.XPATH,'//*[@id="ipgrid_0_slot"]/div[1]')))
time_picker.click()
# Locate the Appointment Time Slots
time_slots = driver.find_elements(by="xpath", value='//div[@class="visible menu transition"]/div')

print("Available Time Slots")
for time in time_slots:
    time_slots_text = time.find_element(by="xpath", value='./span').text
    if time_slots_text.strip():
        print(time_slots_text)
        sleep(5)
#         if "20:00" in time_slots_text or "21:00" in time_slots_text or "22:00" in time_slots_text or "23:00" in time_slots_text:
#             print("Found time slots:", time_slots_text)
#             break
# else:
#     print("No time slots were found between 20:00 and 23:00.")




print("Done")


# Close the browser
driver.quit()