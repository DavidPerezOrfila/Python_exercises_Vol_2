# Exercise 8
'''
Using the built-in datetime module, calculate the number of days until the end of the current year.
Expected result:
'Number of days until the end of the year: x'
The value of x will vary depending on the time taken to complete the exercise.
'''
from datetime import date

current_day = date.today()
last_day_current_year = date(date.today().year, 12, 31)
diff = (last_day_current_year - current_day).days
print(f'Number of days until the end of the year: {diff}')
