from math import factorial, radians


def sinus(x):
    summa = 0
    next_part = 1
    eps = 0.0001
    n = 0
    while abs(next_part) > eps:
        next_part = (-1) ** n * ((x ** (2 * n + 1)) / (factorial(2 * n + 1)))
        summa += next_part
        n += 1
    return summa


def cosinus(x):
    summa = 0
    next_part = 1
    eps = 0.0001
    n = 0
    while abs(next_part) > eps:
        next_part = (-1) ** n * ((x ** (2 * n)) / (factorial(2 * n)))
        summa += next_part
        n += 1
    return summa


x = float(input("Set anngle in degrees: "))
x = round(radians(x), 2)

print("Sin:", sinus(x))
print("Cos:", cosinus(x))
