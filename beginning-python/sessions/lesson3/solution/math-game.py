import random

print("Hello!")
myName = input('What is your name?')
print('Lets play a Math Game ' + myName + '?')
score = 0
times = 5
while times>0:
    num1 = random.randint(1,20)
    num2 = random.randint(1,20)    
    print('What is ',num1,' + ',num2,'?')
    answer = input()
    
    if int(answer)==num1 + num2:
        print("Correct. Well Done!")
        score = score+1
    else:
        print("Oops. The answer is ",num1 + num2)
    times = times-1

if score==5:
    print('Wow, you answered them all correcly!!!')
else:
    print('You got',score,'out of 5 correct!')
    