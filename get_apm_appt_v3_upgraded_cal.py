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

# Create a function to get the selected value and close the window
def on_submit():
    global date_picker, start_time, end_time
    # date_picker = cal.get_date().strftime('%Y-%m-%d')
    date_string = cal.get_date()  # Assuming cal.get_date() returns the date string '5/9/23'
    date_object = datetime.strptime(date_string, '%m/%d/%y')
    date_picker = date_object.strftime('%Y-%m-%d')
    # print(type(date_picker))
    # print(date_picker)
    # Get the selected values from the dropdowns
    start_time_1 = start_time_var.get()
    end_time_2 = end_time_var.get()
    
    # Check if the selected time range is available
    start_time = start_time_1
    end_time = end_time_2
    
    
    root.destroy()

root = Tk()
root.title("Appointment Scheduler")
root.geometry("500x500")

# create a list of available times
# available_time = ['00:00','01:00','02:00','03:00','04:00','05:00','06:00','07:00','08:00','09:00','10:00','11:00','12:00','13:00','14:00','15:00','16:00','17:00','18:00','19:00','20:00','21:00','22:00','23:00']
choose_time = [f'{i:02}:00' for i in range(24)]
# create a calendar picker
cal = Calendar(root, selectmode="day", year=2023, month=5, day=9)
cal.grid(column=1, row=0, padx=10, pady=5)

# create labels and dropdowns for start and end times
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

# create submit button
submit_button = Button(root, text="Submit", command=on_submit)
submit_button.grid(column=1, row=3, padx=10, pady=5)

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
ctnrno = 'MEDU4918194'

# print(date_picker)
appt_date = str(int(date_picker[-2:]))
# print(apptdate)
# print(type(apptdate))


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

# Click the date picker element to open the date picker
calendar_picker.click()
# print("Clicked Calendar")
sleep(1)

# Locate the dates of this month
picker_day_current = driver.find_elements(by="xpath", value='//div[@class="react-flex-view align-content-center justify-content-center react-datepicker-picker day current"]')
picker_day_current_selected = driver.find_elements(by="xpath", value='//div[@class="react-flex-view align-content-center justify-content-center react-datepicker-picker day current selected"]')

# Create a for loop to find the Appointment Date
for date in picker_day_current + picker_day_current_selected:
    date_text = date.find_element(by="xpath", value='./span').text
    #print(date_text)
    if date_text == appt_date:
        date.click()        
        # print("Clicked Date")
        sleep(1)
        break
    
print(f"Selected Appt Date: {date_picker}")

# Click Time Slots
time_slots = wait.until(EC.presence_of_element_located((By.XPATH,'//*[@id="ipgrid_0_slot"]/i')))
time_slots.click()
# sleep(1)
# print("Clicked Time Slots")
# Locate the Appointment Time Slots
time_slots_container = driver.find_elements(by="xpath", value='//*[@class="visible menu transition"]/div') # //*[@id="ipgrid_0_slot"]/div[2]/div[1] SAME AS //div[@class="visible menu transition"]/div

available_time_slots=[]

# Print available time slots
print("Available Time Slots:")

# Check available time slots
for time in time_slots_container:
    try:
        # Read time slot text
        time_slots_text = time.find_element(by="xpath", value='./span').text  
        # strip is without whitespace       
        if time_slots_text.strip():   
            # Appending time slot                         
            available_time_slots.append(time_slots_text)            
            print(time_slots_text) 
    except:
        print("No Time Slots Appended")
# print(f"This is available_time_slots: {available_time_slots}")

# Check available times in selected range from start time to end time
available_times = [time for time in available_time_slots if start_time <= time <= end_time]
# print(f"This is available_time: {available_times}")

# error counter
error_count = 0

for click_time in time_slots_container:
    try:
        # Read time slot text
        click_time_slots_text = click_time.find_element(by="xpath", value='./span').text         
        # Choose the earliest available time
        earliest_time = available_times[0]
            
        # Print available times
        
        if click_time_slots_text == earliest_time:               
            click_time.click()            
            # Print available time slots
            # print(available_times)
            # Print Appointment Date and Time
            print(f"Selected Appt Times From: {start_time} to {end_time}")
            # Print a success message
            print(f"Successfully Booked The Earliest time: {earliest_time}") 
            # sleep(2)
                   
    except:
        if error_count == 0:
            # print(available_time_slots)
            print(f"No Time Slots Available From: {start_time} to {end_time}")
        error_count += 1


print("Done")


# Close the browser
driver.quit()