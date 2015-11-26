# This file was only intended to help debug code for a Codewars challenge.

def convertToCelsius(temperature):
    celsius = (temperature - 32) * (5/9)
    return celsius

print(convertToCelsius(50))

def weather_info(temperature):
    c = convertToCelsius(temperature)
    if c > 0:
        return str(c) + " is above freezing temperature"
    else:
        return str(c) + " is freezing temperature"
