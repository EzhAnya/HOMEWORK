# 3. Пользователь вводит месяц в виде целого числа от 1 до 12.
# Сообщить к какому времени года относится месяц (зима, весна, лето, осень).
# Напишите решения через list и через dict.
month_user = int(input('Input your month (1 - 12): '))

# dictionary:
seasons = {'winter': (1, 2, 12), 'spring': (3, 4, 5), 'summer': (6, 7, 8), 'autumn': (9, 10, 11)}
for key in seasons.keys():
    if month_user in seasons[key]:
        print(key)

# list:
list_seasons = [(1, 2, 12), (3, 4, 5), (6, 7, 8), (9, 10, 11)]
list_year = ['winter', 'spring', 'summer', 'autumn']
for i in range(len(list_seasons)):
    if month_user in list_seasons[i]:
        print(list_year[i])
