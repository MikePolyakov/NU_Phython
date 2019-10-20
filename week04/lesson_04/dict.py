def print_key_val(**kwargs):
    """
    Функция выводит переданные параметры в фиде key --> value
    key - имя параметра
    value - значение параметра
    :param kwargs: любое количество именованных параметров
    :return: None
    """
    for key, value in kwargs.items():
        print("{} --> {}".format(key, value))


history = {'##': ('покупка', 'цена')}
print(history)


history2 = {1: ('q', 5)}
print(history2)
history.update(history2)
print(history)
history3 = {2: ('r', 6)}
history.update(history3)
print(history)
print('_______________')
print(history.keys())
print(history.values())
for element in history.keys():
    print(history[element][0], '---->' , history[element][1])




