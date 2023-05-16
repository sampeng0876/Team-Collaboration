from datetime import datetime
                # next_day = appt_date + timedelta(days=1)
                
                # print(f'this is next_day {next_day}')
                
                # if next_day.month > appt_date.month:
                #     driver.find_element(By.XPATH,'//*[@id="ipgrid_0"]/div[3]/div[2]/div/div[2]/div/div[1]/div[1]/div[3]').click()    
                #     sleep(1)
                #     continue

# year, month, day = map(int, appt_date.split('-'))

appt_dates = ["2023-5-30", "2023-5-31", "2023-6-1", "2023-6-2"]

previous_month = None

for appt_date in appt_dates:
    appt_date_obj = datetime.strptime(appt_date, '%Y-%m-%d')
    month = appt_date_obj.strftime("%m")

    if previous_month is not None and int(previous_month) < int(month):
        print(f'This is a new month: {month}')

    previous_month = month
    print(f'This is the month of appt_date: {month}')

    # if previous_month is None:
    #     # Set the previous_month to the current month for the first iteration
    #     previous_month = month
    # elif month != previous_month:
    #     # Check if the current month is different from the previous month
    #     print("This is a new month!")
    #     previous_month = month
    



# month_mapping = {
#     'January': '01',
#     'February': '02',
#     'March': '03',
#     'April': '04',
#     'May': '05',
#     'June': '06',
#     'July': '07',
#     'August': '08',
#     'September': '09',
#     'October': '10',
#     'November': '11',
#     'December': '12'
# }

# month_xpath = '//*[@id="ipgrid_0"]/div[3]/div[2]/div/div[2]/div/div[1]/div[1]/div[2]/strong'
# month_element = "May"  # Replace this with the actual value obtained from the XPath

# # Extract the month name from the element
# month = month_element.strip()

# # Convert the month name to its corresponding numerical representation
# month_number = month_mapping.get(month)

# if month_number:
#     print(month_number)
# else:
#     print("Invalid month:", month)
