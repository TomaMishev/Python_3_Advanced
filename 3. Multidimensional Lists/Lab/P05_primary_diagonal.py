# Write a program that finds the sum of all numbers in a matrix's primary diagonal (runs from top left to bottom
# right). On the first line, you will receive an integer N – the size of a square matrix. The next N lines holds the
# values for each column - N numbers, separated by a single space.

rows_count = int(input())
matrix = []
for _ in range(rows_count):
    row_info = [int(x) for x in input().split()]
    matrix.append(row_info)

primary_diagonal_sum = 0

for rows in range(len(matrix)):
    for cols in range(len(matrix[0])):
        if rows == cols:
            primary_diagonal_sum += matrix[rows][cols]
print(primary_diagonal_sum)