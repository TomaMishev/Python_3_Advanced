# Write a program that receives a matrix of numbers and prints a new one only with the numbers that are even. Use
# nested comprehension for that problem. On the first line, you will receive the rows of the matrix. On the next
# rows, you will get elements for each column separated with a comma and a space ", ".

rows_count = int(input())
matrix = []
for row in range(rows_count):
    row_info = input().split(", ")
    matrix.append(list(map(int, row_info)))
evens = [[x for x in row if x % 2 == 0] for row in matrix]
print(evens)