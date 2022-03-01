import json

import requests
from bs4 import BeautifulSoup


def GetVtb():
    with open('./DD.json', 'rb') as fp:
        json_data = json.load(fp)
    channel = json_data.get('channel')
    return channel


def is_liveYT():
    channel_url = "https://www.youtube.com/c/かぐらななななかぐ辛党Ch/live"
    proxy = '127.0.0.1:8099'
    proxies = {
        'http': 'http://' + proxy,
        'https': 'http://' + proxy,
    }
    page = requests.get(channel_url, cookies={
        'CONSENT': 'YES+42'}, proxies=proxies, timeout=10)
    soup = BeautifulSoup(page.content, "html.parser")
    # noinspection PyTypeChecker
    # 禁止idea检查此句防止报错
    live = soup.find("link", {"rel": "canonical"}, {
        "href": "https://www.youtube.com/c/かぐらななななかぐ辛党Ch"})
    # TODO 输出并组成json
    if not live:
        print("Streaming")
    else:
        print("Not Streaming")


if __name__ == "__main__":
    print(GetVtb())
