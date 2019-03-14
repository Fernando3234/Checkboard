#Checkers 01 by Fernando
from graphics import *

print("""Pleasew input hwo big you want the tiles to be.
Your answer must only contain whole numbers.
50 is standard size""")

try:
    sqSz = int(input("Square Sizes: "))
except ValueError:
    sqSz = 50

def create_tile(tR, tC, color):
    global sqSz
    tL = Rectangle(Point(sqSz * (tR + 1), sqSz * (tC + 1)),
                   Point(sqSz * (tR + 2), sqSz * (tC + 2)))
    tL.setFill(color)
    tL.draw(chWin)

print (""" Please input what color you would like the checkerboard to be.
Your input must be all lower case and no spaces.
Black and Red is the standard color""")

uC1 = input ("Color 1: ")
if uC1 != "":
    uC2 = input ("Color 2: ")
else:
    uC1 = "red"
    uC2 = "black"

    
chWin = GraphWin ("Checkers", sqSz * 10, sqSz * 10)
chWin.setCoords(0, 0, sqSz * 10, sqSz * 10)

for j in range (8):
    for i in range(8):
        if j % 2 == 0 :
            if i % 2 == 0 :
                sqCol = uC1
            else:
                sqCol = uC2
        else:
            if i %  2 == 1:
                sqCol = uC1
            else:
                sqCol = uC2
        create_tile(i, j, sqCol)
  
chWin.getMouse()
chWin.close()

