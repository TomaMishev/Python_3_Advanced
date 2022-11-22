# Find the number of all 2x2 squares containing identical chars in a matrix. On the first line, you will receive the
# matrix's dimensions in the format "{rows} {columns}". On the following rows, you will receive characters separated
# by a single space. Print the number of all square matrices you have found.

rows_count, cols_count = [int(x) for x in input().split()]
matrix = [[x for x in input().split()] for x in range(rows_count)]
square_matrices_count = 0
for row in range(len(matrix) - 1):
    for col in range(len(matrix[row]) - 1):
        element = matrix[row][col]
        if element == matrix[row][col + 1] and element == matrix[row + 1][col] and element == \
                matrix[row + 1][col + 1]:
            square_matrices_count += 1

print(square_matrices_count)
