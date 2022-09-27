# Сергей
import json
import csv
from typing import List


def read_csv():
    '''
    Чтение из файла csv
    '''
    with open('data.csv', encoding='utf-8') as file:
        reader = csv.reader(file, delimiter=' ')
        contact_list = []
        for line in reader:
            line = ' '.join(line)
            contact_list.append(line)
        return contact_list


def write_csv(contact: List, mode_type) -> None:
    '''
    Запись в csv фаил. Добавляем контакт. На дозвпись в файл mode_type = 'а', на перезапись файла = 'w'
    '''
    with open('data.csv', mode=mode_type, encoding='utf-8', newline='') as f:
        writer = csv.writer(f, delimiter=' ')
        writer.writerow(contact)


def search_contact(searchstring: str) -> list:
    '''
    Поиск в телефонной книге
    '''
    contact_list = read_csv()
    searched_contact = []
    for contact in contact_list:
        if searchstring in contact:
            searched_contact.append(contact)
    return searched_contact


def edit_contact(searchstring: str, change_value: str) -> None:
    '''
    Редактирование контакта. На вход метод принимает поисковую строку для контакта и измененную строку. 
    После перезаписываем файл с новыми измененниям
    '''
    contact_list = read_csv()
    for contact in contact_list:
        if searchstring in contact:
            index = contact_list.index(contact)
            contact_list[index] = change_value
    write_csv(contact_list, 'w')


def delete_contact(searchstring: str) -> None:
    '''
    Ищем контакт и удаляем его из списка. Перезаписываем файл
    '''
    contact_list = read_csv()
    for contact in contact_list:
        if searchstring in contact:
            contact_list.remove(contact)
    write_csv(contact_list, 'w')


# def write_json(list: list):
#     with open('data.json', 'w') as fp:
#         json.dump(list, fp, separators=('\n', ' '), indent=4)
