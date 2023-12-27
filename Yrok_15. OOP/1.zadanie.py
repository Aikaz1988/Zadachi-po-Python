# Задание №1
# Есть родительский класс:
# class Transport:
#    def __init__(self, name, max_speed, mileage):
#        self.name = name
#        self.max_speed = max_speed
#        self.mileage = mileage
# Создайте объект Autobus, который унаследует все переменные и методы родительского класса Transport и выведете его.
# Ожидаемый результат вывода:
# Название автомобиля: Renaul Logan Скорость: 180 Пробег: 12

class Transport:
    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage

class Autobus(Transport):
    pass  # Реализация класса не требуется, потому что нужны все переменные и методы родительского класса

# Создание экземпляра класса Autobus
auto = Autobus('Renaul Logan', 180, 12)

# Выводим на экран информацию об автобусе
print(f"Название автомобиля: {auto.name} Скорость: {auto.max_speed} Пробег: {auto.mileage}")
