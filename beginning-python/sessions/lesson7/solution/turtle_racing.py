import turtle              # 1.  import the modules
import random
wn = turtle.Screen()       # 2.  Create a screen
wn.bgcolor('lightblue')

shelly = turtle.Turtle()    # 3.  Create two turtles
bob = turtle.Turtle()
shelly.color('red')
bob.color('blue')
shelly.shape('turtle')
bob.shape('turtle')

bob.up()                  # 4.  Move the turtles to their starting point
shelly.up()
bob.goto(-100,20)
shelly.goto(-100,-20)


line_drawer = turtle.Turtle()
line_drawer.up()
line_drawer.goto(-100,50)
line_drawer.right(90)
line_drawer.down()
line_drawer.forward(100)

line_drawer.up()
line_drawer.goto(300,50)
line_drawer.down()
line_drawer.forward(100)



turtles = [bob,shelly]
winner=False
while winner==False:
    movingTurtle = random.choice(turtles)
    movingTurtle.forward(random.randrange(1,5))
    if movingTurtle.xcor()>300:
        winner=True
    

    
    
wn.exitonclick()