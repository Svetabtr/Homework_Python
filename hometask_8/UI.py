import modul_work as work
import view as view

work.clear_screen()

def menu ():
    while True:
        menu_item = int(input( 
               '----------\n'
               'Выберите действие:\n\n'
               '(1) Просмотреть все данные\n'
               '(2) Добавить запись\n'
               '(3) Удалить запись\n'
               '(4) Редактировать запись\n'
               '(5) Поиск\n'
               '(6) Выход из приложения\n'
               '----- \n'))

        if menu_item == 1:
            print('\nСписок учеников\n')
            view.print_data()

        elif menu_item == 2:
            print('\nЗаполните данные об ученике\n')
            name = input("Фамилия, Имя: ")
            date_birth = input("Дата рождения: ")
            sch_class = input("№ класса: ")
            mid_ball = input("Средний балл: ")
            data = work.add_contact(name, date_birth, sch_class, mid_ball)
            print('\nДанные добавлены')
            work.recording_file(data)

        elif menu_item == 3:
            num = int(input('\nУкажите id для удаления: '))

            work.dell_contact(num)
            print('\nДанные удалены')
            
            
        elif menu_item == 4:
            num = int(input('\nУкажите id для редактирования: '))
            finder = int(input('\nВыберите параметр для редактирования: \n'
                ' -1-  Фамилия, Имя\n'
                ' -2-  Дата рождения\n'
                ' -3-  Класс\n'
                ' -4-  Средний балл'
                ' > '))
            if finder == 1:
                name = input('Новое значение: Фамилия, Имя: ')
                data = work.edit_contact(num,name, 0, 0, 0)
                # view.view_resultat(res)
            if finder == 2:
                date_birth = input('Новое значение: Дата рождения: ')
                data = work.edit_contact(num, 0, date_birth, 0, 0)
                # view.view_resultat(res)
            if finder == 3:
                sch_class = input('Новое значение: Класс: ')
                data = work.edit_contact(num, 0, 0, sch_class, 0)
            if finder == 4:
                mid_ball = input('Новое значение: Средний балл: ')
                data = work.edit_contact(num, 0, 0, 0, mid_ball)
            print('\nДанные изменены')
            work.recording_file(data)

        elif menu_item == 5:
            finder = int(input('\nВыберите параметр поиска: \n'
                ' -1-  Фамилия, Имя\n'
                ' -2-  Дата рождения\n'
                ' -3-  Класс\n'
                ' > '))
            if finder == 1:
                name = input('Поиск: Фамилия, Имя: ')
                res = work.find_contact(name, 0, 0)
                view.view_resultat(res)
            if finder == 2:
                date_birth = input('Поиск: Дата рождения: ')
                res = work.find_contact(0, date_birth, 0)
                view.view_resultat(res)
            if finder == 3:
                sch_class = input('Поиск: Класс: ')
                res = work.find_contact(0, 0, sch_class)
                view.view_resultat(res)
        elif menu_item == 6:
            break
        else:
            print('\nВыберите команду из списка')
            