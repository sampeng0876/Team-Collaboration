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
import pandas as pd
from openpyxl import load_workbook
from openpyxl.utils import get_column_letter


# chrome_options = Options()
# # #chrome_options.add_argument("--disable-extensions")
# # #chrome_options.add_argument("--disable-gpu")
# chrome_options.add_argument("--headless")

# Set the options to run the browser in headless mode
# chrome_options.headless = True

# Load the workbook
workbook = load_workbook('LFD.xlsx')

# Select sheet2
sheet = workbook['APM']  # Change the sheet name accordingly

driver = webdriver.Chrome()
driver.maximize_window()
wait = WebDriverWait(driver, 15)
# driver.get("https://www.apmterminals.com/en/los-angeles")

driver.get("https://www.apmterminals.com/en/los-angeles/online-services/container-tracking")

sleep(2)
# Click cookies
# driver.find_element(By.XPATH, '//*[@id="main"]/div[2]/div/div[2]/button').click()
driver.find_element(By.XPATH, '//*[@id="main"]/div[3]/div/div[2]/button').click()
sleep(3)

# Click track and trace button
containers = ['EMCU8377066','MEDU7539050']
driver.find_element(By.XPATH, '//*[@class="track-and-trace__tags"]').click()
# print(containers)
container_list = '\n'.join(containers)
# print(container_list)

# Enter container number
driver.find_element(By.XPATH, '//div[@class="track-and-trace__tags"]/input').send_keys(container_list)

# Click submit button
driver.find_element(By.XPATH, '//*[@class="track-and-trace__submit-inner"]/button').click()


# driver.find_elements(By.XPATH, '//*[@class="trace-listing__tbody"]/tr')
# WebDriverWait(driver, 15).until(EC.presence_of_all_elements_located((By.XPATH, '//*[@class="trace-listing__tbody"]/tr')))
# driver.find_element(by='xpath', value='//*[@id="main"]/div[2]/div[1]/div[2]/div/div[8]/div/table/tbody/tr/td[5]').text
# sleep(10)

#container_id_elements = WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.XPATH, '//*[@id="main"]/div[2]/div[1]/div[2]/div/div[8]/div/table/tbody/tr[1]/td')))
# table_header = WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.XPATH, '//*[@class="trace-listing__row"]/th')))
# table_row = WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.XPATH, '//*[@class="trace-listing__tbody"]/tr')))

# Get data
get_data = WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.XPATH, '//*[@class="trace-listing__tbody"]/tr/td')))
data_list = []

# Loop through the container_id_elements and extract the text
for info in get_data:
    info_text = info.text  
    data_list.append(info_text)
    
# Store the data to Excel file
row = 2 # Start row
column = 1 # Start column
availablebilities = driver.find_element(By.XPATH,'//*[@id="main"]/div[2]/div[1]/div[2]/div/div[8]/div/table/tbody/tr/td[4]/span').text

# Find the element using its class name


# alt_value = driver.find_element(By.XPATH, '//*[@ class="trace-listing__icon"]').get_attribute('alt')
alt_elements = driver.find_elements(By.XPATH, '//*[@ class="trace-listing__icon"]')
# Print the value of "alt"
# print(alt_elements.get_attribute('alt')[0])
# print(alt_elements.get_attribute('alt')[1])


for item in data_list:
    
    # for alt_value in alt_elements:
    #     get_alt_attribute = alt_value.get_attribute('alt')
    #     if get_alt_attribute == 'ready':
    #         item = 'Yes'
    #         print(f'this is READY {item}')
            
    #     elif get_alt_attribute == 'not-ready':
    #         item = 'No'
    #         print(f'this is NOT READY {item}')
            
    print(item)
    sheet.cell(row=row, column=column).value = item
    column += 1

    if column % 21 == 0:
        row += 1
        column = 1


# Save the modified workbook
workbook.save("LFD.xlsx")





sleep(2)
print("Done")


# Close the browser
driver.quit()