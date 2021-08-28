# Вы решили сделать вклад в банк некоторой суммы на n лет.
# Банк вам предложил x% годовых с расчетом по простым процентам или
# y% годовых по сложным % с периодом капитализации 1 месяц.
# При заданных процентных ставках, определите какой из вкладов вам выгоднее на 5 лет.
# Примечание: формулы расчета простых и сложных процентов ищите на гуглодиске в папке с материалами.


def simple_deposit(dep, rate, years):
    return dep * (1 + years * rate / 100)


def complex_deposit(dep, rate, years, cap):
    """
    cap – количество периодов капитализации в году
    """
    return dep * (1 + rate / 100 / cap) ** (cap * years)


def choose_deposit(dep, s_rate, c_rate, years=5, c_cap=12):
    s_total = simple_deposit(dep, s_rate, years)
    c_total = complex_deposit(dep, c_rate, years, c_cap)
    if s_total > c_total:
        result = f'SIMPLE_DEPOSIT is better ({s_total:.2f} > {c_total:.2f})'
    elif s_total < c_total:
        result = f'COMPLEX_DEPOSIT is better ({c_total:.2f} > {s_total:.2f})'
    else:
        result = f'Any deposit ({s_total:.2f})'
    return result


p = 100000
x = 5
y = 4
print(choose_deposit(p, x, y))
