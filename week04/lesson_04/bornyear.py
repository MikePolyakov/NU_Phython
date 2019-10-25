def input_int(p_message):
    m_value = None
    while True:
        if m_value is not None:
            if m_value.isdigit():
                return int(m_value)
            else:
                print('  -> Не является целым числом, попробуйте ещё раз...')
        m_value = input(f'{p_message} ')


year = input_int('Ввведите год рождения А.С.Пушкина:')
while year != 1799:  # AV: правильный ответ преобразован в целое
    print("Не верно")
    year = input_int('Ввведите год рождения А.С.Пушкина:')

day = input_int('Ввведите день рождения Пушкин?')
while day != 6:  # AV: правильный ответ преобразован в целое
    print("Не верно")
    day = input_int('В какой день июня родился Пушкин?')

print('Верно')