# Вводятся целые числа A и B.
# Гарантируется, что A ≤ B.
# Выведите все четные числа на заданном отрезке через пробел.

a = int(input('Введите число А: '))
b = int(input('Введите число B: '))

while a <= b:
    if a % 2 == 0:
        print(a)
    a += 1
