# Function with quiz
import random


def quiz():
    famous_men_list = {'Ньютон': '25.12.1642',
                        'Колумб': '31.10.1451',
                        'Энштейн': '14.03.1879',
                        'Шекспир': '26.04.1564',
                        'Дарвин': '12.02.1809',
                        'Коперник': '19.02.1473',
                        'Наполеон': '15.08.1769',
                        'Максвел': '13.06.1831',
                        'Вашингтон': '22.02.1731',
                        'Маркс': '05.05.1818'}
    rounds = int(input('Сколько раз вы хотите играть? '))
    true_answer = 0
    for i in range(rounds):
        name, date = random.choice(list(famous_men_list.items()))
        answer = input(f'Когда родился {name} ? ')
        # Если введенная дата совпадает с правильной
        if answer == date:
            print('Верно')
            true_answer += 1
        else:
            print('Неверно')
    print('*' * 30)
    true_answer = 'Вы ответили правильно ' + str(true_answer) + ' раз!'
    print('Пока!')
    return true_answer
