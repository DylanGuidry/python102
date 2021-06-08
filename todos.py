todos = ["pet the cat", "go to work", "shop for groceries", "go home", "feed the cat"]

def print_todos():
    print("------- To Dos --------")
    count = 1
    for todo in todos:
        print(f"{count}: {todo}")
        count +=1
    print("------- To Dos --------")

while True:
    print("""
Choose an option:

1. Print Todos
2.Add Todos
3. Remove
0. Qit
    """)
    user_choice = input("")

    if user_choice == "1":
        #Print current todos
        print_todos()
    elif user_choice == "2":
        #Adding items 
        add_to_list = input("Add to this list:")
        todos.append(add_to_list)
    elif user_choice == "3":
        #Delete or remove a todo.
        index = 0
        print_todos()
        delete_index = int(input("Which item would you like to delete?"))
        del todos[delete_index]
    elif user_choice == "0":
        break
