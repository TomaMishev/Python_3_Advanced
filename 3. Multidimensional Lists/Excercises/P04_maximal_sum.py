# Write a program that reads a rectangular matrix's dimensions and finds the 3x3 square with a maximum sum of its
# elements. There will be no case with two or more 3x3 squares with equal maximal sum. Input •	On the first line,
# you will receive the rows and columns in the format "{rows} {columns}" – integers in the range [1, 20] •	On the
# following lines, you will receive each row with its columns - integers, separated by a single space in the range [
# -20, 20] Output •	On the first line, print the maximum sum of the elements in the 3x3 square in the format "Sum = {
# sum}" •	On the following 3 lines, print each element of the found submatrix, separated by a single space


rows, cols = [int(x) for x in input().split()]
matrix = []

for _ in range(rows):
    matrix.append([int(x) for x in input().split()])

maximal_sum = 0
max_row = 0
max_col = 0

for row in range(len(matrix) - 2):
    for col in range(len(matrix[row]) - 2):
        first_row = matrix[row][col] + matrix[row][col + 1] + matrix[row][col + 2]
        second_row = matrix[row + 1][col] + matrix[row + 1][col + 1] + matrix[row + 1][col + 2]
        third_row = matrix[row + 2][col] + matrix[row + 2][col + 1] + matrix[row + 2][col + 2]

        current_sum = first_row + second_row + third_row

        if current_sum >= maximal_sum:
            maximal_sum = current_sum
            max_row = row
            max_col = col

print(f"Sum = {maximal_sum}")
print(f"{matrix[max_row][max_col]} {matrix[max_row][max_col + 1]} {matrix[max_row][max_col + 2]}")
print(f"{matrix[max_row + 1][max_col]} {matrix[max_row + 1][max_col + 1]} {matrix[max_row + 1][max_col + 2]}")
print(f"{matrix[max_row + 2][max_col]} {matrix[max_row + 2][max_col + 1]} {matrix[max_row + 2][max_col + 2]}")
