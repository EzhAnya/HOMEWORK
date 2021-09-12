#  Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя:
#  имя, фамилия, год рождения, город проживания, email, телефон.
#  Функция должна принимать параметры как именованные аргументы. Реализовать вывод данных о пользователе одной строкой.

def cv(name, surname, location, mail, phone):
    result = 'User data: ' + str(name) + str(surname) + ', lives in ' + str(location) + ', contacts: ' + str(mail) + ', ' + str(phone)
    print(result)

list_arg = {'name': [], 'surname': [], 'location': [], 'mail': [], 'phone': []}
i = 0
for i in list_arg.keys():
    item = input(f'Input your {i}, please: ')
    list_arg[i].append(item)

cv(**list_arg)
