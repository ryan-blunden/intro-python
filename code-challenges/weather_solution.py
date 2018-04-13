#! /usr/bin/env python3

import os
from enum import Enum

# Need a valid open weather map api key
import requests

API_KEY = os.environ.get('OWM_API_KEY', 'b6907d289e10d714a6e88b30761fae22')
API_URL = 'https://openweathermap.org/data/2.5/forecast?q={city},{country}&units={units}&appid={api_key}'


class TemperatureUnit(Enum):
    CELSIUS = 'celsius'
    FAHRENHEIT = 'fahrenheit'
    KELVIN = 'kelvin'

    def get_unit_of_measurement(self):
        pass

    @staticmethod
    def units() -> str:
        return ', '.join([temp_unit.value for temp_unit in TemperatureUnit])


# TODO: Currently hard-coded to celsius.
# TODO: Change output message to include unit.
def get_weather_forecast(city: str, country: str, unit: TemperatureUnit = TemperatureUnit.CELSIUS) -> str:
    url = API_URL.format(city=city, country=country, units='metric', api_key=API_KEY)
    temp = requests.get(url).json()['list'][0]['main']['temp']
    return 'It is currently {} degrees celsius in {},{}'.format(temp, city, country)


if __name__ == '__main__':
    city = input('City: ').strip().lower()
    country_code = input('Country Code (2 characters): ').strip().lower()[0:2]
    temp_unit = TemperatureUnit(input('Unit ({}): '.format(TemperatureUnit.units())).strip().lower())

    print(get_weather_forecast(city, country_code, temp_unit))
