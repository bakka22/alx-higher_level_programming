#!/usr/bin/python3
""" Python script that fetches https://alx-intranet.hbtn.io/status """
import urllib.request
import urllib.parse
import sys
if __name__ == '__main__':
    url = sys.argv[1]
    try:
        with urllib.request.urlopen(url) as r:
            va = r.read().decode('utf-8')
            print(va)
    except urllib.error.HTTPError as e:
        print(f"Error code: {e.code}")
