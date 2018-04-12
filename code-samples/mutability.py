#! /usr/bin/env python3

names = ['Dan', 'Jen', 'Harry']


def change_names(names_to_change):
    names_to_change.pop()


print('Value of names = {}'.format(names))
change_names(names)
print('Value of names = {}'.format(names))
