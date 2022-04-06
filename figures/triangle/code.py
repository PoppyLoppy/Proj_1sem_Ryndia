from math import sqrt
_a = 7
_b = 2
_c = 8


def triangle_perimeter(x=_a, y=_b, z=_c):
    return x + y + z


def triangle_area(x=_a, y=_b, z=_c):
    p = (x + y + z)/2
    return sqrt(p * (p - x) * (p - y) * (p - z))
