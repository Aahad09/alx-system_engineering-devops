#/usr/bin/python3
"""function that queries the Reddit API and returns the number of subscribers for a given subreddit"""

import requests

def number_of_subscribers(subreddit):
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {'User-Agent': 'Custom User Agent'}  # Set a custom User-Agent header

    try:
        response = requests.get(url, headers=headers)
        data = response.json()
        return data['data']['subscribers']
    except (requests.RequestException, KeyError):
        return 0
