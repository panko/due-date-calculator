#!/usr/bin/env python3

import datetime

START_HOUR = 9
END_HOUR = 17
WORKTIME = END_HOUR - START_HOUR


def is_weekday(submit_datetime):
    """
    Returns True if the submit_datetime is a weekday, false otherwise.
    The used builtin weekday method returns the day of the week as an integer,
    where Monday is 0 and Sunday is 6.
    """
    return submit_datetime.weekday() <= 4


def is_working_hours(submit_datetime):
    """
    Checks if the date is in the working hour range or not.
    Returns True or False
    """
    date_hour = submit_datetime.hour
    return date_hour >= START_HOUR and date_hour < END_HOUR


def is_valid_submitdate(submit_datetime):
    """
    Checks if the profided date is valid or not.
    Returns True or False
    """
    return is_weekday(submit_datetime) and is_working_hours(submit_datetime)


def calculate_due_date(submit_datetime, turnaround_hours):
    """
    Calculates the due date from the submit time and the turnaround hours.
    It does not take into account the weekends, only the weekdays.
    submit_datetime - datetime object, when does the ticket got submitted
    turnaround_hours - integer, how much working hour does it take
    Returns: due_date as a datetime object.
    """
    if not is_valid_submitdate(submit_datetime):
        raise ValueError("The submit datetime is not valid.")
    if turnaround_hours < 1:
        raise ValueError("The turnaround hour cant be negative or zero.")

    due_date = submit_datetime
    remaining_hours = turnaround_hours - (END_HOUR - submit_datetime.hour)

    if remaining_hours < 1:  # if due on the same day
        return due_date.replace(hour=due_date.hour + turnaround_hours)

    remaining_days = remaining_hours // WORKTIME
    remaining_hours = remaining_hours % WORKTIME

    while remaining_days >= 0:
        due_date = due_date.replace(day=due_date.day + 1)
        if is_weekday(due_date):
            remaining_days -= 1

    due_date = due_date.replace(hour=START_HOUR + remaining_hours)
    return due_date


if __name__ == '__main__':
    submit_datetime = datetime.datetime(2020, 8, 21, 14, 12)
    print("1", calculate_due_date(submit_datetime, 1))
    print("5", calculate_due_date(submit_datetime, 5))
    print("17", calculate_due_date(submit_datetime, 17))
