# Write a program that reads a text from the console and counts the occurrences of each character in it. Print the
# results in alphabetical (lexicographical) order.

input_line = input()
symbols_count = dict()

for ch in input_line:
    if ch not in symbols_count:
        symbols_count[ch] = 1
    else:
        symbols_count[ch] += 1

for key, value in sorted(symbols_count.items()):
    print(f"{key}: {value} time/s")