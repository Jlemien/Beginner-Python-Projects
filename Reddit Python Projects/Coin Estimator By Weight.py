"""
When some people receive change after shopping, they put it into a container and let it add up over time.
Once they fill up the container, they'll roll them up in coin wrappers which can then be traded in at a
bank for what they are worth. While most banks will give away coin wrappers for free, it's convenient to
have an idea of how many you will need. Instead of counting how many coins you have, it's easier to separate
all of your coins, weigh them, and then estimate how many of each type you have and then how many wrappers you'll need.
For example, if you weigh all of your dimes and see that you have 1276.9g of them, you can estimate that
you have about 563 dimes (since each one is 2.268g) and you would be able to fill 11 dime wrappers.
Goal:
Create a program that allows the user to input the total weight of each type of coin they have
(pennies, nickels, dimes, and quarters), and then print out how many of each type of wrapper they would need,
how many coins they have, and the estimated total value of all of their money.
Weight of each coin and how many fit inside each type of wrapper.
https://en.wikipedia.org/wiki/Coin_wrapper#Amount_in_a_roll_in_the_United_Statesh
ttps://www.usmint.gov/about_the_mint/?action=coin_specifications
"""
while True:
    try:
        type_of_coin = str(input("Which type of coin do you have? (pennies, nickels, dimes, or quarters): "))
    except ValueError:
        print("Sorry, I didn't understand that.")
        continue
    except NameError:
        print("Sorry, I didn't understand that.")
        continue
    else:
        break
if type_of_coin == "pennies": 
    print("Now we will figure out how many pennies you have.")
    while True:
        try:
            weight_of_pennies = float(input("How many grams do all your pennies weigh together? "))
        except ValueError:
            print("Sorry, I didn't understand that.")
            continue
        else:
            break
    quantity_of_pennies = (weight_of_pennies) / 3.11
    dollar_value_of_pennies = quantity_of_pennies / 100
    quantity_of_penny_rolls_needed = quantity_of_pennies / 50
    print("You have about", int(quantity_of_pennies), "pennies, which are worth about", int(dollar_value_of_pennies), "dollars.\nYou will need about", int(quantity_of_penny_rolls_needed), "rolls for these pennies.")
elif type_of_coin == "nickels": 
    print("Now we will figure out how many nickels you have.")
    while True:
        try:
            weight_of_nickels = float(input("How many grams do all your nickels weigh together? "))
        except ValueError:
            print("Sorry, I didn't understand that.")
            continue
        else:
            break
    quantity_of_nickels = (weight_of_nickles) / 5.00
    dollar_value_of_nickels = quantity_of_nickles / 20
    quantity_of_nickels_rolls_needed = quantity_of_nickels / 40
    print("You have about", int(quantity_of_nickels), "nickels, which are worth about", int(dollar_value_of_nickels), "dollars.\nYou will need about", int(quantity_of_nickels_rolls_needed), "rolls for these nickels.")
elif type_of_coin == "dimes": 
    print("Now we will figure out how many dimes you have.")
    while True:
        try:
            weight_of_dimes = float(input("How many grams do all your dimes weigh together? "))
        except ValueError:
            print("Sorry, I didn't understand that.")
            continue
        else:
            break
    quantity_of_dimes = (weight_of_dimes) / 2.268
    dollar_value_of_dimes = quantity_of_dimes / 10
    quantity_of_dimes_rolls_needed = quantity_of_dimes / 50
    print("You have about", int(quantity_of_dimes), "dimes, which are worth about", int(dollar_value_of_dimes), "dollars.\nYou will need about", int(quantity_of_dimes_rolls_needed), "rolls for these dimes.")
elif type_of_coin == "quarters": 
    print("Now we will figure out how many quarters you have.")
    while True:
        try:
            weight_of_quarters = float(input("How many grams do all your quarters weigh together? "))
        except ValueError:
            print("Sorry, I didn't understand that.")
            continue
        else:
            break
    quantity_of_quarters = (weight_of_quarters) / 5.670
    dollar_value_of_quarters = quantity_of_quarters / 4
    quantity_of_quarters_rolls_needed = quantity_of_quarters / 40
    print("You have about", int(quantity_of_quarters), "quarters, which are worth about", int(dollar_value_of_quarters), "dollars.\nYou will need about", int(quantity_of_quarters_rolls_needed), "rolls for these quarters.")
else:
    print("That is not a valid coin. Are you sure you spelled it right? Try running the program again.")
