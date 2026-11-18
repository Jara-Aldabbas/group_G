def create_task():
    task = "start the report"
    due_date = "tomorrow"
    is_completed = "No"

    print("Task:", task)
    print("Due Date:", due_date)
    print("Completed:", is_completed)

create_task()

def create_task():
    task = "Finish the project"
    due_date = "yesterday"
    is_completed = False

    if due_date == "yesterday" and not is_completed:
        status = "Overdue"
    else : 
        status = "On Time"

    print("task:" , task)
    print("due date:", due_date)
    print("status:", status)

create_task()

from datetime import date

#Example tasks (only for testing)

tasks = [
    {
            "id": 1,
            "title":"Finish the project",
            "due": date(2026, 11, 10),
            "priority": "High",
            "done": False 
    },
    {
            "id": 2,
            "title": "Study Python",
            "due": date(2026, 11, 25),
            "priority" : "Medium",
            "done": False
    },
    {
            "id": 3,
            "title": "Do the assignments",
            "due": date(2026, 11, 12),
            "priority": "Low",
            "done": True
    }
]

#View overdue tasks
def view_overdue_tasks():
    today = date.today()
    found = False 

    print("\n---OVERDUE TASKS---")

    for task in tasks:

        if task["due"] < today and not task["done"]:
            print("Task:", task["title"])
            print("Due date:", task["due"])
            print("Priority:", task["priority"])
            print("--------------------")
            found = True 

    if not found :
        print("No overdue tasks!")

#Run the function
view_overdue_tasks