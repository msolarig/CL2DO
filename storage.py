import os

TASK_FILE = os.path.join(os.path.dirname(__file__), 'task_file.txt')

def load_file():
    'reads tasks file'
    from task import Task
    tasks = []
    with open(TASK_FILE, 'r') as task_file:
        for task in task_file:
            task = task.rstrip('\n')
            done = True if task[:3] == '[X]' else False
            tasks.append(Task(task[4:], done))
    return tasks

def save_file(tasks):
    'writes to tasks file'
    with open(TASK_FILE, 'w') as task_file:
        for task in tasks:
            task_file.write(str(task) + '\n')