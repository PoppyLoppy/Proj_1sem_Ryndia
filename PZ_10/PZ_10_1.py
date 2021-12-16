# Вариант 21.
# Средствами языка Python сформировать два текстовых файла (.txt), содержащих по одной
# последовательности из целых положительных и отрицательных чисел. Сформировать
# новый текстовый файл (.txt) следующего вида, предварительно выполнив требуемую
# обработку элементов.

n1 = ['-43 -6 12 -66 10 -45 100 -15']  # создаём первый файл
f1 = open('data_1.txt', 'w')
f1.writelines(n1)
f1.close()

n2 = ['90 -5 4 2 54 -5 -6']  # создаём второй файл
f1 = open('data_2.txt', 'w')
f1.writelines(n2)
f1.close()

f3 = open('data_3.txt', 'w')  # записываем в новый файл содержимое первого
f3.write('Содержимое первого файла: ')
f3.write('\n')
f3.writelines(n1)
f3.close()

f1 = open('data_2.txt')  # разбиваем строку и её значения преобразуем в числа
k = f1.read().split()
for i in range(len(k)):
    k[i] = int(k[i])
f1.close()

f1 = open('data_1.txt')  # находим отрицательные числа
a = []
for i in range(len(k)):
    if int(k[i]) < 0:
        a.append(k[i])
f1 = open('data_3.txt', 'a')  # открываем файл для дозаписи
f1.write('\n')
print('Отрицательные числа: ', file=f1)
print(*a, file=f1)
f1.close()

f1 = open('data_1.txt')  # находим количество отрицательных чисел
t = 0
for i in range(len(k)):
    if int(k[i]) < 0:
        t += 1

f1 = open('data_3.txt', 'a')  # открываем файл для дозаписи
print('Количество отрицательных элементов: ', file=f1)
print(t, file=f1)
f1.close()

f1 = open('data_1.txt')  # находим среднеее арифметическое
s = 0
for i in range(len(k)):
    s += k[i]
s = s / len(k)
f1 = open('data_3.txt', 'a')  # открываем файл для дозаписи
print('Среднеее арифметическое: ', file=f1)
print(s, file=f1)
f1.close()

f3 = open('data_3.txt', 'a')  # записываем в новый файл содержимое второго
f3.write('\n')
f3.write('Содержимое второго файла: ')
f3.write('\n')
f3.writelines(n2)
f3.close()

f1 = open('data_1.txt')  # находим положительные числа
a = []
for i in range(len(k)):
    if int(k[i]) > 0:
        a.append(k[i])
f1 = open('data_3.txt', 'a')  # открываем файл для дозаписи
f1.write('\n')
print('Положительные числа: ', file=f1)
print(*a, file=f1)
f1.close()

f1 = open('data_1.txt')  # находим количество положительных чисел
t = 0
for i in range(len(k)):
    if int(k[i]) > 0:
        t += 1

f1 = open('data_3.txt', 'a')  # открываем файл для дозаписи
print('Количество положительных элементов: ', file=f1)
print(t, file=f1)
f1.close()

f1 = open('data_1.txt')  # находим сумму положительных чисел
s = 0
for i in range(len(k)):
    if int(k[i]) > 0:
        s += k[i]

f1 = open('data_3.txt', 'a')  # открываем файл для дозаписи
print('Сумма положительных чисел: ', file=f1)
print(s, file=f1)
f1.close()
