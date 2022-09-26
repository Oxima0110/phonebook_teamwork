def view_data(lst_input:list)->str:
    '''
    Вывод информации пользователю
    '''
    for line in lst_input:
        print(line)

def get_action(input_string: str)-> str:
    '''
    Ввод информации от пользователя
    '''
    return input(input_string)