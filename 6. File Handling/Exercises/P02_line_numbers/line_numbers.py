# Write a program that reads a text file, inserts line numbers in front of each line, and counts all the letters and
# punctuation marks. The result should be written to another text file.
import re

with open('text.txt', 'r') as input_file, open('output.txt', 'w') as output_file:

    for row, line in enumerate(input_file):
        alphabet_pattern = "[A-Za-z]"
        total_alphabet_chars = len(re.findall(alphabet_pattern, line))
        special_chars_pattern = "[-,'.?!]"
        total_special_chars = len(re.findall(special_chars_pattern, line))
        output_file.writelines(f"Line {row + 1}: {line.strip()} ({total_alphabet_chars})({total_special_chars})\n")

