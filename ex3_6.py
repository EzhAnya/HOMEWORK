#  Реализовать базовый класс Worker (работник), в котором определить атрибуты: name, surname, position (должность),
#  income (доход). Последний атрибут должен быть защищенным и ссылаться на словарь, содержащий элементы:
#  оклад и премия, например, {"wage": wage, "bonus": bonus}. Создать класс Position (должность) на базе класса Worker.
#  В классе Position реализовать методы получения полного имени сотрудника (get_full_name) и дохода с учетом премии
#  (get_total_income). Проверить работу примера на реальных данных (создать экземпляры класса Position,
#  передать данные, проверить значения атрибутов, вызвать методы экземпляров).

class Worker:
    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {'wage': int(wage), 'bonus': int(bonus)}


class Position(Worker):

    def get_full_name(self):
        print(f'This is {self.name} {self.surname}, the {self.position}.')

    def get_total_income(self):
        result = self._income['wage'] + self._income['bonus']
        print(f'His total income, including bonus, is {result}.')


lindon = Position('Mark', 'Lindon', 'carpenter', 1200, 800)
cooper = Position('Solan', 'Cooper', 'plumber', 900, 1000)

lindon.get_full_name()
lindon.get_total_income()
cooper.get_full_name()
cooper.get_total_income()
