from math import factorial


def exponent(x):
    e = 0
    part_sum = 1
    eps = 0.0001
    n = 0
    while part_sum > eps:
        part_sum = (x**n) / factorial(n)
        e += part_sum
        n += 1
    return e


print("e ** x =", exponent(5))
