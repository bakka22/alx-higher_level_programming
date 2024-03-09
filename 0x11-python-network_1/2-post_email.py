#!/usr/bin/python3
""" Python script that fetches https://alx-intranet.hbtn.io/status """
import urllib.request
import sys
if __name__ == '__main__':
    values = {'email': sys.argv[2]}
    data = urllib.request.urlencode(values)
    url = sys.argv[1]
    with urllib.request.urlopen(url, data) as r:
        va = r.read().decode('utf-8')
        print(va)
