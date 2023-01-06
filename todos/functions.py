def modify_todos_file(todos):
    with open("todos.txt", "w") as todos_file:
        todos_file.writelines(todos)