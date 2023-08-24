def display_tasks(tasks):
    if not tasks:
        print("Your to-do list is empty.")
    else:
        print("Your to-do list:")
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")

def add_task(tasks):
    task = input("Enter the task: ")
    tasks.append(task)
    print(f"Task '{task}' added to your to-do list.")

def remove_task(tasks):
    if not tasks:
        print("Your to-do list is already empty.")
        return

    display_tasks(tasks)
    index = int(input("Enter the task number to remove: "))
    if 1 <= index <= len(tasks):
        task = tasks.pop(index - 1)
        print(f"Task '{task}' removed from your to-do list.")
    else:
        print("Invalid index. No task removed.")

def main():
    tasks = []
    while True:
        print("\nOptions:")
        print("1. Display tasks")
        print("2. Add a task")
        print("3. Remove a task")
        print("4. Exit")

        choice = input("Enter your choice (1/2/3/4): ")

        if choice == '1':
            display_tasks(tasks)
        elif choice == '2':
            add_task(tasks)
        elif choice == '3':
            remove_task(tasks)
        elif choice == '4':
            print("Exiting the to-do list.")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
