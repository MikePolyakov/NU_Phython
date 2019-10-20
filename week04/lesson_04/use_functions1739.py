"""
МОДУЛЬ 3
Программа "Личный счет"
Описание работы программы:
Пользователь запускает программу у него на счету 0
Программа предлагает следующие варианты действий
1. пополнить счет
2. покупка
3. история покупок
4. выход
1. пополнение счета
при выборе этого пункта пользователю предлагается ввести сумму на сколько пополнить счет
после того как пользователь вводит сумму она добавляется к счету
снова попадаем в основное меню
2. покупка
при выборе этого пункта пользователю предлагается ввести сумму покупки
если она больше количества денег на счете, то сообщаем что денег не хватает и переходим в основное меню
если денег достаточно предлагаем пользователю ввести название покупки, например (еда)
снимаем деньги со счета
сохраняем покупку в историю
выходим в основное меню
3. история покупок
выводим историю покупок пользователя (название и сумму)
возвращаемся в основное меню
4. выход
выход из программы
При выполнении задания можно пользоваться любыми средствами
Для реализации основного меню можно использовать пример ниже или написать свой
"""


def rounding(value):
    print(value)
    kopeyka = abs(value * 100)
    print('k1=', kopeyka)
    ruble = int(kopeyka // 100)
    print('r=', ruble)
    kopeyka = abs(value) - ruble
    print('kop_do= ', kopeyka)
    kopeyka = int(kopeyka * 10000 // 100)
    print('kop=', kopeyka)
    value = ruble + kopeyka / 100
    print('value=', value)
    if kopeyka < 10:
        str_kopeyka = '0' + str(kopeyka)
    else:
        str_kopeyka = str(kopeyka)
    ruble_and_kopeyka = dict([(1, ruble), (2, kopeyka), (3, str_kopeyka), (4, value)])
    return ruble_and_kopeyka


def refill_account(old_balance):
    add_value = input('Введите сумму пополения: ')
    if ',' in add_value:
        add_value = add_value.replace(',', '.')
    add_value = float(add_value)
    round_add_value = rounding(add_value)
    print(f'На Ваш счет будет добавлено {round_add_value[1]} руб {round_add_value[3]} коп')
    print('-------------------')
    print(round_add_value[4])
    new_balance = old_balance + round_add_value[4]
    print(new_balance)
    return new_balance


def purchase(old_balance):
    price = float(input('Введите сумму покупки: '))
    round_price = rounding(price)
    print(f'Цена покупки {round_price[1]} руб {round_price[3]} коп')
    if old_balance < price:
        print('На покупку не хватает денег')
        history = {}
        return old_balance, history
    else:
        purchase_name = input('Введите название покупки, например (еда) ')
        history = dict([(purchase_name, round_price[4])])
        print(history)
        old_balance -= round_price[4]
        return old_balance, history


balance = float(0)
purchase_history = {}
while True:
    print('1. пополнение счета')
    print('2. покупка')
    print('3. история покупок')
    print('4. выход')
    print('-------------------')

    choice = input('Выберите пункт меню ')
    if choice == '1':
        balance = refill_account(balance)
        round_value = rounding(balance)
        print(f'У Вас на счете {round_value[1]} руб {round_value[3]} коп')
        print('-------------------')
    elif choice == '2':
        balance, new_purchase = purchase(balance)
        round_value = rounding(balance)
        print(f'У Вас на счете {round_value[1]} руб {round_value[3]} коп')
        print(new_purchase)
        purchase_history.update(new_purchase)
        print(purchase_history)
        print('-------------------')
    elif choice == '3':
        pass
    elif choice == '4':
        break
    else:
        print('Неверный пункт меню')


