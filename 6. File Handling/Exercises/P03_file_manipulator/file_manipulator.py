# Create a program that will receive commands until the command "End". The commands can be: "Create-{file_name}"
# -Creates the given file with an empty content. If the file already exists, remove the existing text in it (as if the
# file is created again) •	"Add-{file_name}-{content}" - Append the content and a new line after it. If the file does
# not exist, create it, and add the content •	"Replace-{file_name}-{old_string}-{new_string}" - Open the file and
# replace all the occurrences of the old string with the new string. If the file does not exist, print: "An error
# occurred" •	"Delete-{file_name}" - Delete the file. If the file does not exist, print: "An error occurred"

from os import path, remove

user_input = input()

while user_input != "End":
    tokens = user_input.split("-")
    command = tokens[0]
    file_name = tokens[1]

    if command == "Create":
        open(file_name, 'w').close()
    elif command == "Add":
        content = tokens[2]
        with open(file_name, 'a') as file:
            file.write(content + "\n")
    elif command == "Delete":
        if path.exists(file_name):
            remove(file_name)
        else:
            print('An error occurred')
    elif command == "Replace":
        old_string = tokens[2]
        new_string = tokens[3]
        with open(file_name, 'r+') as file:
            new_file_content = file.read().replace(old_string, new_string)
            file.seek(0)
            file.truncate()
            file.write(new_file_content)





    user_input = input()
