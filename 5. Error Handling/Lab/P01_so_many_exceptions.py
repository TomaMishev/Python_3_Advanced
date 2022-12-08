# # # You are provided with the following code:
# #
# # numbers_list = input().split(", ")
# # result = 0
# #
# # for i in range(numbers_list):
# #     number = numbers_list[i + 1]
# #     if number < 5:
# #         result *= number
# #     elif number > 5 and number > 10:
# #         result /= number
# #
# # print(result)
#
# This code raises many exceptions. Fix it, so it works correctly.

numbers_list = [int(x) for x in input().split(", ")]
result = 1

for i in range(len(numbers_list)):

    number = numbers_list[i]
    if number <= 5:
        result *= number
    elif 5 < number <= 10:
        result /= number

print(round(result))
