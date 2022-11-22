# Write a program that finds the difference between the sums of the square matrix diagonals (absolute value). On the
# first line, you will receive an integer N - the size of a square matrix. The following N lines hold the values for
# each column - N numbers separated by a single space. Print the absolute difference between the primary and the
# secondary diagonal sums.

rows_count = int(input())
matrix = [[int(x) for x in input().split()] for x in range(rows_count)]
primary_diagonal = []
secondary_diagonal = []

for index in range(len(matrix)):
    primary_diagonal.append(matrix[index][index])
    secondary_diagonal.append(matrix[index][rows_count - 1 - index])

print(abs(sum(primary_diagonal) - sum(secondary_diagonal)))