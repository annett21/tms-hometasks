from math import sqrt, sin, e, pi


def calculate_four(n, x):
    summa = 0
    for k in range(1, n + 1):
        summa += (sin((k - 1) / (k + 1))) ** 2 + e ** sqrt(x / k)
    return summa * (pi / ((x ** (1 / 3)) + 3 / (x + 5)))


for n in range(10, 16):
    for x in (a / 100 for a in range(60, 111, 25)):
        result = calculate_four(n, x)
        print(f"{n=} {x=} {result=}")
