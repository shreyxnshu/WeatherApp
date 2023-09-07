import requests
import json

# Defining API Key
api_key = 'dc7f42f55e7f370d1054480bb3cf87b1'

# Taking input as the name of the city whose temperature has to be find out
city = input("Enter the name of city: ")

# Requesting openweathermap.org for the weather data
weather_data = requests.get(
  f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}")

# Sorting the data we need from the recieved data and storing it
weather = weather_data.json().get("main")["temp"]

# Converting the value in 'C and storing the final value of temperature
temp = weather - 273

# Printing the desired Output
print("The temperature in ", city, " is ", temp, "'C")
