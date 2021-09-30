#  Реализовать проект «Операции с комплексными числами». Создайте класс «Комплексное число», реализуйте перегрузку
#  методов сложения и умножения комплексных чисел. Проверьте работу проекта, создав экземпляры класса
#  (комплексные числа) и выполнив сложение и умножение созданных экземпляров.
#  Проверьте корректность полученного результата.

class CompNum:
    def __init__(self, real, imag):
        self.full = complex(real, imag)
        self.real = real
        self.imag = imag

    def __add__(self, other):
        print(f'({self.real + other.real}+{self.imag + other.imag}*j)')

    def __mul__(self, other):
        print(f'({self.real * other.real - self.imag * other.imag}+{self.imag * other.real + self.real * other.imag}*j)')


a = CompNum(1, 2)
print(a.full)

b = CompNum(3.1, 1)
print(b.full)

a.__add__(b)
a.__mul__(b)