from datetime import datetime, date, timedelta
def display_current_datetime():
    current_date = datetime.date.today()
    current_time = datetime.datetime.now()
    print("Current date and time:", current_date, current_time)
    input_date = input("Enter the number of days to add to the current date: ")
    def calculate_future_date():
        future_date = current_date + datetime.timedelta(days=int(input_date))
        print("Future date:", future_date)