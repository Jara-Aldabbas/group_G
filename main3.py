tasks = []
while True: 
    name = input("Enter task (or exit): ")
    if name == "exit": 
        break
    print("Choose a category:")
    print("1. School")
    print("2. Work")
    print("3. Personal")

    choice = input("Enter 1, 2 or 3: ")

    if choice == "1": 
        category = "School"
    elif choice == "2": 
        category = "Work"
    elif choice == "3": 
        category = "Personal"
    else: 
        category = "Other"
    task = {
        "name": name, 
        "category": category 

        

    }

    