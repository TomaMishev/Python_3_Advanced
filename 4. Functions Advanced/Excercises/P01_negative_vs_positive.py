# You will receive a sequence of numbers (integers) separated by a single space. Separate the negative numbers from
# the positive. Find the total sum of the negatives and positives, and print the following: •	On the first line,
# print the sum of the negatives •	On the second line, print the sum of the positives •	On the third line: o	If
# the absolute negative number is larger than the positive number: "The negatives are stronger than the positives"
# o	If the positive number is larger than the absolute negative number: "The positives are stronger than the
# negatives" Note: you will not receive any zeroes in the input.


input_line = [int(x) for x in input().split()]
negatives = 0
positives = 0

for el in input_line:
    if el < 0:
        negatives += el
    else:
        positives += el

print(negatives)
print(positives)

if abs(negatives) > positives:
    print(f"The negatives are stronger than the positives")
else:
    print(f"The positives are stronger than the negatives")