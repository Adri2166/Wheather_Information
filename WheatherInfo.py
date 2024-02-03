import datetime as dt
import requests # pip install requests

# Base URL for the OpenWeatherMap API
base_URL = "http://api.openweathermap.org/data/2.5/weather?"

# Read API key from a file named 'API_WEATHER'
API_key = open('API_WEATHER', 'r').read()

# Get user input for the city and capitalize the first letter
city = input("Choose a city: ").capitalize()

# Function to convert temperature from Kelvin to Celsius and Fahrenheit
def kelvin_to_celsius_fahrenheit(kelvin):
    celsius = kelvin - 273.15
    fahrenheit = celsius * (9/5) + 32
    return celsius, fahrenheit

# Construct the URL for the API request
url = base_URL + "appid=" + API_key + "&q=" + city

# Send a GET request to the API and parse the JSON response
response = requests.get(url).json()

# Extract temperature information from the response
temp_kelvin = response['main']['temp']
temp_celsius, temp_fahrenheit = kelvin_to_celsius_fahrenheit(temp_kelvin)

# Extract "feels like" temperature from the response
feels_like_kelvin = response['main']['feels_like']
feels_like_celsius, feels_like_fahrenheit = kelvin_to_celsius_fahrenheit(feels_like_kelvin)

# Extract wind speed, humidity, description, sunrise time, and sunset time from the response
wind_speed = response['wind']['speed']
humidity = response['main']['humidity']
description = response['weather'][0]['description']
sunrise_time = dt.datetime.utcfromtimestamp(response['sys']['sunrise'] + response['timezone'])
sunset_time = dt.datetime.utcfromtimestamp(response['sys']['sunset'] + response['timezone'])

# Print weather information for the chosen city
print(f"Temperature in {city}: {round(temp_celsius)}°C ({round(temp_fahrenheit)}°F)")
print(f"Temperature in {city} feels like: {round(feels_like_celsius)}°C ({round(feels_like_fahrenheit)}°F)")
print(f"Humidity in {city}: {humidity}%")
print(f"Wind speed in {city}: {round(wind_speed * 3.6)}km/h")
print(f"General weather in {city}: {description}")
print(f"Sun rises in {city} at {sunrise_time} local time")
print(f"Sun sets in {city} at {sunset_time} local time")
