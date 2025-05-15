import os

def get_current_directory():
    return os.getcwd()

def list_items_in_directory():
    return os.listdir(get_current_directory())

def create_new_file(file_name):
    open(file_name, 'w').close()

def read_from_file(file_name):
    try:
        with open(file_name, 'r') as file:
            content = file.read()
            print(content)
    except FileNotFoundError:
        print("File not found. Please provide a correct file name.")

def append_to_file(file_name, content):
    try:
        with open(file_name, 'a') as file:
            file.write(content)
    except FileNotFoundError:
        print("File not found. Please provide a correct file name.")

def change_directory(path):
    try:
        os.chdir(path)
    except FileNotFoundError:
        print("Directory not found.")

# Main loop
while True:
    user_input = input(f"\n{get_current_directory()}> Enter your command: ").split(" ", maxsplit=2)
    command = user_input[0]

    if command == "exit":
        break

    elif command == "touch":
        file_name = user_input[1]
        if len(user_input) == 3:
            content = user_input[2]
            append_to_file(file_name, content)
        else:
            create_new_file(file_name)

    elif command == "ls":
        directory_items = list_items_in_directory()
        for item in directory_items:
            display_name = item + "\\" if os.path.isdir(item) else item
            print(display_name, end="   ")
        print()

    elif command == "cd":
        if len(user_input) > 1:
            change_directory(user_input[1])
            print(get_current_directory())
        else:
            print("Usage: cd <directory>")

    else:
        print("Unknown command.")
