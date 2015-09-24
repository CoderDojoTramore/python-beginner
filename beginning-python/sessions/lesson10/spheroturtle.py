from turtle import *
import sphero
import time

s = sphero.Sphero("/dev/rfcomm0")
s.connect()

setup(500, 500)
Screen()
title("Turtle Keys")
sphero = Turtle()
sphero.shape("circle")
showturtle()

def up():
    sphero.setheading(90)
    sphero.forward(45)
    s.roll(0x20, 90)
    time.sleep(1)

def left():
    sphero.setheading(180)
    sphero.forward(45)
    s.roll(0x20, 180)
    time.sleep(1)

def right():
    sphero.setheading(0)
    sphero.forward(45)
    s.roll(0x20, 0)
    time.sleep(1)

def down():
    sphero.setheading(270)
    sphero.forward(45)
    s.roll(0x20, 270)
    time.sleep(1)

onkey(up, "Up")
onkey(left, "Left")
onkey(right, "Right")
onkey(down, "Down")

listen()
mainloop()