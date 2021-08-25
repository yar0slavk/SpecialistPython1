# Даны координаты центров двух окружностей (x1; y1) (x2; y2) и и их радиусы  R1 и R2.
# Находится ли одна окружность целиком внутри другой

def distance(x1, y1, x2, y2):
    return ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5


def inside(c1, r1, c2, r2):
    return distance(*c1, *c2) <= abs(r1 - r2)


print(inside(c1=(3, -3), r1=2, c2=(0, 0), r2=7))
print(inside(c1=(0, 0), r1=7, c2=(0, 3), r2=4))
print(inside(c1=(0, 3), r1=4, c2=(-4, -3), r2=3))
print(inside(c1=(3, -3), r1=2, c2=(-4, -4), r2=3))
