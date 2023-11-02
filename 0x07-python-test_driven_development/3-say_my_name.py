#!/usr/bin/python3
"""Print first and last name"""


def say_my_name(first_name, last_name=""):
    """Func that print name
    Args:
    first_name (str)
    last_name (str) """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print(f"My name is {first_name} {last_name}")
