#!/usr/bin/python3
def lookup(obj):
    """ Function that returns the list of available attributes

    Args:
        obj: the class

    Returns:
        List of attributes and methodes
    """

    return dir(obj)

