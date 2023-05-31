from random import randint
from math import pi
import decimal
from fractions import Fraction
from collections import defaultdict


# ЗАДАНИЕ 6
# -------------------------------------------------------
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
# -------------------------------------------------------

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
# -------------------------------------------------------

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


# СЕМИНАР 3
# -----------------------------------------
# Задание 1

# def set_func(numbers: list) -> list:
#     result = []
#     for i in numbers:
#         if i not in result:
#             result.append(i)
#     return result
#
# def set_func2(numbers: list) -> list:
#     return set(numbers)
#
# arr = [1, 1, 2, 3, 3, 3, 4, 5]
# print(set_func(arr))


# -----------------------------------------
# Задание 2

# def check_str(data: str) -> (int, str, float):
#     if data.isdigit():
#         result = int(data)
#     elif data.count("-") or data.count(".") > 0:
#         result = float(data)
#     elif data.lower() != data:
#         result = data.lower()
#     else:
#         result = data.upper()
#
#     return result
#
# print(type(check_str("12")), check_str("12"))
# print(type(check_str("12.5")), check_str("12.3"))
# print(check_str("cHeck"))
# print(check_str("check"))


# -----------------------------------------
# Задание 3

# def dict_tuple(data: tuple) -> dict:
#     result_dict = {}
#     for i in data:
#         result_dict.setdefault(type(i), []).append(i)
#     return result_dict
#
#
#
# data = (1, 2.3, "text", [1, 2, 3], (1, 2))
# print(dict_tuple(data))


# -----------------------------------------
# Задание 4

# def uniq_elements_list(input_list: list) -> list:
#     return list(filter(lambda x : input_list.count(x) != 2, input_list))
#
# cur_list = [1, 1, 2, 1, 2, 3]
#
# print(uniq_elements_list(cur_list))


# -----------------------------------------
# Задание 5

# def numerate_list(input_list: list[int]) -> list[int]:
#     return [i for i, j in filter(lambda x: x[1] % 2 != 0, enumerate(input_list, 1))]
#
# cur_list = [1, 1, 2, 1, 2, 3]
# print(numerate_list(cur_list))

#
# -----------------------------------------
# Задание 6
#
# def text_format(data: str):
#     result = sorted(data.split())
#     [print(f"{i} - {word:>{len(max(result, key=len))}}") for i, word in enumerate(result, 1)]
#
# text = input("Введите текст: ")
# text_format(text)


# -----------------------------------------
# Задание 7

# def text_count(data: str) -> dict:
#     result = {}
#     for i in data:
#         if i.count(i) >= 2:
#             result[i] = data.count(i)
#         result.setdefault(i, data.count(i))
#     return result
#
# print(text_count("Robocop"))


# -----------------------------------------
# Задание 8
# def camping
#
# camping_dict = {
#     "Rob" : ("water", "food", "matches", "knife", "axe"),
#     "Jhon" : ("water", "food", "matches", "tent"),
#     "Rick" : ("water", "food", "matches", "grill")
# }


# Домашнее задание 3

# 1. Повторяющиеся элементы
# -----------------------------------------------------
# def list_of_duplicate(in_list: list) -> list:
#     arr = []
#     result = []
#     for i in in_list:
#         if i not in arr:
#             arr.append(i)
#         else:
#             result.append(i)
#     return set(result)
#
# arr = [1, 1, 1, 2, 2, 3]
# print(list_of_duplicate(arr))


# 2. Десять самых частых слов
# -----------------------------------------------------
#
# test = "В 1864—1870 годах Генрих Семирадский обучался в Академии художеств " \
#        "в Санкт-Петербурге, где сначала (до апреля 1866 года) был вольнослушателем, " \
#        "а затем — постоянным учеником. Его наставниками были Карл Вениг и Богдан " \
#        "Виллевальде[5][14][8]. В 1866—1867 годах Семирадский получил одну малую " \
#        "и две большие серебряные медали за рисунки и этюд с натуры[15]. В 1868 году" \
#        " за картину «Диоген, разбивающий чашу», сюжет которой был основан на одной из " \
#        "историй из жизни древнегреческого философа Диогена, он был награждён малой" \
#        " золотой медалью Академии художеств[16][17] - эта награда давала ему право" \
#        " участвовать в конкурсе на большую золотую медаль[18].Тема конкурса на" \
#        " большую золотую медаль была объявлена в начале 1870 года - «Доверие Александра " \
#        "Македонского к врачу Филиппу во время тяжкой болезни»[5][6]. Это был не первый" \
#        " академический конкурс на подобную тему - известно, что в 1830 году исторические" \
#        " живописцы получили следующее задание: «Изобразить Александра Великого в ту минуту," \
#        " когда он, будучи в болезни и получив извет, будто бы врач его Филипп желает отравить" \
#        " его, не доверяя сему извету, принимает от Филиппа лекарство, и выпивает оное, вручив " \
#        "между тем Филиппу означенный извет для прочтения»[19]. Золотую медаль второго достоинства " \
#        "в конкурсе 1830 года получил художник Ян Ксаверий Каневский за картину под названием " \
#        "«Доверие Александра Македонского врачу своему Филиппу»[20]. Кроме того, в 1836 году " \
#        "рисунок на эту тему создал учившийся тогда в Санкт-Петербурге Тарас Шевченко[21]."
#
# def most_frequent(text: str) -> list[str]:
#     dict_counts = {}
#     SHOW_LIMIT = 10
#     new_sorted_dictionary = {}
#     new_text = text.replace(',', ''). \
#         replace('.', ''). \
#         replace('!', ''). \
#         replace('?', ''). \
#         replace('"', ''). \
#         replace('-', ''). \
#         lower(). \
#         strip()
#     words_list = new_text.split()
#     for word in words_list:
#         counter = words_list.count(word)
#         dict_counts[word] = counter
#     sorted_values = sorted(dict_counts.values())[::-1]
#     for i in sorted_values:
#         for k in dict_counts.keys():
#             if dict_counts[k] == i:
#                 new_sorted_dictionary[k] = dict_counts[k]
#     return list(new_sorted_dictionary.items())[0: SHOW_LIMIT]
#
# print(most_frequent(test))


# 3. Рюкзак для похода
# -----------------------------------------------------
# BAG_VOLUME = 60
# bag = {"вода" : 10,
#        "еда" : 10,
#        "посуда" : 5,
#        "топор" : 5,
#        "спички" : 2,
#        "спальник" : 5,
#        "магнитофон" : 10,
#        "мяч" : 10,
#        "мангал" : 20}
# def collector_bag(data: dict) -> list:
#     result = []
#     volume_count = 0
#     count = 0
#     for i in data.values():
#         if volume_count < BAG_VOLUME:
#             result.append(data.items())
#             volume_count += i
#             count += 1
#     return result
#
# print(collector_bag(bag))






# СЕМИНАР 4
# -----------------------------------------
# Задание 1

# def str_split(data: str) -> str:
#     cur_str = data.split()
#     max_word = len(max(cur_str, key=len))
#     for i, s in enumerate(cur_str, start=1):
#         print(f"{i} {s:>{max_word}}")
#
# # [print(f"{i} - {word:>{len(max(result, key=len))}}") for i, word in enumerate(result, 1)]
#
# test_str = "random text"
# str_split(test_str)


# -----------------------------------------
# Задание 2

# def code_list(data: str) -> str:
#     result = set()
#     for i in data:
#         result.add(ord(i))
#     result = sorted(result, reverse=True)
#     return result
#
# print(code_list("Text"))


# -----------------------------------------
# Задание 3

# def str_to_dict(data: str) -> dict[int]:
#     result = {}
#     split_text = sorted([int(i) for i in data.split()])
#     for i in range(split_text[0], split_text[1] + 1):
#         result[chr(i)] = i
#     return result
#
# print(str_to_dict("501 626"))


# -----------------------------------------
# Задание 4

# def my_sort(data: list) -> list:
#     length = len(data)
#     for i in range(length):
#         for j in range(length - 1):
#             if data[j + 1] < data[j]:
#                 data[j], data[j + 1] = data[j + 1], data[j]
#     return data
#
# print(my_sort([1, 0, 12, 3, 666, 12]))


# -----------------------------------------
# Задание 5

# def bonus(name: list[str], salary: list[int], bonus: list[str]) -> dict[str : float]:
#     return {name: money / 100 * perc
#             for name, money, perc in zip(name, salary, (float(i[:-1]) for i in bonus))}
#
#
# print(bonus(["claire", "John"], [1000, 1500], ["10.15","0.75"]))


# -----------------------------------------
# Задание 6

# def sum_numbers(data: list[int], num1: int, num2: int) -> int:
#     sum_num = 0
#     for i in len(data):
#         sum_num = data[num1] + data[num1 + 1]


# СЕМИНАР 5
# ----------------------------------------------

# Задание 1

# text = '3/5/7/8/10/12/13'
#
#
# def make_dict(text: str) -> dict[int:int]:
#     first, second, third, *other = (int(i) for i in text.split('/'))
#     return {second: first, third: tuple(other)}
#
#
# print(make_dict(text))

# Задание 2

# def from_str_to_dict(text_2: str) -> dict[str:int]:
#     return {k: ord(k) for k in text_2}
#
#
# print(from_str_to_dict('sdsdsdd'))

# Задание 3

# def from_str_to_dict_2(text_2: str) -> dict[str:int]:
#     res_iter = iter({k: ord(k) for k in text_2}.items())
#     print(next(res_iter))
#     print(next(res_iter))
#     print(next(res_iter))
#     print(next(res_iter))
#
#
# from_str_to_dict_2('sdsdsddfghjkl;zxcvbnm,')

# Задание 4

# def gen_num() -> None:
#     return (i for i in range(1, 101) if i // 10 + i % 10 != 8)
#
#
# for i in gen_num():
#     print(i)

# Задание 5

# def fizz_buzz() -> None:
#     res_list = ([i for i in range(1, 101)])
#     for i in res_list:
#         if i % 15 == 0:
#             print("FizzBuzz")
#         elif i % 3 == 0:
#             print("Fizz")
#         elif i % 5 == 0:
#             print("Buzz")
#         else:
#             print(i)
# fizz_buzz()
#
# print(*('FizzBuzz' if i % 15 == 0 else 'Fizz' if i % 3 == 0 else 'Buzz' if i % 5 == 0 else i for i in range(1, 51)))


# Задание 6

# def product_table() -> iter:
#     LOWER_LIMIT = 2
#     UPPER_lIMIT = 10
#     COLUMN = 4
#
#     for i in range(LOWER_LIMIT, UPPER_lIMIT, COLUMN):
#         for j in range(LOWER_LIMIT, UPPER_lIMIT + 1):
#             for k in range(i, i + COLUMN):
#                 if j == UPPER_lIMIT and k == i + COLUMN - 1:
#                     print(f'{k:>} x {j:>2} = {k * j:>2}\n\n', end='')
#                 elif k == i + COLUMN - 1:
#                     print(f'{k:>} x {j:>2} = {k * j:>2}\n', end='')
#                 else:
#                     print(f'{k:>} x {j:>2} = {k * j:>2}\t\t', end='')
#
# product_table()

# def mult_table():
#     LOWER_LIMIT = 2
#     UPPER_lIMIT = 10
#     COLUMN = 4
#     print(' ', end='')
#     print(*(f'{k:>} x {j:>2} = {k * j:>2}\n\n' if j == UPPER_lIMIT and k == i + COLUMN - 1 else \
#                 f'{k:>} x {j:>2} = {k * j:>2}\n' if k == i + COLUMN - 1 else \
#                     f'{k:>} x {j:>2} = {k * j:>2}\t\t' \
#             for i in range(LOWER_LIMIT, UPPER_lIMIT, COLUMN)
#             for j in range(LOWER_LIMIT, UPPER_lIMIT + 1)
#             for k in range(i, i + COLUMN)))

# mult_table()

# Задание 7

# def simple_numbers(number: int):
#     yield 2
#     for i in range(3, number + 1):
#         simple = True
#         for j in range(2, i - 1):
#             if not i % j:
#                 simple = False
#         if simple:
#             yield i
#
# print(*simple_numbers(20))


# Домашнее задание 3

# 1. Повторяющиеся элементы
# -----------------------------------------------------
# def list_of_duplicate(in_list: list) -> list:
#     arr = []
#     result = []
#     for i in in_list:
#         if i not in arr:
#             arr.append(i)
#         else:
#             result.append(i)
#     return set(result)
#
# arr = [1, 1, 1, 2, 2, 3]
# print(list_of_duplicate(arr))


# 2. Десять самых частых слов
# -----------------------------------------------------
#
# test = "В 1864—1870 годах Генрих Семирадский обучался в Академии художеств " \
#        "в Санкт-Петербурге, где сначала (до апреля 1866 года) был вольнослушателем, " \
#        "а затем — постоянным учеником. Его наставниками были Карл Вениг и Богдан " \
#        "Виллевальде[5][14][8]. В 1866—1867 годах Семирадский получил одну малую " \
#        "и две большие серебряные медали за рисунки и этюд с натуры[15]. В 1868 году" \
#        " за картину «Диоген, разбивающий чашу», сюжет которой был основан на одной из " \
#        "историй из жизни древнегреческого философа Диогена, он был награждён малой" \
#        " золотой медалью Академии художеств[16][17] - эта награда давала ему право" \
#        " участвовать в конкурсе на большую золотую медаль[18].Тема конкурса на" \
#        " большую золотую медаль была объявлена в начале 1870 года - «Доверие Александра " \
#        "Македонского к врачу Филиппу во время тяжкой болезни»[5][6]. Это был не первый" \
#        " академический конкурс на подобную тему - известно, что в 1830 году исторические" \
#        " живописцы получили следующее задание: «Изобразить Александра Великого в ту минуту," \
#        " когда он, будучи в болезни и получив извет, будто бы врач его Филипп желает отравить" \
#        " его, не доверяя сему извету, принимает от Филиппа лекарство, и выпивает оное, вручив " \
#        "между тем Филиппу означенный извет для прочтения»[19]. Золотую медаль второго достоинства " \
#        "в конкурсе 1830 года получил художник Ян Ксаверий Каневский за картину под названием " \
#        "«Доверие Александра Македонского врачу своему Филиппу»[20]. Кроме того, в 1836 году " \
#        "рисунок на эту тему создал учившийся тогда в Санкт-Петербурге Тарас Шевченко[21]."
#
# def most_frequent(text: str) -> list[str]:
#     dict_counts = {}
#     SHOW_LIMIT = 10
#     new_sorted_dictionary = {}
#     new_text = text.replace(',', ''). \
#         replace('.', ''). \
#         replace('!', ''). \
#         replace('?', ''). \
#         replace('"', ''). \
#         replace('-', ''). \
#         lower(). \
#         strip()
#     words_list = new_text.split()
#     for word in words_list:
#         counter = words_list.count(word)
#         dict_counts[word] = counter
#     sorted_values = sorted(dict_counts.values())[::-1]
#     for i in sorted_values:
#         for k in dict_counts.keys():
#             if dict_counts[k] == i:
#                 new_sorted_dictionary[k] = dict_counts[k]
#     return list(new_sorted_dictionary.items())[0: SHOW_LIMIT]
#
# print(most_frequent(test))


# 3. Рюкзак для похода
# -----------------------------------------------------
# BAG_VOLUME = 60
# bag = {"вода" : 10,
#        "еда" : 10,
#        "посуда" : 5,
#        "топор" : 5,
#        "спички" : 2,
#        "спальник" : 5,
#        "магнитофон" : 10,
#        "мяч" : 10,
#        "мангал" : 20}
# def collector_bag(data: dict) -> list:
#     result = []
#     volume_count = 0
#     count = 0
#     for i in data.values():
#         if volume_count < BAG_VOLUME:
#             result.append(data.items())
#             volume_count += i
#             count += 1
#     return result
#
# print(collector_bag(bag))


# Домашнее задание 4
#------------------------------------------------------

# 1. Транспонирование матрицы

# matrix = [[1, 2, 3], [11, 22, 33]]
#
# def transpos_matrix(matrix: list) -> list:
#     trans_matrix = [[0 for i in range(len(matrix))] for j in range(len(matrix[0]))]
#     for i in range(0, len(matrix)):
#         for j in range(0, len(matrix[0])):
#             trans_matrix[j][i] = matrix[i][j]
#     return trans_matrix
#
# print(transpos_matrix(matrix))


#------------------------------------------------------

# 2. Словарь
# test = "12345"
# def key_param(*,name) -> dict:
#     my_dict = {}
#     my_dict["name"] = name
#     return my_dict
# print(key_param(arg=test))



# 3. Банкомат
#-------------------------------------------------------

# class Bank:
#
#     BALANCE = 0
#     MIN = 50
#     COMMISSION = 0.015
#     BONUS = 0.03
#     TAX = 0.10
#     OPERATION: int
#     save_list = []
#     def __init__(self):
#         self.OPERATION = 0
#     def up_balance(self, cash: int) -> tuple[int, int] | None:
#         if cash % self.MIN == 0:
#             self.BALANCE += cash
#             self.OPERATION += 1
#             self.save_list.append(f"операция зачисления - зачислено: {cash}, баланс: {self.BALANCE}")
#             return self.BALANCE, self.OPERATION
#         else:
#             return None
#     def give_money(self, cash: int, commission: int) -> tuple[int, int] | None:
#         if cash % self.MIN == 0 and self.BALANCE > 0 and self.BALANCE - (cash + commission) >= 0:
#             self.BALANCE -= cash
#             self.BALANCE -= commission
#             self.OPERATION += 1
#             self.save_list.append(f"операция снятия - снято: {cash}, баланс: {self.BALANCE}")
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
# print(bank.save_list)