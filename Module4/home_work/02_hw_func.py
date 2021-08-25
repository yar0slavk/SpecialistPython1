# Даны координаты трех точек (xa; ya) (xb; yb) (xc; yc),
# точки соединены отрезками AB, BC и AC. Найдите отрезок с минимальной длинной.
# Если отрезков с минимальной длиной несколько - вывести любой

# При решении задачи необходимо использовать функцию расстояния между двумя точками.

def distance(x1, y1, x2, y2):
    return ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5


def get_shortest_line(a, b, c):
    lines = {
        'AB': distance(*a, *b),
        'AC': distance(*a, *c),
        'BC': distance(*b, *c)
    }
    # print(lines)
    shortest = min(lines.items(), key=lambda x: x[-1])
    return shortest[0]


a = (0, 0)
b = (3, 0)
c = (3, 4)

print("Самый короткий отрезок:", get_shortest_line(a, b, c))  # Выводим название отрезка, например “АС”.
