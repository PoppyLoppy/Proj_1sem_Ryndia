# Вариант 21
# Дано вещественное число X (|X|<1) и целое число N (>0). Найти значение выражения X - X2/2 + X3/3 - ... + (-1)N-1XN/N
x = input("Введите первое число до 1: ")
while type(x) != float:  # обработка исключений
    try:
        x = float(x)
    except ValueError:
        print("Неправильный ввод")
        x = float(input("Введите первое число: "))
while abs(x) >= 1:
    print("Неправльный ввод!")
    x = float(input("Введите первое число до 1: "))
n = input("Введите второе число, больше нуля: ")
while type(n) != int:  # обработка исключений
    try:
        n = int(n)
    except ValueError:
        print("Неправильный ввод")
        n = int(input("Введите второе целое число: "))
while n <= 0:
    print("неправильный ввод")
    n = int(input("Введите второе число, больше нуля"))
s = 0
while n != 0:
    s += (-1) ** (n - 1) * (x ** n) / n
    n -= 1
print(float(s))
