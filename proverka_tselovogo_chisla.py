﻿
a = int(input('Введите целое число: '))
if a == 0:
    print('нулевое число\n')
elif a > 0:
    if a % 2 == 0:
        print('положительное четное число\n')
    else:
        print('положительное нечетное число\n')
elif a < 0:
    if a % 2 == 0:
        print('отрицательное четное число\n')
    else:
        print('отрицательное нечетное число\n')
else:
    print('число не является четным\n')