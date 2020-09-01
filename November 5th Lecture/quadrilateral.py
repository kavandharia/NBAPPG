class Quadrilateral:
    def __init__(self, side1, side2, side3, side4):
        self._side1 = side1
        self._side2 = side2
        self._side3 = side3
        self._side4 = side4

    def getSide1(self):
        return self._side1

    def getSide2(self):
        return self._side2

    def getSide3(self):
        return self._side3

    def getSide4(self):
        return self._side4

    def getPerimeter(self):
        return self._side1 + self._side2 + self._side3 + self._side4

    def __repr__(self):
        return ''

