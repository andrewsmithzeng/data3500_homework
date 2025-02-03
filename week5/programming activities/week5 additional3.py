"""
2. You are building a weather decision-making system for a camping trip. 
To decide whether to go camping, you need to consider the weather conditions and other factors. 
You will make the decision based on the following criteria:

The weather should be either clear or partly cloudy.
The temperature should be between 50°F (10°C) and 85°F (30°C).
It should not be raining or snowing.
It should not be too windy (wind speed less than 20 mph).
Your program should prompt the user to enter the current weather conditions, temperature, and wind speed, 
and then determine whether it's a good day to go camping.

Write a Python program for weather-based decision-making that takes weather conditions, temperature, and wind speed as input 
and checks if it's a good day for camping based on the criteria above. 
Display a message indicating whether it's a good day to go camping or not.
"""
weather = input("Enter the weather conditions (clear, partly cloudy, raining, snowing): ").lower()
temperature = float(input("Enter the temperature in Fahrenheit: "))
wind_speed = float(input("Enter the wind speed in mph: "))

#check weather
weather = weather == "clear" or weather == "partly cloudy"
#check temperature
temperature = 50 <= temperature <= 85
#check wind speed
wind_speed = wind_speed < 20

#use boolean expression to determine whether it's a good day to go camping
good_day = weather and temperature and wind_speed

if good_day:
    print("It's a good day to go camping!")
else:
    print("It's not a good day to go camping.")