#!/usr/bin/python3
""" script that fetches https://alx-intranet.hbtn.io/status using requests """
if __name__ == '__main__':
    import requests
    import sys
    payload = {'email': sys.argv[2]}
    url = sys.argv[1]
    r = requests.post(url, data=payload)
    print(r.text)
