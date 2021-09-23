# Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты: speed, color, name, is_police (булево).
# А также методы: go, stop, turn(direction), которые должны сообщать,
# что машина поехала, остановилась, повернула (куда).
# Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar.
# Добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля.
# Для классов TownCar и WorkCar переопределите метод show_speed. При значении скорости свыше 60 (TownCar) и 40 (WorkCar)
# должно выводиться сообщение о превышении скорости.
# Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат.
# Выполните вызов методов и также покажите результат.

import random


class Car:

    def __init__(self, color, name, speed, max_speed=None):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = False
        self.max_speed = max_speed

    def go(self):
        print(f'{self.color} {self.name} just took off')

    def stop(self):
        print(f'{self.color} {self.name} has stopped')

    def turn(self):
        print(f'{self.color} {self.name} has turned to the {random.choice(["left", "right", "back"])}')

    def show_speed(self):
        if self.max_speed:
            if self.speed > self.max_speed:
                print(f'Oh, look! {self.color} {self.name} is moving faster than allowed ({self.max_speed})! '
                      f'He is going {self.speed}! He gonna kill us!')
            else:
                print(f'{self.color} {self.name} is keeping the speed {self.speed}')
        else:
            print(f'{self.color} {self.name} is keeping the speed {self.speed}')

    def move(self):
        self.go()
        self.turn()
        self.show_speed()
        self.stop()


class SportCar(Car):
    pass


class PoliceCar(Car):
    is_police = True


class TownCar(Car):
    pass


class WorkCar(Car):
    pass


police = PoliceCar('Black', 'Voronok', random.randint(10, 210))
police.move()
town = TownCar('Green', 'MiniCooper', random.randint(10, 210), 60)
town.move()
work = WorkCar('Yellow', 'Bus', random.randint(10, 210), 40)
work.move()
sport = SportCar('Red', 'Ferrari', random.randint(10, 210))
sport.move()
