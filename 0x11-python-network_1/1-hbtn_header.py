#!/usr/bin/python3
"""script that displays X-Request-Id"""
import urllib.request
import sys


if __name__ == "__main__":
    with urllib.request.urlopen(sys.argv[1]) as response:
        data = response.info()
        print(data["X-Request-Id"])
