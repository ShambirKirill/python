# Первое задание
example_1 = [1, 10, 'example', 'seller']
for el in range(len(example_1)):
    print(type(example_1[el]))
#Второе задание. Не разобрал формулировку.

# Третье задание
list_mounth = ['Winter', "Spring", 'Summer', 'Fall']
dict_mounth = {1 : 'Winter', 2 : 'Spring', 3 : 'Summer', 4 : 'Fall'}

ex_list = int(input('Введите месяц от 1 до 12: '))

if ex_list > 12 or ex_list < 1:
    print("Нужно ввести от 1 до 12")
elif ex_list == 12 or ex_list == 1 or ex_list == 2:
    print(list_mounth[0])
elif ex_list == 3 or ex_list == 4 or ex_list == 5:
    print(list_mounth[1])
elif ex_list == 6 or ex_list == 7 or ex_list == 8:
    print(list_mounth[2])
elif ex_list == 9 or ex_list == 10 or ex_list == 11:
    print(list_mounth[3])

ex_dict = int(input('Введите месяц от 1 до 12: '))
if ex_list > 12 or ex_list < 1:
    print("Нужно ввести от 1 до 12")
elif ex_list == 12 or ex_list == 1 or ex_list == 2:
    print(dict_mounth.get(1))
elif ex_list == 3 or ex_list == 4 or ex_list == 5:
    print(dict_mounth.get(2))
elif ex_list == 6 or ex_list == 7 or ex_list == 8:
    print(dict_mounth.get(3))
elif ex_list == 9 or ex_list == 10 or ex_list == 11:
    print(dict_mounth.get(4))

#Четвертое задание.
ex_text = input("Напишите сообщение из нескольких слов: ")
ex_text = ex_text.split()
n = 1
for i in ex_text:
    print(f"{n}: {i[0:10]}")
    n += 1
#Пятое задание. Не смог реализовать.



