from math import factorial, log


def one_plus_x(x, m):
    if not abs(x) < 1:
        raise ValueError("|x| must be less then 1")

    summa = 0
    part_sum = 1
    k = 0
    eps = 0.0001

    while part_sum > eps:
        part_sum = (m**k * (log(1 + x)) ** k) / factorial(k)
        print(part_sum)
        summa += part_sum
        k += 1

    return summa


x = 0.9
m = 3
print(f"(1 + {x})**{m} =", one_plus_x(x, m))
