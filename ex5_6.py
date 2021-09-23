# Реализовать класс Stationery (канцелярская принадлежность).
# Определить в нем атрибут title (название) и метод draw (отрисовка).
# Метод выводит сообщение “Запуск отрисовки.”
# Создать три дочерних класса Pen (ручка), Pencil (карандаш), Handle (маркер).
# В каждом из классов реализовать переопределение метода draw.
# Для каждого из классов методы должен выводить уникальное сообщение.
# Создать экземпляры классов и проверить, что выведет описанный метод для каждого экземпляра.

class Stationery:

    def __init__(self, title):
        self.title = title

    def draw(self):
        print(f'{self.title} starts drawing')


class Pen(Stationery):

    def draw(self):
        print(f'{self.title} pen starts writing elegant letters.')


class Pencil(Stationery):

    def draw(self):
        print(f'{self.title} pencil starts sketching the draft of your portrait.')


class Handle(Stationery):

    def __init__(self, title, thickness, color):
        Stationery.__init__(self, title)
        self.color = color
        self.thickness = thickness  # mm

    def draw(self):
        print(f'{self.title} handle starts drawing {self.thickness} mm thick {self.color} line')


my_pen = Pen('Parker')
my_pencil = Pencil('Koh-I-Noor')
my_handle = Handle('Practik', 8, 'green')

my_pen.draw()
my_pencil.draw()
my_handle.draw()