# Create a function called func_executor() that can receive a different number of tuples, each of which will have
# exactly 2 elements: the first will be a function, and the second will be a tuple of the arguments that need to be
# passed to that function. You should execute each function and return its result in the format: "{function name} - {
# function result}" For more clarification, see the examples below. Submit only your function in the judge system.

def sum_numbers(num1, num2):
    return f"sum_numbers - {num1 + num2}"


def multiply_numbers(num1, num2):
    return f"multiply_numbers - {num1 * num2}"


def func_executor(*args):
    result = []
    for func, nums in args:
        result.append(func(*nums))
    return '\n'.join(result)


print(func_executor(
    (sum_numbers, (1, 2)),
    (multiply_numbers, (2, 4))
))
