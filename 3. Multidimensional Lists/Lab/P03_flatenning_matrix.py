# Write a program that receives a matrix and prints the flattened version of it (a list with all the values). For
# example, the flattened list of the matrix: [[1, 2], [3, 4]] will be [1, 2, 3, 4]. On the first line,
# you will receive the number of a matrix's rows. On the next rows, you will get the elements for each column
# separated with a comma and a space ", ".

row_count = int(input())
matrix = []

for row in range(row_count):
    row_info = [int(x) for x in input().split(", ")]
    matrix.append(row_info)
flatted = []

for row in range(len(matrix)):
    for col in range(len(matrix[row])):
        element = matrix[row][col]
        flatted.append(element)
print(flatted)