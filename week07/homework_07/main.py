"""
Модуль для запуска консольного файлового менеджера
"""
import filemanager
from bill import run_bill
from victory import run_victory
from all_functions import separator
import os
from os import walk


# Названия пунктов меню
COPY_FILE_FOLDER = 'Копировать (файл/папку)'
SHOW_FILES = 'Просмотр содержимого рабочей директории'
SAVE_NAMES = 'Сохранить содержимое рабочей директории в файл'
AUTHOR = 'Создатель программы'
VICTORY = 'Играть в викторину'
BILL = 'Мой банковский счет'
EXIT = 'Выход'

# Набор пунктов меню
menu_items = (
    COPY_FILE_FOLDER,
    SHOW_FILES,
    SAVE_NAMES,
    AUTHOR,
    VICTORY,
    BILL,
    EXIT
)


def copy_file_or_folder():
    """
    Копирование файла или папки
    :return:
    """
    # спрашиваем имя и новое имя
    name = input('Введите имя файла')
    new_name = input('Введите имя копиии')
    # копируем
    filemanager.copy_file_or_directory(name, new_name)


def print_author():
    """
    Функция печати информации об авторе
    :return:
    """
    # получаем информацию
    author = filemanager.author_info()
    # печатаем
    print(author)


def print_files():
    """
    Функция печати файлов/папок в рабочей папке
    :return: None
    """
    # Получаем файлы
    files = filemanager.filenames()
    # Выводим
    print(f'В текущей директории {os.getcwd()} находятся: ')
    for item in files:
        print(item)


def save_names_to_file():
    """
    создать файл listdir.txt (если он есть то пересоздать) и сохранить туда
    содержимое рабочей директории следующим образом: сначала все файлы, потом
    все папки
    :return:
    """
    files_list = []
    for (dirpath, dirnames, filenames) in walk(os.getcwd()):
        files_list.extend(filenames)
        break
    files_str = 'files: '
    for i in range(len(files_list)):
        files_str += files_list[i]
        if i < len(files_list) - 1:
            files_str += ', '

    dirs_list = []
    for (dirpath, dirnames, filenames) in walk(os.getcwd()):
        dirs_list.extend(dirnames)
        break
    dirs_str = 'dirs: '
    for i in range(len(dirs_list)):
        dirs_str += dirs_list[i]
        if i < len(dirs_list) - 1:
            dirs_str += ', '

    with open('listdir.txt', 'w') as f:
        f.write(f'{files_str}\n')
        f.write(f'{dirs_str}\n')


# Словарь действия связывает название пункта меню с той функцией которую нужно выполнить
actions = {
    COPY_FILE_FOLDER: copy_file_or_folder,
    SHOW_FILES: print_files,
    SAVE_NAMES: save_names_to_file,
    AUTHOR: print_author,
    VICTORY: run_victory,
    BILL: run_bill,
    EXIT: filemanager.quit
}


def print_menu():
    """
    Функция вывода меню
    :return: None
    """
    print(separator())
    # Выводим названи пункта меню и цифру начиная с 1
    for number, item in enumerate(menu_items, 1):
        print(f'{number}) {item}')
    print(separator())


def is_correct_choice(choice):
    """
    Функция проверяет что выбран корректный пункт меню
    :param choice: выбор
    :return: True/False
    """
    return choice.isdigit() and int(choice) > 0 and int(choice) <= len(menu_items)


if __name__ == '__main__':
    # цикл основной программы
    while True:
        # рисуем меню
        print_menu()
        # пользователь выбирает цифру
        choice = input('Выберите пункт меню ')
        # проверяем что это корректный выбор
        if is_correct_choice(choice):
            # получаем назвнание пункта меню по номеру
            # choice - 1, т.к. в меню пункты выводятся с 1 а в картеже хранятся с 0
            choice_name = menu_items[int(choice) - 1]
            # получаем действие в зависимости от пунктам меню
            action = actions[choice_name]
            # вызываем функцию
            action()
        else:
            print('Неверный пункт меню')
