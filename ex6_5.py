# Необходимо создать (не программно) текстовый файл, где каждая строка описывает учебный предмет
# и наличие лекционных, практических и лабораторных занятий по этому предмету и их количество.
# Важно, чтобы для каждого предмета не обязательно были все типы занятий.
# Сформировать словарь, содержащий название предмета и общее количество занятий по нему. Вывести словарь на экран.
# Примеры строк файла:
# Информатика: 100(л) 50(пр) 20(лаб).
# Физика: 30(л) — 10(лаб)
# Физкультура: — 30(пр) —
#
# Пример словаря:
# {“Информатика”: 170, “Физика”: 40, “Физкультура”: 30}


# разделяем списки на будущие ключи и значения по двоеточию:
plan = {}
key = []
values = []
with open('txt6.txt', 'r', encoding='UTF-8') as f:
    f_data = f.read().split('\n')
    for i in f_data:
        key.append(i.split(':')[0])
        values.append(i.split(':')[1].split('('))

# избавляемся от лишних символов в списке значений:
    values_new = []
    for z in values:
        values_true = []
        for x in z:
            value_true = [letter for letter in list(x) if (letter and letter.isdigit() is True)]
            values_true.append(''.join(value_true))
        values_true.pop()
        values_true = [int(el) for el in values_true]
        values_new.append(values_true)

# рассчитываем итоговые значения:
    values_final = []
    for y in values_new:
        values_final.append(sum(y))

# выводим в словарь полученные списки:
    plan = dict(zip(key, values_final))
    print(plan)
