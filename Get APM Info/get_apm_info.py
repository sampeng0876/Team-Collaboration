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


# chrome_options = Options()
# # #chrome_options.add_argument("--disable-extensions")
# # #chrome_options.add_argument("--disable-gpu")
# chrome_options.add_argument("--headless")

# Set the options to run the browser in headless mode
# chrome_options.headless = True

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
containers = ['EMCU8377066','TLLU4574003']
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
table_header = WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.XPATH, '//*[@class="trace-listing__row"]/th')))
table_row = WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.XPATH, '//*[@class="trace-listing__tbody"]/tr')))


# print(container_id_elements)
# print(len(container_id_elements))

# for info in container_id_elements:
#     #info_text = info.find_element(By.XPATH, '//*[@class="trace-listing__tbody"]/tr/td').text
#     info_text = info.text
#     print(info_text)

# get_table_data = pd.read_html("https://www.apmterminals.com/en/los-angeles/track-and-trace/import-availability")

# print(get_table_data)
# Create a list to store the extracted text
data = []
i=1
# Loop through the container_id_elements and extract the text
for info in WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.XPATH, f'//*[@id="main"]/div[2]/div[1]/div[2]/div/div[8]/div/table/tbody/tr[{i}]/td'))):
    info_text = info.text    
    data.append([info_text])
    print(data)
    i+=1
# Create a DataFrame from the data
# df = pd.DataFrame(data, columns=["Check Box",
#                                  "Container ID",
#                                  "Bill Of Lading",
#                                  "Status","Line",
#                                  "Vessel name",
#                                  "Vessel ETA",
#                                  "Discharge Date", 
#                                  "Yard Location Location",
#                                  "Freight",
#                                  "Customs",
#                                  "Holds",
#                                  "LFD",
#                                  "Demurrage",
#                                  "Size / Type / Height",
#                                  "Weight","Hazardous",
#                                  "Appointment date*",
#                                  "Gate Out Date"])
df = pd.DataFrame(data, columns=["Check Box"])
# print(df)

# Save the DataFrame to an Excel file named apm_container_info.xlsx
df.to_excel("apm_container_info.xlsx", index=False)





sleep(2)
print("Done")


# Close the browser
driver.quit()