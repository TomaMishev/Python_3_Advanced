# Write a function called operate that receives an operator ("+", "-", "*" or "/") as first argument and multiple
# numbers (integers) as additional arguments (*args). The function should return the result of the operator applied
# to all the numbers. For more clarification, see the examples below. Submit only your function in the Judge system.

from functools import reduce


def operate(op, *args):
    ops = {
        "+": lambda a, b: a+b,
        "-": lambda a, b: a-b,
        "*": lambda a, b: a*b,
        "/": lambda a, b: a/b,
    }
    return reduce(ops[op], args)


print(operate("*", -1, 4))