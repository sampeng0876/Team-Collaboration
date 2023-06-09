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
from datetime import datetime



# Version v3_check_next_monty
# Multiple Dates Checker 
def multi_date_checker(appt_dates, wait, start_time, end_time, driver, check_days, container_number, container_list, check_date):
    
    earliest_time = None  # initializing earliest_time with a default value
    
    for appt_date in appt_dates:
        days_checked = 0
        start_over = 1
        check_date+=1
        if appt_date.weekday() in [5, 6]:  # Skip weekends (Saturday: 5, Sunday: 6)
            appt_date += timedelta(days=1)
            continue
        # break the while loop if checked 3 times
        # elif start_over == 4:
        #     break

        print(f"Checking...\nContainer#: {container_number}")    
        print(f"Selected Appt Date: {appt_date}")
        print(f"Selected Appt Times From: {start_time} to {end_time}")

        # Wait for Searching for time slots...
        WebDriverWait(driver, 20).until(EC.invisibility_of_element_located((By.XPATH,'//*[@id="timeslot_loading_bar"]/span')))
        # Click Date / Time Slots Box
        WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH,'//*[@id="id_DateTimeRow_CreateAppt"]/td[2]/span/span/span/span[1]'))).click()


        # V1
        ################################################################
        # Locate the Appointment Time Slots
        # time_slots_container = driver.find_elements(by="xpath", value='//*[@id="newDateTime_CreateAppt_listbox"]/li')

        # # Available Time Slots List
        # available_time_slots = []

        # # Check available time slots
        # for time in time_slots_container:
        #     try:
        #         # Read time slot text
        #         time_slots_text = time.text  
        #         if time_slots_text.strip():
        #             # Append time slots to the list
        #             available_time_slots.append(time_slots_text)
        #         print(time_slots_text)
        #     except:
        #         print("NOT AVAILABLE")



        # V2
        ################################################################

        # Locate the Appointment Time Slots
        # WebDriverWait(driver, 20).until(EC.presence_of_all_elements_located((By.XPATH,'//*[@id="newDateTime_CreateAppt_listbox"]/li')))
        time_slots = WebDriverWait(driver, 20).until(EC.presence_of_all_elements_located((By.XPATH,'//*[@id="newDateTime_CreateAppt-list"]/div[2]/ul/li')))
        # Available Time Slots List
        available_time_slots = []

        # Check available time slots
        for time in time_slots:            
            slot = time.text
            available_time_slots.append(slot)
            print(slot)
                
        # print(available_time_slots)
        print(len(available_time_slots))
        
        # slot_list = driver.find_elements(By.XPATH, '//*[@id="newDateTime_CreateAppt_listbox"]')[0].text
        # print(slot_list)


        # Check available times in selected range from start time to end time
        available_times = [time[6:12].strip() for time in available_time_slots if start_time <= time[6:12].strip() <= end_time]

        # If no available time slots or no time slots in selected range
        # if not available_time_slots or not available_times:
        #     print(f"No available time slots or no time slots in selected range for {appt_date}.")
        #     days_checked += 1
        #     appt_date += timedelta(days=1)
            
        #     if days_checked == len(appt_dates):
        #         appt_date = appt_dates[0]
        #         print(f"Sorry, No Time Slot Was Booked in {check_days} days. Starting Over again {start_over} times.\n\nChecking... next appointment date.\n\n")
        #         start_over += 1
        #         days_checked = 0

        available_appt_dates = [date[:2].strip() for date in available_time_slots]
        # check if appte dates are in the available_appt_dates
        if appt_date.strftime("%d") in available_appt_dates:

            new_available_time_slots=[]

            print(f'****************************')
            print(f'***    Available Appts   ***')
            print(f'****************************')
            for available_date in available_time_slots:
                # Check if available date is available
                if available_date[:2].strip() == appt_date.strftime("%d"):
                    new_available_time_slots.append(available_date)              
                    print(f'***  {available_date[:19]} ***')
            print(f'****************************')
            # Check available times in selected range from start time to end time
            available_times = [time[6:12].strip() for time in new_available_time_slots if start_time <= time[6:12].strip() <= end_time]
            
            if available_times:
                print(f"\nSelected Appt Times From {start_time} to {end_time}")
                print(f'Available Times in Selected Range: {available_times}\n')
                print(f'Successful Booked Appt: {available_times[0]}\n')

                # When Appt Made Remove Container Number From Container List
                container_list.remove(container_number)
                print(f"Updated list: {container_list}\n")
                earliest_time == available_times[0]
                break
                # Click Create Appointment                    
                # WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH,'//*[@id="id_sub_CreateAppt"]'))).click()

            else:
                print(f'\nAppt is Available\nBut No Appt Time in Selected Range From {start_time} to {end_time}\n')

                # Click Date / Time Slots Box
                sleep(5)
                WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH,'//*[@id="id_DateTimeRow_CreateAppt"]/td[2]/span/span/span/span[1]'))).click() # //*[@id="id_DateTimeRow_CreateAppt"]/td[2]/span/span/span/span[1]
                # Click Refresh
                WebDriverWait(driver, 35).until(EC.element_to_be_clickable((By.XPATH,'//*[@id="id_sub_RefreshTimeslot"]'))).click()
        else:
            print(f'No Appt on {appt_date}\n')

             
               
                     

            # # Break the while loop if a successful booking is made
            # if earliest_time:
            #     break

            # # Increment the appointment date by one day
            # appt_date += timedelta(days=1)              
            
        # break the while loop if checked 3 times     
        # if earliest_time: # or start_over == 4
        #     break
    

    
