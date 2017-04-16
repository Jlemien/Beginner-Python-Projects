#get input from the user
num_str = (input("Please enter a Richter scale number (must be greater than 0): "))

#I need to make sure that the user inputs a number
#if num_str is not int:
#    print("Please enter a number.")
#elif float(num_str) <= 0:
#    print("Please enter a number above 0.")
#else:


#convert it to a float
num_float = float(num_str)
#get the equivilant amount of joules
joules = 10 ** ((num_float * 1.5) + 4.8)
#I thought that I would need to convert joules to gigajoules, but maybe I don't need this step
#gigajoules = joules / 1000000000
#convert gigajoules to tons of TNT
TNT = joules * 0.00000000024
#print the original number, and the equivilant on joules and tons of TNT
print("An earthquake which is a", num_str, "on the Richter scale realeases", joules, "joules of energy, which is equivilant to", TNT, "tons of TNT.")
