import shutil
import os
import sys
from all_functions import separator


def copy_file_or_directory(name, new_name):
    # прежний код -
    # if os.path.isdir(name):
    #     shutil.copytree(name, new_name)
    # else:
    #     shutil.copyfile(name, new_name)

    # тернарный оператор
    shutil.copytree(name, new_name) if os.path.isdir(
        name) else shutil.copyfile(name, new_name)


#  посмотреть файлы/папки
def filenames():
    # result = []
    directory = os.getcwd()
    # прежний код -
    # for i in range(len(os.listdir(directory))):
    #     result.append(os.listdir(directory)[i])

    #  тот же код в виде генератора списка
    result = [os.listdir(directory)[i] for i in range(len(os.listdir(directory)))]
    return result


def author_info():
    return 'PUBLIC DOMAIN ⓒ2019'


def quit():
    sys.exit(0)
