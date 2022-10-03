def ln(x):
    if not abs(x) < 1:
        raise ValueError("|x| must be less then 1")

    ln = 0
    part_sum = 1
    eps = 0.0001
    n = 1

    while abs(part_sum) > eps:
        part_sum = (-1) ** (n + 1) * (x**n / n)
        ln += part_sum
        n += 1

    return ln


print("Ln(1 + x) =", ln(0.3))
