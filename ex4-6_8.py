# Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад. А также класс «Оргтехника»,
# который будет базовым для классов-наследников. Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс).
# В базовом классе определить параметры, общие для приведенных типов. В классах-наследниках реализовать параметры,
# уникальные для каждого типа оргтехники.
#
# Разработать методы, отвечающие за приём оргтехники на склад и передачу
# в определенное подразделение компании. Для хранения данных о наименовании и количестве единиц оргтехники,
# а также других данных, можно использовать любую подходящую структуру, например словарь.

# Реализуйте механизм валидации вводимых пользователем данных. Например,
# для указания количества принтеров, отправленных на склад, нельзя использовать строковый тип данных.
# Подсказка:
# постарайтесь реализовать в проекте «Склад оргтехники» максимум возможностей, изученных на уроках по ООП.

class OutOfStock(Exception):
    def __init__(self, txt):
        self.txt = txt


class Unit:

    def __init__(self, article, name, price, on_stock):
        self.name = name
        self.article = article
        self.price = int(price)
        self.on_stock = int(on_stock)
        self._dict = {'Article': self.article, 'Name': self.name, 'Price': self.price, 'Units on stock': self.on_stock}


    def receipt(self, num_into):
        self.on_stock += num_into
        self._dict['Units on stock'] = self.on_stock
        print(f'{num_into} of {self.name} accepted at warehouse. Current balance on stock: {self.on_stock}. ')

    def assign(self, dept, num_out):
        try:
            self.on_stock -= num_out
            if num_out > self.on_stock:
                raise OutOfStock(f'Warehouse balance is insufficient. '
                                 f'The order for {num_out} units of {self.name} to {dept} is NOT executed.')
        except OutOfStock as err:
            print(err)
        else:
            self._dict['Units on stock'] = self.on_stock
            current_balance[dept] += num_out
            print(f'{num_out} of {self.name} was assigned to {dept}. '
                  f'Units total on {dept}: {current_balance[dept]}. Units left on stock: {self.on_stock}. ')


class Printer(Unit):
    def __init__(self, article, name, price, on_stock, print_type, pages):
        Unit.__init__(self, article, name, price, on_stock)
        self.print_type = print_type
        self.pages = int(pages)
        self._dict.update({'Printer type': self.print_type, 'Resource, pages': self.pages})
        print(self._dict)


class Scanner(Unit):
    def __init__(self, article, name, price, on_stock, scan_type, resolution):
        Unit.__init__(self, article, name, price, on_stock)
        self.scan_type = scan_type
        self.resolution = int(resolution)
        self._dict.update({'Scanner type': self.scan_type, 'Resolution, dpi': self.resolution})
        print(self._dict)


class Copier(Unit):
    def __init__(self, article, name, price, on_stock, capacity):
        Unit.__init__(self, article, name, price, on_stock)
        self.capacity = capacity
        self._dict.update({'Capacity, pages/min': self.capacity})
        print(self._dict)


current_balance = {'Legal': 2, 'Accounting': 1, 'HR': 0}


print1 = Printer(555, 'Canon2000', 5800, 2, 'Lazer', 150_000)
scan1 = Scanner(666, 'HP8000', 12000, 1, 'Slide', 640)
copy1 = Copier(777, 'Xerox1000', 4800, 3, 40)

print1.receipt(3)
scan1.receipt(2)
copy1.receipt(4)

print1.assign('Legal', 8)
scan1.assign('Accounting', 1)
copy1.assign('HR', 1)

print(print1._dict)
print(scan1._dict)
print(copy1._dict)
