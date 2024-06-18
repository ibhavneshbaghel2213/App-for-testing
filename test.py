import pytest
from app import TodoList

def test_add_task():
    todo_list = TodoList()
    task = "Buy milk"
    print(task)
    result = todo_list.add_task(task)
    assert result == task
    assert task in todo_list.view_tasks()
    

def test_view_tasks():
    todo_list = TodoList()
    tasks = ["Buy milk", "Read book"]
    for task in tasks:
        todo_list.add_task(task)
    assert todo_list.view_tasks() == tasks

def test_delete_task():
    todo_list = TodoList()
    task = "Buy milk"
    todo_list.add_task(task)
    result = todo_list.delete_task(task)
    assert result == task
    assert task not in todo_list.view_tasks()

def test_delete_nonexistent_task():
    todo_list = TodoList()
    task = "Buy milk"
    result = todo_list.delete_task(task)
    assert result is None

