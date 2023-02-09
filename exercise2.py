# Exercise 2
'''
Using the built-in datetime module, create time objects for the given hours:
12:00:00
6:30:00
9:15:00
Then print these objects to the console.

Expected result:
12:00:00
06:30:00
09:15:00
'''
from datetime import time

time_one = time(12, 0, 0)
time_two = time(6, 30, 0)
time_three = time(9, 15, 0)
print(time_one)
print(time_two)
print(time_three)
