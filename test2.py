available_time_slots = [
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
    "04-Jun 15:00-15:29 (Current Openings: 15) (Canceled: 1)"
]

dates = [
    (2023, 6, 4),
    (2023, 6, 5)
]
for slot in available_time_slots:
    slot_date = slot.split()[0]  # Extract the date from the time slot entry
    print(slot_date)
    for date in dates:
        if slot_date == f"{date[2]:02d}-{date[1]:02d}":  # Format date as "day-month"
            print(f"Matching date found: {date[2]}-{date[1]}-{date[0]}")
