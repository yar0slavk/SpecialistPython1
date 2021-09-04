# Дан список, заполненный произвольными целыми числами.
# Примечание: для генерации списка используйте функцию.
# Найдите:
# 1. Количество элементов списка не превышающие 10
# 2. Сумму всех положительных элементов списка
# 3. Среднее арифметическое всех четных элементов
import random


def create_list(size, of=0, to=100):
    return [random.randint(of, to) for _ in range(size)]


lst = create_list(8, of=-10, to=20)
print(lst)

cnt = len([el for el in lst if el <= 10])
print(cnt)

s = sum([el for el in lst if el > 0])
print(s)

even_lst = [el for el in lst if el % 2 == 0]
print(sum(even_lst) / len(even_lst))
