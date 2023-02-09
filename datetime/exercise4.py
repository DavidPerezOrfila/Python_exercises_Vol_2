# Exercise 4
'''
Using the built-in datetime module, determine the number of days between 2020-07-21 and 2020-12-31.
Then print the result to the console as shown below.
Expected result:
Number of days: 163
'''
from datetime import date

date_one = date(2020, 7, 21)
date_two = date(2020, 12, 31)
delta = (date_two - date_one).days
print(f'Number of days: {delta}')
