from quadrilateral import Quadrilateral

class Trapezoid(Quadrilateral):
    def __init__(self, base1, base2, side3, side4, height):
        super().__init__(base1, base2, side3, side4)
        self._height = height

    def getArea(self):
        return (0.5)*(self.getSide1() + self.getSide2()) * self._height

    def getHeight(self):
        return self._height

    def __repr__(self):
        return 'Trapezoid'