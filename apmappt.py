from re import I
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
from openpyxl import workbook, load_workbook
from selenium.webdriver.chrome.options import Options
from datetime import datetime


# chrome_options = Options()
# #chrome_options.add_argument("--disable-extensions")
# #chrome_options.add_argument("--disable-gpu")
# chrome_options.add_argument("--headless")
# driver = webdriver.Chrome(options=chrome_options)

ctnrno = 'MEDU4918194' #要刷的柜号
j = 3 #刷柜次数

# 假设要选择 2023 年 X 月 X 日
date = datetime(2023, 4, 18)

# 将 0 < x < 25 作为变量，放在前面便于每次更改 i = 0
available_range = range(6, 23)


driver = webdriver.Chrome()
driver.maximize_window()
driver.get('https://termpoint.apmterminals.com')
sleep(1)
# WebDriverWait(driver, 5).until( # Wait ID
#     EC.presence_of_all_elements_located((By.XPATH, '//*[@id="Login_form"]/div[1]/div/div/input'))
# )
driver.find_element(By.XPATH, '//*[@id="Login_form"]/div[1]/div/div/input').send_keys('twenty')
driver.find_element(By.XPATH, '//*[@id="Login_form"]/div[2]/div/div/input').send_keys('20Trans!')
driver.find_element(By.XPATH,'//*[@id="Login_form"]/div[3]/div/button').click() #login
# sleep(1)
WebDriverWait(driver, 15).until( # Wait schedule
    EC.presence_of_all_elements_located((By.XPATH, '//*[@id="main-container"]/div/div/div/div/div[1]/div[1]/div[1]/button'))
)
driver.find_element(By.XPATH,'//*[@id="main-container"]/div/div/div/div/div[1]/div[1]/div[1]/button').click() #Schedule a new appointment
sleep(1)
driver.find_element(By.XPATH,'//*[@id="ApptTypeDdDv"]').click() #APPT
sleep(1)
driver.find_element(By.XPATH,'//*[@id="ApptTypeDdDv"]/div/div[2]/div[4]').click() #EMPTY DROPOFF
sleep(1)
driver.find_element(By.XPATH,'//*[@id="containerName"]').send_keys(ctnrno) #Empty Container#
driver.find_element(By.XPATH,'//*[@id="formcontent"]/form/div[2]/div[2]/button').click() #Submit
sleep(1)

# 等待日期选择器元素加载完成
date_picker = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="ipgrid_0"]/div[3]/div[2]/div/div/div')))
# date_picker.click() #Calendar

sleep(1)
# Own Chassis Select No
driver.find_element(By.XPATH,'//*[@id="ipgrid_0_own_chassis?"]/input').send_keys('NO') #Input Chassis
driver.find_element(By.XPATH,'//*[@id="ipgrid_0_own_chassis?"]/div[2]/div/span').click() #Click Chassis

i = 0
# j = 3 #刷柜次数
while i < j:
    
    # driver.find_element(By.XPATH,'//*[@id="calendar0"]').click() #Calendar
    sleep(1)

    # 生成对应的 XPath
    # xpath = '//*[@id="ipgrid_0"]/div[3]/div[2]/div/div[2]/div/div[2]/div[2]/div[{day}]/span'
    # day = date.day - 1  # 注意 XPath 中索引从  开始
    # xpath = xpath.format(day=day)

    # # 点击日期
    # driver.find_element(By.XPATH, xpath).click()
    
    # 找到 input 元素
    input_element = driver.find_element(By.ID, "calendar0")
    
    driver.execute_script("arguments[0].removeAttribute('readonly')", input_element)
    input_element.clear()
    input_element.send_keys(date.strftime('%m/%d/%Y'))

    sleep(1)

    slot_xpath = '//*[@id="ipgrid_0_slot"]'

    driver.find_element(By.XPATH,'//*[@id="ipgrid_0_slot"]').click() #Click Timeslot
    slot_list = driver.find_elements(By.XPATH,'//*[@id="ipgrid_0_slot"]/div[2]')[0].text.splitlines() #Read Timeslot
    
    print('所选日期：' + date.strftime('%Y-%m-%d'))
    print(slot_list)
    
    # 筛选符合条件的时间段
    valid_slots = []
    for slot in slot_list:
        try:
            start_hour = int(slot[:2])
            if start_hour in available_range:
                valid_slots.append(slot)
        except ValueError:
            continue
        
    # 输出筛选结果
    if valid_slots:
        print(f'第 {i+1} 次，共找到 {len(valid_slots)} 个可用时间段:')
        for j, slot in enumerate(valid_slots):
            print(f'[{j+1}] {slot}')

        # 选择第一个符合条件的时间段
        slot_index = slot_list.index(valid_slots[0]) + 1
        print(f'选择第 {slot_index} 个时间段: {valid_slots[0]}')

        # 点击选择时间段
        slot_item = driver.find_elements(By.XPATH, f'{slot_xpath}/div[2]/div')[slot_index]
        slot_item.find_element(By.XPATH, './span').click()
        break
    else:
        print(f'第 {i+1} 次，没有可用时间段')
        i += 1
# else:
#     print('没有找到可用时间段')
        

# driver.find_element(By.XPATH,'//*[@id="action-section"]/button[1]').click() #Submit

sleep(3)
driver.quit()

print('完成')