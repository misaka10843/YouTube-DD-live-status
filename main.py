import datetime
import json

import requests
from bs4 import BeautifulSoup


def GetVtb():
    with open('./DD.json', 'rb') as fp:
        json_data = json.load(fp)
    channel = json_data.get('channel')
    return channel


def IsLiveYT():
    ChannelUrl = "https://www.youtube.com/channel/UCdn5BQ06XqgXoAxIhbqw5Rg/live"
    proxy = '127.0.0.1:8099'
    proxies = {
        'http': 'http://' + proxy,
        'https': 'http://' + proxy,
    }
    page = requests.get(ChannelUrl, cookies={
        'CONSENT': 'YES+42'}, proxies=proxies, timeout=10)
    soup = BeautifulSoup(page.content, "html.parser")

    # noinspection PyTypeChecker
    # 禁止idea检查此句防止报错
    live = soup.find("link", {"rel": "canonical"}).get(
        "href")
    # TODO 输出并组成json
    if not live == "https://www.youtube.com/channel/UCdn5BQ06XqgXoAxIhbqw5Rg":
        print("Streaming")
        return live
    else:
        print("Not Streaming")
        return "null"


def GetWaitTime():
    LiveUrl = IsLiveYT()
    proxy = '127.0.0.1:8099'
    proxies = {
        'http': 'http://' + proxy,
        'https': 'http://' + proxy,
    }
    page = requests.get(LiveUrl, cookies={
        'CONSENT': 'YES+42'}, proxies=proxies, timeout=10)
    soup = BeautifulSoup(page.content, "html.parser")
    # noinspection PyTypeChecker
    # 禁止idea检查此句防止报错
    LiveTime = soup.find("meta", {"itemprop": "startDate"}).get(
        "content")
    return LiveTime


def ConversionTime():
    GetTime = GetWaitTime()
    GetTime = GetTime.split("+")[0]
    GetTime = datetime.datetime.strptime(GetTime, "%Y-%m-%dT%H:%M:%S")
    UTC8 = (GetTime + datetime.timedelta(hours=8)).strftime("%Y-%m-%d %H:%M:%S")
    return UTC8


if __name__ == "__main__":
    IsLiveYT()
    if IsLiveYT() == "null":
        print("并未直播")
    else:
        print(ConversionTime())
