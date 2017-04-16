"""I'm sure you've used a magic 8 ball at one point in your life.
You can create one in python. You must:
1) Allow the user to enter their question
2) Display an in progress message( i.e. "thinking")
3) Create 20 responses, and show a random response
4) Allow the user to ask another question or quit"""

from random import choice
from time import sleep

def main ():
    specific_inquiry = input("What question would you like to ask of the Magic 8 Ball? ")
    x = 0
    while x < 5:
        print("Thinking...")
        sleep(1) # delays for 1 seconds
        x = x + 1

    print("Your answer is:")
    print(choice(['Reply hazy try again', 'It is certain', 'It is decidedly so', 'Most likely', 'Signs point to yes ', 'Yes', 'Outlook good', 'As I see it, yes', 'You may rely on it', 'Yes, definitely', 'Without a doubt', 'My reply is no', 'My sources say no', 'Don\'t count on it', 'Concentrate and ask again', 'Ask again later', 'Cannot predict now', 'Better not tell you now', 'Outlook not so good', 'Very doubtful']))
    restart()
	
def restart():
    initial_question = input("Would you like to a ask another question of the Magic 8 Ball? (Yes or no)")
    if initial_question == "yes":
        main()    
    else:
        print("Goodbye")

main()