available_appt_slots = [
    "04-Jun 09:00-09:29 (Current Openings: 5) (Canceled: 2)",
    "04-Jun 09:30-09:59 (Current Openings: 14)",
    "04-Jun 10:00-10:29 (Current Openings: 13) (Canceled: 2)",
    "04-Jun 10:30-10:59 (Current Openings: 12) (Canceled: 1)",
    "04-Jun 11:00-11:29 (Current Openings: 18) (Canceled: 3)",
    "04-Jun 11:30-11:59 (Current Openings: 25) (Canceled: 1)",
    "04-Jun 12:00-12:29 (Current Openings: 19)",
    "04-Jun 12:30-12:59 (Current Openings: 23)",
    "04-Jun 13:00-13:29 (Current Openings: 14)",
    "04-Jun 13:30-13:59 (Current Openings: 13)",
    "04-Jun 14:00-14:29 (Current Openings: 14)",
    "04-Jun 14:30-14:59 (Current Openings: 17)",
    "05-Jun 15:00-15:29 (Current Openings: 15) (Canceled: 1)"
]

appt_dates_list = ['2023-06-04', '2023-06-05']

for date in appt_dates_list:
    found = False
    for slot in available_appt_slots:
        if slot[:2] == date[-2:]:
            found = True
            
    if found:
        print(f"The date {date} is present in the available appointment slots.")
    else:
        print(f"The date {date} is not present in the available appointment slots.")
