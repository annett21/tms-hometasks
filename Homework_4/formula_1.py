from math import sqrt, log, cos, sin


def calculate_one(n, x):
    summa = 0
    for k in range(1, n + 1):
        summa += (log(abs(x + k))) ** 2 * cos(
            (k + pow(sin(x), 1 / 5)) / (k * x)
        )
    return summa * (1 / 45 * sqrt(3 ** (x + n)))


for n in range(10, 16):
    for x in (a / 100 for a in range(60, 111, 25)):
        result = calculate_one(n, x)
        print(f"{n=} {x=} {result=}")
