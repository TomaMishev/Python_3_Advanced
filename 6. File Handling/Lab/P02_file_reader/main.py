# You are given a file called numbers.txt with the following content:

# 1
# 2
# 3
# 4
# 5

# Create a program that reads the numbers from the file. Print on the console the sum of those numbers.

text_file = open('numbers.txt')
total_sum = 0
for i in text_file.readlines():
    current_num = int(i)
    total_sum += current_num

print(total_sum)
