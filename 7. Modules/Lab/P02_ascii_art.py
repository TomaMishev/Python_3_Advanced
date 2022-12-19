# Write a program that encrypts given words by using the characters: "-|_/\()" to structure the word. Use the
# pyfiglet module. You can read more about it here -
# https://www.geeksforgeeks.org/python-ascii-art-using-pyfiglet-module/

from pyfiglet import figlet_format

text = input()
print(figlet_format(text))