# Реализовать проект расчета суммарного расхода ткани на производство одежды.
# Основная сущность (класс) этого проекта — одежда, которая может иметь определенное название.
# К типам одежды в этом проекте относятся пальто и костюм.
# У этих типов одежды существуют параметры: размер (для пальто) и рост (для костюма).
# Это могут быть обычные числа: V и H, соответственно.
# Для определения расхода ткани по каждому типу одежды использовать формулы: для пальто (V/6.5 + 0.5),
# для костюма (2 * H + 0.3). Проверить работу этих методов на реальных данных.
# Реализовать общий подсчет расхода ткани. Проверить на практике полученные на этом уроке знания:
# реализовать абстрактные классы для основных классов проекта, проверить на практике работу декоратора @property.

from abc import ABC, abstractmethod


class Clothes(ABC):

    def __init__(self, size):
        self.size = size  # size 38 - 72 for Coat and height in meters for Suit

    @property
    def material(self, k, n):
        return float(self.size * k + n)

    @abstractmethod
    def abstract(self):
        print(f'Everyone, go to out Insta and buy our rags!')


class Coat(Clothes):
    @property
    def material(self, k=1 / 6.5, n=0.5):
        return round(float(self.size * k + n), 2)

    def abstract(self):
        pass


class Suit(Clothes):
    @property
    def material(self, k=2, n=0.3):
        return round(float(self.size * k + n), 2)

    def abstract(self):
        pass


my_coat = Coat(44)
my_suit = Suit(1.92)


print(f'Total material consumption for Coat is {my_coat.material} m.')
print(f'Total material consumption for Suit is {my_suit.material} m.')
print(f'Total material consumption for both items is {my_coat.material + my_suit.material} m')
