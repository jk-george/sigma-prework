from datetime import timedelta
from datetime import datetime
from datetime import date


def date_input(date_given):
    try:
        return datetime.strptime(date_given, "%d-%m-%Y")
    except ValueError:
        print("That date cannot be entered.")
        return False


def age():
    correct_input_date = False
    today_print = date.today().strftime('%d-%m-%Y')

    print('The date today is: ')
    print(today_print)

    today = datetime.now()
    while not correct_input_date:
        date_given = input('I would like you to enter a date: dd-mm-yyyy')
        correct_input_date = date_input(date_given)
    time_diff = today - correct_input_date
    years_between = time_diff.days//365
    print(years_between)


age()
