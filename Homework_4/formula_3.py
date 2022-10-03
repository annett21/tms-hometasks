from math import sqrt, log, sin, e


def calculate_three(n, x):
    summa = 0
    for k in range(1, n + 1):
        summa += (1 + ((k + 1) / n)) / (
            (e**k) * sqrt(x ** (k - 1)) + log(x, 10)
        )
    return summa * sqrt((sin(x / n)) ** 3)


for n in range(10, 16):
    for x in (a / 100 for a in range(60, 111, 25)):
        result = calculate_three(n, x)
        print(f"{n=} {x=} {result=}")
