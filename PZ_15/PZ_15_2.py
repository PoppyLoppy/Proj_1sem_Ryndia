# Вариант 21.
# В квадратной матрице элементы на главной диагонали увеличить в 2 раза.

from random import randint

width = randint(3, 10)

matrix = [[randint(-10, 10) for i in range(width)] for j in range(width)]

print('Матрица: ')
for i in range(width):
    print(matrix[i])

el = 0
row = 0
while el <= width - 1:
    matrix[row][el] = matrix[row][el] ** 2
    el += 1
    row += 1

print('Новая матрица: ')
for i in range(width):
    print(matrix[i])
