from time import time


def time_counter(func):
    def timer(*args, **kwargs):
        start = time()
        result = func(*args, **kwargs)
        end = time()
        print("Time of function execution:", end - start)
        return result

    return timer


@time_counter
def factorial_one(n: int) -> int:
    factorial = 1
    for i in range(2, n + 1):
        factorial *= i
    return factorial


print(factorial_one(5))
