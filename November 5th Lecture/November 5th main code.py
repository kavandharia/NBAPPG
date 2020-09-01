from quadrilateral import Quadrilateral
from rectangle import Rectangle
from square import Square

q1 = Quadrilateral
print(q1)
r1 = Rectangle(9,6)
print(r1.getDiagonal)
print(r1.getPerimeter)
print(r1)


s1 = Square(7)
print(s1.getDiagonal())
print(s1.getPerimeter())
s1.printDiagonal()
