# Дан список из n элементов, заполненный произвольными целыми числами в диапазоне от -100 до 100.
# Вывести на экран сумму всех положительных элементов кратных двум.

import random

n = int(input('Input n: '))
numbers = [random.randint(-100, 100) for i in range(n)]
print(numbers)

# sum = 0
# for num in numbers:
#     if num > 0 and num % 2 == 0:
#         sum += num
# print('Sum =', sum)

print('Sum =', sum([num for num in numbers if num > 0 and num % 2 == 0]))
