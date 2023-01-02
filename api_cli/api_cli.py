import requests

city = input("Enter city: ")

r = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid=d165339b5bc5a67a68ea36b2a7695185&units=imperial")

data = r.json()

temp = int(data["main"]["temp"])

print(f"The current temp in {city} is {temp}°F.")
