import program_work as prog

# dictionary = prog.open_file()

def menu ():
    menu_item = int(input( 
           '----------\n'
           'Выберите действие:\n\n'
           '(1) Просмотреть справочник\n'
           '(2) Добавить запись\n'
           '(3) Удалить запись\n'
           '(4) Выйти из приложения\n'
           '----- \n'))

    if menu_item == 1:
        print('----------------------\n'
              'Телефонный справочник\n'
              '----------------------\n')
        prog.print_dictionary()
        menu()

    elif menu_item == 2:
        print('----------\n'
              'Заполните данные справочника\n'
              '----------\n')
        surname = input("Фамилия: ")
        name = input("Имя: ")
        date_birth = input("Дата рождения: ")
        company = input("Место работы: ")
        tel_number = input("Телефон: ")
        prog.add_contact(surname, name, date_birth, company, tel_number)
        prog.recording_file()
        menu()

    elif menu_item == 3:
        item_choice = int (input('Хотите просмотреть справочник?\n'
            '(1) Да\n'
            '(2) Нет\n'
            '-----\n'))
        if item_choice == 1:
            prog.print_dictionary()
        
        num = int(input('----------\n'
                        'Укажите номер строки для удаления: '))
                      
        prog.dell_contact(num)
        print('----------')
        print(f'Строка {num} удалена из файла')
        prog.recording_file()
        menu()
    elif menu_item == 4:
        exit()
    else:
        print('Выберите команду из списка')
        menu()