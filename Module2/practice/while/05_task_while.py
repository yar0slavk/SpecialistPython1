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

# 2 cycles
i = 1
while i <= a:
    tmp = ''
    j = 1
    while j <= a:
        if j == i or j == a-i+1:
            tmp += SIGN
        else:
            tmp += ' '
        j += 1
    print(tmp)
    i += 1

# 1 cycle
tmp = ''
i = 1
while i <= a ** 2:
    if i == a*((i-1)//a) + (i-1)//a + 1 or i == ((i-1)//a+1)*(a-1) + 1:
        tmp += SIGN
    else:
        tmp += ' '
        
    if i % a == 0:
        print(tmp)
        tmp = ''
    i += 1
