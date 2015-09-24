import turtle
import random

wn = turtle.Screen()
wn.bgcolor('lightblue')
wn.title("Event Turtle")

speedy = turtle.Turtle()
speedy.shape('turtle')
speedy.penup()

def up():
    speedy.setheading(90)
    speedy.forward(45)

def left():
    speedy.setheading(180)
    speedy.forward(45)

def right():
    speedy.setheading(0)
    speedy.forward(45)

def down():
    speedy.setheading(270)
    speedy.forward(45)
    
def togglePen():
    if (speedy.isdown()):
        speedy.penup()
    else:
        speedy.pendown()
        
def changeColour():
    speedy.color(random.choice(["red","green","blue"]))

turtle.onkey(up, "Up")
turtle.onkey(left, "Left")
turtle.onkey(right, "Right")
turtle.onkey(down, "Down")
turtle.onkey(togglePen, "p")
turtle.onkey(changeColour, "c")


turtle.listen()
turtle.mainloop()