# Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата «день-месяц-год».
# В рамках класса реализовать два метода. Первый, с декоратором @classmethod, должен извлекать число, месяц, год
# и преобразовывать их тип к типу «Число». Второй, с декоратором @staticmethod, должен проводить валидацию
# числа, месяца и года (например, месяц — от 1 до 12).
# Проверить работу полученной структуры на реальных данных.

import datetime


class Date:
    def __init__(self, data):
        self.data = str(data)

    @classmethod
    def integer_me(cls, data):
        day, month, year = [int(el) for el in str(data).split('-')]
        return[year, month, day]


    @staticmethod
    def validate_me(data):
        y = Date.integer_me(data)
        try:
            full_data = datetime.date(y[0], y[1], y[2])
        except ValueError:
            print('Указанные значения не могут быть датой. Внимательнее, пожалуйста.')
        else:
            print(full_data)


usr_data = input('Введите дату в формате дд-мм-гггг: ')

Date.validate_me(usr_data)