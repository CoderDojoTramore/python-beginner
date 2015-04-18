# Guess My Number
# The computer picks a random number between 1 and 100
# The player tries to guess it and the computer lets
# the player know if the guess is too high, too low
# or correct
# YOUR_NAME 28/2/2015
import random

print("Welcome to 'Guess My Number'!")
print("I'm thinking of a number between 1 and 100.")
print("Try to guess it in as few attempts as possible.")

# set the initial values
number = random.randint(1,100)
print("Take a guess: ")
guess = int(input())
tries = 1

# guessing loop
while (guess != number):
    if (guess > number):
        print("Lower...")
    else:
        print("Higher...")
    print("Take a guess: ")
    guess = int(input())    
    tries = tries + 1
    
print("You guessed it! The number was", number)
print("And it only took you", tries, "tries!")