# Built in Python library
import sys

# Our created api module
import api

# 1. Get formatted city name
input_city = input('City (must be in WA, USA): ')
formatted_city = input_city.strip().lower()

# 2. Get location and validate
location = api.get_location_from_city(formatted_city)
if location is None:
    sys.stderr.write(
        '[error]: The city "{}" could not be found. Note! Only cities in Washington state are currently supported. '
        'Please check the spelling of your city and try again."'.format(input_city)
    )
    exit(1)

# 3. Get result and display to user
result = api.get_sunrise_sunset(location.lat, location.lng)
sys.stdout.write(
    'In {city} {state}, sunrise will be at {sunrise} and sunset will be at {sunset}.\n'.format(
        city=location.city,
        state=location.state,
        sunrise=result['sunrise'],
        sunset=result['sunset']
    )
)
