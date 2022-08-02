#!/usr/bin/python3
"""Object to a text file, using a JSON representation:"""
import json


def save_to_json_file(my_obj, filename):
    """Object to a text file, using a JSON representation:"""
    with open(filename, 'w', encoding='utf-8') as fs:
        json.dump(my_obj, fs)
