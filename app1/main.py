todos = []

while True:
    user_action = input("Type add or show: ")

    match user_action:
        case 'add':
            todo = input("Enter a todo: ")
            