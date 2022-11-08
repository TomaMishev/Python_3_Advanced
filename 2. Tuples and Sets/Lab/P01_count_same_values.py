# You will be given numbers separated by a space. Write a program that prints the number of occurrences of each
# number in the format "{number} - {count} times". The number must be formatted to the first decimal point.

nums = [float(x) for x in input().split(" ")]
nums_occurs = dict()

for num in nums:
    if num not in nums_occurs:
        nums_occurs[num] = 0
    nums_occurs[num] += 1
for el in nums_occurs.items():
    print(f"{el[0]} - {el[1]} times")

