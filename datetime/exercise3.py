# Exercise 3
'''
Using the built-in datetime module, create datetime objects for the given dates:

Jul 20 2020 11:30:00

1990-03-10 12:00:00

2021-01-01 00:00:00

Then print these objects to the console.

Expected result:
2020-07-20 11:30:00
1990-03-10 12:00:00
2021-01-01 00:00:00
'''
from datetime import datetime

datetime_one = datetime(2020, 7, 20, 11, 30, 0)
datetime_two = datetime(1990, 3, 10, 12, 0, 0)
datetime_three = datetime(2021, 1, 1, 0, 0, 0)
print(datetime_one)
print(datetime_two)
print(datetime_three)
