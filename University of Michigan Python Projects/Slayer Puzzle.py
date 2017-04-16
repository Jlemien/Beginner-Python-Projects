#You will write a program that can be used to check guesses for the following puzzle:
#For what six-digit number SLAYER is the following equation true, where each letter stands for the
#digit in the position shown: SLAYER + SLAYER + SLAYER = LAYERS
print("Guess a six-digit number SLAYER so that following equation is true\nwhere each letter stands for the digit in the position shown: \nSLAYER + SLAYER + SLAYER = LAYERS")
while True:
    try:
        # Note: Python 2.x users should use raw_input, the equivalent of 3.x's input
        guess = int(input("Enter your guess for SLAYER: "))
        while len(str(guess)) != 6:
            guess = int(input("Please enter six digits. Enter your guess for SLAYER: "))
    except ValueError:
        print("Sorry, I didn't understand that. Please enter digits.")
        continue
    else:
        break

guess = str(guess)
S = int(guess[0])
L = int(guess[1])
A = int(guess[2])
Y = int(guess[3])
E = int(guess[4])
R = int(guess[5])

three_slayers = S + L + A + Y + E + R + S + L + A + Y + E + R + S + L + A + Y + E + R
layers =L + A + Y + E + R + S

if three_slayers == layers:
    print("SLAYER + SLAYER + SLAYER = ", three_slayers)
    print("LAYWER = ", layers)
    print("Congragulations! You solved the puzzle")
else:
    print("Nope. That's not correct. Try again.")