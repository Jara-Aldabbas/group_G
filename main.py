while True:
    print("\n=== TO-DO LIST ===")
    print("1. Add task")
    print("2. View tasks")
    print("3. Exit")
    choice = input("Choose an option: ")

    if choice == "1":
        print("You chose Add task")
    elif choice == "2":
        print("You chose View tasks")
    elif choice == "3":
        print("Goodbye")
        break
    else:
        print("Invalid choice.")