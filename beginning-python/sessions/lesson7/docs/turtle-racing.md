![enter image description here](http://cdn.evbuc.com/images/4313815/85781426917/1/logo.jpg =50x50)

Beginning Python: Lesson 7
=================



###*Turtle Racing*
In this lesson we'll continue using Python Turtle to create a racing turtles program. Two or more turtles will race across the screen from left to right. The turtle that goes the farthest is the winner.

There is more than one way to write a program that solves this problem. As we did in previous lessons, let’s look at what needs to be done, and then try to come up with a set of steps for the solution. For now we'll have a race between just two turtles.


Here is a possible sequence of steps that we will need to accomplish:

1. Import the modules we need
2. Create a screen
3. Create two turtles
4. Move the turtles to their starting positions
5. Send them moving across the screen

Here's the code for the first 4 steps. Create a new program called 'turtle_racing.py' and enter the following code:

```python
import turtle           
import random
wn = turtle.Screen()      
wn.bgcolor('lightblue')

shelly = turtle.Turtle()   
speedy = turtle.Turtle()
shelly.color('red')
speedy.color('blue')
shelly.shape('turtle')
speedy.shape('turtle')

speedy.up()                  
shelly.up()
speedy.goto(-300,20)
shelly.goto(-300,-20)

wn.exitonclick()
```
Now run the code and see what happens. You should see your two turtles, Speedy and Shelly, move to their starting position for the race. 

###*Move the Turtles*
The next part of the program is to make them race across the screen. We want it to look as realistic as possible. This is where the Random module comes in. We can use a for loop to do this. Inside the loop we'll move each turtle forward a random number of steps between 1 and 20. Then the turtle who has moved the farthest is the winner. We'll also make the for loop move the turtles 50 times.
Put the following code **before the ``wn.exitonclick()``** line of code:

```python
for x in range(50):
    speedySteps = random.randrange(1,20)
    shellySteps = random.randrange(1,20)
    speedy.forward(speedySteps)
    shelly.forward(shellySteps)
```



##*Challenges*
There's lots of ways to make this program better:

- Add more turtles to the race.
- Draw a starting line for the turtles. (hint: use another turle to draw a line from (-300, 30) to (-300, -30) )
- Draw a finish line. Finish the race when one of the turtles crosses the line. 
- **Super Challenge**: To make the race look more realistic, move just one of the turtles every time the for loop repeats.
