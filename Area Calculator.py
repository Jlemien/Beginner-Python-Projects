#Get some input from the user to figure out what shape they have
shape = str(input("What kind of a shape do you have? (triangle, rectangle, circle): "))
if shape == str("triangle"):
    height = float(input("What is the height of your triangle?"))
    base = float(input("What is the base of your triangle?"))
    area = base * height * .5
    print("Your triangle has an area of", area)
if shape == str("rectangle"):
    height = float(input("What is the height of your rectangle?"))
    base = float(input("What is the base of your rectangle?"))
    area = base * height
    print("Your rectangle has an area of", area)
# If it is a rectangle, calculate length * width
if shape == str("circle"):
    radius = float(input("What is the radius of your circle?"))
    area = radius * radius * 3.14
    print("Your circle has an area of", area)
elif shape != str("triangle") and shape != str("rectangle") and shape != str("circle") and shape != str("square"):
    print("I don't recognize that shape. Goodbye.")
   
# If it is a circle A=πr2 (ask user for the radius of the circle)

# If it is another shape, "That is too complicated of a shape for me."
