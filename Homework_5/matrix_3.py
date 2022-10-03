# Выполнить обработку элементов квадратной матрицы А,
# имеющей N строк и N столбцов. Найти сумму элементов,
# стоящих на главной диагонали, и сумму элементов,
# стоящих на побочной диагонали.

from random import randint


def summ_main_diagonal(matrix):
    return sum([matrix[i][i] for i in range(len(matrix))])


def summ_sec_diagonal(matrix, N):
    summ = 0
    for row in range(N):
        for column in range(N):
            if row + column == N - 1:
                summ += matrix[row][column]
    return summ


N = randint(1, 5)
matrix = [[randint(1, 9) for column in range(N)] for row in range(N)]

for row in matrix:
    print(row)

print("-----------")
print("The sum of the main diagonal's elements:", summ_main_diagonal(matrix))
print(
    "The sum of the secondary diagonal's elements:",
    summ_sec_diagonal(matrix, N),
)
