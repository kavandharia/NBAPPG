from quadrilateral import Quadrilateral

class Rectangle(Quadrilateral):
    def __init__(self, length, width):
        super().__init__(length, width, length, width)
        self._diagonal = math.sqrt(length**2 + width**2)

    def getDiagonal(self):
        return self._diagonal

    def getArea(self):
        #return self._side1 * self._side2
        return self.getSide1() + self.getSide2()

    def __repr__(self):
        return 'Rectangle' + str(self.getSide1()) + ' x ' + str(self.getside2())