class Task :

    def __init__(self, task_id, title, category="general", priority="medium", completed=False):
        self.task_id = task_id
        self.title = title
        self.category = category
        self.priority = priority
        self.completed = completed

    def show_info(self):
        status = "Done" if self.completed else "Not done"
        print(f"{self.task_id}. {self.title} \nStatus: [{status}] | Category: {self.category} | Priority: {self.priority}")

    def to_dict(self):
        return {
            "task_id": self.task_id,
            "title": self.title,
            "completed": self.completed,
            "priority": self.priority,
            "category": self.category
        }