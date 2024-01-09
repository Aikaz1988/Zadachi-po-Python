# Задание №2
# Создайте класс Черепашка, который хранит позиции x и y черепашки, а также s - количество клеточек, 
# на которое она перемещается за ход
# у этого класс есть методы:
# go_up() - увеличивает y на s
# go_down() - уменьшает y на s
# go_left() - уменьшает x на s
# go_right() - увеличивает y на s
# evolve() - увеличивает s на 1
# degrade() - уменьшает s на 1 или выкидывает ошибку, когда s может стать ≤ 0
# count_moves(x2, y2) - возвращает минимальное количество действий, 
# за которое черепашка сможет добраться до x2 y2 от текущей позиции

import math

class Turtle:
    def __init__(self, x, y, s):
        self.x = x
        self.y = y
        self.s = s
    
    def go_up(self):
        self.y += self.s # go_up() - увеличивает y на s
        return self.y
    
    def go_down(self):
        self.y -= self.s # go_down() - уменьшает y на s
        return self.y
    
    def go_left(self):
        self.x -= self.s # go_left() - уменьшает x на s
        return self.x
    
    def go_right(self):
        self.y += self.s # go_right() - увеличивает y на s
        return self.y
    
    def evolve(self):
        self.s += 1 # evolve() - увеличивает s на 1
        return self.s
    
    def degrade(self):
        if self.s <= 1:
            raise ValueError('s не может стать <= 0')
        else:
            self.s -= 1 # degrade() - уменьшает s на 1 или выкидывает ошибку, когда s может стать ≤ 0
            return self.s
        
    # count_moves(x2, y2) - возвращает минимальное количество действий, за которое черепашка сможет добраться до x2 y2 от текущей позиции
    def count_moves(self, x2, y2):
        distance = math.sqrt((x2 - self.x)**2 + (y2 - self.y)**2)
        return math.ceil(distance / self.s)

r = Turtle(5, 15, 26)
print(r.go_up())
print(r.go_down())
print(r.go_left())
print(r.go_right())
print(r.evolve())
print(r.degrade())
print(r.count_moves(12, 10))
