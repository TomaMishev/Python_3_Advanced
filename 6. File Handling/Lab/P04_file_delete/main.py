# Create a program that deletes the file you created in the previous task. If you try to delete the file multiple
# times, print the message: 'File already deleted!'.

import os

try:
    os.remove('../P03_file_writer/my_first_file.txt')
except FileNotFoundError:
    print("File already deleted!")