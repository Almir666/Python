from random import randint
from math import pi
import decimal
from fractions import Fraction

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

# LOWER_LIMIT = 0
# UPPER_LIMIT = 1000
# count = 10
# num = randint(LOWER_LIMIT, UPPER_LIMIT)
# print("Попробуйте угадать число! У вас 10 попыток)")
# while True:
#     if count <= 0:
#         print("Сожалею, но у вас закончились попытки, попытайте удачу в слудующий раз!")
#         break
#     else:
#         user_num = int(input("Введите число: "))
#         if user_num == num:
#             print("Поздравляю вы угадали! :3")
#             break
#         else:
#             if user_num > num:
#                 print("Меньше")
#                 count -= 1
#             else:
#                 print("Больше")
#                 count -= 1

# СЕМИНАР 2
# -----------------------------------------

# a = 1
# b = "text"
# c = []
# d = (1, 2, 3)
# e = {}
#
# print(type(a))
# print(type(b))
# print(type(c))
# print(type(d))
# print(type(e))

# data = [1, "text", 0.5, (1, 2, 3)]
# for i, el in enumerate(data):
#     print(i + 1, el, id(el), el.__sizeof__(), hash(el))
#     if isinstance(el, int):
#         print("целое число")
#     if isinstance(el, str):
#         print("это строка")


# def bin_number(num: int, mode: str) -> str:
#     result = ''
#     match mode:
#         case 'bin':
#             convert = 2
#         case 'oct':
#             convert = 8
#
#     while num >= 1:
#         res = num % convert
#         num = num // convert
#
#         result += str(res)
#     return print(result[::-1])
#
# num1 = int(input("Введите число: "))
# bin_number(num1, mode="bin")
# bin_number(num1, mode="oct")
# print(bin(25), oct(25))


# def circle(d: decimal) -> tuple[decimal, decimal]:
#     decimal.getcontext().prec = 42
#     _pi = decimal.Decimal(pi)
#     if d <= 1000:
#         s = (_pi * d**2) / 4
#         l = _pi * d
#
#     return decimal.Decimal(s), decimal.Decimal(l)
#
# print(circle(10))


# class Bank:
#
#     BALANCE = 0
#     MIN = 50
#     COMMISSION = 0.015
#     BONUS = 0.03
#     TAX = 0.10
#     OPERATION: int
#
#     def __init__(self):
#         self.OPERATION = 0
#     def up_balance(self, cash: int) -> tuple[int, int] | None:
#         if cash % self.MIN == 0:
#             self.BALANCE += cash
#             self.OPERATION += 1
#             return self.BALANCE, self.OPERATION
#         else:
#             return None
#     def give_money(self, cash: int, commission: int) -> tuple[int, int] | None:
#         if cash % self.MIN == 0 and self.BALANCE > 0 and self.BALANCE - (cash + commission) >= 0:
#             self.BALANCE -= cash
#             self.BALANCE -= commission
#             self.OPERATION += 1
#
#             return self.BALANCE, self.OPERATION
#         else:
#             return None
#     def exit(self):
#         return "Gud luck"
#
#     def check_commission(self, cash: int) -> int:
#         sum_commission = cash * self.COMMISSION
#         MAX = 600
#         MIN = 30
#
#         if sum_commission > MAX:
#             return MAX
#         elif sum_commission < MIN:
#             return MIN
#         else:
#             return int(sum_commission)
#
#     def check_operation(self):
#         return (False, True)[self.OPERATION % 3 == 0]
#
#     def start(self, mode: str, cash: int) -> str:
#
#         if self.check_operation():
#             self.BALANCE += self.BALANCE * self.BONUS
#         match mode:
#             case "up_balance":
#                 self.up_balance(cash=cash)
#                 return f"Счет пополнен, сумма: {cash}, баланс: {self.BALANCE}"
#
#             case "give_money":
#                 com_data = self.check_commission(cash=cash)
#
#                 data = self.give_money(cash=cash, commission=com_data)
#
#                 if data:
#                     return f"Снятие средств: {cash}, коммисcия: {com_data}, баланс: {self.BALANCE}"
#                 else:
#                     return "Нехватает средств"
#             case "exit":
#                 return self.exit()
#
# bank = Bank()
# cash_in_1: int = 500
# cash_in_2: int = 1500
# cash_in_3: int = 1000
# cash_out = 300
# print(bank.start(mode="up_balance", cash=cash_in_1))
# print(bank.start(mode="up_balance", cash=cash_in_2))
# print(bank.start(mode="up_balance", cash=cash_in_3))
# print(bank.start(mode="give_money", cash=cash_out))


# Домашнее задание 2

# 1. шестнадцатиричное представление
# -----------------------------------------------------
# def convert_number(num: int) -> str:
#     result = ''
#     convert = 16
#
#     while num >= 1:
#         res = num % convert
#         num = num // convert
#         result += str(res)
#     return print(result[::-1])
#
# number = int(input("Введите число: "))
# convert_number(number)
# print(hex(25))


# 2. Произведение дробей
# -----------------------------------------------------
# def sum_d(a: int, b: int, c: int, d: int) -> str:
#     if b == d:
#         numenator = a + c
#         denominator = b
#     else:
#         numenator = a * d + b * c
#         denominator = b * d
#     if numenator == denominator:
#         return f"Сумма дробей: 1"
#     else:
#         return f"Сумма дробей: {numenator}/{denominator}"
#
# def mult_d(a: int, b: int, c: int, d: int) -> str:
#     numenator = a * c
#     denominator = b * d
#     return f"Произведение дробей: {numenator}/{denominator}"
#
# a = Fraction(2, 3)
# b = Fraction(1, 8)
# print(a + b)
#
# ab = input('Введите дробь в виде a/b: ')
# cd = input('Введите дробь в виде c/d: ')
# a = int(ab.split("/")[0])
# b = int(ab.split("/")[1])
# c = int(cd.split("/")[0])
# d = int(cd.split("/")[1])
#
# print(sum_d(a, b, c, d))
# print(mult_d(a, b, c, d))







