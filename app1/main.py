

while True:
    user_action = input("Type add, show, edit, or exit: ")
    user_action = user_action.strip()

    match user_action:
        case 'add':
            todo = input("Enter a todo: ") + "\n"

            file = open("todos.txt", 'r')
            todos = file.readlines()


            todos.append(todo)

            file = open('todos.txt', 'w')
            file.writelines(todos)
            file.close()
        case 'show':
            file = open('todos.txt', 'r')
            todos = file.readlines()
            file.close()

            for index, item in enumerate(todos):
                item = item.strip("\n")
                row = f"{index + 1}: {item}"
                print(row)
        case 'edit':
            number = int(input('enter the number of the todo to edit'))
            number = number - 1
            new_todo = input('Enter new todo: ')
            todos[number] = new_todo
        case 'exit':
            break
            
print("Bye!")
            