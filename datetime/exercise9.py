# Exercise 9
'''
Using the built-in datetime module, calculate the exact time remaining until the end of the current year.
Expected result:
'Until the end of the year: x'
The value of x will vary depending on the time taken to complete the exercise.
For example, for the date: 2020-07-21 07:39:39.188939 the return value should be:
'Until the end of the year: 162 days, 16:20:20.811061'
'''
from datetime import datetime

now = datetime.now()
last_day_current_year = datetime(datetime.now().year + 1, 1, 1)
diff = last_day_current_year - now

print(f'Until the end of the year: {diff}')
