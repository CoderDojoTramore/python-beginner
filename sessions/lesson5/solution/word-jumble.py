# Guessing-Game
# frankx 28/2/2015

import random

print("Welcome to Word Jumble! Unscramble the letters to make a word...")


words = ["python", "jumble", "easy", "difficult", "answer", "xylophone"]

word = random.choice(words)

correct = word

jumble =""

while word:
    position = random.randrange(len(word))
    jumble = jumble + word[position]
    word = word[:position] + word[(position + 1):]

print ("The jumbled word is:", jumble)

guess = input("\nYour guess: ")
guess = guess.lower()
while (guess != correct) and (guess != ""):
    print("Sorry, that's not it.")
    guess = input("Your guess: ")

if guess == correct:
    print("That's it! You guessed it!\n")
    
print("Thanks for playing.")