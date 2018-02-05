#
# Seattle mood
#
# This script takes input from the user about the
# results of the most recent Mariners and Sea Hawks
# game in order to calculate the mood of the people
# of Seattle.
#

# TODO: Refactor this code into functions.
# TODO: Add automated tests.
# TODO: Improve validation of input, to ask again if input is not "yes" or "no".

import json
import sys

from utils.strings import text_to_boolean

seahawks_win_text = input('Did the Sea Hawks win? [yes/no]: ')
seahawks_win = text_to_boolean(seahawks_win_text)

mariners_win_text = input('Did the Mariners win? [yes/no]: ')
mariners_win = text_to_boolean(mariners_win_text)

with open('messages.json', 'r') as messages_file:
    messages = json.loads(messages_file.read())

# Determine message
chosen_message = None

if seahawks_win and mariners_win:
    chosen_message = messages['both_win']
elif seahawks_win or mariners_win:
    chosen_message = messages['either_win']
else:
    chosen_message = messages['no_win']

# Show result to user
sys.stdout.write('Seattle is saying "{}"\n'.format(chosen_message))
