import os
import sys

USER_LANG = os.environ.get('USER_LANG', 'en')

strings = {
    'en': {
        'hello_world': '\n{greeting} {name}\n'
    },

    'hi': {
        'hello_world': '{name}, I wish you {greeting}'
    }
}


def get_env(env_var: str, default_val):
    try:
        return os.environ[env_var]
    except KeyError:
        if default_val:
            return default_val
        else:
            return None


# Better hello_world that returns the greeting text

def hello_world(name: str, greeting: str) -> str:
    greeting_message = strings[USER_LANG]['hello_world']
    return greeting_message.format(name=name, greeting=greeting)


def print_value(value):
    sys.stdout.write('{}\n'.format(value))


# Nicely formatting function calls
# print(
#     hello_world('Ryan', 'Hello')
# )
#
# # Nice formatting with named parameters
# print(
#     hello_world(
#         name='Ryan',
#         greeting='Hello'
#     )
# )

# TODO: Add an optional `float_precision` parameter,
# to give users the option of getting the value back as a float
def fahrenheit_to_celsius(fahrenheit: int) -> int:
    """
    Convert fahrenheit to celsius.
    Note: We are not using float for the input our output, because at this time, our users
    prefer not to have that level of precision.
    :param fahrenheit:int
    :return:int
    """

    # Formula: Subtract 32 and multiply by .5556 (or 5/9).
    return int((fahrenheit - 32) * .5556)

fahrenheit_to_celsius('sdfd')