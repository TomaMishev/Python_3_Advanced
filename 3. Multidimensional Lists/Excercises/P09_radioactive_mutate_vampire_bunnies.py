# First, you will receive a line holding integers N and M, representing the lair's rows and columns. Next, you receive
# N strings that can consist only of ".", "B", "P". They represent the initial state of the lair. There will be only
# one player. The bunnies are marked with "B", the player is marked with "P", and everything else is free space,
# marked with a dot ".". Then you will receive a string with commands (e.g., LRRULUD) - each letter represents the
# next move of the player: •	L - the player should move one position to the left •	R - the player should move one
# position to the right •	U - the player should move one position up •	D - the player should move one position
# down After every step made, each bunny spreads one position up, down, left, and right. If the player moves to a
# bunny cell or a bunny reaches the player, the player dies. If the player goes out of the lair without encountering a
# bunny, the player wins. When the player dies or wins, the game ends. All the activities for this turn continue (
# e.g., all the bunnies spread normally), but there are no more turns. There will be no cases where the moves of the
# player end before he dies or escapes. In the end, print the final state of the lair with every row on a separate
# line. On the last line, print either "dead: {row} {col}" or "won: {row} {col}". "Row" and "col" are the cell
# coordinates where the player has died or the last cell he has been in before escaping the lair. Input •	On the
# first line of input, the numbers N and M are received - the number of rows and columns in the lair •	On the
# following N lines, each row is received in the form of a string. The string will contain only ".", "B",
# "P". All strings will be the same length. There will be only one "P" for all the input •	On the last line,
# the directions are received in the form of a string, containing "R", "L", "U", "D" Output •	On the first N lines,
# print the final state of the bunny lair •	On the last line, print: o	If the player won - "won: {row} {col}" o	If
# the player dies - "dead: {row} {col}" Constraints •	The dimensions of the lair are in the range [3…20] •	The
# directions string length is in the range [1…20]
def is_outside(row, col, rows, cols):
    return row < 0 or col < 0 or row >= rows or col >= cols


def get_next_pos(row, col, command):
    if command == 'U':
        return row - 1, col
    if command == 'L':
        return row, col - 1
    if command == 'R':
        return row, col + 1
    if command == 'D':
        return row + 1, col


rows, cols = [int(x) for x in input().split()]

matrix = []
player_row = 0
player_col = 0
bunnies = set()

for row in range(rows):
    row_elements = list(input())
    matrix.append(row_elements)
    for col in range(cols):
        if row_elements[col] == 'P':
            player_row = row
            player_col = col
        elif row_elements[col] == 'B':
            bunnies.add(f"{row} {col}")

commands = input()

won = False
dead = False

matrix[player_row][player_col] = '.'

for command in commands:
    next_row, next_col = get_next_pos(player_row, player_col, command)

    if is_outside(next_row, next_col, rows, cols):
        won = True
    elif matrix[next_row][next_col] == "B":
        dead = True
        player_row, player_col = next_row, next_col
    else:
        player_row, player_col = next_row, next_col

    new_bunnies = set()
    for bunny in bunnies:
        bunny_row, bunny_col = [int(x) for x in bunny.split()]

        if not is_outside(bunny_row - 1, bunny_col, rows, cols):
            new_bunnies.add(f'{bunny_row - 1} {bunny_col}')
            matrix[bunny_row - 1][bunny_col] = 'B'
        if not is_outside(bunny_row + 1, bunny_col, rows, cols):
            new_bunnies.add(f'{bunny_row + 1} {bunny_col}')
            matrix[bunny_row + 1][bunny_col] = 'B'
        if not is_outside(bunny_row, bunny_col - 1, rows, cols):
            new_bunnies.add(f'{bunny_row} {bunny_col - 1}')
            matrix[bunny_row][bunny_col - 1] = 'B'
        if not is_outside(bunny_row, bunny_col + 1, rows, cols):
            new_bunnies.add(f'{bunny_row} {bunny_col + 1}')
            matrix[bunny_row][bunny_col + 1] = 'B'

    bunnies = bunnies.union(new_bunnies)

    if matrix[player_row][player_col] == 'B':
        dead = True

    if won or dead:
        break

for row in matrix:
    print(*row, sep= "")

if won:
    print(f"won: {player_row} {player_col}")
else:
    print(f"dead: {player_row} {player_col}")
