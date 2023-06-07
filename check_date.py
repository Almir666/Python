from datetime import datetime
from sys import argv

def check_leap_year(date: str) -> bool:
    CHECK_NORMAL_1 = 4
    CHECK_NORMAL_2 = 100
    CHECK_NORMAL_3 = 400
    YEARS = range(1, 10000)
    year = int(date.split(".")[-1])
    if year in YEARS and year % CHECK_NORMAL_1 == 0 and year % CHECK_NORMAL_2 != 0 or year % CHECK_NORMAL_3 == 0:
        return True
    return False
def check_date(year: str) -> bool:
    if datetime.strptime(year, "%d.%m.%Y").date():
        check_leap_year(year)
        return True
    else:
        return False

def final_check(date: str) -> str:
    if check_date(date):
        return "Такая дата может существовать, это високосный год" if check_leap_year(date) \
            else "Такая дата может существовать, это не високосный год"
    else:
        return "Такой даты не может быть"