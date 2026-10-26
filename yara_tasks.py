print("MY", "TASKS")
task1 = "study python"
print(task1)
task2 = "finish homework"
print(task2)
task3 = "prepare presentation"
print(task3)
status1 = "incomplete"
print(f" 1. {task1} - {status1}")
status2 = "completed"
print(f" 2. {task2} - {status2}")
status3 = "incomplete"
print(f" 3. {task3} - {status3}")
while True:
  choice = input("enter_your_choice_:")
  print(f" you selected : {choice}")
  if choice == "1":
   print("you selected View All Tasks")
   print(f"1. {task1}- {status1}")
   print(f"2. {task2}- {status2}")  
   print(f"3. {task3}- {status3}")
  elif choice == "2":
   print("you selected delete tasks")
   delete_choice = input("which task do you want to delete? (1, 2, 3): ")
   if delete_choice == "1":
      task1 = ""
      print("task 1 deleted")
   elif delete_choice == "2":
      task2 = ""
      print("task 2 deleted")
   elif delete_choice == "3":
      task3 = ""
      print("task 3 deleted")
   else:
      print("invalid task number")
  elif choice == "3":
   print("you selected search task")
   search = input("enter task name: ")
   if search == task1 and task1 != "":
      print("task found:", task1)
   elif search == task2 and task2 != "":
      print("task found:", task2)
   elif search == task3 and task3 != "":
      print("task found:", task3)
   else:
      print("task not found")
  elif choice == "4":
   print("Goodbye!")
   break
  else:
   print("invalid choice")
