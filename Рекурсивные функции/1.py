# Вычислить сумму элементов набора чисел

def sum(el1):
    if len(el1) == 1:
        return el1[0]
    return el1[0] + sum(el1[1:])


print("Сумма элементов набора чисел:", sum([1, 2, 3, 4, 5, 6]))

# Вычислить количество отрицательных чисел в наборе

def count(el2):
    if len(el2) == 1:
        if el2[0] < 0:
            return 1
        return 0
    if el2[0] < 0:
        return 1 + count(el2[1:])
    else:
        return 0 + count(el2[1:])


print("Количество отрицательных чисел в наборе:", count([-1, 2, -3, -4, 5, 6]))


# Вычисление суммы чисел с поддержкой вложенных списков

def sum2(el3):
    if len(el3) == 1:
        return el3[0]
    if type(el3[0]) == list:
        return sum2(el3[0]) + sum2(el3[1:])
    return el3[0] + sum2(el3[1:])


print("Сумма чисел с поддержкой вложенных списков:", sum2([1, 2, [1, 2, 3], 4, 5, [4, 5, 6], 6]))


# Реверсирование числа

def reverse(a):
    a = str(a)
    if len(a) == 1:
        return a
    return a[-1] + reverse(a[:-1])


print("Реверсирование числа:", reverse(234))

# Возведение числа x в степень y

def power(x, y):
    if y == 0:
        return 1
    return x * power(x, y - 1)

print("Возведение числа x в степень y:", power(3, 3))

# Определение максимального элемента списка

def maximum(el4):
    if len(el4) == 1:
        return el4[0]
    if el4[0] > maximum(el4[1:]):
        return el4[0]
    else:
        return maximum(el4[1:])


print("Определение максимального элемента списка:", maximum([1, 4, 3, 6]))


# Возврат ряда Фибоначчи

def fib(n, el5=[0, 1]):
    num1 = el5[-1]
    num2 = el5[-2]
    if (num1 + num2) <= n:
        el5 += [num1 + num2]
        return fib(n, el5)
    else:
        return el5


print("Возврат ряда Фибоначчи:", fib(13))
