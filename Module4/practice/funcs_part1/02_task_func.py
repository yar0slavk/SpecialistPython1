# Напишите функцию,  определяющую является ли число палиндромом.
# Палиндром - число читающееся одинаково слева направо и справа налево.
# Пример палиндрома: 34543
# * попробуйте решить данную задачу, не преобразуя число к строке

def palindrome(number):
    return str(number) == str(number)[::-1]


def get_digit_count(number):
    if number > 0:
        number = 1 + get_digit_count(number // 10)
    return number


def palindrome(number):
    flag = True
    digit_count = get_digit_count(number)
    for i in range(digit_count // 2):
        last_digit = number // (10 ** i) % 10
        first_digit = number // (10 ** (digit_count - i - 1)) % 10
        if last_digit != first_digit:
            flag = False
            break
    return flag


def palindrome(number):
    reverse_number = 0
    digit_count = get_digit_count(number)
    for i in range(digit_count):
        digit = number // (10 ** i) % 10
        reverse_number += digit * (10 ** (digit_count - i - 1))
    return reverse_number == number


# Тестируем функцию
print(palindrome(3454))
print(palindrome(3443))
print(palindrome(1234541))
print(palindrome(1234321))
print(palindrome(77777))
