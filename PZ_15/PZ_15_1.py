# Вариант 21.
# В матрице найти минимальный элемент в предпоследней строке.

from random import randint

rows = randint(3, 10)
columns = randint(3, 10)

matrix = [[randint(0, 10) for i in range(columns)] for j in range(rows)]

print('Матрица: ')
for i in range(rows):
    print(matrix[i])

pinultimate_column = []

for j in range(rows):
    pinultimate_column.append(matrix[j][-2])
print(f'Минимальный элемент в предпоследней строке: {min(pinultimate_column)}')
