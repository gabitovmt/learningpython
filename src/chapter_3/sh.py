"""Модуль sh. Содержит классы Shape, Square и Circle"""


class Shape:
    """Класс Shape: содержит метод move"""
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def move(self, delta_x, delta_y):
        self.x = self.x + delta_x
        self.y = self.y + delta_y


class Square(Shape):
    """Класс Square: наследует от Shape"""
    def __init__(self, side=1, x=0, y=0):
        Shape.__init__(self, x, y)
        self.side = side


class Circle(Shape):
    """Класс Circle: наследует от Shape и содержит метод area"""
    pi = 3.14159

    def __init__(self, r=1, x=0, y=0):
        Shape.__init__(self, x, y)
        self.radius = r

    def area(self):
        """метод area класса Circle: возвращает площадь круга"""
        return self.radius ** 2 * self.pi

    def __str__(self):
        return "Circle of radius %s at coordinates (%d, %d)" \
            % (self.radius, self.x, self.y)
