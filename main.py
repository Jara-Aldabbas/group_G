from datetime import datetime

def input_string(prompt):
    while True:
        value = input(prompt)
        if value.strip():
            return value
        else:
            print("Input cannot be empty. Please try again.")

def input_date(prompt):
    while True:
        value = input_string(prompt)
        try:
            datetime.strptime(value, "%Y-%m-%d")
            return value
        except ValueError:
            print("Please enter the date in YYYY-MM-DD format.")

tasks = []
next_id = 1

while True:
    print("\n=== TO-DO LIST ===")
    print("1. Add task")
    print("2. View tasks")
    print("3. Exit")
    choice = input("Choose an option: ")

    if choice == "1":
        title = input_string("Enter task title: ")
        due = input_date("Enter due date (YYYY-MM-DD): ")
        task = {"id": next_id, "title": title, "due": due, "priority": "Medium", "done": False}
        tasks.append(task)
        next_id = next_id + 1
        print("Task added:", title)
    elif choice == "2":
        if len(tasks) == 0:
            print("No tasks available.")
        else:
            for task in tasks:
                print(task["id"], task["title"], task["due"], task["done"])
    elif choice == "3":
        print("Goodbye")
        break
    else:
        print("Invalid choice.")
        