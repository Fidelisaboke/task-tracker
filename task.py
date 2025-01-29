from datetime import datetime

class Task:
    def __init__(self, id: int, description: str, status):
        current_datetime = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        self.id = id
        self.description = description
        self.status = status
        self.created_at = current_datetime
        self.updated_at = current_datetime


task = Task(1, "A task", "to-do")
print(vars(task))
