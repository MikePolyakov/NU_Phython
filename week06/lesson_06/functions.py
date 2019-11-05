def hello_who(name):
    """
    :param name: имя
    :return: строка приветствия
    """
    return f'Hello, {name}'


def salary(hours, salary_by_hour):
    """
    рассчет зп сотрудника
    :param hours: кол-во часов
    :param salary_by_hour: зарплата за час
    :return: итоговая стоимость
    """
    k = 2
    return hours * salary_by_hour * k

def my_func(param01, param02):
    """
    my function
    :param param01: param 01
    :param param02: param 02
    :return:
    """
    return param01 + param02
