# Вариант 21.
# Даны две последовательности. Найти элементы, различные для двух последовательностей и их среднее арифметическое.

from random import randint

first = [randint(-50, 50) for i in range(randint(3, 10))]
print(f'Первая последовательность: {first}')

second = [randint(-50, 50) for i in range(randint(3, 10))]
print(f'Вторая последовательность: {second}')
diff = set()

for i in first:
    for j in second:
        if i != j:
            diff.add(i)
            diff.add(j)

print(f'Элементы, различные для двух последовательностей: {diff}')
print(f'Среднее арифметическое элементов: {sum(diff)/len(diff)}')
