from datetime import date 

# Example tasks (only for testing)
tasks = [
    {
        "id": 1,
        "title": "Finish the project",
        "due": date(2026, 11, 20),
        "priority" : "High",
        "done": False
    },
    {
        "id": 2,
        "title": "Study Python",
        "due": date(2026, 11, 25),
        "priority": "Medium",
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

# Export tasks to a text file
def export_tasks():
    with open("tasks_export.txt", "w", encoding="utf-8") as file:

        file.write("---TASK LIST---\n\n")

        for task in tasks:
            file.write("Task ID: " + str(task["id"]) + "\n")
            file.write("Title:" + task["title"] + "\n")
            file.write("Due date:" + str(task["due"]) + "\n")
            file.write("Priority:" + task["priority"] + "\n")

            if task["done"]:
                file.write("Status: Completed\n")
            else:
                file.write("Status: Not completed\n")
            
            file.write("----------------\n\n")
    
    print("Tasks exported successfully!")

#Run the function
export_tasks()


