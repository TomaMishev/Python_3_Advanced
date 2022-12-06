# On the first line, you will receive a sequence of pizza orders. Each order contains a different number of pizzas,
# separated by comma and space ", ". On the second line, you will receive a sequence of employees with pizza-making
# capacities (how much pizzas an employee could make), separated by comma and space ", ". Your task is to check if all
# pizza orders are completed. To do that, you should take the first order and the last employee and see: •	If the
# number of pizzas in the order is less than or equal to the employee's pizza making capacity, the order is completed.
# Remove both the order and the employee. •	If the number of pizzas in the order is greater than the employee's pizza
# making capacity, the remaining pizzas from the order are going to be made by the next employees until the order is
# completed. o	If there are no more employees to finish the order, consider it not completed. •	The restaurant
# does not take orders for more than 10 pizzas at once. •	If an order is invalid (less than or equal to 0),
# you need to remove it before it is taken by an employee. You should keep track of the total pizzas that are being
# made. Input •	On the first line you will be given a sequence of pizza orders each represented as a number – integers
# separated by comma and space ", " •	On the second line you will be given a sequence of employees with pizza-making
# capacities – integers separated by comma and space ", " Output •	If all orders are successfully completed,
# print: All orders are successfully completed! Total pizzas made: {total count} Employees: {left employees joined by
# ", "} •	Otherwise, if you ran out of employees and there are still some orders left print: Not all orders are
# completed. Orders left: {left orders joined by ", "}
from collections import deque

pizza_orders = deque([int(x) for x in input().split(", ")])
employees_capabilities = [int(x) for x in input().split(", ")]

total_pizza_made = 0
flag = False
while pizza_orders:

    if not employees_capabilities:
        flag = True
        break
    current_order = pizza_orders[0]
    current_employee = employees_capabilities[-1]
    if current_order <= 0:
        pizza_orders.popleft()
        continue
    if current_order > 10:
        pizza_orders.popleft()
        continue

    if current_order <= current_employee:
        total_pizza_made += pizza_orders.popleft()
        employees_capabilities.pop()
    else:
        while True:
            if current_order > current_employee:
                if employees_capabilities:
                    total_pizza_made += current_employee
                    pizza_orders[0] -= current_employee
                    employees_capabilities.pop()
                    break

if flag:
    print("Not all orders are completed.")
    print(f"Orders left: {', '.join([str(x) for x in pizza_orders])}")
else:
    print("All orders are successfully completed!")
    print(f"Total pizzas made: {total_pizza_made}")
    print(f"Employees: {', '.join([str(x) for x in employees_capabilities])}")