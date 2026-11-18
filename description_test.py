
#Example tasks (only for testing)
tasks =[
    {
            "id": 1,
            "title": "Finish the project",
            "description": "",
    }
]

#Add a description
def add_description():
    print("\n---ADD A DESCRIPTION---")

    task_id = int(input("Enter he task ID: "))

    for task in tasks:
        if task["id"] == task_id:
            description = input("Enter the task description:")
            task["description"] = description

            print("Description added successfully!")
            print("Task:", task["title"])
            print("Description:", task["description"])
            return
    
    print("Task not found!")

#Run the function 
add_description()


