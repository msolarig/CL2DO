from storage import *

class Task:

    def __init__(self, task, done = False):
        self.task = task.lower()
        self.done = done

    def __str__(self):
        if self.done == False:
            return f'[ ] {self.task.capitalize()}'
        else:
            return f'[X] {self.task.capitalize()}'

def add(task):
    'add a task to the list'
    tasks = load_file()
    tasks.append(task)
    save_file(tasks)
    return 

def rem(task):
    'remove a task from the list'
    tasks = load_file()
    for i in tasks:
        if i.task == task.task.lower():
            tasks.remove(i)
    save_file(tasks)
    return 

def check(task):
    'mark a task as completed'
    tasks = load_file()
    for i in tasks:
        if i.task == task.task.lower():
            i.done = True
    save_file(tasks)
    return 

def uncheck(task):
    'mark a task as incomplete'
    tasks = load_file()
    for i in tasks:
        if i.task == task.task.lower():
            i.done = False 
    save_file(tasks)
    return 
