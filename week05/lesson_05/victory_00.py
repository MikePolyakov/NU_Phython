"""
Программа викторина будет задавать нам вопросы несколько раз
"""
import random
FAMOUS_PEOPLE = {'Александр Сергеевич Пушнин': '26.06.1799',
                 'Михаил Юрьевич Лермонтов': '15.10.1814',
                 'Сергей Александрович Есенин': '03.10.1895',
                 'Владимир Семенович Высоцкий': '25.01.1938',
                 'Виктор Робертович Цой': '21.06.1962',
                 'Константин Эдуардович Циолковский': '17.09.1857',
                 'Сергей Павлович Королев': '12.01.1907',
                 'Валентин Петрович Глушко': '20.08.1908',
                 'Андрей Николаевич Туполев': '29.10.1888',
                 'Юрий Алексеевич Гагарин': '09.03.1934'}

rounds = int(input('Сколько раз вы хотите играть?'))

for i in range(rounds):
    name, date = random.choice(list(FAMOUS_PEOPLE.items()))
    answer = input(f'Когда родился {name} ')

    # Если введенный год совпадает с правильным
    if answer == date:
        print('Верно')
    else:
        print('Неверно')

print('Пока!')
