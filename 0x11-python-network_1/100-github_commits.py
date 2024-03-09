#!/usr/bin/python3
""" script that fetches https://alx-intranet.hbtn.io/status using requests """
if __name__ == '__main__':
    import requests
    import sys
    owner = sys.argv[2]
    repo = sys.argv[1]
    url = f"https://api.github.com/repos/{owner}/{repo}/commits"
    heads = {'Accept': 'application/vnd.github+json',
             'X-GitHub-Api-Version': '2022-11-28'}
    r = requests.get(url, headers=heads)
    dic = r.json()
    for i in range(0, 10):
        sha = dic[i].get('sha')
        name = dic[i].get('commit').get('author').get('name')
        print(f"{sha}: {name}")
