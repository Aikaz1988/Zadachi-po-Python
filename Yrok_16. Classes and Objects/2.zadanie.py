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

class Turtle:
    def __init__(self, x, y, s):
        self.x = x
        self.y = y
        self.s = s
    
    def go_up(self):
        self.y += self.s
        return self.y

    def go_down(self):
        self.y -= self.s
        return self.y

    def go_left(self):
        self.x -= self.s
        return self.x

    def go_right(self):
        self.x += self.s
        return self.x

    def evolve(self):
        self.s += 1
        return self.s

    def degrade(self):
        if self.s <= 0:
            print('s = 0')
        self.s -= 1
        return self.s

    def count_moves(self, x2, y2):
        return self.x - x2, self.y - y2

r = Turtle(5, 15, 26)
print(r.go_up())
print(r.go_down())
print(r.go_left())
print(r.go_right())
print(r.evolve())
print(r.degrade())
print(r.count_moves(12, 10))
