import csv
import string
from typing import List



def read_csv():
    '''
    Чтение из файла csv
    '''
    with open('todo.csv','r', encoding='utf-8') as f:
        tasks = [{key: value  for key, value in task.items()}
                for task in csv.DictReader(f, skipinitialspace=True)]
    return tasks

def search_task(searchstring: str, tasks:List):
    '''
    Поиск в телефонной книге
    '''
    for task in tasks:
        for value in task.values():
            if searchstring in value:
                   searched_tasks.append(task)
    return searched_tasks 

def filter_task(searchstring_1: str, tasks:List):
    '''
    Поиск в телефонной книге
    '''
    for task in tasks:
        for value in task.values():
            if searchstring_1 in value:
                   filter_tasks.append(task)
    return filter_tasks 

searched_tasks = []
filter_tasks = []
tasks = read_csv()
print(tasks)
searchstring_1 = 'Оксана'
searchstring = 'гулять'
tasks_1 = filter_task(searchstring_1, tasks)
print(tasks_1)
searched_tasks = search_task(searchstring, tasks_1)
print(searched_tasks)



