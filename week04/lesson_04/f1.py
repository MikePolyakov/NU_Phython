def main_menu():
    print('1. пополнение счета')
    print('2. покупка')
    print('3. история покупок')
    print('4. выход')


current_del = "\n"

account = 0.0
pay_history = []
while True:
    main_menu()

    choice = input('Выберите пункт меню: ')
    if choice == '1':
        user_sum = input('Укажите сумму пополнения счета, разделитель - точка: ')
        try:
            if float(user_sum) <= 0:
                raise Exception("Введено не корректное значение")
            account += float(user_sum)
        except:
            print("Указана не корректная сумма пополнения счета")
        print(f"Текущее состояние счета: {account}")
    elif choice == '2':
        pay_sum = input('Укажите сумму предполагаемой покупки, разделитель - точка: ')
        try:
            if float(pay_sum) <= 0:
                raise Exception("Введено не корректное значение")
            pay_sum = float(pay_sum)
        except:
            print("Указана не корректная сумма предполагаемой покупки")
            continue
        if account < pay_sum:
            print(f"Не хватает денег для покупки. На счете: {account}")
        else:
            pay_name = input('Укажите название предполагаемой покупки: ')
            account -= pay_sum
            while not pay_name.isalpha():
                pay_name = input('Укажите название предполагаемой покупки: ')
            pay_history.append(f"Товар: {pay_name}; Стоимость: {pay_sum}")
            print(f"Текущее состояние счета: {account}")
    elif choice == '3':
        if len(pay_history) == 0:
            print("Отсутствует история покупок")
        else:
            print("История покупок: ")
            print(current_del.join(pay_history))
    elif choice == '4':
        break
    else:
        print('Неверный пункт меню')

print('Приходите ещё!)')