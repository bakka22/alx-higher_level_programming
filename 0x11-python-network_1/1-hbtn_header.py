#!/usr/bin/python3
""" Python script that fetches https://alx-intranet.hbtn.io/status """
import urllib.request
import sys
if __name__ == '__main__':
    url = sys.argv[1]
    with urllib.request.urlopen(url) as r:
        va = r.headers.get('X-Request-Id')
        print(va)
