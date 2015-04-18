import random

num1 = random.randint(1,20)

num2 = random.randint(1,20)

print("Lets play a maths game...")
print("What is" ,num1," + ",num2)
answer = input()
if answer == (num1 + num2):
    print("CORRECT!!!")
else:
    print("Nope - the answer is ",num1+num2)

