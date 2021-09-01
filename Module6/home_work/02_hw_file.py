# Дан файл data/info.txt, в каждой строке которого содержится строка или целое число
# Найдите сумму всех чисел, пропуская все строки содержащие не числовые значения
import os


def is_numeric(number):
    number = str(number).strip()
    if len(number) and number[0] in ('-', '+'):
        number = number[1:]
    return number.isnumeric()


path = os.path.join('data', 'info.txt')
sum = 0
with open(path, 'r') as f:
    for line in f:
        line = line.rstrip()
        if is_numeric(line):
            sum += int(line)
print(sum)
