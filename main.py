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

def input_priority(prompt):
    while True:
        value = input(prompt).strip().capitalize()
        if value in ["High", "Medium", "Low"]:
            return value
        else:
            print("Priority must be High, Medium or Low.")

tasks = []
next_id = 1

def save_tasks():
    with open("tasks.txt", "w") as file:
        for task in tasks:
            line = str(task["id"]) + ";" + task["title"] + ";" + task["due"] + ";" + task["priority"] + ";" + str(task["done"])
            file.write(line + "\n")

def load_tasks():
    global next_id
    try:
        with open("tasks.txt", "r") as file:
            for line in file:
                parts = line.strip().split(";")
                if len(parts) != 5:
                    print("Skipping invalid line:", line.strip())
                    continue
                task = {
                    "id": int(parts[0]),
                    "title": parts[1],
                    "due": parts[2],
                    "priority": parts[3],
                    "done": parts[4] == "True"
                }
                tasks.append(task)
                if task["id"] >= next_id:
                    next_id = task["id"] + 1
    except FileNotFoundError:
        pass

def add_task():
    global next_id
    title = input_string("Enter task title: ")
    due = input_date("Enter due date (YYYY-MM-DD): ")
    priority = input_priority("Enter priority (High/Medium/Low): ")
    task = {"id": next_id, "title": title, "due": due, "priority": priority, "done": False}
    tasks.append(task)
    next_id = next_id + 1
    print("Task added:", title)
    save_tasks()

def view_tasks():
    if len(tasks) == 0:
        print("No tasks available.")
    else:
        for task in tasks:
            if task["done"]:
                status = "[X]"
            else:
                status = "[ ]"
            print(task["id"], status, task["title"], task["due"], task["priority"])

def complete_task():
    task_id = input_int("Enter the ID of the task to complete: ")
    found = False
    for task in tasks:
        if task["id"] == task_id:
            task["done"] = True
            found = True
            print("Task", task_id, "marked as completed.")
    if not found:
        print("Task ID not found.")
    save_tasks()

def edit_task():
    task_id = input_int("Enter the ID of the task to edit: ")
    found = False
    for task in tasks:
        if task["id"] == task_id:
            task["title"] = input_string("Enter new title: ")
            task["priority"] = input_priority("Enter new priority (High/Medium/Low): ")
            found = True
            print("Task", task_id, "updated.")
    if not found:
        print("Task ID not found.")
    save_tasks()

load_tasks()

while True:
    print("\n=== TO-DO LIST ===")
    print("1. Add task")
    print("2. View tasks")
    print("3. Mark task as completed")
    print("4. Edit task")
    print("5. Exit")
    choice = input("Choose an option: ")

    if choice == "1":
        add_task()
    elif choice == "2":
        view_tasks()
    elif choice == "3":
        complete_task()
    elif choice == "4":
        edit_task()
    elif choice == "5":
        print("Goodbye")
        break
    else:
        print("Invalid choice.")