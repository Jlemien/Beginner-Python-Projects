"""BACKGROUND INFORMATION
If you do not know how basic right triangles work,
read this article on wikipedia: https://en.wikipedia.org/wiki/Pythagorean_triple
MAIN GOAL
Create a program that allows the user to input the sides of any triangle,
and then return whether the triangle is a Pythagorean Triple or not.
SUBGOALS
If your program requires users to input the sides in a specific order,
change the coding so the user can type in the sides in any order.
Remember, the hypotenuse (c) is always the longest side.
Loop the program so the user can use it more than once without having to restart the program.
"""
print("We are going to check if the triangle you have is a Pythagorean Triagle")
while True:
    try:
        hypotenuse = int(input("Please enter the length of the hypotenuse (the longest side of the trianlge: "))
    except ValueError:
        print("Sorry, I didn't understand that. Please be sure to enter a digit.")
        continue
    else:
        break
while True:
    try:
        b = int(input("Please enter the length of the second side of the trianlge: "))
    except ValueError:
        print("Sorry, I didn't understand that. Please be sure to enter a digit.")
        continue
    else:
        break
while True:
    try:
        a = int(input("Please enter the length of the third side of the trianlge: "))
    except ValueError:
        print("Sorry, I didn't understand that. Please be sure to enter a digit.")
        continue
    else:
        break

#Test if a * a + b * b = c * c
two_sides = a * a + b * b
third_side = hypotenuse * hypotenuse
if two_sides == third_side:
    print("Yup, it looks like this is a Pythagorean Triple")
if two_sides != third_side:
    print("No, this is not a Pythagorean Triple")