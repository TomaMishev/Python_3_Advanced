# You are given an algebraic expression with parentheses. Scan through the string and extract each set of parentheses.
# Print the result back on the console.

expression = input()
line = list()

for index in range(len(expression)):
    if expression[index] == "(":
        line.append(index)
    elif expression[index] == ")":
        start_index = line.pop()
        print(expression[start_index:index + 1])