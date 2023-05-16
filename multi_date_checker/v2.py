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
def multi_date_checker(appt_date, wait, start_time, end_time, driver):
    days_checked = 0
    start_over = 1
    selected_dates = []  # Store the selected dates for looping

    while start_over <= 3:  # Set the maximum number of start-over attempts
        successful_booking = False
        while days_checked < 3:
            if appt_date.weekday() in [5, 6]:  # Skip weekends (Saturday: 5, Sunday: 6)
                appt_date += timedelta(days=1)
                continue
            # Find the calendar picker element
            calendar_picker = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="calendar0"]')))

            # Click the date picker element to open the date picker
            calendar_picker.click()
            sleep(1)

            # Locate the dates of this month
            picker_day_current = driver.find_elements(by="xpath", value='//div[@class="react-flex-view align-content-center justify-content-center react-datepicker-picker day current"]')
            picker_day_current_selected = driver.find_elements(by="xpath", value='//div[@class="react-flex-view align-content-center justify-content-center react-datepicker-picker day current selected"]')

            # Find the Appointment Date
            selected_date = None
            for date_element in picker_day_current + picker_day_current_selected:
                date_text = date_element.find_element(by="xpath", value='./span').text
                if date_text == appt_date.strftime("%d"):
                    selected_date = date_element
                    date_element.click()
                    break
           
            if selected_date is None:
                print(f"No available time slots or no time slots in selected range for {appt_date}. \nChecking the next appointment date.")
                appt_date += timedelta(days=1)
                days_checked += 1
                continue

            print(f"Selected Appointment Date: {appt_date}")

            # Click Time Slots
            time_slots = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="ipgrid_0_slot"]/i')))
            time_slots.click()

            # Locate the Appointment Time Slots
            time_slots_container = driver.find_elements(by="xpath", value='//*[@class="visible menu transition"]/div')

            # Check available time slots
            available_time_slots = [time_slot.find_element(by="xpath", value='./span').text for time_slot in time_slots_container]
            
            
            available_times = [time for time in available_time_slots if start_time <= time <= end_time]

            if not available_time_slots or not available_times:
                print(f"No available time slots or no time slots in selected range for {appt_date}. \nChecking the next appointment date.")
                appt_date += timedelta(days=1)
                days_checked += 1
                continue

            # Iterate over the time slots container
            
            for time_slot in time_slots_container:
                time_slot_text = time_slot.find_element(by="xpath", value='./span').text
                if time_slot_text == available_times[0]:
                    time_slot.click()
                    print(f"Selected Appointment Times From: {start_time} to {end_time}")
                    print(f"Successfully Booked The Earliest Time: {time_slot_text}")
                    successful_booking = True
                    break

            if successful_booking:
                break

            appt_date += timedelta(days=1)
            days_checked += 1

        if successful_booking:
            break

        if days_checked == 3:
            print(f"Sorry, no time slot was booked within 3 days. Starting over again {start_over} times.")
            selected_dates.append(appt_date)
            start_over += 1

            if selected_dates:
                appt_date = selected_dates[start_over - 1 - 1] - timedelta(days=3)
            else:
                appt_date -= timedelta(days=3)
                print(f"This is {appt_date} - 3 days")
            days_checked = 0  # Reset the days_checked counter
        
    if start_over > 3:
        print("No available time slots were found after 3 attempts.")
        return

    
