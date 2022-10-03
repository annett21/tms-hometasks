# С помощью анонимной функции извлеките из списка числа, делимые на 15
from random import randint

some_list = [randint(1, 100) for _ in range(10)]
print(some_list)

print(list(filter(lambda x: x % 15 == 0, some_list)))
