import script_homework_4
import random
# Первое задание
# wage_hours = float(input('Введите часы. Через запятую введите минуты: '))
# wage_rate = float(input('Введите ставку в час: '))
# wage_prize = float(input('Введите премию: '))
#
# print(script_homework_4.wage(wage_hours, wage_rate, wage_prize))

# Второе задание
random_list = []
i = 0
while i < 15:
    random_list.append(random.randint(1, 350))
    i += 1
for i, j in enumerate(random_list):
    if random_list[i - 1] < random_list[i]:
        print(j)
new_list = []
for i, j in enumerate(random_list):
    if random_list[i] > random_list[i - 1]:
        new_list.append(j)
new_list.pop(0) # Нулевой элемент не может быть больше предедущего, т.к его нет, то удаляем этот элемент
print(random_list)
print(new_list)

# Третье задание
my = [el for el in range(20, 201) if el%20 == 0 or el%21 == 0]
#Четвертое задание
example = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
example_unique = []

for el in example:
    if el in example_unique:
        example_unique.remove(el)
    else:
        example_unique.append(el)

print(example_unique)
# Пятое задание
my_list = [i for i in range(100, 1001, 2)]
def func_hw_5(a, b):
    return a * b
from functools import reduce
print(reduce(func_hw_5, my_list))
# Шестое задание
# a)
from itertools import count
from itertools import cycle

start = 1
end = 40
for i in count(start):
    if i > end:
        break
    else:
        print(i)
#б)
list_hw_6_b = [1, 10, 20, 30, 40, 'end']
b_end = 10
stop = 0
for el in cycle(list_hw_6_b):
    if stop == b_end:
        break
    else:
        print(el)
        stop += 1
# Седьмое задание
from math import factorial

def func(n):
    stop = factorial(n)
    print(f'Находим факториал числа {n}. Для этого нужно найти произведение следующих чисел:')
    for i in range(1, n+1):
        if i == stop:
            break
        else:
            yield i
    print(f'Факториал числа {n} равен: {factorial(n)}')

for i in func(25):
    print(i)









