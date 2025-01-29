from datetime import datetime

class Task:
    def __init__(self, id: int, description: str):
        current_datetime = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        self.id = id
        self.description = description
        self.status = "to-do"
        self.created_at = current_datetime
        self.updated_at = current_datetime

