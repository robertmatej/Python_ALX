'''
podać w konsoli miasto i ma po tym wyswietlić dane o pogodzie
w pierwszym kroku pobrać miasto: pierwszy element później woeid

w drugium kroku pobrać po woeid pogodę dla lokalizacji

wypisać: wilgotność, temperatura, cisnienie,  wiatr?

https://www.metaweather.com/api/location/523920/


'''

import sys
import json
import urllib.request
from collections import namedtuple

Weather = namedtuple("Weather")

def get_location_id():
    url = f"https://www.metaweather.com/api/location/search/?query={location_id}"
    with urllib.request.urlopen(url) as f:
        kod_miasto = json.loads(f.read())
        return kod_miasto[0]['woeid']

def get_location_weather(location_id):
    url = f"https://www.metaweather.com/api/location/search/?query={location_id}"
    with urllib.request.urlopen(url) as f:
        result = json.loads(f.read())
        return result[0]['woeid']

def print_weather(weather):
    print('''
Pogoda w lokalizacji: {weather.location} 
    
    ''')


if __name__ == '__main__':
    #pobrać ID dla lokalizacji
    location_id = get_location_id(sys.argv[1])
    print(location_id)

    #pobrać pogodę dla lokalizacji
    weather = get_location_weather(location_id)

    #wyświeltić wynik