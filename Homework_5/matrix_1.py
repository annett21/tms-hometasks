# Выполнить обработку элементов прямоугольной матрицы А,
# имеющей N строк и М столбцов. Найти сумму элементов всей матрицы.
# Определить, какую долю в этой сумме составляет сумма элементов каждого
# столбца. Результат оформить в виде матрицы из N+1 строк и M столбцов.

from random import randint
matrix = []

N = 3
M = 4

for i in range(N):
    matrix.append([])
    for j in range(M):
        matrix[i].append(randint(1, 9))

all_sum = sum([sum(row) for row in matrix])

matrix.append([
    round(sum([row[column] for row in matrix]) / all_sum, 2)
    for column in range(M)
])

for row in matrix:
    print(row)
