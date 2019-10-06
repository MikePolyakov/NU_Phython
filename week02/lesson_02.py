# 2 урок
print('Hello')
print('Hello', 'Max')
greeting = 'Hello'
name = 'Max'
student_class = 1
student_class += 1

print('Class', 1)
print('Hello', 'Max', sep='////')
print('Hello', 'Max', end='xxxx')

"""
comment multiline
"""
print(type(greeting))

# str
# int
# float
# bool

is_man = True

name = input('input your name ')
print('Hello', name)

age = input()
age = int(age)

print('age', age)

a = 10
b = 20
print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(a ** 2)
print(not a + b)
print(a and b)
print(a or b)

if a > b:
    print(a)
else:
    print(b)
print('end')

answer = input('how are you')
while answer != 'ok':
    print('good')
    answer = input('how are you')
print('nice')


answer = None
while answer != 'ok':
    answer = input('how are you')
    if answer == 'good':
        break
    print('good')
print('nice')

school_class = ''
school_class = input(' what class are you')
while not school_class.isdigit():
    school_class = input(' what class are you')
school_class = int(school_class)

while school_class <= 11:
    if school_class == 4:
        school_class += 1
        continue
    print(school_class)
    school_class += 1
print('end')