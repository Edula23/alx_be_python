import datetime
from datetime import timedelta, date
def display_current_datetime():
    current_date = datetime.datetime.now().date()
    current_time = datetime.datetime.now().time()
    print("Current date and time:", current_date, current_time)
    input_date = input("Enter the number of days to add to the current date: ")
    def calculate_future_date():
        future_date = current_date + timedelta(days=int(input_date))
        print("Future date:", future_date)
    calculate_future_date()
display_current_datetime()