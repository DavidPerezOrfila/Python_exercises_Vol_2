# Exercise 5
'''
Using the built-in datetime module, determine the exact time elapsed between the dates:
Jul 20 2020 11:30:00
2021-02-20 10:25:00
Then print the result to the console.
Expected result:

214 days, 22:55:00
'''

from datetime import datetime

date_one = datetime(2020, 7, 20, 11, 30, 0)
date_two = datetime(2021, 2, 20, 10, 25, 0)
delta = date_two - date_one
print(delta)
