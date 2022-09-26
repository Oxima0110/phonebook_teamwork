
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
    lst = []
    text = ui.get_action('Фамилия Имя: ')
    lst.append(text)
    text = ui.get_action('Номер телефона: ')
    lst.append(text)
    text = ui.get_action('Комментари: ')
    lst.append(text)
    with open ('data.csv', mode = 'a', encoding='utf-8') as w_file:
        file_writer = csv.writer(w_file, delimiter='\n', lineterminator='\r')
        file_writer.writerow(lst)

def write_txt():
    '''
    Запись в txt фаил
    '''
    lst = []
    text = ui.get_action('Фамилия Имя: ')
    lst.append(text)
    text = ui.get_action('Номер телефона: ')
    lst.append(text)
    text = ui.get_action('Комментари: ')
    lst.append(text)
    with open('data.txt', "a", encoding='utf-8') as file:
        for  line in lst:
            file.write(line + ' ')
        file.write('\n')


def read_txt():
    with open('data.txt', 'r', encoding='utf-8') as file:
        file_reader_1 = file.readlines()
        file_reader = []
        for line in file_reader_1:
            line = line[:-2]
            file_reader.append(line)
    return file_reader

def search(lst_input: list)-> list:
    '''
    Поиск в телефонной книге
    '''
    text = ui.get_action('Введите значение для поиска: ')
    line_output = []
    for line in lst_input:
        if text in line:
            line_output.append(line)
    return line_output