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
print(read_csv())


def write_csv(contact: List, mode_type) -> None:
    '''
    Запись в csv фаил. Этот же метод добавляет контакт. На дозвпись в файл mode_type = 'а', на перезапись файла = 'w'
    '''
    with open('data.csv', mode=mode_type, encoding='utf-8', newline='') as f:
        writer = csv.writer(f, delimiter=' ')
        writer.writerow(contact)

def write_csv_list(contact: List, mode_type) -> None:
    '''
    Запись в csv фаил. Этот же метод добавляет контакт. На дозвпись в файл mode_type = 'а', на перезапись файла = 'w'
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
#print(search_contact('Ник'))
#     text = ui.get_action('Введите значение для поиска: ')
#     line_output = []
#     for line in lst_input:
#         if text in line:
#             line_output.append(line)
#     return line_output


# def write_json():
#     data = []
#     text = ui.get_action('Фамилия Имя: ')
#     data.append(f'Фамилия Имя: {text}')
#     text = ui.get_action('Номер телефона: ')
#     data.append(text)
#     text = ui.get_action('Комментари: ')
#     data.append(text)
#     with open('data.json', 'w') as fp:
#         json.dump(data, fp, separators=('\n',' '), indent=4)
         
        



def edit_contact(searchstring: str, new_contact: List) -> None:
    '''
    Редактирование контакта. На вход метод принимает поисковую строку для контакта и измененную строку. 
    После перезаписываем файл с новыми измененниям
    '''
    contact_list = read_csv()
    for contact in contact_list:
        if searchstring in contact:
            index = contact_list.index(contact)
            contact_list.remove(contact_list[index])
            contact_list.append(new_contact)
    write_csv_list(contact_list, 'w')


def delete_contact(searchstring: str) -> None:
    '''
    Ищем контакт и удаляем его из списка. Перезаписываем файл
    '''
    contact_list = read_csv()
    for contact in contact_list:
        if searchstring in contact:
            contact_list.remove(contact)
    write_csv_list(contact_list, 'w')
    


def write_json(contact: List)->None:
    '''
    Вызвать метод для первой записи в файле
    '''
    with open('data.json', 'w', encoding='utf-8') as rf:
        json.dump(contact, rf, ensure_ascii=False)


def add_contact_json(contact: List)->None:
    '''
    Добавление новых контактов после записи первого
    '''
    data = read_json()
    data.append(contact)
    write_json(data)


def read_json()->List:
    '''
    Чтение с json
    '''
    with open('data.json', 'r', encoding='utf-8') as rf:
        data = json.load(rf)
    return data


# contact = ['Максим Иванов 5677 друг']
# add_contact_json(contact)

# read_json()

