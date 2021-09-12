# Реализовать функцию my_func(), которая принимает три позиционных аргумента
# и возвращает сумму наибольших двух аргументов

def sum_max(a, b, c):
    result = a + b + c - min(a, b, c)
    print(result)


a, b, c = [int(s) for s in input('Введите три числа через запятую: ').split(',')]
sum_max(a, b, c)