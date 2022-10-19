import os
import UI as user

with open('Book1.csv','r', encoding='utf-8') as f:
    dictionary = f.readlines()
f.close()


def clear_screen():
    os.system('cls')


def print_dictionary():
    with open('Book1.csv','r', encoding='utf-8') as f:
        dictionary = f.readlines()
    for line in dictionary:
        print(line.replace(';', '   ').replace('\n', ''))
    f.close()

def recording_file():
    with open('Book1.csv','r', encoding='utf-8') as f:
        dictionary = f.readlines()
    with open('Book1.csv', 'w', encoding='utf-8') as file:
        for line in dictionary:
            file.writelines(line)
    file.close()

def add_contact(surname, name, date_birth, company, tel_number):
    with open('Book1.csv','r', encoding='utf-8') as f:
        dictionary = f.readlines()
    f.close()
    count = 0
    for line in dictionary:
        count=int(line[0])
    res = 0
    new_line = []
    id = str(count+1) 
    
    new_line = [id, surname, name, date_birth, company, tel_number]
    res = ';'.join(new_line)+'\n'
    dictionary.append(res)
          
    print('-'*10)
    print('Данные добавлены в справочник\n')  
    print(res.replace(';', ' '))
    
    with open('Book1.csv', 'w', encoding='utf-8') as file:
        for line in dictionary:
            file.writelines(line)
    file.close()
    
def dell_contact(num_str):
    with open('Book1.csv','r', encoding='utf-8') as f:
        dictionary = f.readlines()
    with open('Book1.csv', 'w', encoding='utf-8') as file:        
        for line in dictionary:
            id = int(line[0])
            if id != num_str:
                file.writelines(line)
    file.close()
        