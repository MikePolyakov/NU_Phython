# Personal account Function
"""
Функция "Личный счет"
"""


# переводим копейки < 10 в строковое значение
def str_value(value):
    if value[1] < 10:
        str_kopeyka = '0' + str(value[1])
    else:
        str_kopeyka = str(value[1])
    str_money = [value[0], value[1], str_kopeyka]
    return str_money


# проверка суммы
def check_sum(question):
    while True:
        value = input(question)
        if '.' in value:
            value_main, value_rest = value.split('.')
            if len(value_rest) <= 2:
                if value_main == '':
                    value_main = '0'
                value = [int(value_main), int(value_rest)]
                break
            else:
                print('Неправильный ввод суммы')
                pass
        elif value.isnumeric():
            value = [int(value), 0]
            break
        else:
            print('Неправильный ввод суммы')
            pass
    return value


# пополнение счета
def refill_account(old_balance):
    add_value = check_sum('Введите сумму пополнения руб.коп: ')
    str_add_value = str_value(add_value)
    print(f'На Ваш счет будет добавлено {str_add_value[0]} руб {str_add_value[2]} коп')
    print('*' * 30)
    rubles = old_balance[0] + add_value[0] + (old_balance[1] + add_value[1])//100
    kopeyka = (old_balance[1] + add_value[1]) - ((old_balance[1] + add_value[1])//100)*100
    new_balance = [rubles, kopeyka]
    return new_balance


# покупка
def purchase(money, number):
    price = check_sum('Введите сумму покупки: ')
    str_price = str_value(price)
    print(f'Цена покупки {str_price[0]} руб {str_price[2]} коп')
    if (money[0]*100 + money[1]) < (str_price[0]*100 + str_price[1]):
        print('На покупку не хватает денег')
        history = ''
        return number, money, history
    else:
        number += 1
        purchase_name = input('Введите название покупки, например (еда) ')
        history = [purchase_name, str(str_price[0]), str_price[2]]
        new_money = money[0]*100 + money[1] - str_price[0]*100 - str_price[1]
        ruble = new_money//100
        kopeyka = new_money - ruble*100
        money = [ruble, kopeyka]
        return number, money, history


def history_of_purchase(history):
    for i in range(len(history)):
        print(f'#{i+1} {history[i][0]} стоимостью {history[i][1]} руб {history[i][2]} коп')


def personal_account():
    in_file = open('balance.txt', 'r', encoding='utf8')
    in_balance = list(in_file.readline().split(' '))
    if in_balance[0] == '':
        balance = [0, 0]
    else:
        balance = [int(in_balance[2]), int(in_balance[4])]
    in_file.close()
    in_file = open('history.txt', 'r', encoding='utf8')
    in_purchase_history = list(in_file.readlines())
    purchase_history = []
    if len(in_purchase_history) == 0:
        purchase_history = []
        purchase_number = 0
    else:
        purchase_number = len(in_purchase_history)
        for i in range(len(in_purchase_history)):
            i_line = list(in_purchase_history[i].split(' '))
            i_name = i_line[:-4]
            name = ''
            for j in range(len(i_name)):
                name += i_name[j]+' '
            purchase_line = [name, i_line[-4], i_line[-2]]
            purchase_history.append(purchase_line)

    while True:
        print('0. посмотреть баланс')
        print('1. пополнение счета')
        print('2. покупка')
        print('3. история покупок')
        print('4. выход')
        print('*' * 30)

        choice = input('Выберите пункт меню ')
        if choice == '0':
            now_value = str_value(balance)
            print('*' * 30)
            print(f'Сейчас у Вас на счете {now_value[0]} руб {now_value[2]} коп')
            print('*' * 30)
        elif choice == '1':
            new_balance = refill_account(balance)
            balance = new_balance
            now_value = str_value(balance)
            print(f'У Вас на счете стало {now_value[0]} руб {now_value[2]} коп')
            print('*' * 30)
        elif choice == '2':
            purchase_number, balance, new_purchase = purchase(balance, purchase_number)
            now_value = str_value(balance)
            print(f'У Вас на счете {now_value[0]} руб {now_value[2]} коп')
            if new_purchase != '':
                purchase_history.append(new_purchase)
            print('*' * 30)
        elif choice == '3':
            if purchase_number == 0:
                print('*' * 30)
                print('У Вас нет истории покупок.')
                print('*' * 30)
            else:
                print('*' * 30)
                history_of_purchase(purchase_history)
                print('*' * 30)
        elif choice == '4':
            out_file = open('balance.txt', 'w', encoding='utf8')
            now_value = str_value(balance)
            print(f'текущий баланс {now_value[0]} руб {now_value[2]} коп', file=out_file)
            out_file.close()
            out_file = open('history.txt', 'w', encoding='utf8')
            for i in range(len(purchase_history)):
                history_line = purchase_history[i]
                print(f'{purchase_history[i][0]} {purchase_history[i][1]} руб {purchase_history[i][2]} коп', file=out_file)
            out_file.close()
            break
        else:
            print('Неверный пункт меню')