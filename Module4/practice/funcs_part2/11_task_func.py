# Используя функцию average() из предыдущей задачи, найдите среднее арифметическое всех элементов списка и кортежа

def average(*args):
    return sum(args)/len(args)


def gen_list(size, at=-10, to=10):
    import random  # импорт в функции возможен, но не рекомендуется PEP-8
    """
    :param size: кол-во элементов списка
    :param at: минимально возможное значение элементов
    :param to: максимально возможное значение элементов
    :return: списко из size произвольных элементов вдиапазоне at..to 
    """
    return [random.randint(at, to) for _ in range(size)]


my_list = gen_list(10)
my_tuple = 5, 7, -4, 10, 8

print(my_list)
print(average(*my_list))
print(my_tuple)
print(average(*my_tuple))
