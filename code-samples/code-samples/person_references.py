"""
This file is for demonstrating the differences between simple and complex types in Python.
"""


class Person:
    first_name: str = ''
    last_name: str = ''

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
