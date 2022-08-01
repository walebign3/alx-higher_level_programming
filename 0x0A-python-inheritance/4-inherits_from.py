#!/usr/bin/python3
"""
Returns True if the object is an instance of a class that inherited
"""


def inherits_from(obj, a_class):
    """
    Returns True if the object is an instance of a class that inherited
    """
    if type(obj) == a_class:
        return (False)
    return isinstance(obj, a_class)
