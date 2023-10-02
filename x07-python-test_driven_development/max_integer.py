#!/usr/bin/python3
def max_integer(list=[]):
    """
    Finds the max integer in a list.

    Args:
        list (List[int]): The list to find the max integer from.

    Returns:
        The max integer from the list, or None if list is empty.

    >>> max_integer([1, 2, 3, 4])
    4
    >>> max_integer([])
    None
    """
    if len(list) == 0:
        return None
    result = list[0]
    i = 1
    while i < len(list):
        if not isinstance(list[i], (int, float)):
            raise TypeError("All elements must be numbers")
        if list[i] > result:
            result = list[i]
        i += 1
    return result
