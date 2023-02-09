# Exercise 10
'''
Using the built-in datetime module, the date and timedelta classes from the
given date 2020-01-01 00:00:00 get the date:

shifted by 7 days

shifted by 30 days

shifted by 30 hours

shifted by 15 minutes

Expected result:
2020-01-08 00:00:00
2020-01-31 00:00:00
2020-01-02 06:00:00
2020-01-01 00:15:00
'''
from datetime import datetime, timedelta

given_date = datetime(2020, 1, 1)
shifted_7_days = given_date + timedelta(days=7)
shifted_30_days = given_date + timedelta(days=30)
shifted_30_hours = given_date + timedelta(hours=30)
shifted_15_min = given_date + timedelta(minutes=15)

print(shifted_7_days)
print(shifted_30_days)
print(shifted_30_hours)
print(shifted_15_min)
