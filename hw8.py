import os

contacts_file = r'C:\Users\DNS\Desktop\GeekBrains\Seminar\Python\hw_8\contacts_first.txt'
contacts_file_second = r'C:\Users\DNS\Desktop\GeekBrains\Seminar\Python\hw_8\contacts_second.txt'
def append_contact(contacts_file):
    contact = input('Введите контакт в формате Ф И О Телефон:')
    with open(contacts_file, 'a', encoding="utf-8") as f:
        f.write(f'\n{contact}')
        print ('Контакт добавлен')

def read_file(contacts_file):
    with open(contacts_file, 'r', encoding="utf-8") as f:
        print (f.read()) 

def search_contact(contacts_file):
    search_by = input("Введите информацию для поиска (фамилия, имя или отчество):")
    with open(contacts_file, 'r', encoding="utf-8") as f:
        for line in f:
            if search_by in line:
                print(line)

def del_contact(contacts_file):
    search_by = input("Введите информацию для удаления (фамилия, имя или отчество):")
    with open(contacts_file, 'r', encoding="utf-8") as f:
        for line in f:
            line_=line
            if search_by not in line:        
                with open(contacts_file_second, 'a', encoding="utf-8") as file:
                    file.write(f'{line_}')
    with open(contacts_file, 'w', encoding="utf-8") as f1:
        clear=['']
        f1.writelines(clear)
    with open(contacts_file_second, 'r', encoding="utf-8") as file_1:
        for line in file_1:
            line_=line
            with open(contacts_file, 'a', encoding="utf-8") as f:
                    f.write(f'{line_}')
    with open(contacts_file_second, 'w', encoding="utf-8") as f1:
        clear=['']
        f1.writelines(clear)

def change_contact(contacts_file):
    search_by = input("Введите информацию для изменения (фамилия, имя или отчество):")
    with open(contacts_file, 'r', encoding="utf-8") as f:
        for line in f:
            line_=line
            if search_by not in line:        
                with open(contacts_file_second, 'a', encoding="utf-8") as file:
                    file.write(f'{line_}')
            elif search_by in line:
                change=input('write ФИО + номер')        
                with open(contacts_file_second, 'a', encoding="utf-8") as file:
                    file.write(f'{change}\n')
    with open(contacts_file, 'w', encoding="utf-8") as f1:
        clear=['']
        f1.writelines(clear)
    with open(contacts_file_second, 'r', encoding="utf-8") as file_1:
        for line in file_1:
            line_=line
            with open(contacts_file, 'a', encoding="utf-8") as f:
                    f.write(f'{line_}')
    with open(contacts_file_second, 'w', encoding="utf-8") as f1:
        clear=['']
        f1.writelines(clear)

def user_action():
    print ('Добро пожаловать!\n 1) Вывести весь справочник\n 2) Добавить контакт\n 3)Найти контакт\n 4)Удалить контакт\n 5)Изменить контакт')
    while (input1:= int(input('Выберите действие со справочником (0 = выход):'))) != 0:
        if input1 == 1:
            read_file(contacts_file)
        elif input1 == 2:
            append_contact(contacts_file)
        elif input1 == 3:
            search_contact(contacts_file)
        elif input1 == 4:
            del_contact(contacts_file)
        elif input1 == 5:
            change_contact(contacts_file)
        else:
            print("Некорректный ввод")
user_action()
