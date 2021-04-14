import random
#how can I use .upper or .lower on the strings so that the aren't case-sensitive?

original = (input("Type in a word or a phrase: "))
original_list = list(original)
jumbled = ""

for letter in range(0, len(original_list)):
    jumbled += original_list.pop(random.randint(0, len(original_list) - 1))

print("Can you guess what the original word or phrase was just by looking at this jumbled verion?\n", jumbled)
guess = (input("What do you think the original word or phrase was? "))
while 1 == 1:
    if guess == original:
        print("Hooray! You guessed it right!")
        break
    else:
        print("That isn't correct.")
        print("This is the jumbled word or phrase:", jumbled)
        guess = (input("Guess again. What would you like to guess? "))






"""
import random

VOWELS = ("a", "e", "i", "o", "u")

message = input("Enter your message: ")

new_message = ""

for letter in message:
    if letter not in VOWELS:
        new_message += letter
    else:
        new_message += random.choice(VOWELS)  

print(new_message)
"""