"""import webbrowser
webbrowser.open(r"http://www.cse.msu.edu/~cse231/PracticeOfComputingUsingPython/01_Beginnings/FirstWeekProjects/WindChill/project01.pdf")
"""

air_temp = 10.0
windspeed = 15
wct_index = 35.74 + 0.6215 * air_temp - 35.75 * windspeed**0.16 + 0.4275 * air_temp * windspeed**0.16
print("A temperature of", air_temp, "and a windspeed of", windspeed,  "means that the windchill will be", wct_index, ".")
air_temp = 0.0
windspeed = 25
wct_index = 35.74 + 0.6215 * air_temp - 35.75 * windspeed**0.16 + 0.4275 * air_temp * windspeed**0.16
print("A temperature of", air_temp, "and a windspeed of", windspeed,  "means that the windchill will be", wct_index, ".")
air_temp = -10.0
windspeed = 35
wct_index = 35.74 + 0.6215 * air_temp - 35.75 * windspeed**0.16 + 0.4275 * air_temp * windspeed**0.16
print("A temperature of", air_temp, "and a windspeed of", windspeed,  "means that the windchill will be", wct_index, ".")

print("Lets calculate the windchill.")
air_temp = float(input("What is the current air temperature? "))   
windspeed = float(input("What is the current wind speed? "))
wct_index = 35.74 + 0.6215 * air_temp - 35.75 * windspeed**0.16 + 0.4275 * air_temp * windspeed**0.16
print("A temperature of", air_temp, "and a windspeed of", windspeed,  "means that the windchill will be", wct_index, ".")
