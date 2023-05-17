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
#-------------------------------------------------------

# for i in range(2, 10):
#     for j in range(2, 6):
#         print(f'{j} * {i} = {i * j}\t', end='   ')
#     print()
# print()
# for i in range(2, 10):
#     for j in range(6, 10):
#         print(f'{j} * {i} = {i * j}\t', end='   ')
#     print()


