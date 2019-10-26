# Main menu
import quiz, os_name


while True:
    print('*' * 30)
    print(' 1. создать папку ')
    print(' 2. удалить (файл/папку)')
    print(' 3. копировать (файл/папку)')
    print(' 4. просмотр содержимого рабочей директории')
    print(' 5. посмотреть только папки')
    print(' 6. посмотреть только файлы')
    print(' 7. просмотр информации об операционной системе')
    print(' 8. создатель программы')
    print(' 9. играть в викторину')
    print('10. мой банковский счет')
    print('11. смена рабочей директории')
    print('12. выход ')
    print('*' * 30)

    choice = input('Выберите пункт меню ')
    if choice == '1':
        pass
    elif choice == '2':
        pass
    elif choice == '3':
        pass
    elif choice == '4':
        pass
    elif choice == '5':
        pass
    elif choice == '6':
        pass
    elif choice == '7':
        print(os_name.my_os())
    elif choice == '8':
        pass
    elif choice == '9':
        print(quiz.quiz())
    elif choice == '10':
        pass
    elif choice == '11':
        pass
    elif choice == '12':
        break
    else:
        print('Неверный пункт меню')