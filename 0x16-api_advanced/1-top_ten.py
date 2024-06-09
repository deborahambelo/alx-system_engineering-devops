#!/usr/bin/python3
"""Function that queries the Reddit API and prints the top 10 hot posts"""
import requests


def top_ten(subreddit):
    """
    Queries the Reddit API and prints the titles of the first 10 post.
    """
    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=10"
    headers = {'User-Agent': 'myApp/0.0.1'}

    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        if response.status_code == 200:
            data = response.json().get("data", {}).get("children", [])
            if not data:
                print(None)
            for post in data:
                print(post["data"]["title"])
        else:
            print(None)
    except requests.RequestException:
        print(None)
