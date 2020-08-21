#!/usr/bin/env python3

import unittest
import datetime
from due_date_calculator import calculate_due_date, is_weekday

class TestDueDateCalculator(unittest.TestCase):

    def test_same_day(self):
        """
        If a problem was reported at 2:12PM on Tuesday
        and the turnaround time is 1 hour,
        then it is due by 3:12PM on the same day.
        """
        submit_datetime = datetime.datetime(2020, 8, 18, 14, 12)
        resolved_time = calculate_due_date(submit_datetime, 1)
        assert resolved_time == datetime.datetime(2020, 8, 18, 15, 12)

    def test_simple_example(self):
        """
        If a problem was reported at 2:12PM on Tuesday
        and the turnaround time is 16 hours,
        then it is due by 2:12PM on Thursday.
        """
        submit_datetime = datetime.datetime(2020, 8, 18, 14, 12)
        resolved_time = calculate_due_date(submit_datetime, 16)
        assert submit_datetime.strftime("%A") == "Tuesday"
        assert resolved_time == datetime.datetime(2020, 8, 20, 14, 12)

    def test_nextday(self):
        """
        If a problem was reported at 2:12PM on Tuesday
        and the turnaround time is 4 hours,
        then it is due by 10:12AM on Wednesday.
        """
        submit_datetime = datetime.datetime(2020, 8, 18, 14, 12)
        resolved_time = calculate_due_date(submit_datetime, 4)
        self.assertEqual(resolved_time.strftime("%A"), "Wednesday")
        self.assertEqual(resolved_time, datetime.datetime(2020, 8, 19, 10, 12))

    def test_nextday_friday_monday(self):
        """
        If a problem was reported at 3:12PM on Friday
        and the turnaround time is 5 hours,
        then it is due by 12:12AM on Monday.
        """
        submit_datetime = datetime.datetime(2020, 8, 21, 15, 12)
        resolved_time = calculate_due_date(submit_datetime, 5)
        self.assertEqual(resolved_time.strftime("%A"), "Monday")
        self.assertEqual(resolved_time, datetime.datetime(2020, 8, 24, 12, 12))

    def test_is_weekday(self):
        friday = datetime.datetime(2020, 8, 21)
        saturday = datetime.datetime(2020, 8, 22)
        sunday = datetime.datetime(2020, 8, 23)
        monday = datetime.datetime(2020, 8, 24)

        assert is_weekday(friday) is True
        assert is_weekday(saturday) is False
        assert is_weekday(sunday) is False
        assert is_weekday(monday) is True

    def test_reported_during_workhours(self):
        """
        Test a couple of times, if the time is invalid the
        function should raise a ValueError.
        There is and edge case as 17:00, I treat it as invalid.
        """
        before_workhour = datetime.datetime(2020, 8, 21, 8, 59)
        at_nine = datetime.datetime(2020, 8, 21, 9, 0)
        at_random = datetime.datetime(2020, 8, 21, 11, 32)
        at_five = datetime.datetime(2020, 8, 21, 17, 0)
        after_workhour = datetime.datetime(2020, 8, 21, 17, 2)

        self.assertRaises(ValueError, calculate_due_date, before_workhour, 1)
        calculate_due_date(at_nine, 1)
        calculate_due_date(at_random, 1)
        self.assertRaises(ValueError, calculate_due_date, at_five, 1)
        self.assertRaises(ValueError, calculate_due_date, after_workhour, 1)

    def test_valid_turnaround_hour(self):
        valid_datetime = datetime.datetime(2020, 8, 21, 13, 2)
        self.assertRaises(ValueError, calculate_due_date, valid_datetime, 0)
        self.assertRaises(ValueError, calculate_due_date, valid_datetime, -1)
        calculate_due_date(valid_datetime, 1)


if __name__ == '__main__':
    unittest.main()
