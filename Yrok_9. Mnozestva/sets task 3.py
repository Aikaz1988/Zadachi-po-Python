# Задание №3
# Во входную строку водится последовательность чисел через пробел. 
# Для каждого числа выведите слово ”YES” (в отдельной строке), если это число ранее встречалось в последовательности 
# или ”NO”, если не встречалось.

numbers = input('Введите последовательность чисел: ').split()

seq_numbers = set() # sequence of numbers последовательность чисел

for number in numbers:
    if number in seq_numbers:
        print('YES')
    else:
        print('NO')
    seq_numbers.add(number) # добавляем число в последовательность чисел