# Hot Potato is a game in which children form a circle and toss a hot potato. The counting starts with the first kid.
# Every nth toss, the child holding the potato leaves the game. When a kid leaves the game, it passes the potato to
# the next kid. It continues until there is only one kid left. Create a program that simulates the game of Hot
# Potato. On the first line, you will receive kids' names, separated by a single space. On the second line,
# you will receive the nth toss (integer) in which a child leaves the game. Print every kid who is removed from the
# circle in the format "Removed {kid}". In the end, print the only kid left in the format "Last is {kid}".

from collections import deque
children_deque = deque(input().split())
rotation = int(input())

while len(children_deque) > 1:
    children_deque.rotate(-rotation)
    print(f"Removed {children_deque.pop()}")

print(f"Last is {children_deque.pop()}")
