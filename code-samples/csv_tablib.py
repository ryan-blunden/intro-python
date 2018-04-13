#! /usr/bin/env python3

import json
import sys

# We're using the excellent `tablib` library.
# Docs at http://docs.python-tablib.org/en/master/
import tablib

# Import data from CSV
usa_cities_dataset = tablib.Dataset().load(open('data/cities.csv').read())
washington_cities = []
filter_city = 'Washington'

# Filter CSV data to only select cities in Washington state
for city in usa_cities_dataset.dict:
    if city['state_name'] == filter_city:
        washington_cities.append({
            'state': city['state_name'],
            'city': city['city'],
            'lat': city['lat'],
            'lng': city['lng'],
        })

# Dump list of dictionaries to stdout
sys.stdout.write(json.dumps(washington_cities, indent=4))
