# 2.1 Дан список, вывести только уникальные элементы

from time import time
from typing import Iterable
from random import randint


def time_counter(func):
    def timer(*args, **kwargs):
        start = time()
        result = func(*args, **kwargs)
        end = time()
        print(f"Time of {func.__name__} function execution:", end - start)
        return result

    return timer


@time_counter
def find_unique_numbers(array: Iterable) -> Iterable:
    return [i for i in array if array.count(i) == 1]


@time_counter
def find_unique(array: Iterable) -> Iterable:
    return list(filter(lambda i: array.count(i) == 1, array))


some_array = [randint(1, 100) for _ in range(10)]
print("Given array:", some_array)

print("Unique numbers:", find_unique_numbers(some_array))
print("Unique numbers:", find_unique(some_array))
