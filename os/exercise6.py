# Exercise 6
"""Exercise 6
Using the built-in os module in your working directory create a directory called documents. Then, in the documents directory, create 12 directories for each month with the names 01_sales, ..., 12_sales, respectively.

In response, print directory names sorted alphabetically in the documents directory to the console."""
import os

os.mkdir('documents')

directories = [f'{str(i).zfill(2)}_sales' for i in range(1, 13)]

for dirname in directories:
    path = os.path.join('documents', dirname)
    os.mkdir(path)

print(sorted(os.listdir('documents')))
