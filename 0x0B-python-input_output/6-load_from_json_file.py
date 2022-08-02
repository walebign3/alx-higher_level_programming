#!/usr/bin/python3
"""A function that creates an Obj form Json"""
import json


def load_from_json_file(filename):
    """A function that creates n Obj from json """
    with open(filename, 'r', encoding="utf-8") as f:
        return json.load(f)
