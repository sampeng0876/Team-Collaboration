from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from datetime import datetime, date, timedelta
from time import sleep
import tkinter as tk
from tkcalendar import DateEntry
from selenium.webdriver.chrome.options import Options
from tkinter import *
from tkcalendar import *
import datetime as dt

# Multiple Dates Checker
def multi_date_checker(appt_dates, wait, start_time, end_time, driver, check_days):
    for appt_date in appt_dates:
        days_checked = 0
        start_over = 1
        while True:
            if appt_date.weekday() in [5, 6]:  # Skip weekends (Saturday: 5, Sunday: 6)
                appt_date += timedelta(days=1)
                continue

            # Find the calendar picker element
            calendar_picker = wait.until(EC.presence_of_element_located((By.XPATH,'//*[@id="calendar0"]')))

            # Click the date picker element to open the date picker
            calendar_picker.click()
            sleep(1)

            # Locate the dates of this month
            picker_day_current = driver.find_elements(by="xpath", value='//div[@class="react-flex-view align-content-center justify-content-center react-datepicker-picker day current"]')
            picker_day_current_selected = driver.find_elements(by="xpath", value='//div[@class="react-flex-view align-content-center justify-content-center react-datepicker-picker day current selected"]')

            # Create a for loop to find the Appointment Date
            for date in picker_day_current + picker_day_current_selected:
                date_text = date.find_element(by="xpath", value='./span').text
                if date_text == appt_date.strftime("%d"):
                    date.click()
                    sleep(1)
                    break

            print(f"Selected Appt Date: {appt_date}")
            print(f"Selected Appt Times From: {start_time} to {end_time}")

            # Click Time Slots
            time_slots = wait.until(EC.presence_of_element_located((By.XPATH,'//*[@id="ipgrid_0_slot"]/i')))
            time_slots.click()

            # Locate the Appointment Time Slots
            time_slots_container = driver.find_elements(by="xpath", value='//*[@class="visible menu transition"]/div')

            available_time_slots = []

            # Check available time slots
            for time in time_slots_container:
                try:
                    # Read time slot text
                    time_slots_text = time.find_element(by="xpath", value='./span').text  
                    if time_slots_text.strip():
                        available_time_slots.append(time_slots_text)
                        print(time_slots_text) 
                except:
                    print("No Time Slots Appended")

            # Check available times in selected range from start time to end time
            available_times = [time for time in available_time_slots if start_time <= time <= end_time]

            # If no available time slots or no time slots in selected range
            if not available_time_slots or not available_times:
                print(f"No available time slots or no time slots in selected range for {appt_date}. \nChecking next appointment date.")
                days_checked += 1
                appt_date += timedelta(days=1)
                
                if days_checked == len(appt_dates):
                    appt_date = appt_dates[0]
                    print(f"Sorry, No Time Slot Was Booked in {check_days} days. Starting Over again {start_over} times")
                    start_over += 1
                    days_checked = 0
                continue

            # Error counter
            error_count = 0

            # Iterate over the time slots container
            for click_time in time_slots_container:
                try:
                    click_time_slots_text = click_time.find_element(by="xpath", value='./span').text
                    earliest_time = available_times[0]

                    if click_time_slots_text == earliest_time:
                        click_time.click()
                        #print(f"Selected Appt Times From: {start_time} to {end_time}")
                        print(f"Successfully Booked The Earliest Time: {earliest_time}")
                        break
                except:
                    if error_count == 0:
                        print(f"No Time Slots Available From: {start_time} to {end_time}")
                    error_count += 1

            # Break the while loop if a successful booking is made
            if earliest_time:
                break

            # Increment the appointment date by one day
            appt_date += timedelta(days=1)

        if earliest_time:
            break
        # Print a message if no earliest time slot was booked after checking all days
        if days_checked == len(appt_dates):
            appt_date = appt_dates[0]
            print(f"Sorry, No Time Slot Was Booked in {check_days} days. Starting Over again {start_over} times")
            start_over += 1
            days_checked = 0

        days_checked = 0  # Reset the days_checked counter

