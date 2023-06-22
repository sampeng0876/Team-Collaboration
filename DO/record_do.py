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
from tkinter import *
from tkcalendar import *
import datetime as dt
import sv_ttk
import tkinter
from tkinter import ttk
import customtkinter

def on_submit():
    global record_do
    
    # Get Username value
    record_do = record_do_var.get()

    root.destroy()

# UI settings
####################################################################################################################
root = tkinter.Tk()
# Set theme
# sv_ttk.use_dark_theme()
sv_ttk.use_light_theme()
# root.title("Appointment Scheduler")
# root.geometry("500x500")

root.title("Appointment Scheduler")

# Get the screen width and height
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

# Calculate the x and y coordinates for the window to be centered
x = (screen_width - 200) // 2
y = (screen_height - 100) // 2

# Set the position of the window
root.geometry(f"200x100+{x}+{y}")


# Create a list of a times options
choose_time = [f'{i:02}:00' for i in range(24)]

# Create a list of a day options
check_day = [str(i) for i in range(1, 11)]

# Create a list of appointment type options
appt_types = ['LOAD OUT', 'EMPTY DROPOFF']

# List to store container entries
container_list = []

# List of Username
record_do_info = ['DO','LFD','DELIVERY']


# Create Username Seclection
Label(root, text="Record Task: ").grid(column=0, row=6, padx=10, pady=5)
record_do_var = StringVar(root)
# check_day_var.set("1")
record_do_dropdown = ttk.OptionMenu(root, record_do_var, 'DO', *record_do_info)
record_do_dropdown.config(width=5)
record_do_dropdown.grid(column=1, row=6, padx=10, pady=5)

# Create submit button
# style = ttk.Style()
# style.configure('Blue.TButton', foreground='blue', background='white')
submit_button = customtkinter.CTkButton(root, width=60, text="OK", command=on_submit)
submit_button.grid(column=1, row=7, padx=10, pady=5)

# Start the mainloop to display the window
root.mainloop()


chrome_options = Options()
chrome_options.add_argument('--ignore-certificate-errors')

# #chrome_options.add_argument("--disable-extensions")
# #chrome_options.add_argument("--disable-gpu")
chrome_options.add_argument("--headless")


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
print(record_do)
if record_do == 'DO':
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
    # print(container_list)


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
        
elif record_do == 'LFD':
    def load_google_sheet_data():
        SERVICE_ACCOUNT_FILE = 'service_account.json'
        # If modifying these scopes, delete the file token.json.
        SCOPES = ['https://www.googleapis.com/auth/spreadsheets']

        my_creds = None
        my_creds = service_account.Credentials.from_service_account_file(SERVICE_ACCOUNT_FILE, scopes=SCOPES)

        # The ID and range of a sample spreadsheet.
        google_sheet_id = '12lnRmQoBsITIYTQPEGYdHGVNUkoPPFQEhx5HaC3JTJQ'
        sheet_name = 'UPDATE_LFD!A:B'
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
    # print(container_list)

    print('Appending... Data')

    row = 1
    for data in container_list:
        container, lfd= data
        print(f'Row {row} {container} {lfd}')
        
        iframe = driver.find_element(By.XPATH,'//*[@class="layui-tab-item layui-show"]/iframe') #Change iframe
        driver.switch_to.frame(iframe)
        input_container = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@class="layui-form layui-col-space5"]/div[3]/input'))) # 输入柜号
        input_container.clear() #Clear
        input_container.send_keys(container)
        WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, '//*[@class="layui-inline layui-show-xs-block"]/button'))).click() # 点击搜索 
        sleep(2)       
        WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, '//*[@class="layui-table-cell laytable-cell-1-0-19"]/a[1]'))).click() # 点击编辑

        sleep(1)
        iframe = driver.find_element(By.XPATH,'//*[@class="layui-layer-content"]/iframe') #Change iframe
        driver.switch_to.frame(iframe)

        input_element = driver.find_element(By.ID, value="date_container") # 找到 提柜(LFD)日期
        driver.execute_script("arguments[0].removeAttribute('readonly')", input_element)
        input_element.clear()
        input_element.send_keys(f'{lfd} 00:00:00') #lfd.strftime('%Y/%m/%d')
        # WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, '//*[@class="laydate-footer-btns"]/span[3]'))).click() #点击日期 确定
        WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, '//*[@class="layui-form"]/div[2]/button'))).click() # 点击 提交

        print(f'Submitted: {row} row') 
        sleep(3)
        row+=1

elif record_do == 'DELIVERY':
    def load_google_sheet_data():
        SERVICE_ACCOUNT_FILE = 'service_account.json'
        # If modifying these scopes, delete the file token.json.
        SCOPES = ['https://www.googleapis.com/auth/spreadsheets']

        my_creds = None
        my_creds = service_account.Credentials.from_service_account_file(SERVICE_ACCOUNT_FILE, scopes=SCOPES)

        # The ID and range of a sample spreadsheet.
        google_sheet_id = '12lnRmQoBsITIYTQPEGYdHGVNUkoPPFQEhx5HaC3JTJQ'
        sheet_name = 'UPDATE_LFD!A:B'
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
    # print(container_list)

    print('Appending... Data')

    row = 1
    for data in container_list:
        container, lfd= data
        print(f'Row {row} {container} {lfd}')
        
        iframe = driver.find_element(By.XPATH,'//*[@class="layui-tab-item layui-show"]/iframe') #Change iframe
        driver.switch_to.frame(iframe)
        input_container = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@class="layui-form layui-col-space5"]/div[3]/input'))) # 输入柜号
        input_container.clear() #Clear
        input_container.send_keys(container)
        WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, '//*[@class="layui-inline layui-show-xs-block"]/button'))).click() # 点击搜索 
        sleep(2)       
        WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, '//*[@class="layui-table-cell laytable-cell-1-0-19"]/a[1]'))).click() # 点击编辑

        sleep(1)
        iframe = driver.find_element(By.XPATH,'//*[@class="layui-layer-content"]/iframe') #Change iframe
        driver.switch_to.frame(iframe)

        input_element = driver.find_element(By.ID, value="enter_date") # 找到 预约日期
        driver.execute_script("arguments[0].removeAttribute('readonly')", input_element)
        input_element.clear()
        input_element.send_keys(f'{lfd} 00:00:00') #lfd.strftime('%Y/%m/%d')
        # WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, '//*[@class="laydate-footer-btns"]/span[3]'))).click() #点击日期 确定
        WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, '//*[@class="layui-form"]/div[2]/button'))).click() # 点击 提交

        print(f'Submitted: {row} row') 
        sleep(3)
        row+=1



print("Finished")
driver.quit()
