# Сначала вводится число N, затем вводится ровно N целых чисел. 
# Подсчитайте, сколько из них равны нулю, и выведите это количество.

n = int(input("Введите число N: ")) # Вводим число N
count = 0 # Счетчик количества чисел
# Цикл for для ввода чисел. Вводится N целых чисел и проверяется, равны ли они нулю
for i in range(n):
    num = int(input("Введите целые числа: "))
    if num == 0: # Проверка равно ли число нулю
        count += 1 # Если да, увеличивается счетчик количества чисел.

print("Количество нулей:",count)