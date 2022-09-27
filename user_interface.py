#Саша
import check as ch


def view_all_contact(lst_input: list) -> str: #показать телефонную книгу
    '''
    Вывод информации пользователю
    '''
    for line in lst_input:
        print(line)

def add_contact(): #добавить контакт
    contact = []
    text = ch.get_number_int(get_action('Фамилия: '))
    contact.append(text)
    text = get_action('Имя: ')
    contact.append(text)
    text = get_action('Номер телефона: ')
    contact.append(text)
    text = get_action('Комментарий: ')
    contact.append(text)
    return contact

def delete_contact(): 
    pass

def edit_contact():
        pass        

def search_contact():
    pass

def get_choice(input_string: str) -> str:
    '''
    Ввод выбора действия пользователя

    '''
    choise = ch.get_selection(input_string)
    return choise

def get_action(input_string: str) -> str:
    '''
    Ввод выбора действия пользователя

    '''
    return input(input_string)    


def show_menu():
    return 'Выберите нужное действие: \n1 - добавление записи в телефонную книгу: \n2 - поиск записи в телефонной книге: \n3 - просмотр телефонной книги: \n4 - запись в json: \n5 - выход: '


    
    
print(get_contact )    
    
