def create_task(name, description="", completed=False, due_date=None):
    task = {
        "name": name,
        "description": description,
        "completed": completed,
        "due_date": due_date,
    }
    return task


def user_input_task():
    name = input("Task name: ")
    description = input("Description (optional): ")
    due_date = input("Due date (optional): ")
    if due_date == "":
        due_date = None
    task = create_task(name, description, False, due_date)
    return task


def print_task(task, number):
    if task["completed"]:
        status = "completed"
    else:
        status = "incomplete"

    name = task["name"]
    description = task["description"]
    due_date = task["due_date"]
    if due_date == None:
        due_date = "no due date"

    print(f"{number}. {name} - {status}")
    print(f"   description: {description}")
    print(f"   due date: {due_date}")


def view_tasks(tasks):
    print("you selected View Tasks")
    if len(tasks) == 0:
        print("No tasks available.")
    else:
        for i in range(len(tasks)):
            print_task(tasks[i], i + 1)


def delete_task(tasks):
    print("you selected Delete Task")
    if len(tasks) == 0:
        print("No tasks available.")
    else:
        try:
            number = int(input(f"which task do you want to delete? (1-{len(tasks)}): "))
        except ValueError:
            print("Task not found.")
        else:
            if number >= 1 and number <= len(tasks):
                name = tasks[number - 1]["name"]
                del tasks[number - 1]
                print(f"task '{name}' deleted")
            else:
                print("Task not found.")


def search_task(tasks):
    print("you selected Search Task")
    if len(tasks) == 0:
        print("No tasks available.")
    else:
        search = input("enter task name: ")
        found = False
        for i in range(len(tasks)):
            if tasks[i]["name"] == search:
                print("task found:")
                print_task(tasks[i], i + 1)
                found = True
        if not found:
            print("Task not found.")


def add_task(tasks):
    print("you selected Add Task")
    task = user_input_task()
    if task["name"] == "":
        print("Task name cannot be empty.")
    else:
        tasks.append(task)
        print(f"task '{task['name']}' added")


def print_menu():
    print("1. View Tasks")
    print("2. Delete Task")
    print("3. Search Task")
    print("4. Add Task")
    print("5. Exit")


# Program flow
tasks = [
    create_task("Study Python"),
    create_task("Finish Homework", completed=True),
    create_task("Prepare Presentation", "Final project slides", False, "2026-12-06"),
]

print("MY TASKS")
print_menu()
choice = input("enter_your_choice_: ")
while choice != "5":
    print(f"you selected : {choice}")
    if choice == "1":
        view_tasks(tasks)
    elif choice == "2":
        delete_task(tasks)
    elif choice == "3":
        search_task(tasks)
    elif choice == "4":
        add_task(tasks)
    else:
        print("invalid choice")
    print_menu()
    choice = input("enter_your_choice_: ")
print("Goodbye!")
