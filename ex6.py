# 6. * Реализовать структуру данных «Товары». Она должна представлять собой список кортежей.
# Каждый кортеж хранит информацию об отдельном товаре.
# В кортеже должно быть два элемента — номер товара и словарь с параметрами (характеристиками товара: название, цена, количество, единица измерения).
# Структуру нужно сформировать программно, т.е. запрашивать все данные у пользователя.

# Необходимо собрать аналитику о товарах.
# Реализовать словарь, в котором каждый ключ — характеристика товара, например название, а значение — список значений-характеристик,
# например список названий товаров.

stock = []
key_list = ['Наименование', 'производство', 'остаток', 'цена']
all_stock_dict = {key_list[0]:[],key_list[1]:[],key_list[2]:[],key_list[3]:[]}
count = 1

while True:
    trigger = input('Добавить новый товар? (да / нет) ')
    if trigger == 'да':
        name = input(f'Введите название товара {count}: ')
        all_stock_dict[key_list[0]].append(name)
        origin = input(f'Введите страну производителя товара {name}: ')
        all_stock_dict[key_list[1]].append(origin)
        on_stock = int(input(f'Введите остаток на складе товара {name}: '))
        all_stock_dict[key_list[2]].append(on_stock)
        price = int(input(f'Введите цену товара {name}: '))
        all_stock_dict[key_list[3]].append(price)
        dict_stock = {key_list[0]: name, key_list[1]: origin, key_list[2]: on_stock, key_list[3]: price}
        element = (count, dict_stock)
        stock.append(element)
        count += 1
    else:
        break

print(stock)

print(all_stock_dict)
