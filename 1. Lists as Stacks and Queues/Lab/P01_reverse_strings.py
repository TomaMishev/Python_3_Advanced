# Write program that:
# •	Reads an input string
# •	Reverses it using a stack
# •	Prints the result back on the console

_input = list(input())
while _input:
    print(_input.pop(), end="")