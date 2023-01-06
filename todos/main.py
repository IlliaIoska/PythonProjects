from functions import modify_todos_file
from datetime import datetime
time = datetime.now()
print(time)


while(True):
    user_input = int(input("Options: \nPress 1 to add a new Item \nPress 2 to display the list's contents "
                           "\nPress 3 to edit an existing item \nPress 4 to exit the program "
                           "\n5 to remove the element"
                           "\n"))
    todos_file = open("todos.txt", "r+")
    todos = todos_file.readlines()

    match user_input:
        case 1:
            user_input = input("Enter a todo item: ")
            if(len(todos) == 0):
                todos_file.writelines(user_input + "\n")
            for i in range(len(todos)):
                if(todos[i].strip("\n") == user_input.strip()):
                    print("There is an item by that name")
                else:
                    todos_file.writelines(user_input + "\n")
        case 2:
            for index, item in enumerate(todos):
                item = item.strip("\n")
                print(f"{index + 1}: {item}")
        case 3:
            todos_file.close()
            user_input = input("Enter the name of an item you want to edit")
            for i in range(len(todos)):
                if(todos[i].strip("\n") == user_input):
                    todos[i] = input("new name: ") + "\n"
                    modify_todos_file(todos)
        case 4:
            break

        case 5:
            user_input = input("Enter the name of an item you want to remove from  the list")
            for i in range(len(todos)):
                if(todos[i].strip() == user_input):
                    todos.remove(todos[i])
                    modify_todos_file(todos)
                    print("the item has been successfully removed")

        case whatever:
            print("Not a valid input. Try again")

    todos_file.close()



