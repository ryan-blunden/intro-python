class Person:
    first_name: str = ''
    last_name: str = ''
    properties = {}

    def __init__(self, first_name: str, last_name: str):
        """
        Set the person's first and last name.

        :param first_name:
        :param last_name:
        """
        self.first_name = first_name
        self.last_name = last_name

    def __repr__(self) -> str:
        # This uses the `full_name` property right now but should be improved
        # to provide more information.
        return self.full_name

    @property
    def full_name(self) -> str:
        return '{} {}'.format(self.first_name, self.last_name)


person = Person('James', 'Taylor')
person.properties['favorite_movie'] = 'Meet Joe Black'
person.properties['favorite_food'] = 'Ice-Cream'

#

# No limit to what you can assign to a Dictionary

my_dict = {}  # empty

# Item assignment
my_dict['favorite_movie'] = 'Meet Joe Black'
my_dict['favorite_food'] = 'Ice-Cream'
my_dict['age'] = 36


# Assignment at creation
my_other_dict = {
    'fav_movie': 'Meet Joe Black',
    'favorite_food': 'pizza'
}

my_dict['favorite_movie']  # Getting a key from a dictionary
my_dict['does_not_exist']  # KeyError

# A way
try:
    my_dict['does_not_exist']
except KeyError:
    pass # That's ok, just keep going :)

# A better way
my_dict.get('does_not_exist', None)  # Return a default value if key doesn't exist






