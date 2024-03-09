#!/usr/bin/python3
""" script that fetches https://alx-intranet.hbtn.io/status using requests """
if __name__ == '__main__':
    import requests
    import sys
    url = 'http://topnada.tech'
    if len(sys.argv) < 2:
        payload = {'q': ""}
    else:
        payload = {'q': sys.argv[1]}
    r = requests.post(url, data=payload)
    try:
        dic = r.json()
        if dic != {}:
            id = dic.get('id')
            name = dic.get('name')
            print(f"[{id}] {name}")
        else:
            print("No result")
    except ValueError:
        print("Not a valid JSON")
