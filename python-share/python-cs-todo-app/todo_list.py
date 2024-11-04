# todo_list.py
from datetime import date

class Task:
    def __init__(self, title, description, due_date, status="Not Started"):
        self.title = title
        self.description = description
        self.due_date = due_date
        self.status = status

    def __repr__(self):
        return f"Task({self.title}, {self.status}, {self.due_date})"


class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        pass

    def remove_task(self, title):
        pass

    def update_task(self, title, new_title=None, new_description=None, new_due_date=None, new_status=None):
        pass

    def list_tasks(self, status=None):
        pass
