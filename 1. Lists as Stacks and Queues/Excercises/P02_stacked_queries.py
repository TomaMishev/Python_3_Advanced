# You have an empty stack. You will receive an integer – N. On the next N lines, you will receive queries. Each query
# is one of these four types: •	'1 {number}' – push the number (integer) into the stack •	'2' – delete the number at
# the top of the stack •	'3' – print the maximum number in the stack •	'4' – print the minimum number in the
# stack It is guaranteed that each query is valid. After you go through all the queries, print the stack from top to
# bottom in the following format: "{n}, {n1}, {n2}, ... {nn}"

count = int(input())
stack = []
for _ in range(count):
    command_line = input().split()
    command = command_line[0]

    if command == '1':
        stack.append(int(command_line[1]))
    elif command == '2' and stack:
        stack.pop()
    elif command == '3' and stack:
        print(max(stack))
    elif command == '4' and stack:
        print(min(stack))

while len(stack) > 1:
    print(stack.pop(), end=", ")
print(stack.pop())