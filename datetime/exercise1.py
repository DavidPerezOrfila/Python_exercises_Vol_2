# Exercise 1
'''
Using the built-in datetime module, create date objects for the given dates:
2021-01-01
31/7/21
May 7, 1990
Then print these objects to the console.

Expected result:
2021-01-01
2021-07-31
1990-05-07
'''
from datetime import date

date_one = date(2021, 1, 1)
date_two = date(2021, 7, 31)
date_three = date(1990, 5, 7)
print(date_one)
print(date_two)
print(date_three)
