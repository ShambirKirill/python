# Первое задание
import time
class TrafficLight:

    __color = 'Red'
    launched = 1

    def running(self):
        while TrafficLight.launched == 1:
            print(TrafficLight.__color)
            time.sleep(7)
            TrafficLight.__color = 'Yellow'
            print(TrafficLight.__color)
            time.sleep(2)
            TrafficLight.__color = 'Green'
            print(TrafficLight.__color)
            time.sleep(15)
            TrafficLight.__color = 'Red'

gg = TrafficLight()
print(gg.running())
# Второе задание
class Road:
    def __init__(self, length, width):
        self._length = int(length)
        self._width = int(width)

    def calculation(self):
        res = self._length * self._width * 25 * 5
        return f'Необходимо {res} кг асфальта'

a = Road(20, 5000)
print(a.calculation())
# Третье задание
class Worker:
    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"wage": wage, "bonus": bonus}


class Position(Worker):
    def get_full_name(self):
        return f'Полное имя: {self.name} {self.surname}'

    def get_total_income(self):
        return f'Должность: {self.position}, Доход с учетом премии: {self._income.get("wage") + self._income.get("bonus")}'

p = Position('Kirill', 'Shambir', 'Director', 1000000, 5000)
print(p.get_full_name())
print(p.get_total_income())
# Четвертое задание
class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print('Машина поехала')

    def stop(self):
        print('Машина остановилась')

    def turn(self, direction):
        print(f'Машина повернула {direction}')

    def show_speed(self):
        print(f'Скорость автомобиля {self.speed}')

class TownCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        print(f'Ваша скорость {self.speed}')
        if self.speed > 60:
            print('Вы превышаете скорость')

class SportCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

class WorkCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        print(f'Ваша скорость {self.speed}')
        if self.speed > 40:
            print('Вы превышаете скорость')

class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

t = TownCar(90, 'White', 'Bus', 0)
t.show_speed()
p = WorkCar(40, 'Yellow', 'Taxi', 0)
p.go()
p.show_speed()
# Пятое задание
class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        print('Запуск отрисовки')

class Pen(Stationery):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        print(f'Вы написали {self.title} ручкой')

class Pencil(Stationery):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        print(f'Вы написали {self.title} карандашом')

class Handle(Stationery):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        print(f'Вы написали {self.title} маркером')

pen = Pen('Привет')
pen.draw()
pencil = Pencil('Hi')
pencil.draw()
handle = Handle('Hello')
handle.draw()