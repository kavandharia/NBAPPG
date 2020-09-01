from rectangle import Rectangle

class Square(Rectangle):
    def __init__(self, side):
        super().__init__(side, side)

    def getDiagonal(self):
        return str(self.getSide1()) + '\/2'

    def printDiagonal(self):
        print(self.getDiagonal)