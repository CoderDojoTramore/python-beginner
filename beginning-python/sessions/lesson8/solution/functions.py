def drawSquare(t, sz):

    for i in range(4):
        t.forward(sz)
        t.left(90)
        
def drawRectangle(t, side1, side2):
    sides=[side1,side2,side1,side2]
    for i in range(4):
        t.forward(sides[i])
        t.left(90)

        
def drawTriangle(t, sz):

    for i in range(3):
        t.forward(sz)
        t.left(120)
        
def drawOctagon(t, sz):

    for i in range(8):
        t.forward(sz)
        t.left(45)
            
def drawPolygon(t, sz, sides):

    for i in range(sides):
        t.forward(sz)
        t.left(360/sides)

import turtle
        
wn = turtle.Screen()      
wn.bgcolor('lightblue')
speedy = turtle.Turtle()



speedy.up()
speedy.setposition(0,-100)
speedy.down()
speedy.begin_fill()
speedy.color("red")
drawSquare(speedy, 150)
speedy.end_fill()


speedy.up()
speedy.setposition(0,50)
speedy.down()
speedy.begin_fill()
speedy.color("blue")
drawTriangle(speedy, 150)
speedy.end_fill()

speedy.up()
speedy.setposition(20,-100)
speedy.down()
speedy.begin_fill()
speedy.color("black")
drawRectangle(speedy, 50, 100)
speedy.end_fill()

speedy.up()
speedy.setposition(85,-50)
speedy.down()
speedy.begin_fill()
speedy.color("white")
drawSquare(speedy, 50)
speedy.end_fill()


wn.exitonclick()

