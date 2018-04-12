#! /usr/bin/env python3

import json

stores_json_response = json.load(open('data/starbucks_stores.json'))

# Challenge 1 - for loop
open_stores = []
for store in stores_json_response['stores']:
    open_stores.append(store)

print('Open stores from for loop:\n{}\n\n'.format(open_stores))

# Challenge - list comprehension
open_stores = [store for store in stores_json_response['stores'] if store['open']]
print('Open stores from list comprehension:\n{}\n\n'.format(open_stores))


# Bonus challenge
def store_has_music_experience(store):
    """Return true or false if the store supports the music experience feature"""

    for feature in store['features']:
        if feature['code'] == 'MX':
            return True

    return False


mx_stores = [store for store in stores_json_response['stores'] if store_has_music_experience(store)]
print('Music Experience stores:\n{}\n'.format(open_stores))
