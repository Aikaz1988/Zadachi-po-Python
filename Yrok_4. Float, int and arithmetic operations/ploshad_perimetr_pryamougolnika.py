﻿# Задание №1
# Пользователь вводит стороны прямоугольника, выведите его площадь и периметр. 
# На вход программе могут подаваться как целые числа, так и вещественные

a = float(input("Введите длину прямоугольника: "))
b = float(input("Введите ширину прямоугольника: "))
p = 2 * (a + b) # Определяем периметр прямоугольника
s = a * b # Определяем площадь прямоугольника
print("Площадь прямоугольника = ",p,'см2\n')
print("Периметр прямоугольника = ",s,'см\n')