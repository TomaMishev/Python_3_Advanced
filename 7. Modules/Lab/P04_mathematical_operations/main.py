# Input Create a module that does basic calculations. You will receive 2 numbers and a sign between them all in one
# string You will receive a single string in the following format "{number1} {sign} {number2}"

from calculation import calculation

input_line = input().split()
fist_number = float(input_line[0])
sign = input_line[1]
second_number = float(input_line[2])

print(f"{calculation[sign](fist_number,second_number):.2f}")