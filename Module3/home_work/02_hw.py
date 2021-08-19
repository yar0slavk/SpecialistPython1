# Напишите алгоритм, заполняющий список произвольными целыми числами
# в диапазоне от -100 до 100. В списке должно быть n - элементов.
# Подсказка:
# для получения случайного числа используйте функцию randint() модуля random
import random
numbers = []
n = int(input('Input n: '))

# while len(numbers) != n:
#     numbers.append(random.randint(-100, 100))

numbers = [random.randint(-100, 100) for i in range(n)]
print(numbers)
