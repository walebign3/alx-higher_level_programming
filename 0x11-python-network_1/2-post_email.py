#!/usr/bin/python3
"""script that send POST"""
import urllib.request
import urllib.parse
import sys


if __name__ == "__main__":
    params = {"email": sys.argv[2]}
    query_string = urllib.parse.urlencode(params)
    data = query_string.encode("ascii")
    with urllib.request.urlopen(sys.argv[1], data) as response:
        print(response.read().decode("utf-8"))
