# Exercise 2
'''
Using the built-in os module print to the console a list containing the names of all files in the working directory.
Expected result:

['exercise.py', 'run_unittest.py', '__pycache__', 'evaluate.py', 'result.py']
'''
import os

print(os.listdir())
