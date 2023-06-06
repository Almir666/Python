from random import randint as rnd

def gues_num(low: int, high: int, try_count: int):
    num = rnd(low, high + 1)
    for __ in range(try_count):
        user_value = int(input(f"Введите число от {low} до {high}: "))
        if user_value == num:
            print(f"Вы угадали! загаданное число - {num}")
            break
        if user_value < num:
            print("Загаданное число больше")
        else:
            print("Загаданное число меньше")
    else:
        print("У вас закончились попытки")