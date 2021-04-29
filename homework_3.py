# Первое задание
def div_func(arg1, arg2):
    div = arg1 / arg2
    return div

a = float(input("Введите первое число: "))
b = float(input("Введите число, на которое нужно поделить: "))

if b == 0:
    print('На ноль делить нельзя.')
else:
    print(div_func(a, b))

# Второе задание
name = input("Введите ваше имя: ")
surname = input("Введите вашу фамилию: ")
year_of_birth = input("Введите ваш год рождения: ")
city = input("Введите ваш город проживания: ")
email = input("Введите вашу почту: ")
phone = input("Введите ваш номер телефона: ")

def info_user(*args):
    return list(args)

print(' '.join(info_user(name, surname, year_of_birth, city, email, phone)))

# Третье задание
def my_func(arg1, arg2, arg3):
    min_arg = min(arg1, arg2, arg3)
    if arg1 == min_arg:
        summ = arg2 + arg3
    elif arg2 == min_arg:
        summ = arg1 + arg3
    elif arg3 == min_arg:
        summ = arg1 + arg2
    return summ

a = int(input("Введите первое число: "))
b = int(input("Введите второе число: "))
c = int(input("Введите третье число: "))

print(f'Сумма наибольших аргументов: {my_func(a, b, c)}')

# Четвертое задание
x1 = int(input('Введите положительное число: '))
y1 = int(input('Введите целое отрицательное число: '))
if x1 <= 0:
    print('Нужно ввести положительное число')
elif y1 >= 0:
    print('Нужно ввести целое отрицательное число. Пример: -45')

def my_func1(x, y):
    pow = x ** y
    return pow

def my_func2(x, y):
    i = -1
    a = x
    while i != y:
        a = a * a
        i -= 1
    pow = 1 / a
    return pow

print(my_func2(x1, y1))
print(my_func2(x1, y1))

# Пятое задание. Не смог реализовать:  Если специальный символ введен после
# нескольких чисел, то вначале нужно добавить сумму этих чисел к полученной ранее сумме и после этого завершить программу
def summ():
    number = input('Введите числа через пробел: ').split()
    list_number = [int(el) for el in number]
    res = sum(list_number)
    print(res)
    q = 0
    for el in range(len(number)):
        res = sum(list_number)
        while q == 0:
            number = input('Введите числа через пробел. Для окончания укажите end: ').split()
            if number[el] == 'end':
                q = 1
                break
            else:
                number1 = [int(el) for el in number]
                res = res + sum(number1)
                print(res)
        return res
print(f'Итоговая сумма получилась: {summ()}')

# Шестое задание
''' Первый вариант '''

def int_func(text):
    return text.capitalize()
print(int_func('hello'))

''' Вариант второй '''

def int_func(text):
    return text.title()
print(int_func('hello how are you'))










