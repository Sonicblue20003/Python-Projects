def get_todos(filepath = 'todos.txt'):
    """Reads todos from a file and returns them as a list."""
    with open(filepath, "r") as file:
        todos_local = file.readlines()
    return todos_local
def write_todos(todos_arg, filepath = 'todos.txt'):
    """Writes todos to a file."""
    with open(filepath, "w") as file:
        file.writelines(todos_arg)

if __name__ == "__main__":
    print(get_todos())