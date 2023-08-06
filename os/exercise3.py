# Exercise 3
'''
Using the built-in os module create names list containing the names of all files and directories in your working directory which names starts with letter 'e'. Sort this list alphabetically.

In response, print the names list to the console.
Expected result:

['evaluate.py', 'exercise.py']
'''
import os

list_dir = sorted(
    [name for name in os.listdir(path=None) if name.startswith('e')]
)
print(list_dir)
