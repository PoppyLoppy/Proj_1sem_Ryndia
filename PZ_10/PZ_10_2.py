# Вариант 21.
# Из предложенного текстового файла (text18-21.txt) вывести на экран его содержимое, количество знаков препинания.
# Сформировать новый файл, в который поместить текст в стихотворной форме выведя строки в обратном порядке.
d = 0
f1 = open('text18-21.txt', encoding='UTF-8')
print(f1.read())

for i in open('text18-21.txt', encoding='UTF-8'):
    for j in i:
        if j == ',':
            d += 1
        if j == '.':
            d += 1
        if j == '!':
            d += 1

print('Количество знаков препинания:', d)

f1 = open('text18-21.txt', encoding='UTF-8')
N = f1.readlines()
N = N[::-1]
f1.close()

f2 = open('text18-21-2.txt', 'w')
f2.writelines(N)
f2.close()
