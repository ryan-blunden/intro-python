from typing import Union


def fahrenheit_to_celsius(fahrenheit: int, float_precision: bool = False) -> Union[int, float]:
    """
    Convert fahrenheit to celsius.
    Note: We are not using float for the input our output, because at this time, our users
    prefer not to have that level of precision.
    :param fahrenheit:int
    :param float_precision:bool
    :return:int
    """
    # Formula: Subtract 32 and multiply by .5556 (or 5/9).
    result = (fahrenheit - 32) * .5556
    if not float_precision:
        return round(result)
    return round(result, ndigits=2)


# Very basic unit tests
assert fahrenheit_to_celsius(32) == 0
assert fahrenheit_to_celsius(46) == 8
assert fahrenheit_to_celsius(46, True) == 7.78
