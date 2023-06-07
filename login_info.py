from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from datetime import datetime, date, timedelta
 


def login_info(username,driver):
    if username == 'p1':
        driver.find_element(By.XPATH, '//*[@id="Login_form"]/div[1]/div/div/input').send_keys("P1logistics")
        driver.find_element(By.XPATH, '//*[@id="Login_form"]/div[2]/div/div/input').send_keys("P1log5418")
    elif username == '20':
        driver.find_element(By.XPATH, '//*[@id="Login_form"]/div[1]/div/div/input').send_keys("twenty")
        driver.find_element(By.XPATH, '//*[@id="Login_form"]/div[2]/div/div/input').send_keys("20Trans!")
    elif username == 'yuna': 
        driver.find_element(By.XPATH, '//*[@id="Login_form"]/div[1]/div/div/input').send_keys("wcofreightinc@gmail.com")
        driver.find_element(By.XPATH, '//*[@id="Login_form"]/div[2]/div/div/input').send_keys("Seawolf321!")
    elif username == 'p2':
        driver.find_element(By.XPATH, '//*[@id="Login_form"]/div[1]/div/div/input').send_keys("p1logistics168")
        driver.find_element(By.XPATH, '//*[@id="Login_form"]/div[2]/div/div/input').send_keys("Port@20072009")
    elif username == 'jimbo':
        driver.find_element(By.XPATH, '//*[@id="Login_form"]/div[1]/div/div/input').send_keys("alinet")
        driver.find_element(By.XPATH, '//*[@id="Login_form"]/div[2]/div/div/input').send_keys("Alnd19885.")