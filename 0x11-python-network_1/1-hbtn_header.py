#!/usr/bin/python3
"""script that displays the value of the X-Request-Id"""
import urllib.request
import sys


url = sys.argv[1]
if __name__ == "__main__":
    with urllib.request.urlopen(url) as response:
        data = response.info()
        print(data["X-Request-Id"])
