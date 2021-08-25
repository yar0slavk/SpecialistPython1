# Дан шестизначный номер билета. Определить, является ли билет счастливым.
# Решение реализовать в виде функции.
# Билет считается счастливым, если сумма его первых и последних цифр равны.

def lucky_ticket(ticket_number):
    digit_list = [int(digit) for digit in str(ticket_number)]
    return len(digit_list) == 6 and sum(digit_list[:3]) == sum(digit_list[3:])


def lucky_ticket(ticket_number):
    sum_first = sum_last = 0
    if 10 ** 5 <= ticket_number <= 10 ** 6 - 1:
        for i in range(6):
            digit = ticket_number // 10 ** i % 10
            if i < 3:
                sum_first += digit
            else:
                sum_last += digit
    else:
        sum_first = None
    return sum_first == sum_last


# Тестируем функцию
print(lucky_ticket(123006))
print(lucky_ticket(12321))
print(lucky_ticket(436751))
