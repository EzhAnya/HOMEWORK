# Создать (не программно) текстовый файл, в котором каждая строка должна содержать данные о фирме:
# название, форма собственности, выручка, издержки.
# Пример строки файла: firm_1 ООО 10000 5000.
# Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль.
# Если фирма получила убытки, в расчет средней прибыли ее не включать.
# Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями, а также словарь со средней прибылью.
# Если фирма получила убытки, также добавить ее в словарь (со значением убытков).
# Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
# Итоговый список сохранить в виде json-объекта в соответствующий файл.
# Пример json-объекта:
# [{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]
#
# Подсказка: использовать менеджеры контекста.

import json
key = []
profit = []
final = []
final2 = {}
with open('txt7.txt', 'r') as f:
    lines = f.read().split('\n')
    for line in lines:
        key.append(line.split(' ')[0])
        profit.append(int(line.split(' ')[2]) - int(line.split(' ')[3]))
        print(f'For {line.split(" ")[0]} financial result is {int(line.split(" ")[2]) - int(line.split(" ")[3])}.')

    av_profit = round(sum([int(number) for number in profit if number >= 0]) / len([number for number in profit if number >= 0]))

    print(f'Average profit (for successful parties) is {av_profit}.')

    final = [dict(zip(key, profit)), final2]
    final2['average profit'] = av_profit

    with open('firms.json', 'w') as temp:
        json.dump(final, temp)