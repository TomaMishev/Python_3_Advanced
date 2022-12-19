def print_upper_part(num):
    for row_num in range(1, num + 1):
        for number in range (1, row_num + 1):
            print(number, end=" ")
        print()


def print_bottom_part(num):
    for row_num in range(num - 1, 0, -1):
        for number in range(1, row_num + 1):
            print(number, end=" ")
        print()


def print_triangle(num):
    print_upper_part(num)
    print_bottom_part(num)