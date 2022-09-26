import csv


def read_from_file(data):
    with open(data, 'r', encoding='UTF - 8') as file:
        for line in data:
             print(file.readline())   


        #return file.readline(data)

data = read_from_file('data.csv')
print(data)  

