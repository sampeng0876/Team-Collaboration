#import selenium

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

from selenium.webdriver.support import expected_conditions as EC
from datetime import datetime, timedelta
from time import sleep

driver = webdriver.Chrome()
wait = WebDriverWait(driver, 10)
#要刷的柜号
ctnrno = 'MEDU4918194'
#Calendar Input
appt_date = '3'

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
# sleep(5)
# Find the day element for the date to select and click it
# day_element = wait.until(EC.element_to_be_clickable((By.XPATH, f"//td[@data-date='{date_str}']")))
# day_element.click()

# a for loop to look for the Date in the date picker

# for date in driver.find_element(By.XPATH,'//*[@id="ipgrid_0"]/div[3]/div[2]/div/div[2]/div/div[2]/div[1]/div[1]/span'):
#     print(date.span.text())

# to find the day element for the date to select and print the date
#print(driver.find_element(By.XPATH,'//*[@id="ipgrid_0"]/div[3]/div[2]/div/div[2]/div/div[2]/div[1]/div[1]/span').text) 

# a for loop to look for the dates element and print

dates = driver.find_element(By.XPATH,'//*[@id="ipgrid_0"]/div[3]/div[2]/div/div[2]/div/div[2]/div[1]')

#print(dates.text) 

for date in dates.text:
    print(date)
    if date == appt_date:
        print("found it")   
        print(type(date))
        # print("clicked")      
        sleep(3)
        break




# Close the browser
driver.quit()