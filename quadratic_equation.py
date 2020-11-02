from math import *


def quadratic_equation(a, b, c):
    if a == 0:
        return [-b / c]
    d = b * b - 4 * a * c
    if d < 0:
        return []
    if d == 0:
        return [-b / (2 * a)]
    x1 = (-b - sqrt(d)) / (2 * a)
    x2 = (-b + sqrt(d)) / (2 * a)
    return [x1, x2]


inputData = input()
a, b, c = [int(x) for x in inputData.split(',')]

res = quadratic_equation(a, b, c)
if len(res) == 0:
    print(-1)
else:
    [print(x, end=' ') for x in res]
