#!/usr/bin/python3
def say_my_name(first_name, last_name=""):
    """
    Prints "My name is <first name> <last name>"

    Args:
                first_name: firstname
        last_name: lastname

        Raises:
        TypeError: If first_name or last_name are not strings.

    Returns:
                nothing

    """
    if not isinstance(first_name, str):
        raise TypeError('first_name must be a string')
    if not isinstance(last_name, str):
        raise TypeError('last_name must be a string')
    print("My name is {}{}".format(first_name, " " +
          last_name if last_name else ""))
