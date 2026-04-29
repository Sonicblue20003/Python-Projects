#from functions import get_todos, write_todos
import functions
text = """
This is a simple task manager that allows 
you to add, show, edit, and complete tasks.
"""

print(text)

while True:
    user_action = input("Type add, show, edit, complete or exit: ")
    user_action = user_action.strip()

    if user_action.startswith('add'):
        todo = user_action[4:]

        todos = functions.get_todos()

        todos.append(todo + '\n')

        functions.write_todos(todos)


    elif user_action.startswith('show'):
            todos = functions.get_todos()


            #new_todos=[]
            #for item in todos:
                #new_item = item.strip('\n')
                #new_todos.append(new_item) <-- this does the same as the inline below
            #new_todos = [item.strip('\n') for item in todos]

            for index, item in enumerate(todos):
                item = item.strip('\n')
                row = f"{index + 1}. {item}"
                print(row)

    elif user_action.startswith('edit'):
        try:
            number = int(user_action[5:])
            number = number - 1

            todos = functions.get_todos()

            if number > len(todos):
                print(f"Invalid number. There is no {number + 1}. Please enter a valid number.")
                continue

            new_todo = input("Enter new todo: ")
            todos[number] = new_todo + '\n'

            functions.write_todos(todos)

            print(f"To do {number + 1} has been edited!")

        except ValueError:
            print("Invalid input. Please enter a number.")
            continue



    elif user_action.startswith('complete'):

       try:
            number = int(user_action[8:])
            index = number - 1
            print(index)

            todos = functions.get_todos()
            todos.pop(index)

            functions.write_todos(todos)


            message = f"Todo {number} has been removed!"

            print(message)
       except IndexError:
           print(f"Invalid number. Please enter a valid number.")
    elif 'exit' in user_action:
        break
    else:
        print("Invalid action")