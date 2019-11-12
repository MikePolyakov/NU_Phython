import os
import pickle


def separator(count=30):
    """
    Функция разделитель
    :param count: количество звездочек
    :return: красивый разделитель
    """
    return '*' * count


def data_reading(file_name, data_param):
    if os.path.exists(file_name):
        with open(file_name, 'rb', encoding='utf-8') as f:
            data = pickle.load(f)
    elif data_param == 'int':
        data = 0
    elif data_param == 'list':
        data = []
    return data


def data_writing(file_name, data):
    with open(file_name, 'wb', encoding='utf-8') as f:
        pickle.dump(data, f)
