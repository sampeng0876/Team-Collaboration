from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
from openpyxl import workbook, load_workbook
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from googleapiclient.discovery import build
from google.oauth2 import service_account

chrome_options = Options()
chrome_options.add_argument('--ignore-certificate-errors')

# #chrome_options.add_argument("--disable-extensions")
# #chrome_options.add_argument("--disable-gpu")
chrome_options.add_argument("--headless")
# # driver = webdriver.Chrome(options=chrome_options)


driver = webdriver.Chrome(options=chrome_options)
driver.maximize_window()
# driver = webdriver.Chrome(options=chrome_options)
print('Running...')
driver.get('https://facaillc2420.yuegekeji66.cn/admin/login/login.html')
print('Loging in...')
WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="admin_login"]/input[1]'))).send_keys('root')
WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="admin_login"]/input[2]'))).send_keys('123123')
driver.find_element(By.XPATH, '//*[@id="admin_login"]/button').click() #Login

WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="nav"]/li[2]/a/cite'))).click() # 点击展开 柜子汇总管理    
WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="nav"]/li[2]/ul/li[1]/a/cite'))).click() #点击 柜子汇总管理
sleep(2)

def load_google_sheet_data():
    SERVICE_ACCOUNT_FILE = 'service_account.json'
    # If modifying these scopes, delete the file token.json.
    SCOPES = ['https://www.googleapis.com/auth/spreadsheets']

    my_creds = None
    my_creds = service_account.Credentials.from_service_account_file(SERVICE_ACCOUNT_FILE, scopes=SCOPES)

    # The ID and range of a sample spreadsheet.
    google_sheet_id = '12lnRmQoBsITIYTQPEGYdHGVNUkoPPFQEhx5HaC3JTJQ'
    sheet_name = 'RECORD_DO!B:G'
    service = build('sheets', 'v4', credentials=my_creds)

    # Retrieve the values from the Google Sheet
    result = service.spreadsheets().values().get(spreadsheetId=google_sheet_id, range=sheet_name).execute()
    values = result.get('values', [])

    container_list = []
    i = 0
    for row in values[1:]:
        row_data = [str(cell).replace('\n', '').strip() if cell else '' for cell in row]
        container_list.append(row_data)
        
        i += 1

    print(f'Total {i} rows')
    return container_list
container_list = load_google_sheet_data()
print(container_list)
print('Appending... Data')
row = 1
for data in container_list:
    container, address, client, type, weight, note = data
    print(f'Row {row} {container} {address} {client} {type} {weight} {note}')
    
    iframe = driver.find_element(By.XPATH,'//*[@class="layui-tab-item layui-show"]/iframe') #Change iframe
    driver.switch_to.frame(iframe)

    WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, '//*[@class="layui-btn-container"]/button[1]'))).click() # 点击 添加数据
    sleep(2)
    iframe = driver.find_element(By.XPATH,'//*[@class="layui-layer-content"]/iframe') #Change iframe
    driver.switch_to.frame(iframe)


    driver.find_element(By.XPATH,'//*[@class="layui-tab-item layui-show"]/div[3]/div/input').send_keys(container) # 柜号
    driver.find_element(By.XPATH,'//*[@class="layui-tab-item layui-show"]/div[4]/div/input').send_keys(address) # 地址
    driver.find_element(By.XPATH,'//*[@class="layui-tab-item layui-show"]/div[5]/div/input').send_keys(client) # 客人
    driver.find_element(By.XPATH,'//*[@class="layui-tab-item layui-show"]/div[7]/div/input').send_keys(type) # 柜型
    driver.find_element(By.XPATH,'//*[@class="layui-tab-item layui-show"]/div[8]/div/input').send_keys(weight) # 重量
    driver.find_element(By.XPATH,'//*[@class="layui-tab-item layui-show"]/div[10]/div/textarea').send_keys(note) # 备注

    sleep(1)
    WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, '//*[@class="layui-form"]/div[2]/button'))).click() # 点击 增加
    print(f'Submitted: {row} row') 
    sleep(3)
    row+=1


print("Finished")
driver.quit()
