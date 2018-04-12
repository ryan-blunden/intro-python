#! /usr/bin/env python3

import sys


def seattle_greeting():
    """Greet the user in varying ways depending upon where they are from. If they are from Seattle, they should get
    a different and special greeting."""

    city = input('Where are you from? ').strip().lower()

    if city == '':
        sys.stderr.write('Sorry, we didn\'t get your city. Please enter next time.\n')
        exit(1)

    if city == 'seattle':
        sys.stdout.write('Go Mariners!\n')
    else:
        sys.stdout.write('Welcome to the home of grunge!\n')


if __name__ == '__main__':
    seattle_greeting()
