# Exercise 7
"""Using the built-in os module create a directory called images. Then create two directories in this directory named images_png and images_jpg. Before creating each directory, check if such directory exists.

In response, execute the following code:

for root, dirs, files in os.walk(base_dir):
    print(root)
"""
import os


base_dir = 'images'
png_dir = os.path.join(base_dir, 'images_png')
jpg_dir = os.path.join(base_dir, 'images_jpg')

if not os.path.exists(base_dir):
    os.mkdir(base_dir)

if not os.path.exists(png_dir):
    os.mkdir(png_dir)

if not os.path.exists(jpg_dir):
    os.mkdir(jpg_dir)

for root, dirs, files in os.walk(base_dir):
    print(root)
