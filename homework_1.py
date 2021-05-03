# Первое задание
year = 2020
mounth = "Апрель"

print(f"Сейчас {year} год, {mounth}")

answer_1 = int(input("Введите ваш возраст: "))
answer_2 = input("Введите ваше имя: ")

print(f"Вас зовут {answer_2}, вам {answer_1} лет")
# Второе задание
seconds = int(input("Введите секунды: "))
h = seconds // 3600
m = int((seconds / 60) % 60)
s = int(seconds % 60)

print(f"Введенные секунды преобразованы в формате ЧЧ:ММ:СС. Результат: {h}:{m}:{s}")
# Третье задание
n = int(input("Введите число: "))
n1 = str(n)
n2 = n1 + n1
n3 = n1 + n1 + n1
print(n + int(n2) + int(n3))
# Четвертое задание
#Не разобрался
# Пятое задание

proceeds = float(input("Укажите вашу выручку: "))
costs = float(input("Укажите издержки: "))

if proceeds > costs:
    print(f"Ваша фирма отработала в прибыль. Рентабельность вашей компании: {proceeds / costs} %")
    staff = int(input("Укажите количество сотрудников: "))
    print(f"Прибыль в расчете на одного сотрудника {proceeds /  staff}")
else:
    print("Ваша фирма отработала в убыток")

# Шестое задание
a = 2
b = 3
day = 1

while a < b:
    a = a + a * 0.10
    print(f"На {day}-й день: {a} км")
    day += 1
print(f"Ответ: на {day}-й день спортсмен достиг результата — не менее {b} км.")




