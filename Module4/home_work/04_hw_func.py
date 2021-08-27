# Написать программу, выполняющую операции (сложение и вычитание) с простыми дробями.
# Дроби вводятся и выводятся в формате: n x/y
# ,где n - целая часть, x - числитель, у - знаменатель.
# Дроби могут быть отрицательные и не иметь целой части, или иметь только целую часть.

# Примеры:
# Ввод: 5/6 + 4/7 (всё выражение вводится целиком в виде строки)
# Вывод: 1 17/42  (результат обязательно упростить и выделить целую часть)
# Ввод: -2/3 - -2
# Вывод: 1 1/3


def calculate(expression):
    expression = ' '.join(expression.split())
    expression = expression.replace(' - ', ' + -').replace('--', '')
    operands = expression.split(' + ')
    tup_1st_op = fraction_to_tuple(operands[0])
    tup_2nd_op = fraction_to_tuple(operands[1])
    tup_result = (tup_1st_op[0] * tup_2nd_op[1] + tup_1st_op[1] * tup_2nd_op[0], tup_1st_op[1] * tup_2nd_op[1])
    tup_result = simplify_tuple(tup_result)
    return tuple_to_fraction(tup_result)


def fraction_to_tuple(fract):
    """
    превращает дробь в кортеж
    -2/3 => (-2, 3)
    """
    fract = fract.strip().replace('- ', '-')
    int_part = num = 0
    den = 1
    if ' ' not in fract and '/' not in fract:
        int_part = int(fract)
    elif ' ' in fract:
        tmp = fract.split(' ')
        int_part = int(tmp[0])
        fract = tmp[1]
    if '/' in fract:
        tmp = fract.split('/')
        num = int(tmp[0]) if int_part >= 0 else -int(tmp[0])
        den = int(tmp[1])
    return int_part * den + num, den


def simplify_tuple(tup):
    """
    упрощает кортеж
    (-10, 6) => (-5, 3)
    """
    lst = list(tup)
    for i in range(min([abs(i) for i in lst]), 1, -1):
        if lst[0] % i == 0 and lst[1] % i == 0:
            lst[0] = int(lst[0] / i)
            lst[1] = int(lst[1] / i)
            lst = simplify_tuple(lst)
            break
    return tuple(lst)


def tuple_to_fraction(tup):
    """
    превращает кортеж в дробь
    (-10, 6) => -1 4/6
    """
    num, den = tup
    fraction = '-' if num < 0 else ''
    num = abs(num)
    int_part = num // den
    num = num - int_part * den
    if int_part > 0:
        fraction += f'{int_part} '
    if num > 0:
        fraction += f'{num}/{den}'
    return fraction or '0'


print('5/6 + 4/7 =', calculate('5/6 + 4/7'))
print('-2/3 - -2 =', calculate('-2/3 - - 2'))
print('7/8 + 1/6 =', calculate('7/8 + 1/6'))
print('-4 5/12 + 1/8 =', calculate('-4 5/12 + 1/8'))
print('2/12 + 9 =', calculate('2/12 + 9'))
print('- 1 1/2 - - 1 20/40 =', calculate('- 1 1/2 - - 1 20/40'))
print('1 2/3 - 12/18 =', calculate('1 2/3 - 12/18'))
