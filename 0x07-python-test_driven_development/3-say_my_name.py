#!/usr/bin/python3
# 3-say_my_name.py


"""this defines a name-printing function."""


def say_my_name(first_name, last_name=""):
    """this print a name.

    Args:
        first_name (string): The first name to print.
        last_name (string): The last name to print.
    Raises:
        TypeError: If either of first_name or last_name are not strings.
    """
    if not isinstance(first_name, str):
        raise TypeError("the first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("the last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))
