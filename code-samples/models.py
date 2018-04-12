#! /usr/bin/env python3

import json
from enum import Enum


class Coffee:
    class Body(Enum):
        LIGHT = 1
        MEDIUM = 2
        FULL = 3

    class RoastProfile(Enum):
        BLONDE = 1
        MEDIUM = 2
        DARK = 3

    name: str = ''
    aroma: str = ''
    body: int = None  # Should use the Body enum
    roast_profile: int = None
    is_starbucks: bool = None

    def __init__(self, name: str, aroma: str, body: Body, roast_profile: RoastProfile, is_starbucks: bool):
        self.name = name
        self.aroma = aroma
        self.body = body
        self.roast_profile = roast_profile
        self.is_starbucks = is_starbucks

    @staticmethod
    def from_json(json_string):
        """Return a `Coffee` instance from the supplied json string"""

        json_data = json.loads(json_string)
        return Coffee(
            name=json_data['name'],
            aroma=json_data['aroma'],
            body=Coffee.Body(json_data['body']),
            roast_profile=Coffee.RoastProfile(json_data['roastProfile']),
            is_starbucks=json_data['isStarbucks']
        )

    def __repr__(self):
        return 'Name: {}'.format(self.name)


# Debugging or testing construct
if __name__ == '__main__':
    pike_place_coffee = Coffee(
        name='Pike Place',
        aroma='Smooth',
        body=Coffee.Body.MEDIUM,
        roast_profile=Coffee.RoastProfile.MEDIUM,
        is_starbucks=True
    )
    assert pike_place_coffee.name == 'Pike Place'
    assert pike_place_coffee.aroma == 'Smooth'
    assert pike_place_coffee.body == Coffee.Body.MEDIUM
    assert pike_place_coffee.roast_profile == Coffee.RoastProfile.MEDIUM
    assert pike_place_coffee.is_starbucks is True

    json_string = '''{
        "name": "Ethiopia",
        "aroma": "Bold",
        "body": 2,
        "roastProfile": 2,
        "isStarbucks": true

    }'''

    ethopia_coffee = Coffee.from_json(json_string)
    assert ethopia_coffee.name == 'Ethiopia'
    assert ethopia_coffee.aroma == 'Bold'
    assert ethopia_coffee.body == Coffee.Body.MEDIUM
    assert ethopia_coffee.roast_profile == Coffee.RoastProfile.MEDIUM
    assert ethopia_coffee.is_starbucks is True
