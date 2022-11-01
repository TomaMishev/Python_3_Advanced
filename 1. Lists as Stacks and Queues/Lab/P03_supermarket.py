# Tom is working at the supermarket, and he needs your help to keep track of his clients. Write a program that reads
# lines of input consisting of a customer's name and adds it to the end of a queue until "End" is received. If,
# in the meantime, you receive the command "Paid", you should print each customer in the order they are served (from
# the first to the last one) and empty the queue. When you receive "End", you should print the count of the remaining
# people in the queue in the format: "{count} people remaining.".
from collections import deque

customers = deque()
input_line = input()

while input_line != "End":
    current_name = input_line
    if current_name != "Paid":
        customers.append(current_name)
    else:
        while customers:
            print(customers.popleft())

    input_line = input()
print(f"{len(customers)} people remaining.")