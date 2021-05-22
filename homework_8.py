# Первое задание
class Data:
    def __init__(self, day, month, year):
        self.day = day
        self.month = month
        self.year = year

    @classmethod
    def converted(cls, data):
        d, m, y = data.split('-')
        d = int(d)
        m = int(m)
        y = int(y)
        return cls(d, m, y)

    @staticmethod
    def validation(copy):
        if copy.day < 1 or copy.day > 31:
            print('Число не может быть меньше 1 или больше 31')
        if copy.month < 1 or copy.month > 12:
            print('Месяц не может быть меньше 1 или больше 12')
        if copy.year < 0 or copy.year > 3000:
            print('Введите от 0 до 3000г')

one = Data.converted('0-20-40')
Data.validation(one)
print(type(one.day))
# Второе задание
class DivisionByZero(Exception):
    def __str__(self):
        return 'На нуль делить нельзя!'

one = input("Введите первое число: ")
two = input("Введите число, на которое нужно поделить: ")

try:
    one = int(one)
    two = int(two)
    if two == 0:
        raise DivisionByZero
except (ValueError, DivisionByZero) as err:
    print(err)
else:
    print(one / two)
# Третье задание
class MyListError(Exception):
    def __str__(self):
        return 'Вы ввели не число!'

li = []
while True:
    try:
        a = input('Введите число: ')
        if a == 'stop':
            print(li)
            break
        if a.isdigit() == False:
            raise MyListError
    except MyListError as err:
        print(err)
    else:
        a = int(a)
        li.append(a)

# 4, 5, 6 задание
class MyValueError(Exception):
    def __str__(self):
        return 'Неверные данные в цене или в количестве'

class Warehouse:
    residual = {}

    def __str__(self):
        return f'На складе осталось {self.residual}'

class OfficeEquipment:
    def __init__(self, name, model, price, quantity):
            self.name = name
            self.model = model
            self.price = price
            self.quantity = quantity

class Printer(OfficeEquipment):
    def __init__(self, name, model, price, quantity, print_color, print_type):
        self.print_color = print_color
        self.print_type = print_type
        super().__init__(name, model, price, quantity)

    def acceptance_to_warehouse(self):
        Warehouse.residual['Принтер', self.name, self.model, self.price, self.print_color, self.print_type] = self.quantity


class Scanner(OfficeEquipment):
    def __init__(self, name, model, price, quantity, color):
        self.color = color
        super().__init__(name, model, price, quantity)

    def acceptance_to_warehouse(self):
        Warehouse.residual['Сканнер', self.name, self.model, self.price, self.color] = self.quantity

class Copier(OfficeEquipment):
    def __init__(self, name, model, price, quantity, format_print, print_speed):
        self.format_print = format_print
        self.print_speed = print_speed
        super().__init__(name, model, price, quantity)

    def acceptance_to_warehouse(self):
        Warehouse.residual['Копир', self.name, self.model, self.price, self.format_print, self.print_speed] = self.quantity
while True:
    start = input('Введите название оргтехники, которой хотите добавить на склад (принтер, сканер, копир). '
                  'Для окончание введите stop: ')
    if start == 'stop':
        break
    elif start == 'принтер' or start == 'Принтер':
        printer = input('Введите через пробел: производитель, модель, цена, количество, цвет печати, тип печати'
                       '(лазерный/струйный): ')
        try:
            name, model, price, quantity, print_color, print_speed = printer.split(' ')
            if price.isdigit() == False or quantity.isdigit() == False:
                raise MyValueError
        except MyValueError as err:
            print(err)
        except ValueError:
            print('Ошибка ввода данных')
        else:
            ex_printer = Printer(name, model, price, quantity, print_color, print_speed)
            ex_printer.acceptance_to_warehouse()
    elif start == 'сканер' or start == 'Сканер':
        printer = input('Введите через пробел: производитель, модель, цена, количество, цвет: ')
        try:
            name, model, price, quantity, color = printer.split(' ')
            if price.isdigit() == False or quantity.isdigit() == False:
                raise MyValueError
        except MyValueError as err:
            print(err)
        except ValueError:
            print('Ошибка ввода данных')
        else:
            ex_printer = Scanner(name, model, price, quantity, color)
            ex_printer.acceptance_to_warehouse()
    elif start == 'копир' or start == 'Копир':
        printer = input('Введите через пробел: производитель, модель, цена, формат печати, скорость печати: ')
        try:
            name, model, price, quantity, color, format_print, print_speed = printer.split(' ')
            if price.isdigit() == False or quantity.isdigit() == False:
                raise MyValueError
        except MyValueError as err:
            print(err)
        except ValueError:
            print('Ошибка ввода данных')
        else:
            ex_printer = Copier(name, model, price, quantity, color, format_print, print_speed)
            ex_printer.acceptance_to_warehouse()
a = Warehouse()
print(a)
# Седьмое задание
class ComplexNumber:
    def __init__(self, *args):
        self.args = args

    def __add__(self, other):
        return ComplexNumber(complex(self.args[0], self.args[1]) + complex(other.args[0], other.args[1]))

    def __mul__(self, other):
        return ComplexNumber(complex(self.args[0], self.args[1]) * complex(other.args[0], other.args[1]))

    def __str__(self):
        return f'{self.args[0]}'

one = ComplexNumber(1.1, 2)
two = ComplexNumber(3, 4)
print(one + two)
print(one * two)



