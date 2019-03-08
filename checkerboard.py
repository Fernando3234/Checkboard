#Checkers 01 by Fernando
from graphics import *


sqSz = 50

chWin = GraphWin ("Checkers", sqSz * 10, sqSz * 10)
chWin.setCoords(0, 0, sqSz * 10, sqSz * 10)

for j in range (8):
    for i in range(8):
        sQ = Rectangle(Point(sqSz *( i + 1), sqSz * (j + 1)),
                       Point(sqSz* (i + 2), sqSz * (j + 2)))
        sQ .setFill(color_rgb(240,0,0))
        sQ.draw(chWin)

chWin.getMouse()
chWin.close()

