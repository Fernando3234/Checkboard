#Checkers 01 by Fernando
from graphics import *

sqSz = 50

chWin = GraphWin ("Checkers", sqSz * 15, sqSz * 15)
chWin.setCoords(0, 0, sqSz * 15, sqSz * 15)

sQ = Rectangle(Point(sqSz, sqSz), Point(sqSz *2, sqSz*2))
sQ .setFill(color_rgb(240,0,0))
sQ.draw(chWin)

chWin.getMouse()
chWin.close()
