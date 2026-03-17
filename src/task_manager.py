import json
import os
from tasks import Task

class TaskManager:

    def __init__(self, filename="data/tasks.json"):
        self.filename = filename
        self.tasks = []
        self.load_tasks()

    def add_task(self, title, category="general", priority="medium", completed=False):
        if not self.tasks:
            new_id = 1
        else:
            new_id = max(task.task_id for task in self.tasks) + 1

        new_task = Task(new_id, title, category, priority, completed)
        self.tasks.append(new_task)
        self.save_tasks()
        print("--Task was added successfully--")

    def show_all_tasks(self):
        print("\n---- TASKS LIST ----")
        if not self.tasks:
            print("--No tasks found--")
        else:
            for task in self.tasks:
                task.show_info()
                print("-" * 30)

    def mark_task_done(self, task_id):
        for task in self.tasks:
            if task.task_id == task_id:
                task.completed = True
                self.save_tasks()
                print("--You`ve done this task!--")
                return
        print("--Task ID was not found--")

    def delete_task(self, task_id):
        for task in self.tasks:
            if task.task_id == task_id:
                self.tasks.remove(task)
                self.save_tasks()
                print("--Task was deleted successfully--")
                return
        print("--Task ID was not found--")

    def save_tasks(self):
        tasks_data = [task.to_dict() for task in self.tasks]

        os.makedirs(os.path.dirname(self.filename), exist_ok=True)

        with open(self.filename, "w", encoding="utf-8") as file:
            json.dump(tasks_data, file, indent=4, ensure_ascii=False)

    def load_tasks(self):
        if not os.path.exists(self.filename):
            return

        with open(self.filename, "r", encoding="utf-8") as file:
            tasks_data = json.load(file)

        self.tasks = []
        for task_data in tasks_data:
            task = Task(
                task_id=task_data["task_id"],
                title=task_data["title"],
                category=task_data["category"],
                priority=task_data["priority"],
                completed=task_data["completed"]
            )
            self.tasks.append(task)