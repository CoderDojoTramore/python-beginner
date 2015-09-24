import turtle
import time


wn = turtle.Screen()
wn.bgcolor('lightblue')
wn.title("Event Turtle")

speedy = turtle.Turtle()
speedy.shape('turtle')

def up():
    speedy.setheading(90)
    

def left():
    speedy.setheading(180)
    

def right():
    speedy.setheading(0)
    

def down():
    speedy.setheading(270)
    
def penDown():
    speedy.pendown() 

turtle.onkey(up, "Up")
turtle.onkey(left, "Left")
turtle.onkey(right, "Right")
turtle.onkey(down, "Down")

turtle.listen()
alive=True
while(alive):
    speedy.forward(1)

turtle.mainloop()
