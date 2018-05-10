import json


class StarbucksStore:
    """
    Starbucks Store that does not allow the user to change the attributes once it has been created.

    This has been done to show you another style of modelling where the model does not allow mutations, therefore, we
    get around potential problems of different parts of our code changing a single model that might be referenced in
    multiple places.
    """
    _name: str = ''
    _address: str = ''
    _is_open: str = ''

    def __init__(self, name: str, address: str, is_open: bool):
        self._name = name
        self._address = address
        self._is_open = is_open

    def __repr__(self):
        return self.description

    @property
    def description(self):
        output = '{}, {}'.format(self.name, self.address)
        if self.is_open is True:
            output += ' (open now).'

        return output

    @property
    def name(self):
        return self._name

    @property
    def address(self):
        return self._address

    @property
    def is_open(self):
        return self._is_open


if __name__ == '__main__':
    store_models = []
    stores_json = json.load(open('data/starbucks_stores.json'))['stores']

    # Generate 10 Store models
    for store in stores_json[0:10]:
        store_models.append(
            StarbucksStore(
                name=store['name'],
                address=' '.join(store['addressLines']),
                is_open=store['open']
            )
        )

    # Display the store models
    for store in store_models:
        print(store)
