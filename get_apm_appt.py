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

# Create a calendar widget
cal = DateEntry(root)
cal.pack()

# Create the dropdown and add the options
dropdown = tk.OptionMenu(root, var, *time_slots_list)
dropdown.pack()

# Create a button to submit the selection and close the window
submit_button = tk.Button(root, text="Submit", command=on_select)
submit_button.pack()

# Start the mainloop to display the window
root.mainloop()


chrome_options = Options()
# #chrome_options.add_argument("--disable-extensions")
# #chrome_options.add_argument("--disable-gpu")
chrome_options.add_argument("--headless")

# Set the options to run the browser in headless mode
# chrome_options.headless = True

driver = webdriver.Chrome()
driver.maximize_window()
wait = WebDriverWait(driver, 10)
driver.get("https://termpoint.apmterminals.com")
# Container Number
ctnrno = 'MEDU4918194'

# Appointment Date
print("Selected Appt Date: " + date_picker[-2:])
apptdate = str(int(date_picker[-2:]))
# print(apptdate)
# print(type(apptdate))
appt_date = apptdate

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
sleep(1)

#NO
driver.find_element(By.XPATH,'//*[@id="ipgrid_0_own_chassis?"]/div[2]/div[2]/span').click()
sleep(1)
#
#driver.find_element(By.XPATH,'//*[@id="ipgrid_0"]/div[3]/div[2]/div/div[1]/div').click()

#Select Calendar
# driver.find_element(By.XPATH,'//*[@id="calendar0"]').click()

# Find the calendar picker element
calendar_picker = wait.until(EC.presence_of_element_located((By.XPATH,'//*[@id="calendar0"]')))

# Get today's date
today = datetime.today()

# Calculate the date to select (e.g. 3 days from now)
# date_to_select = today + timedelta(days=3)
date_to_select = today

# Convert the date to a string that matches the date format used by the date picker
date_str = date_to_select.strftime("%m/%d/%Y")

# Click the date picker element to open the date picker
calendar_picker.click()
print("Clicked Calendar")
# sleep(1)
# Locate the dates of this month
dates = driver.find_elements(by="xpath", value='//div[@class="react-flex-view align-content-center justify-content-center react-datepicker-picker day current"]')

# Create a for loop to find the Appointment Date
for date in dates:
    date_text = date.find_element(by="xpath", value='./span').text
    #print(date_text)
    if date_text == appt_date:
        # print("Found it")
        date.click()        
        print("Clicked Date")
        # sleep(1)
        break

# Click Time Slots
time_clicker = wait.until(EC.presence_of_element_located((By.XPATH,'//*[@id="ipgrid_0_slot"]/i')))
time_clicker.click()
# sleep(1)
print("Clicked Time Slots")
# Locate the Appointment Time Slots
time_slots_container = driver.find_elements(by="xpath", value='//*[@class="visible menu transition"]/div') # //*[@id="ipgrid_0_slot"]/div[2]/div[1] SAME AS //div[@class="visible menu transition"]/div

# time_slots_list = ['00','01','02','03','04','05','06','07','08','09','10','11','12','13','14','15','16','17','18','19','20','21','22','23',]
print("Available Time Slots:")

available_time_slots=[]
for time in time_slots_container:
    try:
        time_slots_text = time.find_element(by="xpath", value='./span').text # Read time slot text        
        if time_slots_text.strip():# strip is without whitespace       
            print(time_slots_text)
            available_time_slots.append(time_slots_text[:2])
    except:
        print("No time slot found")
        
print(available_time_slots)
#available_time_slots = ['02','03','04','05','06','07','08']

for time_slot in available_time_slots:
    # print([i], end=' ')
    # print(i, end=' ')
    # print(time_picker)   
    if time_slot == time_picker:
        print(time_slot)
        print("Successfully Booked " + str(date_picker) + ' at ' + time_slot)
        break        
else: print(time_picker + " is Not Available")



print("Done")


# Close the browser
driver.quit()