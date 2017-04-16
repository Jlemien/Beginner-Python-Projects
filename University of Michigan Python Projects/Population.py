print("I will give you an estimate for what the US population will be in the future")
year = input("what year would you like a prediction for? ")
years_into_the_future = float(year) - 2017
print("That is about", years_into_the_future, "years in the future.")
current_population = 307357870

#I estimate that in X years the US population will be about Y.
#every 7 seconds, a birth
birth_every_7_seconds = years_into_the_future * 365 *24 * 60 * 60 / 7

#every 13 seconds, a death
death_every_13_seconds = years_into_the_future * 365 *24 * 60 * 60 / 13

#every 35 seconds, a new immigrant
new_immigrant_every_35_seconds = years_into_the_future * 365 *24 * 60 * 60 / 35

predicted_population = current_population + (birth_every_7_seconds) + (new_immigrant_every_35_seconds) - (death_every_13_seconds)

print("The population of the US in the year", year, "will be about", predicted_population)