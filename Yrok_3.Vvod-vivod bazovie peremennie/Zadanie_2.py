﻿# Задание №2
# А теперь мы с тобой напишем форму ввода ответа на тест по биологии для студентов. 
# Он должен запрашивать по порядку этапы развития человека (проверим твое умение гуглить, что тоже очень важно для программиста.) 
# и в конце вывести все стадии, разделенные знаком =>, что будет означать постепенный переход от одного к другому. 
# В следующих уроках мы дополним эту форму до полноценного теста, который будет проверять правильность ответов, а пока - начнем с малого. 
# Напоминаем, что разделить эти данные тебе поможет команда sep внутри команды print, 
# например, чтобы разделить переменные знаком + нужно ввести: print(a1, a2, a3, sep='+')
# Подсказка: последняя стадия развития - Homo sapiens sapiens.

print('Введите этапы развития человека по порядку')

a1 = input('Первый этап развития человека: ')
a2 = input('Второй этап развития человека: ')
a3 = input('Третий этап развития человека: ')
a4 = input('Четвертый этап развития человека: ')
a5 = input('Пятый этап развития человека: ')

print('Ваш ответ:', a1, a2, a3, a4, a5, sep=' => ')
print('Правильный ответ: Австралопитек (Australopithecus) => Человек умелый (homo habilis) => \nЧеловек прямоходящий (homo erectus) => Неандерталец (Homo neanderthalensis) => Человек разумный (Homo sapiens)')