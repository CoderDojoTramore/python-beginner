

Beginning Python: Lesson 10
=================



###*Event Handling*
In this lesson we'll continue to use turtle and create a program that allows you to control the turtle on the screen with the arrow keys. To do this, you will learn how write a Python program that can respond to events. An event is something that can happen while your program is running. For example, a key being pressed. When an arrow key is pressed, this program  executes a function which moves a turtle in the direction of the arrow. 

Create a new file called **event_turtle.py** in your Python folder. Add the following code. 

```python
import turtle

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

turtle.onkey(up, "Up")
turtle.onkey(left, "Left")
turtle.onkey(right, "Right")
turtle.onkey(down, "Down")

turtle.listen()
turtle.mainloop()
```

Now run the code. You should be able to move the turtle around the screen using the arrow keys. 
Now lets add some new events
###Drawing Lines
Put the following togglePen() function **just underneath the `down()` function**.

```python
def togglePen():
    if (speedy.isdown()):
        speedy.penup()
    else:
        speedy.pendown()
```
Now add the following line of code **just after ``turtle.onkey(down, "Down")``**
```python
turtle.onkey(togglePen, "p")
```
Now run your program again. This time press the p button and see what happens when you move the turtle. The p button should switch the turtle's pen on and off. 
###Changing Colours
Now add the following code just after the ``togglePen()`` function
```python
ef changeColour():
    speedy.color(random.choice(["red","green","blue"]))
```
This function changes the turtle's colour randomly to red, green, or blue. To make this happen when you press the "c" key. enter the following code  after the last ``turtle.onkey(...)`` line of code:
```python
turtle.onkey(changeColour, "c")
```
Now run your code and see if it works. Everytime you press the "c" key the turtle's colour should change.
##*Challenges*
- add an event that changes the width of the line
- change the program so that the turtle moves forward all the time  and you steer it with the arrow keys.