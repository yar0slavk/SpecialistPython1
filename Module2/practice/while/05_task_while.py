# Вывод символов по диагоналям
# Даны сторона квадрата. Вывести его диагонали символами #.
# Формат входных данных: На вход программе одно целое число a (2<a≤30) - сторона квадрата.
# Формат выходных данных: Требуется вывести диагонали символами # (см. примеры)
# Примеры:
# a = 6
#    #
 #  #
  ##
  ##
 #  #
#    #

# a = 3
# #
 #
# #

SIGN = '#'
a = int(input('Input a (2 < a <= 30): '))
# variant1
print('2 cycles 1..a')
i = 1
while i <= a:
    tmp = ''
    j = 1
    while j <= a:
        if j == i or j == a - i + 1:
            tmp += SIGN
        else:
            tmp += ' '
        j += 1
    print(tmp)
    i += 1
# variant2
print('\n1 cycle 1..a**2')
tmp = ''
i = 1
while i <= a ** 2:
    if i == a * ((i - 1) // a) + (i - 1) // a + 1 or i == ((i - 1) // a + 1) * (a - 1) + 1:
        tmp += SIGN
    else:
        tmp += ' '

    if i % a == 0:
        print(tmp)
        tmp = ''
    i += 1
# variant3
print('\n1 cycle 1..a')
num_spaces = 0
i = 1
while i <= a:
    tmp = SIGN
    if i <= a / 2:
        num_spaces = a - i * 2
    else:
        num_spaces = i * 2 - a - 2
    if num_spaces >= 0:
        tmp += ' ' * num_spaces + SIGN
    print(tmp.center(a))
    i += 1
