![enter image description here](http://cdn.evbuc.com/images/4313815/85781426917/1/logo.jpg)

Beginning Python: Lesson 3
=================


In this lesson we'll recap on some of the topics covered in the last lesson. We'll also do a Python version of the "Math Game" we did in Scratch. Today you'll learn how to do the following in Python:

- What a String is.
- Use Variables.
- Use the input() function.

We will use the Wings IDE again to do the coding. If you do not have this you ask a mentor for help.

###1. Create a Folder for your programs
On your computer, create a new **folder** called ``python-programs`` on your desktop. We will save all out new Python programs in here. You can ask a mentor to help with this... 

###2. Create a New Program in Wing IDE

Open Wing IDE on your computer. Click on the File menu and select New . A new blank window will appear for us to type our program in. This window is the file editor. Enter the following code in the editor window  and save as ``math-game.py`` in the "python-programs" folder.

```python
print("Hello!")
```

Now run the program. You should see "Hello!" printed in the console.




###3. Get Python to Ask Your Name
We want to get Python to ask for the players name. We can do this by following these steps:
1. Print "What is your name?
2. Get users name and assign it to the name variable
3. Print "Lets play a Math Game " followed by the users name
Add the following highlighted lines of code to your program to do this. Your Program 

>print("Hello!")
><mark>print('What is your name?')
>myName = input()
>print('Lets play a Math Game ' + myName)</mark>


###4. Print a random addition problem
To create a random maths problem, we need to compute 2 random numbers. In Python, we can calculate random numbers using the random library. First, we need to import it, then we can calculate a random number using the random.randint(...) function. For example,``random.randint(1,20)`` computes a random number between 1 and 20. Add the following code to your program:



><mark>import random</mark>
>
>print("Hello!")
>print('What is your name?')
>myName = input()
>print('Lets play a Math Game ' + myName)
><mark>num1 = random.randint(1,20)
>num2 = random.randint(1,20)
>print('What is ',num1,'+',num2,'?')</mark>

Now run the code, you should now see the program print a random sum in the console window. Press run a few times to see the program print a different sum every time.

###5. Ask for the  Answer and Check if it's correct
Just like we did for the name, we need to get an answer for the sum using the ``input()`` function. We then want to do the following:
If the answer is correct, print "Correct, Well Done!", otherwise print "Oop! You are incorrect, the answer is ...". Add the following highlighted code to your program to do this...


>import random

>print("Hello!")
>myName = input('What is your name?')
>print('Lets play a Math Game ' + myName + '?')
>num1 = random.randint(1,20)
>num2 = random.randint(1,20)
>print('What is ',num1,' + ',num2,'?')
><mark>answer = input()
>
><mark>if int(answer)==num1 + num2:
>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;print("Correct. Well Done!")
>else:
>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;print("Oops. The answer is ",num1 + num2)</mark>


The ``(int)answer`` converts the answer to a number so that it can be compared to the correct answer (num1 + num2).

Now run your program to see if it works. If not, try to fix it.

###6. Repeat 5 times
Now improve the program by getting the player to answer 5 sums and keeping score of how many are correctly answered. We will need a for loop and a score variable to do this. Now add the following highlighted code. Make sure to add it in the right place and remember to indent your code...

>import random
>
>print("Hello!")
>myName = input('What is your name?')
>print('Lets play a Math Game ' + myName + '?')
><mark>score = 0
>times = 5
>while times>0:</mark>
> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;   num1 = random.randint(1,20)
>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;    num2 = random.randint(1,20)    
> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;   print('What is ',num1,' + ',num2,'?')
>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;    answer = input()
>    
>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;    if int(answer)==num1 + num2:
> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;       print("Correct. Well Done!")
> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;       <mark>score = score+1</mark>
>  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  else:
> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;       print("Oops. The answer is ",num1 + num2)
>
> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;   <mark>times = times-1</mark>
>
><mark>if score==5:
>  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  print('Wow, you answered them all correcly!!!')
>else:
> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;   print('You got',score,'out of 5 correct!')</mark>

Run your program and see if it works. It should now ask 5 questions and , at the end, let you know what the answer is.


###7. Improve your program 
Now try to improve your program as follows:

- How could you make the sums harder (hint: change the ``random.randint(...)`` to compute a number from 1 to 100.)
- How would you get the program to ask 10 questions instead of 5.
- Make another program that does multiplication.
- Like our Scratch program last year, ask the user to enter a level, 1 for easy, 2 for hard.  

