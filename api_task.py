import requests
url = "https://api.open-meteo.com/v1/forecast?latitude=40.71&longitude=-74.01&current_weather=true"
response = requests.get(url)
if response.status_code == 200:
    data = response.json()

    print(" WEATHER REPORT ")
    print("Temperature:", data["current_weather"]["temperature"], "°C")
    print("Wind Speed:", data["current_weather"]["windspeed"], "km/h")
    print("Weather Code:", data["current_weather"]["weathercode"])
else:
    print("Failed to fetch weather data")