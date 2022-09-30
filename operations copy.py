import json
import csv

from typing import List

global contact_list
contact_list = []


def add_contact(contact: List) -> None:
    '''
    Запись в csv фаил. Этот же метод добавляет контакт. На дозвпись в файл mode_type = 'а', на перезапись файла = 'w'
    '''
    contact_list.append(contact)


#add_contact('sdsd,sdsd,dsd,dsd')


def search_contact(searchstring: str) -> list:
    '''
    Поиск в телефонной книге
    '''
    searched_contact = []
    for contact in contact_list:
        if searchstring in contact:
           print(contact)

list_l = [(1 ,['asdd','dsd','sdsd','sdsd'])]  


def select_contact(choice, searched_contacts):
    for search_contact in searched_contacts:
        if choice == searched_contacts[0]:
            return search_contact    
#print(select_contact(1, list_l))

def delete_contact(contact: str) -> None:
    '''
    Ищем контакт и удаляем его из списка. Перезаписываем файл
    '''
    contact_list.remove(contact)


def edit_contact(index, value) -> None:
    '''
    Редактирование контакта. На вход метод принимает поисковую строку для контакта и измененную строку. 
    После перезаписываем файл с новыми измененниям
    '''
    contact_list[index] = value


# add_contact('sdsd,sdsd,dsd,dsd')


def read_csv():
    '''
    Чтение из файла csv
    '''

    with open('data.csv', encoding='utf-8') as f:
        reader = csv.reader(f, delimiter=',')
        for line in reader:
            #line = ', '.join(line)
            contact_list.append(line)
       

# print(read_csv())


def write_csv() -> None:
    '''
    Запись в csv фаил. Этот же метод добавляет контакт. На дозвпись в файл mode_type = 'а', на перезапись файла = 'w'
    '''
    with open('data.csv', 'w', encoding='utf-8') as f:
        writer = csv.writer(f, lineterminator='\r')
        for contact in contact_list:
            writer.writerow(contact)
# phone_book_write_csv(phone_book)

    # actual_contact_list =[]
    # for contact in contact_list:
    #     actual_contact_list.append(contact[2])
    # actual_contact_list.append(line)


#contact = 'dfdfd,dfdf,dfdf'
# print(add_contact_csv(contact))


# contact_list = read_csv()
# # print(len(contact_list))
# print(range(1, len(contact_list))+1)



#print(select_contact('2', contact_list))


def write_json() -> None:
    '''
    Вызвать метод для первой записи в файле
    '''
    
    with open('data.json', 'w', encoding='utf-8', newline='') as rf:
        json.dump(contact_list, rf, ensure_ascii=False, indent=2)


print(contact_list)
