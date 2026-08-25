# My variables



to_do_number = [1., 2., 3. ]
to_do = ["Buy groceries", "Finish homework", "Call the dentist"]




# Project starts here

print("=" * 50)
print("                  My To-Do List")
print("=" * 50)

print(f"1. {to_do[0]}")
print(f"2. {to_do[1]}")
print(f"3. {to_do[2]}")
print("\nTotal tasks: 3")

print("\nWhat would you like to do? ")
print("1. Add a task")
print("2. Remove a task")

# Task Given Choice

try:
    choice = int(input("\nChoice: "))
except ValueError:
    print("Invalid choice. Enter 1 or 2.")
    print("Exiting Program")
    exit()

# Add and remove task 

if choice == 1:
   new_task = input("Enter new task: ") 
   to_do.append(new_task)
   for tasks in to_do:
    print(f"{tasks}")
elif choice == 2:
    list_number = int(input("Enter task number to remove: "))
    to_do.pop(list_number -1)
    for tasks in to_do:
     print(f"{tasks}")












# Recalculate and Display




    