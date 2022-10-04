from ast import Dict

import csv
import datetime
import re
import string

from typing import List
'''
глобальный список для записи контактов. 
'''
global tasks
tasks = [] 


def add_task(key:str, value:str) -> None:
    '''
    добавить в список контакт
    '''
    tasks[key] = value


def search_contact(searchstring: str, contacts:str) -> List:
    '''
    Поиск в телефонной книге
    '''
    for contact in contacts:
        if searchstring in contact:
            return contact


def select_contact(choice: str, searched_contacts: Dict) -> Dict:
    '''
    Выбрать элемент в найденных
    '''
    for key, value in searched_contacts.items():
        if choice == key:
            return key, value


def delete_contact(contact: str) -> None:
    '''
    Удалить контакт из списка 
    '''
    contact_list.remove(contact_list[contact])


def edit_contact(index, value) -> None:
    '''
    Редактирование контакта. 
    '''
    contact_list[index] = value

def view_tasks(tasks: List) -> string:
    '''
    Запись в строку для Telegram
    '''
    strings =[]
    for task in tasks:
        for key, value in task.items():
            strings.append('{}: {}'.format(key.capitalize(), value))
    result ='\n'.join(strings)        
    return result


def read_csv():
    '''
    Чтение из файла csv
    '''
    with open('todo.csv','r', encoding='utf-8') as f:
        tasks = [{key: value  for key, value in task.items()}
                for task in csv.DictReader(f, skipinitialspace=True)]
    return tasks
 
#print(read_csv())

def write_csv(tasks: List) -> None:
    '''
    Запись в csv фаил. 
    '''
    fieldnames = tasks[0].keys()
    with open('todo.csv', 'w', encoding='utf-8', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames,lineterminator='\n')
        writer.writeheader()
        writer.writerows(tasks)
        


print(tasks)
