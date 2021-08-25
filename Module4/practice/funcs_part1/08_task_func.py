# Напишите функцию находящую n-ое число Фибоначчи.

def get_fibonacci(n):
    fib_list = [0, 1]
    for _ in range(n - 1):
        fib_list.append(fib_list[-2] + fib_list[-1])
    return fib_list[n]


def get_fibonacci(n):
    if 0 <= n <= 1:
        cur = n
    else:
        prev, cur = 0, 1
        for _ in range(n - 1):
            prev, cur = cur, prev + cur
    return cur

# очень "тяжелый" вариант
# def get_fibonacci(n):
#     next_fib = n
#     if n >= 2:
#         next_fib = get_fibonacci(n - 2) + get_fibonacci(n - 1)
#     return next_fib


print('F0 =', get_fibonacci(0))
print('F1 =', get_fibonacci(1))
print('F2 =', get_fibonacci(2))
print('F3 =', get_fibonacci(3))
print('F4 =', get_fibonacci(4))
print('F5 =', get_fibonacci(5))
print('F10 =', get_fibonacci(10))
