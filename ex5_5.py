# Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
# Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.


with open('txt5.txt', 'w+') as f:
    f.write(input('Введите числа через пробел:'))
    f.seek(0)
    reader = sum(int(el) for el in (f.read().split(' ')))
    print(reader)
