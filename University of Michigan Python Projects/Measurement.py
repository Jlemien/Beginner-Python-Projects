#Your program will prompt the user for an floating point value representing miles/hour. You will reprint that value along with the value converted to the following values:
# how many miles can you travel in one hour?

Bananas = (float(input("how many miles can you travel in one hour? ")))

hours = 1
print("You can travel", Bananas, "miles in one hour.")
barleycorns_per_day = Bananas * 190080 * 24
print("This means that you can travel", barleycorns_per_day, "barleycorns in one day.")
furlongs_per_fortnight = 7.99998 * Bananas * 24 * 14
print("This means that you can travel", furlongs_per_fortnight, "furlongs per fortnight")
#speed of sound is 1130 feet/second
Bananas_as_feet_per_second = Bananas * 5280 / 60 / 60
mach = Bananas_as_feet_per_second / 1130
print("This means that you can travel at mach", mach)
# the mach number is a measure of speed, the percentage of the speed of sound. Mach 1 is a
#speed equal to the speed of sound in air, which is 1130 feet/second. Mach 1.5 would be
#1.5 times the speed of sound.
Bananas_as_meters_per_second = Bananas * 1609.34 / 60 / 60
percent_of_speed_of_light = Bananas_as_meters_per_second / 299792458
#This means that you can travel at PERCENTAGE of the speed of light
#PSL is a speed, the percentage of the speed of light in a vacuum. The speed of light is 299,792,458 meters/second.
print("This means that you can travel at", percent_of_speed_of_light, "percent of the spped of light.")