import requests

OWM_Endpoint = "https://api.openweathermap.org/data/2.5/forecast"
api_key = "75f90eaf7e859511c0d5dba3dadeb97d"

weather_params = {
    "lat": 28.9005,
    "lon": 81.2637,
    "appid": api_key,
    "cnt": 4,
}

response = requests.get(OWM_Endpoint, params=weather_params)
response.raise_for_status()
weather_data = response.json()
#print(weather_data["list"][0]["weather"][0]["id"])

for hour_data in weather_data["list"]:
    con_code = hour_data["weather"][0]["id"]
    if int(con_code) < 700:
        will_rain = True

if will_rain:
    print("Bring an Umbrella")