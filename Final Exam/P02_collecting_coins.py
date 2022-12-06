# You are playing a game, and your goal is to collect 100 coins. On the first line, you will be given a number
# representing the size of the field with a square shape. On the following few lines, you will be given the field
# with: •	One player - randomly placed in it and marked with the symbol "P" •	Numbers for coins placed at different
# positions of the field •	Walls marked with "X" After the field state, you will be given commands for the player's
# movement. Commands can be: "up", "down", "left", "right". The player moves in the given direction with one step for
# each command and collects all the coins that come across. If he goes out of the field, he should continue to
# traverse the field from the opposite side in the same direction. Note: He can go through the same path many times,
# but he can collect the coins just once (the first time). There are only two possible outcomes of the game: •	The
# player hits a wall, loses the game, and his coins are reduced to 50% and rounded down to the next-lowest integer
# number. •	The player collects at least 100 coins and wins the game. For more clarifications, see the examples below.

def is_inside(row, col, size):
    return 0 <= row and row < size and 0 <= col and col < size
import math

size = int(input())
matrix = []

player_row = 0
player_col = 0
total_coins = 0

player_path = []
wall_hit = False
coins_collected = False

for row in range(size):
    row_elements = input().split()
    matrix.append(row_elements)
    for col in range(size):
        element = row_elements[col]
        if element == 'P':
            player_row = row
            player_col = col
            player_path.append([player_row, player_col])

while True:
    command = input()
    if command == "left":
        next_row = player_row
        next_col = player_col - 1
        if is_inside(next_row, next_col, size):
            matrix[player_row][player_col] = '0'
            player_row = next_row
            player_col = next_col
            if matrix[player_row][player_col] == 'X':
                wall_hit = True
                player_path.append([player_row, player_col])
                break
            else:
                total_coins += int(matrix[player_row][player_col])
                matrix[player_row][player_col] = 'P'
                player_path.append([player_row, player_col])
        else:
            matrix[player_row][player_col] = '0'
            player_row = next_row
            player_col = size - 1
            if matrix[player_row][player_col] == 'X':
                wall_hit = True
                player_path.append([player_row, player_col])
                break
            else:
                total_coins += int(matrix[player_row][player_col])
                matrix[player_row][player_col] = 'P'
                player_path.append([player_row, player_col])

    elif command == 'right':
        next_row = player_row
        next_col = player_col + 1
        if is_inside(next_row, next_col, size):
            matrix[player_row][player_col] = '0'
            player_row = next_row
            player_col = next_col
            if matrix[player_row][player_col] == 'X':
                player_path.append([player_row, player_col])
                wall_hit = True
                break
            else:
                total_coins += int(matrix[player_row][player_col])
                matrix[player_row][player_col] = 'P'
                player_path.append([player_row, player_col])
        else:
            matrix[player_row][player_col] = '0'
            player_row = next_row
            player_col = 0
            if matrix[player_row][player_col] == 'X':
                player_path.append([player_row, player_col])
                wall_hit = True
                break
            else:
                total_coins += int(matrix[player_row][player_col])
                matrix[player_row][player_col] = 'P'
                player_path.append([player_row, player_col])

    elif command == "up":
        next_row = player_row - 1
        next_col = player_col
        if is_inside(next_row, next_col, size):
            matrix[player_row][player_col] = '0'
            player_row = next_row
            player_col = next_col
            if matrix[player_row][player_col] == 'X':
                player_path.append([player_row, player_col])
                wall_hit = True
                break
            else:
                total_coins += int(matrix[player_row][player_col])
                matrix[player_row][player_col] = 'P'
                player_path.append([player_row, player_col])
        else:
            matrix[player_row][player_col] = '0'
            player_row = size - 1
            player_col = next_col
            if matrix[player_row][player_col] == 'X':
                player_path.append([player_row, player_col])
                wall_hit = True
                break
            else:
                total_coins += int(matrix[player_row][player_col])
                matrix[player_row][player_col] = 'P'
                player_path.append([player_row, player_col])
    elif command == "down":
        next_row = player_row + 1
        next_col = player_col
        if is_inside(next_row, next_col, size):
            matrix[player_row][player_col] = '0'
            player_row = next_row
            player_col = next_col
            if matrix[player_row][player_col] == 'X':
                player_path.append([player_row, player_col])
                wall_hit = True
                break
            else:
                total_coins += int(matrix[player_row][player_col])
                matrix[player_row][player_col] = 'P'
                player_path.append([player_row, player_col])
        else:
            matrix[player_row][player_col] = '0'
            player_row = 0
            player_col = next_col
            if matrix[player_row][player_col] == 'X':
                player_path.append([player_row, player_col])
                wall_hit = True
                break
            else:
                total_coins += int(matrix[player_row][player_col])
                matrix[player_row][player_col] = 'P'
                player_path.append([player_row, player_col])

    if total_coins >= 100:
        coins_collected = True
        break

if wall_hit:
    print(f"Game over! You've collected {math.floor(total_coins / 2)} coins.")
if coins_collected:
    print(f"You won! You've collected {total_coins} coins.")
print(f"Your path:")
for el in player_path:
    print(el)



