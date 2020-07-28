# Game - guess number
import random

print("Hello, What is your name?")
userName = input()
ranNumber = random.randint(1,20)
print("I am thinking of a number between 1 and 20. Please guess my number")

for attempts in range(1,6):
    print("Try to guess the number")
    try:
        userNum = int(input())
        if ranNumber < userNum:
            print("Your number is high!")
        elif ranNumber > userNum:
            print("You number is low!")
        else:
            break # Guessed the number successfully!
    except:
        print(userName + "  I think, you did not enter a number")

try:
    if(ranNumber == userNum):
        print("Well done " + userName + "! You guessed the number correctly as: " + str(ranNumber))

    else:
        print("Sorry! You have exceeded the attempts!  " + userName + "! Better luck next time!")
except:
    print(userName + "  I was expecting you to enter a number")
