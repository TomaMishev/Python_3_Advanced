# Write a program that reads a matrix from the console and prints: •	The sum of all numbers in the matrix •	The
# matrix itself On the first line, you will receive the matrix sizes in the format "{rows}, {columns}". On the next
# rows, you will get elements for each column separated by a comma and a space ", ".

rows, cols = [int(x) for x in input().split(", ")]
matrix = []

for row in range(rows):
    row_info = [int(x) for x in input().split(", ")]
    matrix.append(row_info)

sum_elements = 0

for row in range(len(matrix)):
    sum_elements += sum(matrix[row])

print(sum_elements)
print(matrix)