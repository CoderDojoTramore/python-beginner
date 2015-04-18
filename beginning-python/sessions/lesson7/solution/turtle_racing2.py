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

for x in range(50):
    speedySteps = random.randrange(1,20)
    shellySteps = random.randrange(1,20)
    speedy.forward(speedySteps)
    shelly.forward(shellySteps)
    
    
wn.exitonclick()