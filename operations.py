#Сергей
import json
import csv
import user_interface as ui


def read_csv():
    '''
    Чтение из файла csv
    '''
    with open('data.csv', encoding='utf-8') as r_file:
        file_reader_1 = csv.reader(r_file, delimiter=' ')
        file_reader = []
        for line in file_reader_1:
            line = ' '.join(line)
            file_reader.append(line)
        return file_reader


def write_csv():
    '''
    Запись в csv фаил
    '''
    contact = ui.get_contact()
    with open('data.csv', mode='a', encoding='utf-8') as w_file:
        file_writer = csv.writer(w_file, delimiter=' ', lineterminator='\r')
        file_writer.writerow(contact)


def search(lst_input: list) -> list:
    '''
    Поиск в телефонной книге
    '''
    text = ui.get_action('Введите значение для поиска: ')
    line_output = []
    for line in lst_input:
        if text in line:
            line_output.append(line)
    return line_output


def write_json(list:list):
    with open('data.json', 'w') as fp:
        json.dump(list, fp, separators=('\n',' '), indent=4)
        
