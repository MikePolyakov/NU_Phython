from functions import salary, hello_who

"""
Тесты через assert
"""

# assert 2 > 1
# assert 3 > 1
# assert 4 > 1
# assert 1 == 1
#
# # будет ошибка
# assert 1 > 90, 'Какой то текст при возникновении ошибки'
#
# print('Это не выполнится')

assert hello_who('Max') == 'Hello, Max', 'Hello who error'
assert hello_who('Leo') == 'Hello, Leo', 'Hello who error'

assert salary(2, 1) == 4, salary(2, 1)
assert salary(2, 2) == 8
