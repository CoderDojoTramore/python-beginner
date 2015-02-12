![Tramore Coderdojo](https://fbcdn-profile-a.akamaihd.net/hprofile-ak-xap1/v/t1.0-1/p160x160/10805584_759404964113779_3652612083545101618_n.jpg?oh=898f64d797e299d7eeb0c6f9c6ca8c33&oe=555B98CE&__gda__=1432729035_b8f9dd334e729451937f81069aae829f)

Beginning Python: Lesson 1
=================
#### created by David Bau, updated by Tramore Coderdojo
In this lesson you will learn about the Python programming language and 
set up Python on your computer. You will do the following:

- Use a new programming language...
- Use an IDE (Integrated Development Environment)
- Remembering things in Python (Memory and naming)
- Maths using Python
- Use python libraries
 
### 1: Install Python
You need to download the latest version of Python to you laptop. Open an Internet Browser and type this address into the Address Field:

[https://www.python.org/](https://www.python.org/) 

You need to install **Python version 3**. The mentors can help you with this...

### 2: Get Wings IDE
In your Internet Browser, type this address into the Address Field:

[http://wingware.com/downloads/wingide-101](http://wingware.com/downloads/wingide-101) 

Click on “Installer” button. You may need help from a mentor for this...

### 3: The Python Shell
Find the “Python Shell” in Wings. The Python Shell allows us to start coding with python straight away...
Python can remember things, so let's tell it to remember our secret word. Type the following into the Python Shell
```
>>> secret = 'crocodile‘
>>>
```
Now tell Python to print something by using the “print” command:
```python
>>> print(secret)
crocodile
>>>
```
Python will remember the secret until you quit Wings. So you can always go back and print your secret again by saying "print secret.” Now try to print something Python doesn't know:
```
>>> print(number)
Traceback (most recent call last):
File "", line 1, in
NameError: name 'number' is not defined
>>>
```
Python didn't know what number was. Try the following code to “tell” Python what number is.
```
>>> number = 43
>>> print(number)
43
>>>
```
### 4: The Python Calculator ###
Your computer is better than any calculator at doing maths.
Try the following in the Python Shell:
```
>>> print(2+33)
Scratch
...
35
>>> print(33333333 * 44444444)
1481481451851852
>>> n=123456789
>>> print(n*n*n)
1881676371789154860897069
>>>
```
Multiplication and division are done using the * and / symbol. Now use the shell to find the answer to 254 * 341?...
### 6: Python Functions - random ###
Python has lots of functions help you write programs. Let's tell Python to pick a random number. Get the "random" library by typing this:
```python
>>> import random
```
Now we can say "random.randint(1,100)" to pick a random number from 1 to 100.
```
>>> random.randint(1,100)
45
>>>

```

### 7: Python Functions – len() and str()
Coders call words “strings”. The “len” function will count how many letters
are in a word. Try the following:
```
>>> len(secret)
9
```
This means that there is 9 letters in the word “crocodile”. Remember we used *secret* to remember the word "crocodile".

### 8: Words and Numbers
What happens when you try to use words in maths? Try this:
```
>>> print 'red' + 'yellow'
redyellow
>>> print 'red' * 3
redredred
>>> print 'red' + 3
Traceback (most recent call last):
File "", line 1, in
TypeError: cannot concatenate 'str' and 'int' objects
>>>
```
A word that you put in quotes is just a string of letters called a "str" in python. Numbers that don't have a decimal point are integers and are called "int" in python. You can't add a str and an int. But you can turn a number into a string if you use the str() function. Try this:
```
>>>print 'red' + str(3)
red3
```
###9: Repeating Things
Remember the Repeat block in Scratch?  In Python, we can repeat things using a “for” command. If you say "for something in something:" with a colon (:) at the end, python will look for any indented lines(lines moved in a bit) afterwards and repeat them. Try this:
```
>>> for letter in secret:
...print(letter)
...
c
r
o
c
o
d
i
l
e
```
It is saying "for every letter in the secret, do this next thing." The computer repeats "print(letter)" nine times, once for each letter in ‘crocodile’.
This can be tricky. If it doesn’t work try again or ask a mentor for help.
### 10: Create a Program
Now we will start to use python to make a game of hangman. A python program is just a file with code in it. Let's make one.
In Wings, go to File -> New.
Type in the following into the Editor and Save the file with the name “hangman1.py" on your desktop.
To run your program, click on the Run button. You should see ‘time to play hangman’ appear in you shell. Put some other lines of code in and run it.
In the nextlesson we’ll continue to code Hangman...