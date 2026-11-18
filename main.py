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

while True:
    print("\n=== TO-DO LIST ===")
    print("1. Add task")
    print("2. View tasks")
    print("3. Mark task as completed")
    print("4. Edit task")
    print("5. Exit")
    choice = input("Choose an option: ")

    if choice == "1":
        title = input_string("Enter task title: ")
        due = input_date("Enter due date (YYYY-MM-DD): ")
        priority = input_priority("Enter priority (High/Medium/Low): ")
        task = {"id": next_id, "title": title, "due": due, "priority": priority, "done": False}
        tasks.append(task)
        next_id = next_id + 1
        print("Task added:", title)
    elif choice == "2":
        if len(tasks) == 0:
            print("No tasks available.")
        else:
            for task in tasks:             
                if task["done"]:           
                    status = "[X]"          
                else:                      
                    status = "[ ]"         
                print(task["id"], status, task["title"], task["due"], task["priority"])  
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
        edit_task()
    elif choice == "5":
        print("Goodbye")
        break
        