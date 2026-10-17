import requests

city = input("which city? ")

geo_url = "https://geocoding-api.open-meteo.com/v1/search"
geo_response = requests.get(geo_url,params = {"name": city, "count": 1})
geo_data = geo_response.json()


if "results" not in geo_data:
    print("City not found.")

else:
    place = geo_data["results"][0]
    lat = geo_data["results"][0]["latitude"]
    lon = geo_data["results"][0]["longitude"]
    print("found:",place["name"],"-",place.get("country",""))



weather_url = "https://api.open-meteo.com/v1/forecast"

        
params = {
    "latitude": lat,
    "longitude": lon,
    "current_weather": True,
    "timezone": "auto",
}

data = requests.get(weather_url,params=params).json()


if "current_weather" not in data:
    print("server error:",data.get("reason","unknown problem"))

else:
    weather = data["current_weather"]
    print(place["name"],"is",weather["temperature"],"degree C right now")
    print("wind speed:",weather["windspeed"],"km/hr")


