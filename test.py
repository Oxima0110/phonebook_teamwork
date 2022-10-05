
dictionary = {'Пользователь': 'человек',
              'Время заведения задачи': '20.10.22',
              'Дата выполнения задачи': '25.10.22',
              'Задача': 'проснуться'}
strings = []
for key,item in dictionary.items():
    strings.append("{}".format(item))
result = " ".join(strings)
print(result)

dictionary = {'Пользователь': 'человек',
              'Время заведения задачи': '20.10.22',
              'Дата выполнения задачи': '25.10.22',
              'Задача': 'проснуться'}
strings = []
for key,item in dictionary.items():
    strings.append("{}: {}\n".format(key.capitalize(), item))
result = " ".join(strings)
print(result)

