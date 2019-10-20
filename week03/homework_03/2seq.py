# МОДУЛЬ 2
'''
Задание:
Пользователь вводит любые цифры через запятую
Предусмотреть что пользователь может использовать один из 3-х разделителей: запятую, точку с запятой, слэш
Сохранить цифры в список
Получить новый список в котором будут только уникальные элементы исходного
Вывести его на экран. Пример вывода - Результат: 2, 9
'''
initial_input = input('Введите элементы списка через запятую, точку с запятой или слэш: ')
if ',' in initial_input:
    user_sep = ','
elif ';' in initial_input:
    user_sep = ';'
elif '/' in initial_input:
    user_sep = '/'
digit_list = list(map(int, initial_input.split(user_sep)))
new_list = []
for i in range(len(digit_list)):
    if digit_list.count(digit_list[i]) == 1:
        new_list.append(digit_list[i])
print('Результат: ',  end='')
print(*new_list, sep=', ')

initial_input = input('Введите элементы списка через запятую: ')
digit_list = initial_input.split(',')
new_list = []
for i in digit_list:
    if digit_list.count(i) == 1:
        new_list.append(i)
print('Результат: ',  end='')
print(*new_list, sep=', ')
