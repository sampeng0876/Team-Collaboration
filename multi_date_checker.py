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

# Version v3_check_next_monty
# Multiple Dates Checker 
def multi_date_checker(appt_dates, wait, start_time, end_time, driver, check_days, container_number):
    previous_month = None
    earliest_time = None  # initializing earliest_time with a default value

    for appt_date in appt_dates:
        days_checked = 0
        start_over = 1
        while True:
            if appt_date.weekday() in [5, 6]:  # Skip weekends (Saturday: 5, Sunday: 6)
                appt_date += timedelta(days=1)
                continue
            # break the while loop if checked 3 times
            # elif start_over == 4:
            #     break


            # Find the calendar picker element
            calendar_picker = wait.until(EC.presence_of_element_located((By.XPATH,'//*[@id="calendar0"]')))

            # Click the date picker element to open the date picker
            calendar_picker.click()


            if previous_month is not None and int(previous_month) < int(appt_date.strftime("%m")):
                next_month = wait.until(EC.presence_of_element_located((By.XPATH,'//*[@id="ipgrid_0"]/div[3]/div[2]/div/div[2]/div/div[1]/div[1]/div[3]')))
                next_month.click()
                # print(f'Clicked next_month {appt_date.strftime("%m")}')

            elif previous_month is not None and int(previous_month) > int(appt_date.strftime("%m")):
                last_month = wait.until(EC.presence_of_element_located((By.XPATH,'//*[@id="ipgrid_0"]/div[3]/div[2]/div/div[2]/div/div[1]/div[1]/div[1]')))
                last_month.click()
                # print(f'Clicked last_month: {appt_date.strftime("%m")}')

                

            # Locate the dates of this month
            picker_day_current = driver.find_elements(by="xpath", value='//div[@class="react-flex-view align-content-center justify-content-center react-datepicker-picker day current"]')
            picker_day_current_selected = driver.find_elements(by="xpath", value='//div[@class="react-flex-view align-content-center justify-content-center react-datepicker-picker day current selected"]')
            

            # Create a for loop to find the Appointment Date
            for date in picker_day_current + picker_day_current_selected:                          
                # Get all dates in calendar                
                date_text = date.find_element(by="xpath", value='./span').text
                # print(date_text)
                # print(appt_date.strftime("%d").lstrip("0"))
                # # Check if the date is the same as the appointment date
                if date_text == appt_date.strftime("%d").lstrip("0"):
                    date.click()
                    previous_month = appt_date.strftime("%m")
                    # print(f'This Month {appt_date.strftime("%m")}')
                    # print("Cliecked date")
                    sleep(1)
                    break
            print(f"Checking...>>> {container_number}")    
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
                print(f"No available time slots or no time slots in selected range for {appt_date}.")
                days_checked += 1
                appt_date += timedelta(days=1)
                
                if days_checked == len(appt_dates):
                    appt_date = appt_dates[0]
                    print(f"Sorry, No Time Slot Was Booked in {check_days} days. Starting Over again {start_over} times.\n\nChecking... next appointment date.\n\n")
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

                        # # Click Submit Button
                        driver.find_element(By.XPATH,'//*[@id="action-section"]/button[1]').click()
                        
                        print(f'Container# {container_number}')
                        print(f"Successfully Booked The Earliest time at {earliest_time} on {appt_date}")
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
            
        # break the while loop if checked 3 times     
        if earliest_time or start_over == 4:
            break


        # # Print a message if no earliest time slot was booked after checking all days
        # if days_checked == len(appt_dates):
        #     appt_date = appt_dates[0]
        #     print(f"Sorry, No Time Slot Was Booked in {check_days} days. Starting Over again {start_over} times")
        #     start_over += 1
        #     days_checked = 0
        # days_checked = 0  # Reset the days_checked counter

