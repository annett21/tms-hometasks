# Написать функцию для нахождения факториала числа.
# Две реализации: через рекурсию и без рекурсии


def factorial_one(n: int) -> int:
    factorial = 1
    for i in range(2, n + 1):
        factorial *= i
    return factorial


def factorial_two(n: int) -> int:
    if n <= 1:
        return 1
    return factorial_two(n - 1) * n


print(factorial_one(5))
print(factorial_two(5))
