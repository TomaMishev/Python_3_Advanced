# Write a program that reads a number - N, representing the rows and columns of a square matrix. On the next N lines,
# you will receive rows of the matrix. Each row consists of ASCII characters. After that, you will receive a symbol.
# Find the first occurrence of that symbol in the matrix and print its position in the format: "({row}, {col})". You
# should start searching from the top left. If there is no such symbol, print the message "{symbol} does not oc cur
# in the matrix".

rows_count = int(input())
matrix = []

for _ in range(rows_count):
    row_info = input()
    matrix.append(row_info)
symbol = input()

is_found = False

for row in range(len(matrix)):
    if is_found:
        break
    for col in range(len(matrix[row])):
        if matrix[row][col] == symbol:
            is_found = True
            print(f"({row}, {col})")
            break
if not is_found:
    print(f"{symbol} does not occur in the matrix")