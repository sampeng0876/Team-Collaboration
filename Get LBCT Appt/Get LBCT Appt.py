from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
import tkinter as tk
from selenium.webdriver.chrome.options import Options
from tkinter import *
from tkcalendar import *
import datetime as dt
import sv_ttk
import tkinter
from tkinter import ttk
import customtkinter
from bs4 import BeautifulSoup
from openpyxl import load_workbook



# By Pass reCaptcha
# https://www.youtube.com/watch?v=LDlD5k8S0oQ&ab_channel=ThePyCoach

# Get Cookies
# Video: https://www.youtube.com/watch?v=cVnYod9Fhko&ab_channel=JieJenn
# Cookies Convertor: https://curlconverter.com/


# Create a function to get the selected value and close the window
###################################################################################################################
def on_submit():
    global container_entry
    
    # Get container entries
    data = container_entry.get("1.0", "end-1c")
    lines = data.split("\n")
    container_list.extend(lines)
    container_entry.delete("1.0", "end")
    print("Container List:")
    print(container_list)  
    root.destroy()


# UI Window Settings
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
x = (screen_width - 210) // 2
y = (screen_height - 250) // 2

# Set the position of the window
root.geometry(f"210x250+{x}+{y}")

# List to store container entries
container_list = []

# Create a label for data entry
Label(root, text="Enter Container Number:").grid(column=1, row=1, padx=5, pady=5)
container_entry = customtkinter.CTkTextbox(root, height=160, width=200, border_width=1 ,border_color="lightgray" )
container_entry.grid(column=1, row=2, padx=5, pady=5)

# Create submit button
# style = ttk.Style()
# style.configure('Blue.TButton', foreground='blue', background='white')
submit_button = customtkinter.CTkButton(root, width=60, text="OK", command=on_submit)
submit_button.grid(column=1, row=7, padx=10, pady=5)

# Start the mainloop to display the window
root.mainloop()

# Main
####################################################################################################################


# chrome_options = Options()
# chrome_options.add_argument("--headless")
# # #chrome_options.add_argument("--disable-extensions")
# # #chrome_options.add_argument("--disable-gpu")


# Set the options to run the browser in headless mode
# chrome_options.headless = True
# cookies = {
#     'ASP.NET_SessionId': 'ajcfidn1syij0nbqrx41qcyr',
#     '__RequestVerificationToken': 'R3Ls-4a0tP3zMvpVikqXW8u_o_xMqXq-IT21FeZjFgMb6lX18QssE91BZV6wXDwZVbS5Pl_eTof6quUVN1yerTgZ9UkBX6zeIlmw2xrZ8mo1',
#     'BIGipServerwww.lbct.com.app~www.lbct.com_pool': '3221673482.20480.0000',
#     '.ASPXAUTH': '845485CAC45DF8788528D7F49834A1F5E69647807D312DE266DCAAFE8725C4881E8BDE3FEB2FFC96B42223D4BA239BD99559A6AE44493EE5DBA3EC2A87A1C5ACD87E4D4527D402FA1D6E8E335CE937C35969F33152BF07FCB219B9AD6D4CF18B296B619D56EE87DF87AA2CB7429B65B9D258963D346B1DB4B4E83DFD927A3FF4',
#     'TS017fbeab': '01ce6a9536be68ad6f4059a482d3316721a8416acef5bca69f2a797b6d895a42ffffdd4cd51b92413cb56e4ca34e6d877bb6018555',
#     'TSPD_101': '08d349dcdfab280007a29169d6ac66b3550ada38700f5ef2d62c858e3da86c241c6c98c1d99b16dba5dd9fd434dcad87086f3dd718051800f0b2765b473f8a55b971947562f2895f99073794d53abed7',
#     'TS559b2606027': '08d349dcdfab2000740e21de21eb43f51cb04d5113b04293c631baba534620cbc0c76d7ccc499dd5080a5e83cd113000615df65a7b189a25f264bba242775c3f86b2015bf0cc286c22ee2a6f4bcdbefd8cd5b1fa668d4347c6a741e2ba7068ff',
#     'TS80540fb2077': '08d349dcdfab2800fbfd53e2b14fa3527bd0e454a139a3b160fd1368107211798f94fc721db90d3411c874781ea3d368084af3f2da17200077433de7c1f17223107675f1aa47addb8a1552942bed712966f0ddbca439977b',
#     'TS00000000076': '08d349dcdfab28006f125f257b9f657e1343f80e85c58e6d5ffae69943c484eb6a3d8b1b8d8d66736fdecc4a5a5cfc4e086bdfc88d09d000ab0320d87f490b52dbf745bec482a72519a807ee1c6c448220143739f624fcd4c9e5804f1dae9d5955b038bbe4326373e77837d69741ae41b63841e75a847f78064f3f8620bcad556eefd3475ec6ea30df060c77b49e15ccce57c6d7be0959d6148106af88a9d33f5e8f76bd561480b663401d65bdbfdac0121deef80ab6cace14903e25ee45fa08a1bb1ef3fbd80dd359e92aed7b7dd1bfc435922b3b27d0ba3a3cfc5b14d05263ae47686a5feb1d97b7d5b2ed7fcb6fc93ad2a7d5a66fd07a12a3e7c987a519b9e1da1e1ac9e4672f',
#     'TSPD_101_DID': '08d349dcdfab28006f125f257b9f657e1343f80e85c58e6d5ffae69943c484eb6a3d8b1b8d8d66736fdecc4a5a5cfc4e086bdfc88d063800326a663cc58168d3c6e67eaf3ab8835fd6b96538769d578945eec8a1322b82334d577c648cd185e8ffd56638d94b7412e3339bcd2efb3e83',
#     'TS80540fb2075': '0502c10108d349dcdfab28006f125f257b9f657e1343f80e85c58e6d5ffae69943c484eb6a3d8b1b8d8d66736fdecc4a5a5cfc4e:086bdfc88d04a800d56b66f3601f8ad0b0a1f02e73e4476363283a67359ab6ab3934da8a80dc7428bdf3e880d4f8e4de0e42384d1ce0f34951df243e7d6b043b4fe0ed4f429931d33ef959aefa3616df7f1dafc53a788db73ed77c38c9d51ff43f2863a014a07974b1e6005dd8b199bec6b3d90f4bdb0f3cfa9e687b327e85752c8320fea59c5020b2054bc6a3e9d3dc1b2b7b0530a1b0422fa4e2003c38f0c3e90e6cb6ae73bd718e5feccf524896e3a00108d349dcdfab28006f125f257b9f657e1343f80e85c58e6d5ffae69943c484eb6a3d8b1b8d8d66736fdecc4a5a5cfc4e086bdfc88d109800a708d0857b64c8baf43c2e8ae40312e0487b1a35571b4627632f19e4a7e7b2c74f0910d99539f556197c70c66519ba42e15924abfbc898e4836227b9d99bb4b55acf83ca8a56685faf53b4c4a867da2bad0b2fcdaaa37599df79ab7e914f8b5c24cb858018effd9adc6aaa91cd76726ea2d238b2a319b9ce3b36f1763adc8713a8e2b347fc96a0b9ba5f037e132641915ce65e130645e58d0001000f00008d349dcdfab2000fb76fbb1c12287ceb24200302c7e33259460c0f728da0345b629ad049c1aa63108eaa4e0ee0a480037987591331364d6b95493cd0e163d5e0bcf5fcd068927dab96c93f81527dc4230bbb7cb283969b4c32884081e8871fd64d907b43be657b6c79e5d01a1f4ca6bed92537c0b0bd0762700https%3a%2f%2fwww.lbct.com%2fViewMyList',
# }

# headers = {
#     'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
#     'Accept-Language': 'en-US,en;q=0.9',
#     'Cache-Control': 'max-age=0',
#     'Connection': 'keep-alive',
#     # 'Cookie': 'ASP.NET_SessionId=ajcfidn1syij0nbqrx41qcyr; __RequestVerificationToken=R3Ls-4a0tP3zMvpVikqXW8u_o_xMqXq-IT21FeZjFgMb6lX18QssE91BZV6wXDwZVbS5Pl_eTof6quUVN1yerTgZ9UkBX6zeIlmw2xrZ8mo1; BIGipServerwww.lbct.com.app~www.lbct.com_pool=3221673482.20480.0000; .ASPXAUTH=845485CAC45DF8788528D7F49834A1F5E69647807D312DE266DCAAFE8725C4881E8BDE3FEB2FFC96B42223D4BA239BD99559A6AE44493EE5DBA3EC2A87A1C5ACD87E4D4527D402FA1D6E8E335CE937C35969F33152BF07FCB219B9AD6D4CF18B296B619D56EE87DF87AA2CB7429B65B9D258963D346B1DB4B4E83DFD927A3FF4; TS017fbeab=01ce6a9536be68ad6f4059a482d3316721a8416acef5bca69f2a797b6d895a42ffffdd4cd51b92413cb56e4ca34e6d877bb6018555; TSPD_101=08d349dcdfab280007a29169d6ac66b3550ada38700f5ef2d62c858e3da86c241c6c98c1d99b16dba5dd9fd434dcad87086f3dd718051800f0b2765b473f8a55b971947562f2895f99073794d53abed7; TS559b2606027=08d349dcdfab2000740e21de21eb43f51cb04d5113b04293c631baba534620cbc0c76d7ccc499dd5080a5e83cd113000615df65a7b189a25f264bba242775c3f86b2015bf0cc286c22ee2a6f4bcdbefd8cd5b1fa668d4347c6a741e2ba7068ff; TS80540fb2077=08d349dcdfab2800fbfd53e2b14fa3527bd0e454a139a3b160fd1368107211798f94fc721db90d3411c874781ea3d368084af3f2da17200077433de7c1f17223107675f1aa47addb8a1552942bed712966f0ddbca439977b; TS00000000076=08d349dcdfab28006f125f257b9f657e1343f80e85c58e6d5ffae69943c484eb6a3d8b1b8d8d66736fdecc4a5a5cfc4e086bdfc88d09d000ab0320d87f490b52dbf745bec482a72519a807ee1c6c448220143739f624fcd4c9e5804f1dae9d5955b038bbe4326373e77837d69741ae41b63841e75a847f78064f3f8620bcad556eefd3475ec6ea30df060c77b49e15ccce57c6d7be0959d6148106af88a9d33f5e8f76bd561480b663401d65bdbfdac0121deef80ab6cace14903e25ee45fa08a1bb1ef3fbd80dd359e92aed7b7dd1bfc435922b3b27d0ba3a3cfc5b14d05263ae47686a5feb1d97b7d5b2ed7fcb6fc93ad2a7d5a66fd07a12a3e7c987a519b9e1da1e1ac9e4672f; TSPD_101_DID=08d349dcdfab28006f125f257b9f657e1343f80e85c58e6d5ffae69943c484eb6a3d8b1b8d8d66736fdecc4a5a5cfc4e086bdfc88d063800326a663cc58168d3c6e67eaf3ab8835fd6b96538769d578945eec8a1322b82334d577c648cd185e8ffd56638d94b7412e3339bcd2efb3e83; TS80540fb2075=0502c10108d349dcdfab28006f125f257b9f657e1343f80e85c58e6d5ffae69943c484eb6a3d8b1b8d8d66736fdecc4a5a5cfc4e:086bdfc88d04a800d56b66f3601f8ad0b0a1f02e73e4476363283a67359ab6ab3934da8a80dc7428bdf3e880d4f8e4de0e42384d1ce0f34951df243e7d6b043b4fe0ed4f429931d33ef959aefa3616df7f1dafc53a788db73ed77c38c9d51ff43f2863a014a07974b1e6005dd8b199bec6b3d90f4bdb0f3cfa9e687b327e85752c8320fea59c5020b2054bc6a3e9d3dc1b2b7b0530a1b0422fa4e2003c38f0c3e90e6cb6ae73bd718e5feccf524896e3a00108d349dcdfab28006f125f257b9f657e1343f80e85c58e6d5ffae69943c484eb6a3d8b1b8d8d66736fdecc4a5a5cfc4e086bdfc88d109800a708d0857b64c8baf43c2e8ae40312e0487b1a35571b4627632f19e4a7e7b2c74f0910d99539f556197c70c66519ba42e15924abfbc898e4836227b9d99bb4b55acf83ca8a56685faf53b4c4a867da2bad0b2fcdaaa37599df79ab7e914f8b5c24cb858018effd9adc6aaa91cd76726ea2d238b2a319b9ce3b36f1763adc8713a8e2b347fc96a0b9ba5f037e132641915ce65e130645e58d0001000f00008d349dcdfab2000fb76fbb1c12287ceb24200302c7e33259460c0f728da0345b629ad049c1aa63108eaa4e0ee0a480037987591331364d6b95493cd0e163d5e0bcf5fcd068927dab96c93f81527dc4230bbb7cb283969b4c32884081e8871fd64d907b43be657b6c79e5d01a1f4ca6bed92537c0b0bd0762700https%3a%2f%2fwww.lbct.com%2fViewMyList',
#     'Referer': 'https://www.lbct.com/ViewMyList',
#     'Sec-Fetch-Dest': 'document',
#     'Sec-Fetch-Mode': 'navigate',
#     'Sec-Fetch-Site': 'same-origin',
#     'Upgrade-Insecure-Requests': '1',
#     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36',
#     'sec-ch-ua': '"Google Chrome";v="113", "Chromium";v="113", "Not-A.Brand";v="24"',
#     'sec-ch-ua-mobile': '?0',
#     'sec-ch-ua-platform': '"Windows"',
# }

# Load the workbook
workbook = load_workbook('Get Terminal Info.xlsx')

# Select sheet2
sheet = workbook['LBCT']  # Change the sheet name accordingly

# # Create a new Chrome session
driver = webdriver.Chrome()
driver.maximize_window()
wait = WebDriverWait(driver, 10)

# driver.get("https://www.lbct.com/Login/Login")
driver.get("https://www.lbct.com/Home/index")

# # Add the cookies
# for cookie_name, cookie_value in cookies.items():
#     cookie = {
#         'name': cookie_name,
#         'value': cookie_value
#     }
#     driver.add_cookie(cookie)

# sleep(10)
# # Refresh the page to apply the cookies
# driver.refresh()

# containers = ['CCLU7723702',
#               'CSNU8069786',
#               'BMOU5128510',
#               'OOCU8990868',
#               'CCLU7308661',]

# containers = ['CSLU1957155']

# Container List
# container_list = '\n'.join(containers)
container_list = '\n'.join(container_list)

# V1 Make Appointment
################################################################
# WebDriverWait(driver, 15).until( 
#     EC.presence_of_all_elements_located((By.XPATH, '//*[@id="UserName"]'))
# )
# driver.find_element(By.XPATH, '//*[@id="UserName"]').send_keys("p1logistics@mail.com")

# driver.find_element(By.XPATH, '//*[@id="Password"]').send_keys("8802616")
# #driver.get('https://www.lbct.com/Login/Login')

# WebDriverWait(driver, 20).until(EC.frame_to_be_available_and_switch_to_it((By.XPATH,"//iframe[@title='reCAPTCHA']")))
# WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "div.recaptcha-checkbox-border"))).click()
# sleep(20)


# driver.switch_to.default_content()

# # Click cookies Accept Button
# driver.find_element(By.XPATH, '//*[@id="cookie-bar"]/div/span[2]/button').click()


# # WebDriverWait(driver, 20).until(EC.frame_to_be_available_and_switch_to_it((By.XPATH, '//*[@id="loginBoxLogin"]')))
# WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH,'//*[@id="loginBoxLogin"]')))
# driver.find_element(By.XPATH, '//*[@id="loginBoxLogin"]').click()

# # driver.find_element(By.XPATH, '//*[@id="cookie-bar"]/div/span[2]/button').click() # Click Cookies

# WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH,'//*[@class ="k-textbox sideBarCargoAvailabilityTextArea textareaPlaceholder"]')))
# driver.find_element(By.XPATH, '//*[@class ="k-textbox sideBarCargoAvailabilityTextArea textareaPlaceholder"]').click() # Search Box Send Keys
# driver.find_element(By.XPATH, '//*[@class ="k-textbox sideBarCargoAvailabilityTextArea textareaPlaceholder"]').send_keys(container_list)
# driver.find_element(By.XPATH, '//*[@id="sideBarTextareaSubmitBtn"]').click() # Click Search Button

# ################################################################
# # Expand Tables
# get_expand_icon = WebDriverWait(driver, 10).until(
#     # //*[@class="k-hierarchy-cell"]/a
#     # //*[@class="k-icon k-i-expand"]
#     EC.presence_of_all_elements_located((
#     By.XPATH, '//*[@class="k-hierarchy-cell"]/a')))

# # Click on the expand icon
# for icon in get_expand_icon[1:]:
#     icon.click()
#     sleep(1)

# V2 Search Info
################################################################

WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH,'//*[@id="circle-inner"]')))
driver.find_element(By.XPATH, '//*[@id="circle-inner"]').click() # Enter

# Click cookies Accept Button
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH,'//*[@id="cookie-bar"]/div/span[2]/button')))
driver.find_element(By.XPATH, '//*[@id="cookie-bar"]/div/span[2]/button').click()

WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH,'//*[@class ="k-textbox sideBarCargoAvailabilityTextArea textareaPlaceholder"]'))) # WAit for Search Box
driver.find_element(By.XPATH, '//*[@class ="k-textbox sideBarCargoAvailabilityTextArea textareaPlaceholder"]').click() # Cllick Search Box
driver.find_element(By.XPATH, '//*[@class ="k-textbox sideBarCargoAvailabilityTextArea textareaPlaceholder"]').send_keys(container_list) # Search Box Send Keys
driver.find_element(By.XPATH, '//*[@id="sideBarTextareaSubmitBtn"]').click() # Click Search Button

################################################################
# Expand Tables

WebDriverWait(driver, 10).until(
    # //*[@class="k-hierarchy-cell"]/a
    # //*[@class="k-icon k-i-expand"]
    EC.element_to_be_clickable((
    By.XPATH, '//*[@class="k-icon k-i-expand"]')))
get_expand_icon = driver.find_elements(By.XPATH, '//*[@class="k-icon k-i-expand"]')
# print(get_expand_icon)
# Click on the expand icon
for icon in get_expand_icon:
    icon.click()
    sleep(1)

# # Get Details Information
# get_details_info = WebDriverWait(driver, 10).until(
#     EC.presence_of_all_elements_located((
#     By.XPATH, '//*[@class="table-default container-table-horizontal"]/tbody/tr/td/strong')))

# details_info_list = []

# # Loop through the container_id_elements and extract the text
# for info in get_details_info:
#     info_text = info.text
#     print(info_text)
#     details_info_list.append(info_text)

# V2 with beautiful soup
################################################################ 

# Scrape data
soup = BeautifulSoup(driver.page_source, 'html.parser')

# Read all tr from tbody tag
trs = soup.find_all(class_=['k-master-row','k-detail-row', 'k-detail-row k-alt','k-alt k-master-row']) # 

data_list=[]

# V2 Get Data
# GOOD TO USE
################################################################ 

for tr in trs:    

    # GOOD TO USE
    # Get the Main Data
    if 'data-uid' in tr.attrs:
    # Extract the desired data from the element
        main_data = {
            "Container": tr.find("p").text.strip(),
            "Available": tr.find_all("td")[2].text.strip(),
            "Type": tr.find_all("td")[3].text.strip(),
            "Line": tr.find_all("td")[4].text.strip(),
            "Vessel": tr.find_all("td")[5].text.strip(),                        
            # Add more data extraction as needed
        }
        
        data_list.append(main_data)
    else:
        # print("No Main Data")
        pass

    # GOOD TO USE
    # Get the Fees Tab 
    if tr.find('div', class_ ='table-container'):
        # Extract the desired data from the element
        fees_data = {
            "LINE DEMURRAGE": tr.find_all("td")[3].text.strip(),
            "LFD": tr.find_all("td")[5].text.strip(),
            "EXTENDED DWELL TIME FEE": tr.find_all("td")[6].text.strip(),
            "Total": tr.find_all("td")[13].text.strip(),           
            # Add more data extraction as needed
        }
        # Merge the two dictionaries into a single dictionary
        main_data.update(fees_data)

    else:
        fees_data = {
            "LINE DEMURRAGE": 'N/A',
            "LFD": 'N/A',
            "EXTENDED DWELL TIME FEE": 'N/A',
            "Total": 'N/A',           
            # Add more data extraction as needed
        }
        # Merge the two dictionaries into a single dictionary
        main_data.update(fees_data)
 
    # GOOD TO USE
    # Get The Details Tab
    if tr.find('div', class_ ='table-container'):
        # Extract the desired data from the element
        details_data = {
            "Discharged": tr.find_all("strong")[0].text.strip(),
            "Location": tr.find_all("strong")[1].text.strip(),
            "Delivered": tr.find_all("strong")[2].text.strip(),
            "Full/Empty": tr.find_all("strong")[3].text.strip(),
            "Exam Status": tr.find_all("strong")[4].text.strip(),
            "Bond Status": tr.find_all("strong")[5].text.strip(),          
            # Add more data extraction as needed
        }
        # Merge the two dictionaries into a single dictionary
        main_data.update(details_data) 
    else:
        # print("No Details Data")
        pass  
    
    # 'k-detail-row' in tr.get('class', []) or 'k-detail-row k-alt' in tr.get('class', [])   
    # GOOD TO USE 
    # Get the Appointments Tab
    if tr.find('tbody', role='rowgroup'):
        appt_data = {
        "Date": tr.find_all('td', role='gridcell')[0].text.strip(),
        "Time": tr.find_all('td', role='gridcell')[1].text.strip(),
        "State": tr.find_all('td', role='gridcell')[2].text.strip(),
        "Company": tr.find_all('td', role='gridcell')[3].text.strip(),
        "Appt": tr.find_all('td', role='gridcell')[4].text.strip(),
        "SUB-H": tr.find_all('td', role='gridcell')[5].text.strip(),
        }
        main_data.update(appt_data)
        # print(appt_data)
    else:
        appt_data = {
        "Date": 'N/A',
        "Time": 'N/A',
        "State": 'N/A',
        "Company": 'N/A',
        "Appt": 'N/A',
        "SUB-H": 'N/A',
        }
        main_data.update(appt_data)
    
    # GOOD TO USE
    # Get the Holds Tab
    if tr.find('tbody', role='rowgroup'): 
        if  len(tr.find_all('td',role='gridcell')) == 21:
            holds_data = {
            "BLOCK_DOWN": tr.find_all('td', role='gridcell')[7].text.strip(),
            "BLOCK_DOWN_STATUS": tr.find_all('td', role='gridcell')[8].text.strip(),
            # "9": tr.find_all('td', role='gridcell')[9].text.strip(),
            "TMF_CONTAINER_HOLD": tr.find_all('td', role='gridcell')[10].text.strip(),
            "TMF_CONTAINER_HOLD_STATUS": tr.find_all('td', role='gridcell')[11].text.strip(),
            # "12": tr.find_all('td', role='gridcell')[12].text.strip(),
            "CTF_CONTAINER_HOLD": tr.find_all('td', role='gridcell')[13].text.strip(),
            "CTF_CONTAINER_HOLD_STATUS": tr.find_all('td', role='gridcell')[14].text.strip(),
            # # "15": tr.find_all('td', role='gridcell')[15].text.strip(),
            "CUSTOMS_DEFAULT_HOLD": tr.find_all('td', role='gridcell')[16].text.strip(),
            "CUSTOMS_DEFAULT_HOLD_STATUS": tr.find_all('td', role='gridcell')[17].text.strip(),
            # "18": tr.find_all('td', role='gridcell')[18].text.strip(),
            "FREIGHT_BL_HOLD": tr.find_all('td', role='gridcell')[19].text.strip(),
            "FREIGHT_BL_HOLD_STATUS": tr.find_all('td', role='gridcell')[20].text.strip(),
            }
            main_data.update(holds_data)
            # print(len(tr.find_all('td',role='gridcell')))
        if  len(tr.find_all('td',role='gridcell')) == 18:
            holds_data = {
            "TMF_CONTAINER_HOLD": tr.find_all('td', role='gridcell')[7].text.strip(),
            "TMF_CONTAINER_HOLD_STATUS": tr.find_all('td', role='gridcell')[8].text.strip(),
            # "9": tr.find_all('td', role='gridcell')[9].text.strip(),
            "CTF_CONTAINER_HOLD": tr.find_all('td', role='gridcell')[10].text.strip(),
            "CTF_CONTAINER_HOLD_STATUS": tr.find_all('td', role='gridcell')[11].text.strip(),
            # "12": tr.find_all('td', role='gridcell')[12].text.strip(),
            "CUSTOMS_DEFAULT_HOLD": tr.find_all('td', role='gridcell')[13].text.strip(),
            "CUSTOMS_DEFAULT_HOLD_STATUS": tr.find_all('td', role='gridcell')[14].text.strip(),
            # # "15": tr.find_all('td', role='gridcell')[15].text.strip(),
            "FREIGHT_BL_HOLD": tr.find_all('td', role='gridcell')[16].text.strip(),
            "FREIGHT_BL_HOLD_STATUS": tr.find_all('td', role='gridcell')[17].text.strip(),
            }
            main_data.update(holds_data)
            # print(len(tr.find_all('td',role='gridcell')))
    else:
        holds_data = {
        "BLOCK_DOWN": 'N/A',
        "BLOCK_DOWN_STATUS": 'N/A',
        # "9": tr.find_all('td', role='gridcell')[9].text.strip(),
        "TMF_CONTAINER_HOLD": 'N/A',
        "TMF_CONTAINER_HOLD_STATUS": 'N/A',
        # "12": tr.find_all('td', role='gridcell')[12].text.strip(),
        "CTF_CONTAINER_HOLD": 'N/A',
        "CTF_CONTAINER_HOLD_STATUS": 'N/A',
        # # "15": tr.find_all('td', role='gridcell')[15].text.strip(),
        "CUSTOMS_DEFAULT_HOLD": 'N/A',
        "CUSTOMS_DEFAULT_HOLD_STATUS": 'N/A',
        # "18": tr.find_all('td', role='gridcell')[18].text.strip(),
        "FREIGHT_BL_HOLD": 'N/A',
        "FREIGHT_BL_HOLD_STATUS": 'N/A',
        }
        main_data.update(holds_data)

# Step 3: Define the title-key mapping
title_key_mapping = {
    'Container': 'Container',
    'Available': 'Available',
    'Type': 'Type',
    'Line': 'Line',
    'Vessel': 'Vessel',
    'LINE DEMURRAGE': 'LINE DEMURRAGE',
    'LFD': 'LFD',
    'EXTENDED DWELL TIME FEE': 'EXTENDED DWELL TIME FEE',
    'Total': 'Total',        
    'Discharged': 'Discharged',
    'Location': 'Location',
    'Delivered': 'Delivered',
    'Full/Empty': 'Full/Empty',
    'Exam Status': 'Exam Status',
    'Bond Status': 'Bond Status',
    'Date': 'Date',
    'Time': 'Time',
    'Company': 'Company',
    'Appt': 'Appt',
    'SUB-H': 'SUB-H',
    'BLOCK_DOWN': 'BLOCK_DOWN',
    'BLOCK_DOWN_STATUS': 'BLOCK_DOWN_STATUS',
    'TMF_CONTAINER_HOLD': 'TMF_CONTAINER_HOLD',
    'TMF_CONTAINER_HOLD_STATUS': 'TMF_CONTAINER_HOLD_STATUS',
    'CTF_CONTAINER_HOLD': 'CTF_CONTAINER_HOLD',
    'CTF_CONTAINER_HOLD_STATUS': 'CTF_CONTAINER_HOLD_STATUS',
    'CUSTOMS_DEFAULT_HOLD': 'CUSTOMS_DEFAULT_HOLD',
    'CUSTOMS_DEFAULT_HOLD_STATUS': 'CUSTOMS_DEFAULT_HOLD_STATUS',
    'FREIGHT_BL_HOLD': 'FREIGHT_BL_HOLD',
    'FREIGHT_BL_HOLD_STATUS': 'FREIGHT_BL_HOLD_STATUS',
    # Add more titles and keys as needed
}


# Get the existing titles from row 1
titles = [cell.value for cell in sheet[1]]

# Save data to the Excel file
row_index = 2  # Start saving data at row 2 (A2)

for data in data_list:
    for title in titles:
        if title == 'Container':
            sheet.cell(row=row_index, column=titles.index(title) + 1).value = data['Container']
        elif title == 'Available':
            sheet.cell(row=row_index, column=titles.index(title) + 1).value = data['Available']
        elif title == 'Type':
            sheet.cell(row=row_index, column=titles.index(title) + 1).value = data['Type']
        elif title == 'Line':
            sheet.cell(row=row_index, column=titles.index(title) + 1).value = data['Line']
        elif title == 'Vessel':
            sheet.cell(row=row_index, column=titles.index(title) + 1).value = data['Vessel']
        elif title == 'LINE DEMURRAGE':
            sheet.cell(row=row_index, column=titles.index(title) + 1).value = data['LINE DEMURRAGE']
        elif title == 'LFD':
            sheet.cell(row=row_index, column=titles.index(title) + 1).value = data['LFD']
        elif title == 'EXTENDED DWELL TIME FEE':
            sheet.cell(row=row_index, column=titles.index(title) + 1).value = data['EXTENDED DWELL TIME FEE']
        elif title == 'Total':
            sheet.cell(row=row_index, column=titles.index(title) + 1).value = data['Total']
        elif title == 'Discharged':
            sheet.cell(row=row_index, column=titles.index(title) + 1).value = data['Discharged']
        elif title == 'Location':
            sheet.cell(row=row_index, column=titles.index(title) + 1).value = data['Location']
        elif title == 'Delivered':
            sheet.cell(row=row_index, column=titles.index(title) + 1).value = data['Delivered']
        elif title == 'Full/Empty':
            sheet.cell(row=row_index, column=titles.index(title) + 1).value = data['Full/Empty']
        elif title == 'Exam Status':
            sheet.cell(row=row_index, column=titles.index(title) + 1).value = data['Exam Status']
        elif title == 'Bond Status':
            sheet.cell(row=row_index, column=titles.index(title) + 1).value = data['Bond Status']
        elif title == 'Date':
            sheet.cell(row=row_index, column=titles.index(title) + 1).value = data['Date']
        elif title == 'Time':
            sheet.cell(row=row_index, column=titles.index(title) + 1).value = data['Time']
        elif title == 'Company':
            sheet.cell(row=row_index, column=titles.index(title) + 1).value = data['Company']
        elif title == 'Appt':
            sheet.cell(row=row_index, column=titles.index(title) + 1).value = data['Appt']
        elif title == 'SUB-H':
            sheet.cell(row=row_index, column=titles.index(title) + 1).value = data['SUB-H']
        elif title == 'BLOCK_DOWN':
            sheet.cell(row=row_index, column=titles.index(title) + 1).value = data['BLOCK_DOWN']
        elif title == 'BLOCK_DOWN_STATUS':
            sheet.cell(row=row_index, column=titles.index(title) + 1).value = data['BLOCK_DOWN_STATUS']
        elif title == 'TMF_CONTAINER_HOLD':
            sheet.cell(row=row_index, column=titles.index(title) + 1).value = data['TMF_CONTAINER_HOLD']
        elif title == 'TMF_CONTAINER_HOLD_STATUS':
            sheet.cell(row=row_index, column=titles.index(title) + 1).value = data['TMF_CONTAINER_HOLD_STATUS']
        elif title == 'CTF_CONTAINER_HOLD':
            sheet.cell(row=row_index, column=titles.index(title) + 1).value = data['CTF_CONTAINER_HOLD']
        elif title == 'CTF_CONTAINER_HOLD_STATUS':
            sheet.cell(row=row_index, column=titles.index(title) + 1).value = data['CTF_CONTAINER_HOLD_STATUS']
        elif title == 'CUSTOMS_DEFAULT_HOLD':
            sheet.cell(row=row_index, column=titles.index(title) + 1).value = data['CUSTOMS_DEFAULT_HOLD']
        elif title == 'CUSTOMS_DEFAULT_HOLD_STATUS':
            sheet.cell(row=row_index, column=titles.index(title) + 1).value = data['CUSTOMS_DEFAULT_HOLD_STATUS']
        elif title == 'FREIGHT_BL_HOLD':
            sheet.cell(row=row_index, column=titles.index(title) + 1).value = data['FREIGHT_BL_HOLD']
        elif title == 'FREIGHT_BL_HOLD_STATUS':
            sheet.cell(row=row_index, column=titles.index(title) + 1).value = data['FREIGHT_BL_HOLD_STATUS']
        # Add more conditions for additional titles as needed

    row_index += 1
# Save the modified workbook
workbook.save("Get Terminal Info.xlsx")


print("Finished")


# Close the browser
driver.quit()