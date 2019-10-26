# Main menu
import os
import shutil
from os import path
import os_name
import quiz
from bank_account import personal_account

while True:
    print('*' * 30)
    print(' 1. создать папку ')
    print(' 2. удалить папку')
    print(' 3. копировать файл')
    print(' 4. просмотр содержимого рабочей директории')
    print(' 5. посмотреть только папки')
    print(' 6. посмотреть только файлы')
    print(' 7. просмотр информации об операционной системе')
    print(' 8. создатель программы')
    print(' 9. играть в викторину')
    print('10. мой банковский счет')
    print('11. выход ')
    print('*' * 30)

    choice = input('Выберите пункт меню ')
    if choice == '1':
        folder_name = input('Дайте имя папки - ')
        if not path.exists(folder_name):
            os.mkdir(folder_name)
    elif choice == '2':
        folder_name = input('Какую папку хотите удалить? ')
        os.rmdir(folder_name)
    elif choice == '3':
        folder_name = input('Какой файл хотите копировать? ')
        shutil.copy(folder_name, 'file_copy')
    elif choice == '4':
        pass
    elif choice == '5':
        pass
    elif choice == '6':
        pass
    elif choice == '7':
        print(os_name.my_os())
    elif choice == '8':
        print('Author is id2k1149@gmail.com')
    elif choice == '9':
        print(quiz.quiz())
    elif choice == '10':
        personal_account()
    elif choice == '11':
        break
    else:
        print('Неверный пункт меню')