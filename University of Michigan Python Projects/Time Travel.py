#http://www.cse.msu.edu/~cse231/PracticeOfComputingUsingPython/01_Beginnings/FirstWeekProjects/TimeTravel/project01.pdf
import math

speed_of_light = 299792458
original_mass = 70000

percent_of_speed_of_light = float(input("What percent of the speed of light do you wanna move? "))
velocity_in_meter_per_second = percent_of_speed_of_light / speed_of_light
bottom_part_of_equation = math.sqrt(1 - ((velocity_in_meter_per_second ** 2) / (speed_of_light * speed_of_light)))
factor = 1 / bottom_part_of_equation
time_passage = 1 / factor
new_mass = original_mass * factor

print(time_passage)
print("Travelling at", percent_of_speed_of_light, "is", velocity_in_meter_per_second, "meters per second.")
print("Your", original_mass, "kilgram spaceship would weigh", new_mass, "kilograms.")
print("You would need", 4.3 / factor, "years to travel to Alpha Centauri.")
print("You would need", 6.0 / factor, "years to travel to Barnard's Star.")
print("You would need", 309 / factor, "years to travel to to Betelgeuse.")
print("You would need", 2000000 / factor, "years to travel to to the Andromeda Galaxy.")
