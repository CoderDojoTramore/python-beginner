![enter image description here](http://cdn.evbuc.com/images/4313815/85781426917/1/logo.jpg =50x50)

Beginning Python: Lesson 7
=================



###*Turtle Racing*
In this lesson we'll improve the Turtle racing game. We will ask the player to enter the number of turtles in the race, draw a start and finish line, and get the winner to say "I WIN!". 

Enter or update your turtle racing program with  the following code:

```python
import turtle              
import random

numberTurtles = input("enter number of turtles in race..")

wn = turtle.Screen()
wn.bgcolor('lightblue')

line_drawer = turtle.Turtle()
line_drawer.up()

line_drawer.goto(-300,200)
line_drawer.right(90)
line_drawer.down()
line_drawer.forward(450)

line_drawer.up()
line_drawer.goto(250,200)
line_drawer.down()
line_drawer.forward(450)

yCoordStart = 150
turtles=[]

for x in range(int(numberTurtles)):
    nextTurtle = turtle.Turtle()    
    nextTurtle.color(random.random(), random.random(), random.random())
    nextTurtle.shape('turtle')
    turtles.append(nextTurtle)
    nextTurtle.up()
    nextTurtle.goto(-300,yCoordStart)
    yCoordStart=yCoordStart-20

winner=False
while winner==False:
    movingTurtle = random.choice(turtles)
    movingTurtle.forward(random.randrange(1,10))
    if movingTurtle.xcor()>250:
        winner=True
        movingTurtle.write("I Win!!!", font=('Arial', 20, 'normal'))
    
wn.exitonclick()
```
Now run the code and see what happens. You should all your turtles race across the screen.
