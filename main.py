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

def input_int(prompt):
    while True:
        value = input(prompt)
        try:
            return int(value)
        except ValueError:
            print("Please enter a whole number.")

tasks = []
next_id = 1

while True:
    print("\n=== TO-DO LIST ===")
    print("1. Add task")
    print("2. View tasks")
    print("3. Mark task as completed")
    print("4. Exit")
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
        task_id = input_int("Enter the ID of the task to complete: ")
        found = False
        for task in tasks:
            if task["id"] == task_id:
                task["done"] = True
                found = True
                print("Task", task_id, "marked as completed.")
        if not found:
            print("Task ID not found.")
    elif choice == "4":
        print("Goodbye")
        break
        