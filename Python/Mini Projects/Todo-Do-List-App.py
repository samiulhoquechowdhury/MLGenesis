tasks = []

def add_task(task):
    tasks.append(task)
    print("Task added successfully!")

def view_tasks():
    if not tasks:
        print("No tasks available.")
    else:
        for idx, task in enumerate(tasks, 1):
            print(f"{idx}. {task}")

def delete_task(index):
    if 0 < index <= len(tasks):
        removed = tasks.pop(index - 1)
        print(f"Removed task: {removed}")
    else:
        print("Invalid task number!")

while True:
    print("\n1. Add Task\n2. View Tasks\n3. Delete Task\n4. Exit")
    choice = input("Choose an option: ")
    
    if choice == '1':
        task = input("Enter a task: ")
        add_task(task)
    elif choice == '2':
        view_tasks()
    elif choice == '3':
        view_tasks()
        index = int(input("Enter task number to delete: "))
        delete_task(index)
    elif choice == '4':
        break
    else:
        print("Invalid choice, try again!")
