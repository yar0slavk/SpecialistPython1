# Напишите функцию, которая проверит, что точка (x, y)
# находится строго внутри окружности с центром в точке (xc, yc) и радиусом r:

def distance(x1, y1, x2, y2):
    return ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5


def point_in_circle(x, y, xc, yc, r):
    return distance(x, y, xc, yc) < r

print(point_in_circle(3,5,0,0,5))
print(point_in_circle(3,5,0,0,1))
print(point_in_circle(0,5,0,0,5))
