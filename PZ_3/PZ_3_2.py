# Вариант 21.
# Даны два числа. Вывести порядковый номер меньшего из них
a, b = input("Введите первое число: "), input("Введите второе число: ")
while type(a) != int:  # обработка исключений
    try:
        a = int(a)
    except ValueError:
        print("Неправильный ввод")
        a = input("Введите первое число: ")
while type(b) != int:  # обработка исключений
    try:
        b = int(b)
    except ValueError:
        print("Неправильный ввод")
        b = input("Введите второе число: ")
if a > b:
    print("2")
else:
    print("1")
