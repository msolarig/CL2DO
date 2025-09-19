import os
from datetime import date
from task import *
from storage import *

run = True

while run == True:
    'main application loop'
    
    os.system('clear')
    
    print(f'Command Line 2do List                 {date.today()}\n')
    
    tasks = load_file()
    for task in tasks:
        print(str(task).capitalize())
        
    print('________________________________________________')
    
    user_input = input(': ')
    parts = user_input.strip().split(' ', 1)
    command = parts[0].lower()
    arg = parts[1] if len(parts) > 1 else ''

    if command == 'add' and arg:  
            add(Task(arg))
    
    if command == 'rem' and arg:    
            rem(Task(arg))
        
    if command == 'check' and arg:    
            check(Task(arg))
    
    if command == 'uncheck' and arg:   
            uncheck(Task(arg))
        
    if command == 'q':
        os.system('clear')
        run = False