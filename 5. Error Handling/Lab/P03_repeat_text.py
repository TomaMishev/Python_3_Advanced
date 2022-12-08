# Write a program that receives a text on the first line and times (to repeat the text) that must be an integer. If
# the user passes non-integer type for the times variable, handle the exception and print a message "Variable times
# must be an integer".

text_input = input()
while True:
    try:
        times = int(input())
        print(text_input * times)
        break
    except ValueError:
        print("Variable times  must be an integer")
