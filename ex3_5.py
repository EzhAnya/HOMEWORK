# Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов.
# Определить, кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников.
# Выполнить подсчет средней величины дохода сотрудников.

with open('txt3.txt', 'a+', encoding='UTF-8') as f:

    while True:
        record = input('Введите фамилию и оклад через пробел (в файле уже есть строки, но вы можете добавить, или просто нажать enter): ')
        if not record:
            break
        else:
            f.write(f'\n{record}')


    f.seek(0)
    data_f = f.read().split('\n')
    dict = {}
    average = 0
    count = 0

    for line in data_f:
        list = line.split(' ')
        key = list[0]
        value = int(list[1])
        dict[key] = value
        count += 1
        average += round(value)

print(f'Сотрудники с окладом менее 20000: {", ".join([key for key in dict.keys() if dict[key] < 20000])}')
print(f'Средняя зарплата - {round(average / count)}')
