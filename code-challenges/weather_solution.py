#! /usr/bin/env python3

import os
from enum import Enum

import requests

SAMPLE_DATA_API_KEY = 'b6907d289e10d714a6e88b30761fae22'
API_KEY = os.environ.get('API_KEY', SAMPLE_DATA_API_KEY)
API_HOST = os.environ.get('API_HOST', 'https://api.openweathermap.org')
# If no API_KEY supplied by user, change API to point to (hard-coded) sample data-set
if API_KEY == SAMPLE_DATA_API_KEY:
    API_HOST = 'http://samples.openweathermap.org'


class APIError(Exception):
    pass


class TemperatureUnit(Enum):
    CELSIUS = 'celsius'
    FAHRENHEIT = 'fahrenheit'
    KELVIN = 'kelvin'

    @staticmethod
    def units() -> str:
        return ', '.join([unit.value for unit in TemperatureUnit])


def get_weather_forecast(city: str, country: str, unit: TemperatureUnit = TemperatureUnit.CELSIUS) -> str:
    api_path = '{api_host}/data/2.5/forecast?q={city},{country}&units={units}&appid={api_key}'
    temp_to_unit_type = {
        'celsius': 'metric',
        'fahrenheit': 'imperial',
        'kelvin': 'kelvin',
    }

    units = temp_to_unit_type[unit.name.lower()]
    url = api_path.format(api_host=API_HOST, city=city, country=country, units=units, api_key=API_KEY)
    try:
        json_response = requests.get(url).json()
        temp = json_response['list'][0]['main']['temp']
    except KeyError:
        raise APIError('Request to the Weather API Failed: \n{}'.format(json_response))
    return 'It\'s currently {temp}° {unit} in {city}, {country}.'.format(
        temp=round(temp),
        unit=unit.value,
        city=city.capitalize(),
        country=country.upper()
    )


if __name__ == '__main__':
    input_city = input('City: ').strip().lower()
    input_country_code = input('Country Code (2 characters): ').strip().lower()[0:2]
    input_temp_unit = TemperatureUnit(input('Unit ({}): '.format(TemperatureUnit.units())).strip().lower())

    print(get_weather_forecast(input_city, input_country_code, input_temp_unit))
