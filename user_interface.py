#Саша
import check as ch
from colorama import Fore, Back, Style

def greetings_user():
    '''
    Приветсвует пользователя
    '''
    print(f'{Fore.YELLOW + Style.BRIGHT}Добро пожаловать в телефонную записную книжку 📙 {Style.RESET_ALL}')
    
def farewell_user():
    '''
    Прощание с пользователем
    '''
    print(f'{Fore.YELLOW + Style.BRIGHT}До новых встреч 👋{Style.RESET_ALL}')


def view_all_contact(lst_input: list) -> str: #показать телефонную книгу
    '''
    Вывод информации пользователю
    '''
    print(f'\n{Fore.YELLOW + Style.BRIGHT}      <Ваши контакты> ↓ ')
    for line in lst_input:
        print(line)


def get_contact(): #добавить контакт
    print(f'{Fore.YELLOW + Style.BRIGHT}Введите данные о контакте ↓ {Style.RESET_ALL}')
=======
def add_contact(): #добавить контакт

    contact = []
    print(Fore.CYAN + Style.BRIGHT)
    text = get_action(f'-> Имя: {Fore.LIGHTGREEN_EX + Style.BRIGHT}')
    text = text.capitalize()
    contact.append(text)
    text = get_action(f'{Fore.CYAN + Style.BRIGHT}-> Фамилия: {Fore.LIGHTGREEN_EX + Style.BRIGHT}')
    text = text.capitalize()
    contact.append(text)
    text = get_action(f'{Fore.CYAN + Style.BRIGHT}-> Номер телефона: {Fore.LIGHTGREEN_EX + Style.BRIGHT}')
    contact.append(text)
    text = get_action(f'{Fore.CYAN + Style.BRIGHT}-> Комментарий: {Fore.LIGHTGREEN_EX + Style.BRIGHT}')
    text = text.capitalize()
    contact.append(text)
    print(f'\n{Fore.GREEN}✅ Контакт успешно добавлен {Style.RESET_ALL}')
    print(Style.RESET_ALL)
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
    print('\n'
      f'{Fore.YELLOW + Style.BRIGHT}Выберите нужное действие: ↓{Style.RESET_ALL}\n'
      f'{Style.RESET_ALL + Fore.CYAN + Style.BRIGHT}' 
      ' 1 -📲 <добавление записи в телефонную книгу> \n'
      ' 2 -🔎 <поиск записи в телефонной книге> \n'
      ' 3 -👀 <просмотр телефонной книги> \n'
      ' 4 -✍  <запись в json> \n'
      ' 5 -👋 <выход> \n'
      f' ➡ : {Fore.LIGHTGREEN_EX + Style.BRIGHT}')
    print(Style.RESET_ALL)
    
      
# def search_contact_user():
#     print(get_action(f'{Fore.YELLOW + Style.BRIGHT}Введите значение для поиска ->: {Fore.LIGHTGREEN_EX + Style.BRIGHT}'))
#     print(Style.RESET_ALL) 

