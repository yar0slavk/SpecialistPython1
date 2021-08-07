# Дано целое число m, задающее номер месяца года.
# Выведите строку — название времени года, соответствующего данному месяцу.
# Формат входных данных: дано целое число m (1 ≤ m ≤ 12).
# Формат выходных данных: требуется вывести название времени года

m = int(input('Input month (num): '))

if 3 <= m <= 5:
    print('Spring')
elif 6 <= m <= 8:
    print('Summer')
elif 9 <= m <= 11:
    print('Autumn')
else:
    print('Winter')
