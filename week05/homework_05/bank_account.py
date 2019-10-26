# Personal account Function
"""
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
    kopeyka = abs(value * 100)
    ruble = int(kopeyka // 100)
    kopeyka = int(kopeyka - ruble * 100)
    if kopeyka < 10:
        str_kopeyka = '0' + str(kopeyka)
    else:
        str_kopeyka = str(kopeyka)
    value = ruble + int(str_kopeyka) / 100
    ruble_and_kopeyka = dict([(1, ruble), (2, kopeyka), (3, str_kopeyka), (4, value)])
    return ruble_and_kopeyka


def refill_account(old_balance):
    add_value = float(input('Введите сумму пополнения: '))
    round_add_value = rounding(add_value)
    print(f'На Ваш счет будет добавлено {round_add_value[1]} руб {round_add_value[3]} коп')
    print('-------------------')
    return old_balance + round_add_value[4]


def purchase(money, number):
    price = float(input('Введите сумму покупки: '))
    round_price = rounding(price)
    print(f'Цена покупки {round_price[1]} руб {round_price[3]} коп')
    if money < round_price[4]:
        print('На покупку не хватает денег')
        history = {}
        return number, money, history
    else:
        number += 1
        purchase_name = input('Введите название покупки, например (еда) ')
        history = dict([(number, (purchase_name, round_price[4]))])
        money -= round_price[4]
        money = round(money, 2)
        return number, money, history


def hisory_of_purchase(history):
    for element in history.keys():
        round_price = rounding(history[element][1])
        print(f'{element}: {history[element][0]} стоимостью {round_price[1]} руб {round_price[3]} коп')


def personal_account():
    in_file = open('balance.txt', 'r', encoding='utf8')
    balance = float(in_file.readline())
    in_file.close()
    purchase_history = {}
    purchase_number = 0
    while True:
        print('1. пополнение счета')
        print('2. покупка')
        print('3. история покупок во время сеанса')
        print('4. выход')
        print('-------------------')

        choice = input('Выберите пункт меню ')
        if choice == '1':
            round_value = rounding(balance)
            print(f'Сейчас у Вас на счете {round_value[1]} руб {round_value[3]} коп')
            print('-------------------')
            balance = refill_account(balance)
            round_value = rounding(balance)
            print(f'У Вас на счете стало {round_value[1]} руб {round_value[3]} коп')
            print('-------------------')
        elif choice == '2':
            purchase_number, balance, new_purchase = purchase(balance, purchase_number)
            round_value = rounding(balance)
            print(f'У Вас на счете {round_value[1]} руб {round_value[3]} коп')
            purchase_history.update(new_purchase)

            print('-------------------')
        elif choice == '3':
            if purchase_number == 0:
                print('-------------------')
                print('У Вас нет истории покупок.')
                print('-------------------')
            else:
                print('-------------------')
                hisory_of_purchase(purchase_history)
                print('-------------------')
        elif choice == '4':
            out_file = open('balance.txt', 'w', encoding='utf8')
            print(balance, file=out_file)
            out_file.close()
            break
        else:
            print('Неверный пункт меню')
