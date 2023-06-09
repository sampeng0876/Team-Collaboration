from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
from openpyxl import workbook, load_workbook
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains

chrome_options = Options()
chrome_options.add_argument('--ignore-certificate-errors')

# #chrome_options.add_argument("--disable-extensions")
# #chrome_options.add_argument("--disable-gpu")
# chrome_options.add_argument("--headless")
# # driver = webdriver.Chrome(options=chrome_options)

def bypass(driver):
    # # 执行 JavaScript 代码以删除Login的按钮
    # script = """
    # var button = document.getElementById('loginBoxLogin');
    # if (button) {
    #   button.parentNode.removeChild(button);
    # }
    # """
    # driver.execute_script(script)

    # # 执行 JavaScript 代码以删除 iframe
    # script = """
    # var iframeElement = document.querySelector('iframe[title="reCAPTCHA"]');
    # if (iframeElement) {
    # iframeElement.parentNode.removeChild(iframeElement);
    # }
    # """
    # driver.execute_script(script)
    
    iframe = driver.find_element(By.XPATH,'//*[@id="loginBoxTable"]/tbody/tr[4]/td/div/div/div/iframe') #Change iframe
    driver.switch_to.frame(iframe)
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'recaptcha-anchor'))).click() #点recaptch
    WebDriverWait(driver, 120).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'span.recaptcha-checkbox-checked'))) # #判断绿色打勾
    driver.switch_to.default_content()

driver = webdriver.Chrome(options=chrome_options)
driver.maximize_window()
# driver = webdriver.Chrome(options=chrome_options)

driver.get('https://www.lbct.com/Login/Login')

WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="UserName"]'))).send_keys('p1logistics@mail.com')
WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="Password"]'))).send_keys('8802616')

bypass(driver)

driver.switch_to.default_content()
driver.find_element(By.XPATH, '//*[@id="loginBoxLogin"]').click() #Login

WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="sideBarCreateApptItem"]/div'))).click() #Create Appointment    
WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="CreateApptTable"]/tbody/tr[2]/td[2]/span/span/span'))).click() #Dropdownlist click
WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="SelectedType_CreateAppt_listbox"]/li[7]'))).click() #Load out
driver.find_element(By.XPATH,'//*[@id="id_CntrId_txt"]').send_keys('FCIU9479419') #Load Container
WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="id_sub_GetTimeslot"]'))).click() #Get Time Slot
WebDriverWait(driver, 30).until(EC.invisibility_of_element_located((By.XPATH, "//span[contains(text(),'Searching for time slots')]"))) #等待元素消失
WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="id_DateTimeRow_CreateAppt"]/td[2]/span/span/span/span[2]'))).click() #Click Select One
slot_list = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="newDateTime_CreateAppt_listbox"]'))).text #Read Timeslot
print(slot_list)
lines = slot_list.split("\n")
num_lines = len(lines)
print("Number of lines:", num_lines)

# slots = []
# for line in slot_list.split("\n"):
#     slots.append(line)
# print(slots)
# for item in load:
    
#     iframe = driver.find_element(By.XPATH,'//*[@id="businessView"]') #Change iframe
#     driver.switch_to.frame(iframe)

#     driver.find_element(By.XPATH, '//*[@id="cntrNos"]').send_keys(load[i]) #Load
#     driver.find_element(By.XPATH,'//*[@id="form"]/table/tbody/tr/td/table[3]/tbody/tr/td/table[1]/tbody/tr/td[1]/table[3]/tbody/tr/td/table/tbody/tr/td[1]/table/tbody/tr/td[2]/a').click() #Submit

#     driver.find_element(By.XPATH,'//*[@id="1"]/td[26]').click() #Select
#     driver.find_element(By.XPATH,'//*[@id="1_dualYn"]/option[2]').click() #Change Yes

#     driver.find_element(By.XPATH, '//*[@id="1_dualCntrNo"]').send_keys(empty[i]) #Empty
#     driver.find_element(By.XPATH,'//*[@id="form"]/table[1]/tbody/tr/td/table[1]/tbody/tr/td/table[1]/tbody/tr/td[3]/table/tbody/tr/td/table/tbody/tr/td[1]/table/tbody/tr/td[2]').click() #Submit

#     driver.switch_to.default_content()
#     element = driver.find_element(By.XPATH,'//*[@id="nav"]/li[3]/a') #Appointment
#     sleep(1)

#     ActionChains(driver).move_to_element(element).perform() #鼠标悬停选择
#     sleep(1)
#     driver.find_element(By.XPATH,'//*[@id="nav"]/li[3]/ul/li[1]/a').click() #Import Pickup

#     i = i + 1
#     sleep(1)

sleep(3)

driver.quit()
print('完成')