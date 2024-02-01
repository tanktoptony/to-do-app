FILEPATH = "todos.txt"
def get_todos(filepath="todos.txt"):
    """Read a text file and return the list of
    to-do items."""
    with open(filepath, 'r') as file_local:
        todos_local = file_local.readlines()
    return todos_local


def write_todos(todos_arg, filepath="todos.txt"):
    """Write to the original text file with added or
    completed to do items."""
    with open(filepath, 'w') as file:
        file.writelines(todos_arg)

if __name__ == "__main__":
    print("test")