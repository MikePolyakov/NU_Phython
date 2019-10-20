def rounding(value):
    print(value)
    kopeyka = abs(value * 100)
    print(kopeyka)
    ruble = int(kopeyka // 100)
    print(ruble)
    kopeyka = abs(value) - ruble
    print('kopeyka =', kopeyka)
    kopeyka = int(kopeyka * 10000 // 100)
    print(kopeyka)
    value = ruble + kopeyka / 100
    print(value)
    if kopeyka < 10:
        str_kopeyka = '0' + str(kopeyka)
    else:
        str_kopeyka = str(kopeyka)
    ruble_and_kopeyka = dict([('руб', ruble), ('коп_число', kopeyka), ('коп', str_kopeyka), ('величина', value)])
    print(ruble_and_kopeyka)
    return ruble_and_kopeyka


a = 3.90
test = rounding(a)
print(test)
print(test['руб'])
print(test['коп_число'])
print(test['коп'])
print(test['величина'])




