import os
from datetime import date
from task import *
from storage import *

def clear_terminal():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

run = True
while run == True:
    'main application loop'

    clear_terminal()

    print(f'Command Line 2do List                 {date.today()}\n')

    tasks = load_file()
    id = 0
    for task in tasks:
        id += 1
        print(f'{id}. {str(task).capitalize()}')
    print('――――――――――――――――――――――――――――――――――――――――――――――――')

    user_input = input(': ')
    parts = user_input.strip().split(' ', 1)
    command = parts[0].lower()
    arg = parts[1] if len(parts) > 1 else ''

    if command == 'add' and arg:
        add(Task(arg))
    elif command == 'rem' and arg:
        rem(Task(arg))
    elif command == 'remall':
        rem_all()
    elif command == 'check' and arg:
        check(Task(arg))
    elif command == 'checkall':
        check_all()
    elif command == 'uncheck' and arg:
        uncheck(Task(arg))
    elif command == 'uncheckall':
        uncheck_all()
    elif command == 'q':
        clear_terminal()
        run = False
