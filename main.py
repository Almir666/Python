from random import randint

# ЗАДАНИЕ 6
#-------------------------------------------------------
# CHECK_NORMAL_1 = 4
# CHECK_NORMAL_2 = 100
# CHECK_NORMAL_3 = 400
# START_YEAR = 1582
# result = ''
#
# input_year = int(input("Введите год: "))
# if input_year < START_YEAR:
#     result = 'Вы ввели неверную дату'
# elif input_year % CHECK_NORMAL_1:
#     result =("Это обычный год")
# elif not input_year % CHECK_NORMAL_2:
#     if not input_year % CHECK_NORMAL_3:
#         result =("Это високосный год")
#     else:
#         result =("Это обычный год")
# else:
#     result =("Это високосный год")
# print(result)
#
# ЗАДАНИЕ 7
#-------------------------------------------------------

# FROM = 1
# TO = 999
# result = None
#
# while True:
#     number = input("Введите число: ")
#     if FROM <= int(number) <= TO:
#         match len(number):
#             case 1:
#                 result = int(number) ** 2
#             case 2:
#                 result = (int(number) % 10) * (int(number) // 10)
#             case 3:
#                 result = number[::-1]
#         break
# print(result)

# ЗАДАНИЕ 8
#-------------------------------------------------------

# rows = int(input("Введите колличество рядов елки: "))
#
# for i in range(1, rows + 1):
#     spaces = " " * (rows - i)
#     stars = "*" * (2 * i - 1)
#     print(spaces + stars)

# ЗАДАНИЕ 9
# -------------------------------------------------------
#
# for i in range(2, 10):
#     for j in range(2, 6):
#         print(f'{j} * {i} = {i * j}\t', end='   ')
#     print()
# print()
# for i in range(2, 10):
#     for j in range(6, 10):
#         print(f'{j} * {i} = {i * j}\t', end='   ')
#     print()

# Домашнее задание 1

# 1. Треугольник
# -------------------------------------------------------

# print("Введите стороны треугольника: ")
# a = int(input("Сторона a: "))
# b = int(input("Сторона b: "))
# c = int(input("Сторона c: "))
# if a > b + c or b > a + c or c > a + b:
#     print("Треугольника с такими сторонами не существует")
# elif a == b and b == c:
#     print("Этот треугольник равноcторонний")
# elif a == b  or b == c or c == a:
#     print("Этот треугольник равнобедренный")
# else:
#     print("Этот треугольник разноcторонний")


# 2. Число
# -------------------------------------------------------
# count = 0
# while True:
#     number = int(input("Введите число: "))
#     if number < 0 or number > 100000:
#         print("Введите число больше 0 и меньше 100000")
#     else:
#         for i in range(2, number // 2 + 1):
#             if (number % i == 0):
#                 count += 1
#         if (count <= 0):
#             print("Это простое число")
#             break
#         else:
#             print("Число не является простым")
#             break


# 3. Угадываем число
# -------------------------------------------------------

LOWER_LIMIT = 0
UPPER_LIMIT = 1000
count = 10
num = randint(LOWER_LIMIT, UPPER_LIMIT)
print("Попробуйте угадать число! У вас 10 попыток)")
while True:
    if count <= 0:
        print("Сожалею, но у вас закончились попытки, попытайте удачу в слудующий раз!")
        break
    else:
        user_num = int(input("Введите число: "))
        if user_num == num:
            print("Поздравляю вы угадали! :3")
            break
        else:
            if user_num > num:
                print("Меньше")
                count -= 1
            else:
                print("Больше")
                count -= 1