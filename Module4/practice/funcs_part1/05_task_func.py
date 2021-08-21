# Даны координаты трех точек (xa; ya) (xb; yb) (xc; yc), если соединить эти точки отрезками
# и получится треугольник, то нужно найти его периметр и площадь.
# Если по заданным точкам треугольник построить нельзя, выведите соответствующее сообщение.
# Подсказка: для нахождения площади используйте Теорему Герона

def can_triangle(p1, p2, p3):
    return not (p1 == p2 or p2 == p3 or p1[0] == p2[0] == p3[0] or p1[1] == p2[1] == p3[1])


def distance(x1, y1, x2, y2):
    return ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5


def get_triangle_info(a, b, c):
    if can_triangle(a, b, c):
        dist_ab = distance(a[0], a[1], b[0], b[1])
        dist_bc = distance(b[0], b[1], c[0], c[1])
        dist_ac = distance(a[0], a[1], c[0], c[1])
        p = dist_ab + dist_bc + dist_ac
        p2 = p / 2
        s = (p2 * (p2 - dist_ab) * (p2 - dist_bc) * (p2 - dist_ac)) ** 0.5
        result = f'Периметр = {p:2f}\nПлощадь = {s:.2f}'
    else:
        result = 'по заданным точкам треугольник построить нельзя'
    print(result)


get_triangle_info((10, 12), (14, 18), (12, 12))
print()
get_triangle_info((0, 0), (2, 0), (0, 2))
print()
get_triangle_info((0, 0), (2, 0), (0, 0))
