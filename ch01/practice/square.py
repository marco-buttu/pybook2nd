class Square:

    def __init__(self, side):
        self.side = side

    def perimeter(self):
        return self.side * 4

    def area(self):
        return self.side ** 2
