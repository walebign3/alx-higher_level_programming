#!/usr/bin/python3
"""script that , sends a request to the URL"""
import requests
import sys


if __name__ == "__main__":
    r = requests.get(sys.argv[1])
    try:
        if r.status_code > 400:
            print('Error code:', r.status_code)
        else:
            print(r.content.decode("utf-8"))
    except KeyError:
        pass
