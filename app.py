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

def get_lat_lon(lat, lon, API_key):
    resp = requests.get('http://api.openweathermap.org/geo/1.0/direct?q={city name},{state code},{country code}&limit={limit}&appid={API key}').json()
    data = resp[0]
    lat, lon = data.get('lat'), data.get('lon')      
  
    return lat, lon


def get_current_weather(lat, lon, API_key):
    resp = requests.get('http://api.openweathermap.org/geo/1.0/direct?q={city name},{state code},{country code}&limit={limit}&appid={API key}').json()
    data = WheaterData(
        main=resp.get('weather')[0].get('main'),
        description=resp.get('weather')[0].get('description'),
        icon=resp.get('weather')[0].get('icon'),
        temperature=resp.get('main').get('temp')      
    )
    
    return data

def main(city_name, state_name)



    
if __name__ == "__main__":
    lat, lon = get_lat_lon('Toronto', 'ON', 'Canada', api_key)
    get_current_weather(lat, lon, api_key)

