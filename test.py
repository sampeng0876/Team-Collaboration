from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from datetime import datetime, timedelta

# Set up the driver
driver = webdriver.Chrome()
wait = WebDriverWait(driver, 10)

# Navigate to the page with the date picker
driver.get("https://example.com/date-picker")

# Find the date picker element
date_picker = wait.until(EC.presence_of_element_located((By.ID, "date-picker")))

# Get today's date
today = datetime.today()

# Calculate the date to select (e.g. 3 days from now)
date_to_select = today + timedelta(days=3)

# Convert the date to a string that matches the date format used by the date picker
date_str = date_to_select.strftime("%m/%d/%Y")

# Click the date picker element to open the date picker
date_picker.click()

# Find the day element for the date to select and click it
day_element = wait.until(EC.element_to_be_clickable((By.XPATH, f"//td[@data-date='{date_str}']")))
day_element.click()

# Close the browser
driver.quit()