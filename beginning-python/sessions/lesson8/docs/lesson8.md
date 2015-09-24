![enter image description here](http://cdn.evbuc.com/images/4313815/85781426917/1/logo.jpg =50x50)

Beginning Python: Lesson 8
=================



###*Functions*
In this lesson we'll continue using Python Turtle to investigate functions. Often in code we want to do the same thing more than once. You may remeber in our first Turtle lesson we got the turtles to draw shapes by individually coding a `forward` and `right` move for a turtle. Wouldn't it be nice if we could just tell a turtle to draw a square, or a circle, or any other shape. This is where we can use a **function**. A function is a block of reuseable code that performs some action, for example drawing a circle. 

Create a new file called **funtions.py** in your Python folder. Add the following code. 

```python
def drawSquare(t, sz):

    for i in range(4):
        t.forward(sz)
        t.left(90)
```
Now run the code and  what happens? Nothing happens! We need to create a turtle and call the function. 

###*Calling a function*
You need to call a function in order to use it. In this case, when we call the function we need to tell it the following:
- the turtle that will draw the square
- the size of the square.
These are called the **parameters** of the function. Put the following code into your program: 

```python
import turtle
        
wn = turtle.Screen()      
wn.bgcolor('lightblue')
speedy = turtle.Turtle()

speedy.up()
speedy.setposition(100,100)
speedy.down()
drawSquare(speedy, 100)

speedy.up()
speedy.setposition(-100,100)
speedy.down()
speedy.begin_fill()
speedy.color("red")
drawSquare(speedy, 150)
speedy.end_fill()

wn.exitonclick()
```
Run the program. You'll see the turtle move to a new position (100,100), draw a square, and then move to position (-100, 100) and draw another , bigger, square. 

###More Shapes
Now lets write more functions which can draw other shapes. Enter the following code **just underneath the square  function**

```python
def drawTriangle(t, sz):

    for i in range(3):
        t.forward(sz)
        t.left(120)

def drawOctagon(t, sz):

    for i in range(8):
        t.forward(sz)
        t.left(45)
```
Now add the following code to draw a triangle at location (-100,100).
```python
speedy.up()
speedy.setposition(-100,100)
speedy.down()
drawTriangle(speedy, 100)
```

##*Challenges*

- Draw an octagon using the drawOctagon function.
- Draw a yellow five point star 
- **Super Challenge**: Draw a circle.