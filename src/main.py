from task_manager import TaskManager

def main():
    manager = TaskManager()

    while True:
        print("\n===== TASK MANAGER =====")
        print("\t1. Show all tasks")
        print("\t2. Add task")
        print("\t3. Mark task as done")
        print("\t4. Delete task")
        print("\t5. Exit")
        
        choice = input("-- Choose an option: --")
        if choice == "1":
            manager.show_all_tasks()

        elif choice == "2":
            title = input("-- Enter task title: --")
            category = input("-- Enter category: --")
            priority = input("-- Enter priority (low/medium/high): --")
            manager.add_task(title, category, priority)

        elif choice == "3":
            try:
                task_id = int(input("--Enter task ID to mark as done: --"))
                manager.mark_task_done(task_id)
            except ValueError:
                print("--Please enter a valid number.--")

        elif choice == "4":
            try:
                task_id = int(input("--Enter task ID to delete: --"))
                manager.delete_task(task_id)
            except ValueError:
                print("--Please enter a valid number.--")

        elif choice == "5":
            print("--Goodbye!--")
            break

        else:
            print("--Invalid option. Try again.--")


if __name__ == "__main__":
    main()

