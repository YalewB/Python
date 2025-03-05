# Smart To-Do List with Task Prioritization

def show_menu():
    """Display menu options."""
    print("\nSmart To-Do List:")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Mark Task as Completed")
    print("4. Remove Task")
    print("5. Exit")

def add_task(tasks):
    """Add a new task with priority."""
    task = input("Enter task description: ")
    priority = input("Priority (High/Medium/Low): ").strip().lower()
    
    if priority not in ['high', 'medium', 'low']:
        print("Invalid priority! Defaulting to Medium.")
        priority = 'medium'
    
    tasks.append({"task": task, "priority": priority, "completed": False})
    print(f"Task '{task}' added with {priority.capitalize()} priority.")

def view_tasks(tasks):
    """Display tasks with status and priority."""
    if not tasks:
        print("No tasks available.")
        return
    
    print("\nYour Tasks:")
    for idx, task in enumerate(tasks, start=1):
        status = "✓ Completed" if task["completed"] else "✗ Pending"
        print(f"{idx}. [{task['priority'].capitalize()}] {task['task']} - {status}")

def mark_completed(tasks):
    """Mark a task as completed."""
    view_tasks(tasks)
    try:
        task_no = int(input("Enter task number to mark as completed: ")) - 1
        if 0 <= task_no < len(tasks):
            tasks[task_no]["completed"] = True
            print(f"Task '{tasks[task_no]['task']}' marked as completed!")
        else:
            print("Invalid task number!")
    except ValueError:
        print("Please enter a valid number.")

def remove_task(tasks):
    """Remove a task from the list."""
    view_tasks(tasks)
    try:
        task_no = int(input("Enter task number to remove: ")) - 1
        if 0 <= task_no < len(tasks):
            removed_task = tasks.pop(task_no)
            print(f"Removed task: {removed_task['task']}")
        else:
            print("Invalid task number!")
    except ValueError:
        print("Please enter a valid number.")

# Main Program Loop
tasks = []
while True:
    show_menu()
    choice = input("Choose an option: ")

    if choice == "1":
        add_task(tasks)
    elif choice == "2":
        view_tasks(tasks)
    elif choice == "3":
        mark_completed(tasks)
    elif choice == "4":
        remove_task(tasks)
    elif choice == "5":
        print("Goodbye! Happy Productivity 😊")
        break
    else:
        print("Invalid choice! Please try again.")
