# Проверить, все ли числа в последовательности уникальны
from random import randint

some_list = [randint(1, 100) for _ in range(10)]
print(some_list)

if len(set(some_list)) == len(some_list):
    print("All numbers in the array are uniqie")
else:
    print("Not all numbers in the array are uniqie")
