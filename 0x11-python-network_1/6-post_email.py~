#!/usr/bin/python3
""" script that fetches https://alx-intranet.hbtn.io/status using requests """
if __name__ == '__main__':
    import requests
    import sys
    url = sys.argv[1]
    r = requests.get(url)
    va = r.headers.get('X-Request-Id')
    print(va)
