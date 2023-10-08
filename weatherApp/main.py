import requests
import json

city = input("Enter the name of city: ")
url = f"http://api.weatherapi.com/v1/current.json?key=798a43a93f0841f5a5285951230810&q={city}"

r = requests.get(url)
with open("weather.json", "w") as f:
    f.write(str(r.text))

weatherDict = json.loads(r.text)
print("current temp: ", weatherDict["current"]["temp_c"])

