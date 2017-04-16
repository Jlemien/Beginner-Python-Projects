# https://www.reddit.com/r/beginnerprojects/comments/1eqt8i/function_mean_median_and_mode/
#      Background
# In a set of numbers, the mean is the average, the mode is the number that occurs the most, and if you rearrange all the numbers numerically, the median is the number in the middle.
#      Goal
# Create three functions that allow the user to find the mean, median, and mode of a list of numbers. If you have access or know of functions that already complete these tasks, do not use them.
#      Subgoals
# In the mean function, give the user a way to select how many decimal places they want the answer to be rounded to.
# If there is an even number of numbers in the list, return both numbers that could be considered the median.
# If there are multiple modes, return all of them.

import statistics

#here are the functions that I'll be using
def mean(*varargs):
    sum = 0
    count = 0
    for item in varargs:
        sum = sum + item
        count = count + 1
    return sum / count

def median(*arg):
    print(statistics.median(arg))

def mode(*arg):
    print(statistics.mode())


# now I'll start the active part of my program
UserNumbers = str(input("Enter digits separated by spaces: "))
print(mean(UserNumbers))
