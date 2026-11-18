
def create_task(name, description="", completed=False, due_date=None):
    return {
        "name": name,
        "description": description,
        "completed": completed,
        "due_date": due_date,
    }
 
 
def user_input_task():
    name = input("Task name: ").strip()
    description = input("Description (optional): ").strip()
    due_date = input("Due date (optional, e.g. 2026-12-06): ").strip()
    if due_date == "":
        due_date = None
    return create_task(name, description, False, due_date)
 
 
def print_task(task, number):
    status = "Completed" if task["completed"] else "Incomplete"
    due_date = task["due_date"] if task["due_date"] is not None else "No due date"
    description = task["description"] if task["description"] != "" else "-"
    print(f"{number}. {task['name']}  [{status}]")
    print(f"   Description: {description}")
    print(f"   Due date:    {due_date}")
 
 
def view_tasks(tasks):
    print("you selected View Tasks")
    if len(tasks) == 0:
        print("No tasks available.")
        return
    print("-" * 40)
    for i, task in enumerate(tasks, start=1):
        print_task(task, i)
    print("-" * 40)
 
 
def delete_task(tasks):
    print("you selected Delete Task")
    if len(tasks) == 0:
        print("No tasks available.")
        return
    number = input(f"which task do you want to delete? (1-{len(tasks)}): ").strip()
    if number.isdigit() and 1 <= int(number) <= len(tasks):
        removed = tasks.pop(int(number) - 1)
        print(f"task '{removed['name']}' deleted")
    else:
        print("Task not found.")
 
 
def search_task(tasks):
    print("you selected Search Task")
    if len(tasks) == 0:
        print("No tasks available.")
        return
    search = input("enter task name: ").strip().lower()
    for i, task in enumerate(tasks, start=1):
        if task["name"].strip().lower() == search:
            print("task found:")
            print_task(task, i)
            return
    print("Task not found.")
 
 
def add_task(tasks):
    print("you selected Add Task")
    task = user_input_task()
    if task["name"] == "":
        print("Task name cannot be empty.")
        return
    tasks.append(task)
    print(f"task '{task['name']}' added")
 
 
def print_menu():
    print("\n===== MY TASKS =====")
    print("1. View Tasks")
    print("2. Delete Task")
    print("3. Search Task")
    print("4. Add Task")
    print("5. Exit")
 
 
def main():
    tasks = [
        create_task("Study Python"),
        create_task("Finish Homework", completed=True),
        create_task("Prepare Presentation", "Final project slides", False, "2026-12-06"),
    ]
 
    while True:
        print_menu()
        choice = input("enter_your_choice_: ").strip()
        print(f" you selected : {choice}")
        if choice == "1":
            view_tasks(tasks)
        elif choice == "2":
            delete_task(tasks)
        elif choice == "3":
            search_task(tasks)
        elif choice == "4":
            add_task(tasks)
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("invalid choice")
 
 
main()
