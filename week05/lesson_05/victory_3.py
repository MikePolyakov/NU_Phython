"""
Программа викторина будет задавать нам вопросы несколько раз
"""

from all_functions import get_person_and_question


rounds = int(input('Сколько раз вы хотите играть?'))

for i in range(rounds):
    get_person_and_question()

print('Пока!')
