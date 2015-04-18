![enter image description here](http://cdn.evbuc.com/images/4313815/85781426917/1/logo.jpg)

Beginning Python: Lesson 6
=================
In this lesson you will learn about **Turtle**. Turtle is a nice way to learn some of the basics of computer graphics, so in this lesson, we’ll use a Python turtle to draw some simple shapes and lines.


##*Your first turtle program*
Let’s write a couple of lines of Python program to create a new turtle and start drawing a rectangle. (We’ll call the variable that refers to our first turtle *alex*.
```python
import turtle            
wn = turtle.Screen()   

alex = turtle.Turtle()    
alex.forward(50)        
alex.left(90)             
alex.forward(30)          
alex.left(90)            
alex.forward(50)          
alex.left(90)             
alex.forward(30)          

wn.mainloop()             # Wait for user to close windowimport turtle

```

When we run this program, a new window pops up with a rectangle. The arrow on the screen shows the location of the turtle.

##*Colours and Pen Size*
We can change the colour of the line and the background. Try the following program to draw a triangle.

```python
import turtle
wn = turtle.Screen()
wn.bgcolor("lightgreen")      
wn.title("Hello, Tess!")      

tess = turtle.Turtle()
tess.color("blue")            
tess.pensize(3)               
tess.forward(50)
tess.left(120)
tess.forward(50)
tess.left(120)
tess.forward(50)

wn.mainloop()
```

##*A herd of Turtles*
Just like our other programs, we can have more than one variable. In this case we'll create two *instances* of a turtle, Alex and Tess:

```python
import turtle
wn = turtle.Screen()         
wn.bgcolor("lightgreen")
wn.title("Tess & Alex")

tess = turtle.Turtle()       
tess.color("hotpink")
tess.pensize(5)

alex = turtle.Turtle()  
alex.color("blue")
alex.pensize(5)    

tess.forward(80)            
tess.left(120)
tess.forward(80)
tess.left(120)
tess.forward(80)
tess.left(120)            
           
alex.forward(80)             
alex.left(-90)
alex.forward(80)
alex.left(-90)
alex.forward(80)
alex.left(-90)
alex.forward(80)
alex.left(-90)

wn.mainloop()
```

##*Using Loops to Simplify the program*
To draw a square we’d like to do the same thing four times — move the turtle, and turn. We previously used 8 lines to have alex draw the four sides of a square. This does exactly the same, but using just three lines:

```python
import turtle
wn = turtle.Screen()         
wn.bgcolor("lightgreen")
wn.title("Tess & Alex")

alex = turtle.Turtle()

for i in [0,1,2,3]:
    alex.forward(50)
    alex.left(90)

wn.mainloop()
```

##*Turtle  footprints*
Try the following program. It makes a turtle “stamp” it's footprint onto the canvas:

```python
import turtle
wn = turtle.Screen()
wn.bgcolor("lightgreen")
tess = turtle.Turtle()
tess.shape("turtle")
tess.color("blue")

tess.penup()               
size = 20
for i in range(30):
    tess.stamp()             
    size = size + 3         
    tess.forward(size)       
    tess.right(24)           

wn.mainloop()
```

##*Challenges*
Try the following if you're finished:

- Use for loops to make a turtle draw these shapes
An equilateral triangle
A square
A hexagon (six sides)
An octagon (eight sides)

- **Super Challenge**: Write a drunken prirate program as follows: 
A drunk pirate makes a random turn and then takes 100 steps forward, makes another random turn, takes another 100 steps, turns another random amount, etc
