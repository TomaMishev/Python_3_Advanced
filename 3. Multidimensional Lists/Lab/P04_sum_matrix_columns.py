# Write a program that reads a matrix from the console and prints the sum for each column on separate lines. On the
# first line, you will get matrix sizes in format "{rows}, {columns}". On the next rows, you will get elements for
# each column separated with a single space.

rows_count, cols_count = [int(x) for x in input().split(", ")]
matrix = []
for _ in range(rows_count):
    row_info = [int(x) for x in input().split(" ")]
    matrix.append(row_info)

result = []

for col_index in range(cols_count):
    col_sum = 0
    for row_index in range(rows_count):
        col_sum += matrix[row_index][col_index]
    result.append(col_sum)
[print(x) for x in result]