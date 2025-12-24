import requests
from dotenv import load_dotenv
import os
from dataclasses import dataclass

load_dotenv()
api_key = os.getenv('API_KEY')

@dataclass
class WheaterData:
    main: str
    description: str
    icon: str
    temperature: float


def get_lat_lon(city, state, country, API_key):
    url = "http://api.openweathermap.org/geo/1.0/direct"

    params = {
        "q": f"{city},{state},{country}",
        "limit": 1,
        "appid": API_key
    }

    resp = requests.get(url, params=params).json()

    if not resp:
        raise ValueError("Location not found")

    lat = resp[0]["lat"]
    lon = resp[0]["lon"]

    return lat, lon


def get_current_weather(lat, lon, API_key):
    url = "https://api.openweathermap.org/data/2.5/weather"

    params = {
        "lat": lat,
        "lon": lon,
        "appid": API_key,
        "units": "metric"
    }

    resp = requests.get(url, params=params).json()

    data = WheaterData(
        main=resp["weather"][0]["main"],
        description=resp["weather"][0]["description"],
        icon=resp["weather"][0]["icon"],
        temperature=resp["main"]["temp"]
    )

    return data


def main(city_name, state_name, country_name):
    lat, lon = get_lat_lon(city_name, state_name, country_name, api_key)
    wheaterdata = get_current_weather(lat, lon, api_key)
    return wheaterdata
