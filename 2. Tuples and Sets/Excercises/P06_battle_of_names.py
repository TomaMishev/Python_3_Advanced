# You will receive a number N. On the following N lines, you will be receiving names. You should sum the ASCII values
# of each letter in the name and integer divide it by the number of the current row (starting from 1). Save the result
# to a set of either odd or even numbers, depending on if the resulting number is odd or even. After that,
# sum the values of each set. •	If the sums of the two sets are equal, print the union of the values, separated by ",
# ". •	If the sum of the odd numbers is bigger than the sum of the even numbers, print the different values,
# separated by ", ". •	If the sum of the even numbers is bigger than the sum of the odd numbers, print the
# symmetric-different values, separated by ", ". NOTE: On every operation, the starting set should be the odd set

n = int(input())
even_set = set()
odd_set = set()

even_sum = 0
odd_sum = 0
for i in range(1, n + 1):
    name = sum([ord(x) for x in input()]) // i

    if name % 2 == 0:
        even_set.add(name)
        even_sum += name
    else:
        odd_set.add(name)
        odd_sum += name

if even_sum == odd_sum:
    result = odd_set.union(even_set)
    print(*result, sep=", ")
elif odd_sum > even_sum:
    result = odd_set.difference(even_set)
    print(*result, sep=", ")
else:
    result = odd_set.symmetric_difference(even_set)
    print(*result, sep=", ")