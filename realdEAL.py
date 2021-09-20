import turtle
import math
def main():
    win = turtle.Screen()
    t1 = turtle.Turtle()
    t1.width(5)
    width = t1.width()
    sideLength = 400
    sides = 4
    t1.up()
    t1.goto(-400,0)
    t1.down()
    #Dice Values
    d1 = 1
    d2 = 2
    d3 = 3
    d4 = 4
    d5 = 5
    d6 = 6

    #Coordinates

#Dice Locations
    #d1Location
    x1 = -400
    y1 = 100
    #d2Location
    x2 = -125
    y2 = 100
    #d3Location
    x3 = -100 
    y3 = 100
   #d4Location
    x4 = 50
    y4 = 100
    #D5Location
    x5 = 200
    y5 = 100
    #d6Location
    x6 = 350
    y6 = 100
    #Start of D1 Dot
    #t1.up()
    #locationD1 = t1.goto(50,50)
    #t1.down()
    #drawD1 = t1.dot(width//6)
    #t1.up()
    #t1.goto(0,0)
    #t1.down()

    for i in range(4):
        t1.forward(sideLength/sides)
        t1.left(360/sides)
    t1.up()
    t1.goto(x1+50,y1-50)
    drawD1 = t1.dot(width//6)
    t1.up()
    t1.goto(-250,0)
    t1.down()

    for i in range(4):
        t1.forward(sideLength/sides)
        t1.left(360/sides)
    t1.up()
    t1.goto(x2+0,y2+0)
    t1.up()
    t1.goto(x2-100,y2-25)
    drawD2 = t1.dot(width//6)
    t1.goto(x2-50,y2-75)
    drawD2 = t1.dot(width//6)
    t1.goto(1.5*width,0)
    t1.down()

    for i in range(4):
        t1.forward(sideLength/sides)
        t1.left(360/sides)
    t1.goto(x3+0,y3+0)
    t1.up()
    t1.goto(x3+25,y3-25)
    drawD3 = t1.dot(width//6)
    t1.goto(x3+50,y3-50)
    drawD3 = t1.dot(width//6)
    t1.goto(x3+75,y3-75)
    drawD3 = t1.dot(width//6)
    t1.goto(50,0)
    t1.down()

    for i in range(4):
        t1.forward(sideLength/sides)
        t1.left(360/sides)
    t1.goto(x4+0,y4+0)
    t1.up()
    t1.goto(x4+25,y4-25)
    drawD4 = t1.dot(width//6)
    t1.goto(x4+25,y4-75)
    drawD4 = t1.dot(width//6)
    t1.goto(x4+75,y4-25)
    drawD4 = t1.dot(width//6)
    t1.goto(x4+75,y4-75)
    drawD4 = t1.dot(width//6)
    t1.up()
    t1.goto(200,0)
    t1.down()
    for i in range(4):
        t1.forward(sideLength/sides)
        t1.left(360/sides)
    t1.goto(x5+0,y5+0)
    t1.up()
    t1.goto(x5+25,y5-25)
    drawD5 = t1.dot(width//6)
    t1.goto(x5+25,y5-75)
    drawD5 = t1.dot(width//6)
    t1.goto(x5+75,y5-25)
    drawD5 = t1.dot(width//6)
    t1.goto(x5+75,y5-75)
    drawD5 = t1.dot(width//6)
    t1.goto(x5+50,y5-50)
    drawD5 = t1.dot(width//6)
    t1.up()
    t1.goto(350,0)
    t1.down()
    for i in range(4):
        t1.forward(sideLength/sides)
        t1.left(360/sides)
    t1.up()
    t1.goto(x6+25,y6-75)
    drawD6 = t1.dot(width//6)
    t1.goto(x6+75,y6-25)
    drawD6 = t1.dot(width//6)
    t1.goto(x6+75,y6-75)
    drawD6 = t1.dot(width//6)
    t1.goto(x6+25,y6-25)
    drawD6 = t1.dot(width//6)
    t1.goto(x6+25,y6-50)
    drawD6 = t1.dot(width//6)
    t1.goto(x6+75,y6-50)
    drawD6 = t1.dot(width//6)


    print (t1.pos())

    #for i in range(3):
        #x3+=25,y3+=-25
        #drawD3 = t1.dot(width//6)
     #for i in range(3):
           # x3+= 25
           # y3-= 25
           # drawD3 = t1.dot(width//6)
        
main() 
