import json

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

# The usa_cities object is taking up a lot of memory and now that we don't need it, tell Python it can reclaim the
# memory by assigning it the value of nothing.
usa_cities = None

# Dump list of dictionaries to the `locations.json` file
json.dump(washington_cities, open('server/api/v1/locations.json', 'w'), indent=4)
