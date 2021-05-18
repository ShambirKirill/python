# Первое задание
class Matrix:
    def __init__(self, list_of_lists):
        self.matrix = list_of_lists

    def __add__(self, other):
        return Matrix(self.matrix + other.matrix)

    def __str__(self):
        return f'{self.matrix}'

mat = Matrix([10, 20, 1])
mat1 = Matrix([30, 2])
print(mat + mat1)

# Второе задание
class Cloth:

    def __init__(self, size, height, name="No name"):
        self.name = name
        self.size = size
        self.height = height
        self.general = []
        self.v = self.size / 6.5 + 0.5
        self.h = 2 * self.height + 0.3

    @property
    def coat(self):
        v = self.size / 6.5 + 0.5
        return v

    @property
    def costume(self):
        h = 2 * self.height + 0.3
        return h

    def __str__(self):
        return f'Суммарно для одежды "{self.name}" требуется ткани: {self.v + self.h}'


c = Cloth(44, 178, 'buster')
print(c)
print(f'Суммарно для одежды "{c.name}" требуется ткани: {c.costume + c.coat}')
# Третье задание
class Cell:
    def __init__(self, quantity):
        self.quantity = quantity

    def __add__(self, other):
        return Cell(self.quantity + other.quantity)

    def __sub__(self, other):
        sub = self.quantity - other.quantity
        if sub > 0:
            return Cell(self.quantity - other.quantity)
        else:
            return 'Ошибка'

    def __mul__(self, other):
        return Cell(self.quantity * other.quantity)

    def __truediv__(self, other):
        return Cell(self.quantity // other.quantity)

    def __str__(self):
        return f'Результат: {self.quantity}'


c = Cell(10)
c1 = Cell(5)
print(c - c1)
print(c / c1)











