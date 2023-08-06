# Exercise 4
'''
Using the built-in os module create names list containing file names in your working directory with a .py extension. Sort this list alphabetically.

In response, print this list to the console.
Expected result:
['evaluate.py', 'exercise.py', 'result.py', 'run_unittest.py']
'''
import os

list_names = sorted([name for name in os.listdir() if name.endswith('.py')])
print(list_names)
