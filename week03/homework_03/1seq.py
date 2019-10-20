# МОДУЛЬ 1
'''
Задание:
Пользователь вводит количество элементов будущего списка
После этого по очереди по одной вводит любые цифры
Сохранить цифры в список
Отсортировать список по возрастанию и вывести на экран
пример вывода - [2, 4, 5]
'''
number_of_elements = int(input('Введите количество элементов: '))
digit_list = []
i = 1
while i <= number_of_elements:
    digit_list.append(int(input(f'Введите {i} элемент: ')))
    i += 1
digit_list.sort()
print(digit_list)

number_of_elements = int(input('Введите количество элементов: '))
digit_list = []
for i in range(number_of_elements):
    number = int(input('Введите число'))
    digit_list.append(number)

digit_list.sort()
print(digit_list)
