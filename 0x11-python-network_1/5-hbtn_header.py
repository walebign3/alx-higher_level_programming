#!/usr/bin/python3
"""script that fetches value of X-Request-Id"""
import requests
import sys


if __name__ == "__main__":
    url = 'https://alx-intranet.hbtn.io/status'
    r = requests.get(url)
    print(r.headers.get("X-Request-id"))
