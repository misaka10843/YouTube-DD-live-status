import requests
from bs4 import BeautifulSoup
import json


def is_liveYT():
    channel_url = "https://www.youtube.com/c/かぐらななななかぐ辛党Ch/live"
    proxy = '127.0.0.1:8099'
    proxies = {
        'http': 'http://'+proxy,
        'https': 'http://'+proxy,
    }
    page = requests.get(channel_url, cookies={
                        'CONSENT': 'YES+42'}, proxies=proxies, timeout=10)
    soup = BeautifulSoup(page.content, "html.parser")
    live = soup.find("link", {"rel": "canonical"}, {
                     "href": "https://www.youtube.com/c/かぐらななななかぐ辛党Ch"})
    if not live:
        print("Streaming")
    else:
        print("Not Streaming")


if __name__ == "__main__":
    is_liveYT()
