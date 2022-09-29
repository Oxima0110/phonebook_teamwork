# Сергей
import json
import csv
from typing import List


def read_csv():
    '''
    Чтение из файла csv
    '''
    contact_list = []
    with open('data.csv', encoding='utf-8') as f:
        reader = csv.reader(f)
        for line in reader:
            line = ''.join(line)
            contact_list.append(line)
        return contact_list


def phone_book_write_csv(phone_book: List) -> None:
    '''
    Запись в csv фаил. Этот же метод добавляет контакт. На дозвпись в файл mode_type = 'а', на перезапись файла = 'w'
    '''
    with open('data.csv', 'w', encoding='utf-8', newline='') as f:
        writer = csv.writer(f, delimiter='\n')
        writer.writerow(phone_book)


def add_contact_csv(contact: List) -> None:
    '''
    Запись в csv фаил. Этот же метод добавляет контакт. На дозвпись в файл mode_type = 'а', на перезапись файла = 'w'
    '''
    with open('data.csv', 'a', encoding='utf-8', newline='') as f:
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


def edit_contact(searchstring: str, new_contact: List) -> None:
    '''
    Редактирование контакта. На вход метод принимает поисковую строку для контакта и измененную строку. 
    После перезаписываем файл с новыми измененниям
    '''
    delete_contact(searchstring)
    add_contact_csv(new_contact)


def delete_contact(searchstring: str) -> None:
    '''
    Ищем контакт и удаляем его из списка. Перезаписываем файл
    '''
    contact_list = read_csv()
    for contact in contact_list:
        if searchstring in contact:
            contact_list.remove(contact)
    phone_book_write_csv(contact_list)


def write_json() -> None:
    '''
    Вызвать метод для первой записи в файле
    '''
    phone_book = read_csv()
    with open('data.json', 'w', encoding='utf-8', newline='') as rf:
        json.dump(phone_book, rf, ensure_ascii=False, indent=2)
