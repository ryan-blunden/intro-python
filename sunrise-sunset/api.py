from json import JSONDecodeError

import requests
from models import Location


def get_location_from_city(search_city, state="WA"):
    search_city = search_city.strip().lower()
    url = 'http://localhost:8080/api/v1/locations.json'
    locations = requests.get(url).json()

    for location in locations:
        if search_city == location['city'].lower():
            return Location(
                lat=location['lat'],
                lng=location['lng'],
                city=location['city'],
                state=location['state']
            )

    return None


def get_sunrise_sunset(lat, lng, sys=None):
    api_url = 'https://api.sunrise-sunset.org/json?lat={lat}&lng={lng}&formatted=0'
    request_url = api_url.format(lat=lat, lng=lng)

    try:
        return requests.get(request_url).json()['results']
    except JSONDecodeError as err:
        sys.stderr.write('[error]: JSON was not well formed: {url}, {err}'.format(
            url=api_url,
            err=err
        ))
