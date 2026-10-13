# To-Do List – Console Application

    🚧 This is a template repository for student project in the course Programming Foundations at FHNW, BSc BIT.

This project is intended to:

    Practice the complete process from problem analysis to implementation
    Apply basic Python programming concepts learned in the Programming Foundations module
    Demonstrate the use of console interaction, data validation, and file processing
    Produce clean, well-structured, and documented code
    Prepare students for teamwork and documentation in later modules
    Use this repository as a starting point by importing it into your own GitHub account.
    Work only within your own copy — do not push to the original template.
    Commit regularly to track your progress.

Problem

Students often have many tasks, assignments, and deadlines to manage. It can be difficult to remember everything and keep track of what needs to be done.

Our To-Do List application helps users organize their tasks in one place. Users can add, edit, delete, and complete tasks. They can also organize tasks by category and track their progress.

The application will run in the console using Python.

Scenario

A student wants to organize their daily tasks using a simple To-Do List application.

The student opens the application in the console and can add new tasks, view existing tasks, mark tasks as completed, or delete tasks.

For example, the student adds a task called “Study Python”. After finishing it, the student marks it as completed.

The application helps students keep track of their tasks in a simple way.

User (Student)

The user is a student who wants to organize daily tasks.

The user can add, view, edit, complete, and delete tasks.
Role 	Description

### Orgilmaa Shinebaatar

### User Story 1: Add a Task with Deadline
**As a** user,  
**I want** to set a due date when adding a task,  
**so that** I can manage my time effectively and avoid missing deadlines.

* **Given** a task description "Submit Report" and a valid due date input "2026-10-15",  
  **When** the user saves the new task,  
  **Then** the system creates the task with the assigned due date and displays a confirmation message.

* **Given** an invalid due date input such as "next Tuesday" or "32-13-2026",  
  **When** the user submits the form,  
  **Then** the system displays a validation error requesting the date in YYYY-MM-DD format.

### User Story 2: Mark Task as Completed
**As a** user,  
**I want** to mark a task as completed,
**so that** I can track my progress and keep my active list up to date.

* **Given** an existing pending task with ID `3`,  
  **When** the user selects task `3` and chooses "Mark as Completed",  
  **Then** the task status updates to "Completed" `[X]`.

* **Given** a task ID that does not exist (e.g., entering `99` when only 5 tasks exist),  
  **When** the user attempts to complete it,  
  **Then** the system alerts the user that the task ID was not found.

### User Story 3: Edit Existing Task
**As a** user,  
**I want** to edit the details of an existing task (such as its title or priority),  
**so that** I can keep my task list accurate when plans change.

* **Given** a task "Buy Milk" with "Low" priority,  
  **When** the user changes the title to "Buy Almond Milk" and priority to "High",  
  **Then** the task record updates and reflects the new title and high priority status.

* **Given** an active edit session,  
  **When** the user submits a blank string for the updated task title,  
  **Then** the system rejects the change and prompts the user to input a valid title.

### Niman Aldabbas Jara

### User Story 4: Delete a Task

**As a** user,
**I want** to delete a task,
**so that** I can remove tasks I no longer need.

**Acceptance Criteria:**

* **Given** a task named "Study Python",
  **When** the user deletes the task,
  **Then** the task is removed from the list.

* **Given** an empty task list,
  **When** the user tries to delete a task,
  **Then** the system displays "No tasks available."

* **Given** a task list with two tasks,
  **When** the user enters an invalid task number,
  **Then** the system displays "Task not found."

### User Story 5: View All Tasks

**As a** user,
**I want** to view all my tasks,
**so that** I can see what I need to do.

**Acceptance Criteria:**

* **Given** a list containing three tasks,
  **When** the user selects "View Tasks",
  **Then** all three tasks are displayed.

* **Given** an empty task list,
  **When** the user selects "View Tasks",
  **Then** the system displays "No tasks available."

* **Given** a list containing completed and incomplete tasks,
  **When** the user selects "View Tasks",
  **Then** all tasks are displayed with their status.

### User Story 6: Search for a Task

**As a** user,
**I want** to search for a task by its name,
**so that** I can find it quickly.

**Acceptance Criteria:**

* **Given** a task named "Study Python",
  **When** the user searches for "Study Python",
  **Then** the task is displayed.

* **Given** a task list,
  **When** the user searches for a task that does not exist,
  **Then** the system displays "Task not found."

* **Given** an empty task list,
  **When** the user tries to search for a task,
  **Then** the system displays "No tasks available."
  
### Emna Ayari

### User Story 7 : Setting numerous lists of tasks 
**As a** user,
**I want** to be able to set many lists of tasks depending on my week planning or my needs at the moment,
**so that** I can allocate the tasks that I have in a precise list.

**Acceptance Criteria:**

* **Given** an option which permits me to open another tab of list of tasks, 
  **When** the user clicks on the option,
  **Then** the new list will automatically appear.

* **Given** a list with no name, then the user will not be able to open another tab of list.

### User Story 8 : Set reminders to my tasks 
**As a** user,
**I want** to be reminded of my tasks before the due deadline,
**so that** I can finish my task in due time and check it off my list.

**Acceptance Criteria:**

* **Given** a reminder option with notifications,
  **When** the time period of completing the task comes,
  **Then** then a notification will pop out on the screen of the user.


### User Story 9 : Having my tasks set in a calendar
**As a** user,
**I want** to be able to link my tasks to a calendar,
**so that** I can have a bigger picture of what is set for the week, month or the whole year.

**Acceptance Criteria:**

* **Given** a calendar where i can add tasks to its slot,
  **When** the user wants to add a specific task to a day,
  **Then** text can be put within the date cell.


### Razma Nasrullah 

### User Story 10 : Track my habits and goals
**As a** user,
**I want** to assign categories to my tasks, such as School, Work, or Personal,
**so that** I can organise my responsibilities and find related tasks more easily. 

* **Given** a task called "Finish Programming Assignment",
  **When** the user assigns the category "School" to the task,  
  **Then** the system saves and displays the task under the selected category.

  
### User Story 11 : Filter Tasks by Status

**As a** user,
**I want** to filter my tasks by their status, such as Pending or Completed,
**so that** I can focus on unfinished tasks or review what I have already accomplished.

* **Given** a task list containing both pending and completed tasks,
  **When** the user selects the "Pending" filter,
  **Then** the system displays only tasks that have not been completed.


### User Story 12 : Sort Tasks by Priority
**As a** user,
**I want** to sort my tasks according to their priority,
**so that** I can identify and focus on the most important tasks first.

* **Given** a task list containing tasks with High, Medium, and Low priorities,
  **When** the user selects the option to sort by priority,
  **Then** the system displays high-priority tasks first, followed by medium- and low-priority tasks.


Acceptance criteria

    The summary is shown after the staff member enters done.
    The summary starts with the heading --- ORDER SUMMARY ---.
    It lists every ordered item with quantity, name, size, and item total, e.g., 2x Margherita (Medium) - CHF 25.00.
    It lists every applied discount (see US-06).
    It ends with the final amount in the format TOTAL: CHF <amount> with two decimal places.
    Given the staff member enters done without having added any pizza, when the order is finished, then the message ⚠️ No pizzas selected. is displayed, no summary and no invoice are created, and the main menu is shown again.

US-08: Save the invoice as a file

As an owner, I want each completed order to be saved as a numbered invoice file, so that I have a permanent record of all sales.

Acceptance criteria

    An invoice file is created automatically for every order that contains at least one pizza.
    The file name follows the pattern invoice_<NNN>.txt with a three-digit number, e.g., invoice_001.txt.
    Given no invoice file exists yet, when an order is completed, then the file invoice_001.txt is created.
    Given invoice_001.txt and invoice_002.txt already exist, when an order is completed, then the file invoice_003.txt is created and the existing files remain unchanged.
    The invoice contains the heading 🍕 PIZZA RP INVOICE, one line per ordered item (quantity, name, size, item total), all applied discounts, and the line TOTAL: CHF <amount>.
    The amounts in the invoice file are identical to the amounts shown in the order summary (US-07).
    After saving, the message ✅ Invoice saved as invoice_<NNN>.txt is displayed.

US-09: Exit the application

As a staff member, I want to close the application via the main menu, so that I can end my shift in a controlled way.

Acceptance criteria

    Given the main menu is displayed, when the staff member enters 3, then the message Goodbye 👋 is displayed and the program ends.
    All invoices created during the session remain saved after the program has ended.

Use cases:

    Show Menu (from menu.txt)
    Create Order (choose pizzas)
    Show Current Order and Total
    Print Invoice (to invoice_xxx.txt)

✅ Project Requirements

The To-Do List application will be developed using Python and will run in the console.

The application should allow users to:

1. Add new tasks.
2. View all tasks.
3. Edit existing tasks.
4. Mark tasks as completed.
5. Delete tasks.
6. View completed and incomplete tasks.

The application should be simple and easy to use.

2. Data Validation

The application validates all user input to ensure data integrity and a smooth user experience. This is implemented in main-invoice.py as follows:

    Entering a new task: When the user wants to enter a new task to achieve, the "+" sign will be pressed and text cell will directly appear :

    task = input("new task :")

    If not, then text can not be added.

    This ensures that the user knows that to enter new tasks, the "+" sign has to be pressed beforehand.

    Quantity input: After a pizza is selected, the program asks for the quantity until a whole number of at least 1 is entered:

     if not quantity.isdigit() or int(quantity) < 1:
     		print("⚠️ Invalid quantity.")
     		continue

    This rejects 0, negative numbers, decimal numbers, and text.

    Menu file validation: When reading the menu file, the program checks for valid price values and skips invalid lines:

     try:
     		menu.append({"name": name, "size": size, "price": float(price)})
     except ValueError:
     		print(f"⚠️ Skipping invalid line: {line.strip()}")

    Main menu options: The main menu checks for valid options and handles invalid choices gracefully:

     else:
     		print("⚠️ Invalid choice.")

These checks prevent crashes and guide the user to provide correct input, matching the validation requirements described in the project guidelines.
3. File Processing

The application reads and writes data using files:

    Input file: menu.txt — Contains the pizza menu, one item per line in the format PizzaName;Size;Price.
        Example:

         Margherita;Medium;12.50
         Salami;Large;15.00
         Funghi;Small;9.00

        The application reads this file at startup to display available pizzas.

    Output file: invoice_001.txt (and similar) — Generated when an order is completed. Contains a summary of the order, including items, quantities, prices, discounts, and totals.
        Example:

         🍕 PIZZA RP INVOICE
         ---------------------
         3x Diavola (Large) - CHF 52.50
         ---------------------
         Discount: 10% discount (-CHF 5.25)
         TOTAL: CHF 47.25

            The output file serves as a record for both the user and the pizzeria, ensuring accuracy and transparency.

⚙️ Implementation
Technology

    Python 3.x
    Environment: GitHub Codespaces
    No external libraries

📂 Repository Structure

PizzaRP/
├── main.py             # main program logic (console application)
├── menu.txt            # pizza menu (input data file)
├── invoice_001.txt     # example of a generated invoice (output file)
├── docs/               # optional screenshots or project documentation
└── README.md           # project description and milestones

How to Run

    🚧 Adjust if needed.

    Open the repository in GitHub Codespaces
    Open the Terminal
    Run:

    python3 main.py

Libraries Used

    os: Used for file and path operations, such as checking if the menu file exists and creating new files.
    glob: Used to find all invoice files matching a pattern (e.g., invoice_*.txt) to determine the next invoice number.

These libraries are part of the Python standard library, so no external installation is required. They were chosen for their simplicity and effectiveness in handling file management tasks in a console application.
👥 Team & Contributions

    🚧 Fill in the names of all team members and describe their individual contributions below. Each student should be responsible for at least one part of the project.

Name 	Contribution
Student A 	Menu reading (file input) and displaying menu
Student B 	Order logic and data validation
Student C 	Invoice generation (file output) and slides
🤝 Contributing

    🚧 This is a template repository for student projects.
    🚧 Do not change this section in your final submission.

    Use this repository as a starting point by importing it into your own GitHub account.
    Work only within your own copy — do not push to the original template.
    Commit regularly to track your progress.

📝 License

This project is provided for educational use only as part of the Programming Foundations module.
MIT License
