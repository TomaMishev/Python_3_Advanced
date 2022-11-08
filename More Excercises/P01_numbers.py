# First, you will be given two sequences of integers values on different lines. The values of the sequences are
# separated by a single space between them. Keep in mind that each sequence should contain only unique values. Next,
# you will receive a number - N. On the next N lines, you will receive one of the following commands: •	"Add First {
# numbers, separated by a space}" - add the given numbers at the end of the first sequence of numbers. •	"Add
# Second {numbers, separated by a space}" - add the given numbers at the end of the second sequence of numbers. •
# "Remove First {numbers, separated by a space}" - remove only the numbers contained in the first sequence. •
# "Remove Second {numbers, separated by a space}" - remove only the numbers contained in the second sequence. •	"Check
# Subset" - check if any of the given sequences are a subset of the other. If it is, print "True". Otherwise,
# print "False". In the end, print the final sequences, separated by a comma and a space ", ". The values in each
# sequence should be sorted in ascending order.


first_set = set(int(x) for x in input().split(" "))
second_set = set(int(x) for x in input().split(" "))
n = int(input())

for _ in range(n):
    input_line = input().split()
    command = input_line[0]
    argument = input_line[1]
    if command == "Add":
        if argument == "First":
            set([first_set.add(int(x)) for x in input_line[2:]])
        else:
            set([second_set.add(int(x)) for x in input_line[2:]])
    elif command == "Remove":
        if argument == "First":
            first_set = first_set.difference(int(x) for x in input_line[2:])
        else:
            second_set = second_set.difference(int(x) for x in input_line[2:])
    else:
        print(first_set.issubset(second_set) or second_set.issubset(first_set))

first_set = sorted(first_set)
second_set = sorted(second_set)

print(*first_set, sep=", ")
print(*second_set, sep=", ")