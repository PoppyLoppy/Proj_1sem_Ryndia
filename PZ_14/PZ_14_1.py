# Вариант 21.
# В исходном текстовом файле (hotline1.txt) найти все номера телефонов, соответствующих шаблону 8(
# 000)000-00-00. Посчитать количество полученных элементов. После фразы «Горячая линия» добавить фразу «Министерства
# образования Ростовской области», выполнив манипуляции в новом файле.

import re

with open('hotline.txt', 'r', encoding='utf-8') as inp:
    text = inp.read()
    add = re.subn(r'«Горячая линия»', '«Горячая линия» «Министерства образования Ростовской области»', text)
    text = add[0]
    count_of_add = add[1]
    print(f'Количество замен: {count_of_add}')
    count_of_03 = len(re.findall(r'8.*03\n', text))
    print(f'Количество номеров, оканчивающихся на 03: {count_of_03}')
    count_of_50 = len(re.findall(r'8.*50\n', text))
    print(f'Количество номеров, оканчивающихся на 50: {count_of_50}')
    ege_gia = re.findall(r'(ЕГЭ|ГИА).* (8.*)\n', text)
    number_of_ege_gia = [i[1] for i in ege_gia]
    print(f'Номера телефонов, связанных с ЕГЭ и ГИА: {number_of_ege_gia}')
    with open('hotline.txt', 'w', encoding='utf-8') as out:
        out.write(text)
