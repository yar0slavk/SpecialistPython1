# Даны номер месяца и номер года. Найдите сколько дней в этом месяце.
# При вводе неверного номера месяца или некорректного значения программа должна сообщить об ошибке
# и попросить ввести корректные данные. Также необходимо учесть високосный или не високосный год.
# Алгоритм проверки на високосный год оформите в виде отдельной функции.
#
# Входная строка содержит два целых числа – номер месяца (возможно, неправильный) и номер года.
import sys


def is_leap_year(num_year):
    return num_year % 4 == 0 and num_year % 100 != 0 or num_year % 400 == 0


while True:
    try:
        input_data = input('Номер месяца и номер года (через пробел): ')
        month, year = input_data.split()
        month = int(month)
        year = int(year)
        if not (1 <= month <= 12):
            raise ValueError
        break
    except ValueError:
        print("Введены некоррекные данные, попробуйте снова")
    except Exception as e:
        print("Зачем же так грубо? -)", e)
        sys.exit()

if month in (1, 3, 5, 7, 8, 10, 12):
    days = 31
elif month in (4, 6, 9, 11):
    days = 30
elif month == 2 and is_leap_year(year):
    days = 29
else:
    days = 28

print(f'В месяце №{month} {year} года содержится {days} дней')
