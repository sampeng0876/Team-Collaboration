from datetime import timedelta
import datetime
from datetime import date, timedelta
# Can you read through these code and make sure there are no mistakes
# can you now refactor that same code and make it cleaner and easier to understand
# Set the initial date
chosen_date = date(2023, 5, 10)
appt_date = chosen_date

date_check = 0
days_checked = 0

while date_check < 3:
    # Check if appt_date is Saturday, increment it by 2 days to Monday
    if appt_date.weekday() == 5:  # 5 represents Saturday
        appt_date += timedelta(days=2)

    # Perform your other operations or checks here
    # ...

    days_checked += 1

    if days_checked == 3:
        appt_date = chosen_date
        days_checked = 0

    date_check += 1

    # Print the current date after each iteration
    print("Iteration:", date_check)
    print("Current Date:", appt_date)
    print("------------------------")

