#http://www.cse.msu.edu/~cse231/PracticeOfComputingUsingPython/01_Beginnings/FirstWeekProjects/Debt/project01.pdf

#current debt is 19500000000000

#ask the user for the current national debt
current_national_debt = float(input("What is the current national debt of the USA? "))

#ask the user what denomination of bull they want to use
denomination =  str((input("What denomination of US bill between 1 and 100 would you like to use? ")))
if denomination == str(1):
    height_in_miles = current_national_debt / float(denomination) * 0.0043 / 15133980000
    print("A stack of", denomination, "bills equal to the national debt would be", height_in_miles, "miles high.")
    print("That would take you to the moon", height_in_miles / 238857 , "times.")
elif denomination == str(5):
    height_in_miles = current_national_debt / float(denomination) * 0.0043 / 15133980000
    print("A stack of", denomination, "bills equal to the national debt would be", height_in_miles, "miles high.")
    print("That would take you to the moon", height_in_miles / 238857 , "times.")
elif denomination == str(10):
    height_in_miles = current_national_debt / float(denomination) * 0.0043 / 15133980000
    print("A stack of", denomination, "bills equal to the national debt would be", height_in_miles, "miles high.")
    print("That would take you to the moon", height_in_miles / 238857 , "times.")
elif denomination == str(20):
    height_in_miles = current_national_debt / float(denomination) * 0.0043 / 15133980000
    print("A stack of", denomination, "bills equal to the national debt would be", height_in_miles, "miles high.")
    print("That would take you to the moon", height_in_miles / 238857 , "times.")
elif denomination == str(50):
    height_in_miles = current_national_debt / float(denomination) * 0.0043 / 15133980000
    print("A stack of", denomination, "bills equal to the national debt would be", height_in_miles, "miles high.")
    print("That would take you to the moon", height_in_miles / 238857 , "times.")
elif denomination == str(100):
    height_in_miles = current_national_debt / float(denomination) * 0.0043 / 15133980000
    print("A stack of", denomination, "bills equal to the national debt would be", height_in_miles, "miles high.")
    print("That would take you to the moon", height_in_miles / 238857 , "times.")
else:
    print("That isn't a denomination of US bill.")
