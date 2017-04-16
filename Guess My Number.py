7"""Overview: The computer randomly generates a number.
The user inputs a number, and the computer will tell you if you are too high, or too low.
Then you will get to keep guessing until you guess the number.
What you will be Using: Random, Integers, Input/Output, Print, While (Loop), If/Elif/Else"""

from random import randint
number = randint(0,10000000)

print("You need to guess what number I'm thinking of.")
guess = int(input("What number would you like to guess? "))
while 1 == 1:
    if guess == number:
        print("Hooray! You guessed it right!")
        break
    elif guess < number:
        print("The number you guessed is too small.")
        guess = int(input("Guess again. What number would you like to guess? "))
    elif guess > number:
        print("The number you guessed is too big.")
        guess = int(input("Guess again. What number would you like to guess? "))
