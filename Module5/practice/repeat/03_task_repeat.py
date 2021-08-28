# Найдите количество чисел являющихся палиндромами в диапазоне от a до b включительно
# Известно, что a и b целые положительные числа.
def palindrome(number):
    return str(number) == str(number)[::-1]


def get_palindrome_count(of, to):
    cnt = 0
    for i in range(of, to + 1):
        if palindrome(i):
            cnt += 1
    return cnt


a = 10
b = 200
print(get_palindrome_count(a, b))
