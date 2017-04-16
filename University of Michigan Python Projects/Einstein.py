print("This is a game that Albert Einstein liked a lot.")
print("Whatever number you enter will end up being changed into 1089.\n"
      "First, you will enter three-digit number of your choosing,\n"
      " with the first and last digits at least two apart.")



while True:
    try:
        original_number = int(input("What number would you like to choose? Enter the digits here: "))
    except ValueError:
        print("Sorry, I didn't understand that. Did you enter digits?")
        continue
    if len(str(original_number)) > 3:
        print("Please enter three digits.")
        continue
    if len(str(original_number)) < 3:
        print("Please enter three digits.")
        continue
    # first_digit, second_digit, third_digit = str(original_number)   How do I do this part?
    # if int(first_digit) - int(third_digit) >= int(2):
    #     print("Remember that the first digit and the third digit must differ by at least 2.")
    #     continue
    else:
        break

reversed_original = str(original_number)[::-1]
difference_of_original = abs(original_number - int(reversed_original))
reversed_difference = str(difference_of_original)[::-1]
awesome_number = (int(reversed_difference) + int(reversed_original))
print("You chose the number", original_number, "\n"
"Now we will reverse that number so that we have", reversed_original)
print("Subtracting the smaller of these two numbers from the larger gives us", difference_of_original)
print("Flipping that around gives us", reversed_difference)
print("When we add the new number and the reversed number, it gives us,", awesome_number)