#  Реализовать класс Road (дорога), в котором определить атрибуты: length (длина), width (ширина).
#  Значения данных атрибутов должны передаваться при создании экземпляра класса. Атрибуты сделать защищенными.
#  Определить метод расчета массы асфальта, необходимого для покрытия всего дорожного полотна.
#  Использовать формулу: длина * ширина * масса асфальта для покрытия одного кв метра дороги асфальтом,
#  толщиной в 1 см * число см толщины полотна. Проверить работу метода.
# Например: 20м * 5000м * 25кг * 5см = 12500 т

class Road:

    def __init__(self, width, length):
        self._length = width
        self._width = length
        self.mass = 0.025  # tons per 1 cm layer for 1 sq meter
        self.thickness = 0.1  # meter


    def calc(self):
        print(f'The construction of your road will take {round(self._width * self._length * self.mass * self.thickness * 100, 3)} tons of composite materials')


track = Road(int(input('Input road width in meters: ')), int(input('Input road length in meters: ')))
track.calc()
