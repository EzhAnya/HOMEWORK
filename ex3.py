# Для чисел в пределах от 20 до 240 найти числа, кратные 20 или 21. Необходимо решить задание в одну строку.
# Подсказка: использовать функцию range() и генератор.

# способ 1:
print([number for number in range(20, 241, 20)]+[number for number in range(21, 241, 21)])


# способ 2:
print([number for number in range(20, 241) if not (number % 20 and number % 21)])


# способ 3:
print([number for number in range(20, 241) if (number % 20 == 0 or number % 21 == 0)])
