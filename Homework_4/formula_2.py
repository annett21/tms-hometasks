from math import sqrt, log, sin, pi, e


def calculate_two(n, x):
    summa = 0
    for k in range(1, n + 1):
        summa += sqrt(pow((x**k + 1), 1 / k) + pow(e ** (k - 3), 1 / k)) / (
            1 + log(x, 10)
        )
    return summa * sin((pi * n) / (x + 3))


for n in range(10, 16):
    for x in (a / 100 for a in range(60, 111, 25)):
        result = calculate_two(n, x)
        print(f"{n=} {x=} {result=}")
