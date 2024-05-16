def display_menu():
    print("\nTo-Do List Application")
    print("1. Add a task")
    print("2. View tasks")
    print("3. Mark a task as done")
    print("4. Remove a task")
    print("5. Exit")

def add_task(tasks):
    task = input("Enter the task: ")
    tasks.append({"task": task, "done": False})
    print(f"Task '{task}' added.")

def view_tasks(tasks):
    if not tasks:
        print("No tasks in the list.")
    else:
        for idx, task in enumerate(tasks, start=1):
            status = "Done" if task["done"] else "Not Done"
            print(f"{idx}. {task['task']} - {status}")

def mark_task_done(tasks):
    task_num = int(input("Enter the task number to mark as done: ")) - 1
    if 0 <= task_num < len(tasks):
        tasks[task_num]["done"] = True
        print(f"Task '{tasks[task_num]['task']}' marked as done.")
    else:
        print("Invalid task number.")

def remove_task(tasks):
    task_num = int(input("Enter the task number to remove: ")) - 1
    if 0 <= task_num < len(tasks):
        removed_task = tasks.pop(task_num)
        print(f"Task '{removed_task['task']}' removed.")
    else:
        print("Invalid task number.")

def main():
    tasks = []
    while True:
        display_menu()
        choice = input("Choose an option: ")
        
        if choice == '1':
            add_task(tasks)
        elif choice == '2':
            view_tasks(tasks)
        elif choice == '3':
            mark_task_done(tasks)
        elif choice == '4':
            remove_task(tasks)
        elif choice == '5':
            print("Exiting the application. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
