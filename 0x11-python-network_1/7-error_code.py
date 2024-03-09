#!/usr/bin/python3
""" script that fetches https://alx-intranet.hbtn.io/status using requests """
if __name__ == '__main__':
    import requests
    import sys
    url = sys.argv[1]
    r = requests.get(url)
    if r.status_code >= 400:
        print(f"Error code: {r.status_code}")
    else:
        print(r.text)
