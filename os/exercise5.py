# Exercise 5
"""Using the built-in os module create images directory in your working directory. Then go to the images directory and print the current path to the working directory."""
import os

os.mkdir('images')
os.chdir('images')
print(os.getcwd())
