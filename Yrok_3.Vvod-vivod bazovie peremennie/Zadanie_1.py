﻿# Задание №1
# Давай представим, что мы пишем бэкенд для сайта ветеринарной клиники. 
# Нам нужно написать программу, которая будет запрашивать у пользователя вид питомца, его возраст и кличку, а потом выведет все эти данные в одно предложение. 
# Например: Это желторотый питон по кличке "Каа". Возраст: 34 года.

pet_type = input('Введите вид питомца: ')
pet_name = input('Введите кличку питомца: ')
pet_age = input('Введите возраст: ')

print('Это ' + pet_type + ' по кличке ' + pet_name + '. Возраст: ' + pet_age + ' года.')