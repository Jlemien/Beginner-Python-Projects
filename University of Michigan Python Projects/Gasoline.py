#http://www.cse.msu.edu/~cse231/PracticeOfComputingUsingPython/01_Beginnings/FirstWeekProjects/Gasoline/project01.pdf

# get the user to input gallons_of_gasoline of gasoline
gallons_of_gasoline = float(input("How many gallons of gasoline do you have?"))
print(' {} {}'.format("Original number of gallons_of_gasoline is:", gallons_of_gasoline))
#print out the following:
#number of liters
liters = gallons_of_gasoline * 3.7854
#number of barrels of oil required
barrels_of_oil = gallons_of_gasoline / 19.5
#number of pounds of CO2 produced
CO2 = gallons_of_gasoline * 20
#equivilant energy amount of ethanol gallons_of_gasoline
gallon_ethanol = gallons_of_gasoline / .15
#price in US dollars
USD_price = gallons_of_gasoline * 4

#print it all out
print('{} {} {} {}'.format(gallons_of_gasoline, "gallons_of_gasoline of gasoline is the equivilant of", liters, "liters of oil."))
print('{} {} {} {}'.format(gallons_of_gasoline, "gallons_of_gasoline of gasoline requires", barrels_of_oil, "barrels of oil."))
print('{} {} {} {}'.format(gallons_of_gasoline, "gallons_of_gasoline of gasoline produces", CO2, "pounds of CO2"))
print('{} {} {} {}'.format(gallons_of_gasoline, "gallons_of_gasoline of gasoline is equivilant to ", gallon_ethanol, "gallons_of_gasoline of ethanol."))
print('{} {} {} {}'.format(gallons_of_gasoline, "gallons_of_gasoline of gasoline requires", USD_price, "US dollars."))