#http://www.cse.msu.edu/~cse231/PracticeOfComputingUsingPython/01_Beginnings/SecondWeekProjects/Garden2/Project01.pdf
import math

print("This program will help you plan your garden.")
print("First, we need some information about the dimensions you want.")

while True:
    try:
        length_of_one_side_of_the_garden = float(input("How many feet long is one side of the garden? "))
    except ValueError:
        print("Sorry, I didn't understand that. Please enter digits.")
        continue
    else:
        break
while True:
    try:
        recommended_spacing_between_plants = float(input("How many inches of spacing should there be between plants? "))
    except ValueError:
        print("Sorry, I didn't understand that. Please enter digits.")
        continue
    else:
        break
while True:
    try:
        depth_of_the_flowerbeds = float(input("How many feet deep should the flowerbeds be? "))
    except ValueError:
        print("Sorry, I didn't understand that. Please enter digits.")
        continue
    else:
        break
while True:
    try:
        depth_of_fill_areas = float(input("How many feet deep should the fill areas be? "))
    except ValueError:
        print("Sorry, I didn't understand that. Please enter digits.")
        continue
    else:
        break

radius_of_circle = length_of_one_side_of_the_garden / 2
area_of_circle = math.pi * radius_of_circle**2

area_needed_per_plant = recommended_spacing_between_plants**2

area_of_triangle = (length_of_one_side_of_the_garden * .5) * (length_of_one_side_of_the_garden * .5) /2
plants_per_triangle = area_of_triangle / area_needed_per_plant
plants_for_the_circle = area_of_circle / area_needed_per_plant
garden_area = ( area_of_triangle * 4 ) + area_of_circle
soil_per_triangle = area_of_triangle * depth_of_the_flowerbeds * .3
soil_for_the_circle = area_of_circle * depth_of_the_flowerbeds * .3
area_of_fill = (length_of_one_side_of_the_garden * length_of_one_side_of_the_garden) - area_of_circle - (area_of_triangle * 4)

print("\nSummary of your plant needs:")
print("Each outer triangular bed: {0} plants".format(round(plants_per_triangle, 1)))
print("The central circular bed: {0} plants".format(round(plants_for_the_circle, 1)))
print("Total: {0} plants".format(round((plants_for_the_circle + plants_per_triangle),1)))

print("\nSummary of your soil needs:")
print("Each outer triangular bed: {0} cubic yards of soil".format(round(soil_per_triangle, 1)))
print("The central circular bed: {0} cubic yards of soil".format(round(soil_for_the_circle,1)))
print("Total: {0} cubic yards of soil".format(round((soil_per_triangle + soil_for_the_circle),1)))

print("\nSummary of your fill needs:")
print("The diamond shape: {0} cubic yards of fill".format(round((area_of_fill * depth_of_fill_areas * .3),1)))