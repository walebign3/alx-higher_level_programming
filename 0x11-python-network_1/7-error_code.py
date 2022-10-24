#!/usr/bin/python3
"""script that , sends a request to the URL"""
import requests
import sys


if __name__ == "__main__":
    r = requests.get(sys.argv[1])
    if result.status_code > 400
        print('Error code:', r.status_code)
    print(r.content.decode("utf-8"))
