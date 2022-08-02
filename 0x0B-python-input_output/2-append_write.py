#!/usr/bin/python3
"""appends a string at the end of a text file (UTF8) and returns num of chr """


def append_write(filename="", text=""):
    """appends a string at the end of a text file (UTF8) and returns num of chr """

    with open(filename, 'a', encoding="utf-8") as f:
        return f.write(text)
