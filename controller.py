import operations as o
import user_interface as ui



def button_click():
    while True:
        print('''Выберите нужное действие:
        1 - добавление записи в телефонную книгу
        2 - поиск записи в телефонной книге
        3 - просмотр телефонной книги
        4 - запись в json
        5 - выход
        ''')
        action = int(ui.get_action(':'))
        if action == 1:
            o.write_csv()
        elif action == 2:
            lst = o.read_csv()
            result = o.search(lst)
            ui.view_data(result)
        elif action == 3:
            result = o.read_csv()
            ui.view_data(result)
        elif action == 4:
            o.write_json()  
        else:
            break
           