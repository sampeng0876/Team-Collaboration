from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.remote.webelement import WebElement

# change this line
path_driver = "your_path_to_chrome_driver"

by, buy_selector, cookies_selector = By.CSS_SELECTOR, 'button#checkout_submit', "button#onetrust-accept-btn-handler"

driver = webdriver.Chrome(path_driver)
driver.maximize_window()
actions = ActionChains(driver)
driver.get("https://www.spotify.com/us/purchase/offer/premium-family/?country=US")


# wait for loading buy button
sls = wait.until(EC.presence_of_all_elements_located((by, buy_selector)))
if sls:
    # get accept cookies button element and click
    cookies_accept = driver.find_element_by_css_selector(cookies_selector)
    if isinstance(cookies_accept, WebElement):
        cookies_accept.click()
        
    # get buy button element, move to element and click
    buy = driver.find_element_by_css_selector(buy_selector)
    if isinstance(buy, WebElement) and buy.is_displayed() and buy.is_enabled():
        actions.move_to_element(buy).click(buy).perform()
