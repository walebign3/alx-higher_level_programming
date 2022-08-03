#!/usr/bin/python3
"""returns the dictionary description with simple data structure"""


def class_to_json(obj):
    """ returns the dictionary description with simple data structure """
    dct = {}
    if hasattr(obj, "__dict__"):
        dct = obj.__dict__.copy()
    return dct
