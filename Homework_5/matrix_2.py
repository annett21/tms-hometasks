# Выполнить обработку элементов прямоугольной матрицы А,
# имеющей N строк и М столбцов. Все элементы имеют целый тип.
# Дано целое число Н. Определить, какие столбцы имеют хотя бы
# одно такое число, а какие не имеют.

from random import randint

matrix = []

N = 5
M = 3

for row in range(N):
    matrix.append([])
    for column in range(M):
        matrix[row].append(randint(10, 30))

for row in matrix:
    print(row)

H = randint(10, 30)

print("------------")
for column in range(M):
    if H in [num[column] for num in matrix]:
        print(f"The column {column} has a number {H}")
    else:
        print(f"The column {column} doesn't have a number {H}")
