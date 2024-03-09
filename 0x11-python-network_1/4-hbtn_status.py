#!/usr/bin/python3
""" script that fetches https://alx-intranet.hbtn.io/status using requests """
if __name__ == '__main__':
    import requests
    r = requests.get('https://alx-intranet.hbtn.io/status')
    ty  = type(r.text)
    content = r.text
    print(f"Body response:\n\t- type: {ty}\n\t- content: {content}")
