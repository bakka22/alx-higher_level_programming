#!/usr/bin/python3
""" script that fetches https://alx-intranet.hbtn.io/status using requests """
if __name__ == '__main__':
    import requests
    import sys
    url = 'https://api.github.com/users/' + sys.argv[1]
    heads = {'Accept': 'application/vnd.github+json',
             'Authorization': 'Bearer ' + sys.argv[2],
             'X-GitHub-Api-Version': '2022-11-28'}
    r = requests.get(url, headers=heads)
    id = r.json().get('id')
    print(id)
