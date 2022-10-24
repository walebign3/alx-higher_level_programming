#!/usr/bin/python3
"""script that , sends a request to the URL"""
import requests
import sys


if __name__ == "__main__":
    r = requests.get(sys.argv[1])
    print(r.status_code)
