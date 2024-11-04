# test_todo_list.py
import pytest
from todo_list import Task, ToDoList
from datetime import date

def test_add_task():
    todo_list = ToDoList()
    task = Task("Write Report", "Write the monthly report", date(2023, 10, 1))
    assert todo_list.add_task(task) == True
    assert len(todo_list.tasks) == 1
    assert todo_list.tasks[0] == task

def test_prevent_duplicate_addition():
    todo_list = ToDoList()
    task = Task("Write Report", "Write the monthly report", date(2023, 10, 1))
    todo_list.add_task(task)
    assert todo_list.add_task(task) == False  # Duplicate task title

def test_remove_task():
    todo_list = ToDoList()
    task = Task("Write Report", "Write the monthly report", date(2023, 10, 1))
    todo_list.add_task(task)
    assert todo_list.remove_task("Write Report") == True
    assert len(todo_list.tasks) == 0

def test_remove_nonexistent_task():
    todo_list = ToDoList()
    assert todo_list.remove_task("Nonexistent Task") == False  # Task is not in the list

def test_update_task():
    todo_list = ToDoList()
    task = Task("Write Report", "Write the monthly report", date(2023, 10, 1))
    todo_list.add_task(task)
    assert todo_list.update_task("Write Report", new_status="In Progress") == True
    assert task.status == "In Progress"

def test_list_tasks_no_filter():
    todo_list = ToDoList()
    todo_list.add_task(Task("Write Report", "Write the monthly report", date(2023, 10, 1)))
    todo_list.add_task(Task("Prepare Presentation", "Prepare slides for the meeting", date(2023, 10, 2)))
    assert len(todo_list.list_tasks()) == 2

def test_list_tasks_with_filter():
    todo_list = ToDoList()
    task1 = Task("Write Report", "Write the monthly report", date(2023, 10, 1), status="Not Started")
    task2 = Task("Prepare Presentation", "Prepare slides", date(2023, 10, 2), status="Completed")
    todo_list.add_task(task1)
    todo_list.add_task(task2)
    
    not_started_tasks = todo_list.list_tasks(status="Not Started")
    completed_tasks = todo_list.list_tasks(status="Completed")
    
    assert len(not_started_tasks) == 1
    assert not_started_tasks[0] == task1
    assert len(completed_tasks) == 1
    assert completed_tasks[0] == task2
