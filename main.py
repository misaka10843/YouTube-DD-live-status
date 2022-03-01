import datetime
import json

import requests
from bs4 import BeautifulSoup


# 获取DD列表
def GetVtb():
    with open('./DD.json', 'rb') as fp:
        json_data = json.load(fp)
    channel = json_data.get('channel')
    return channel


# 主判断器
def IsLiveYT(ChannelUrl, ChannelName):
    ChannelLiveUrl = ChannelUrl + "/live"
    proxy = '127.0.0.1:8099'
    proxies = {
        'http': 'http://' + proxy,
        'https': 'http://' + proxy,
    }
    page = requests.get(ChannelLiveUrl, cookies={
        'CONSENT': 'YES+42'}, proxies=proxies, timeout=10)
    soup = BeautifulSoup(page.content, "html.parser")

    # noinspection PyTypeChecker
    # 禁止idea检查此句防止报错
    live = soup.find("link", {"rel": "canonical"}).get(
        "href")
    # TODO 输出并组成json
    if not live == ChannelUrl:
        print(ChannelName + " is Streaming")
        return live
    else:
        print(ChannelName + " Not Streaming")
        return "null"


# 时间转换+时区转换
def ConversionTime(LiveUrl):
    # 引用获取开播时间
    GetTime = GetWaitTime(LiveUrl)
    GetTime = GetTime.split("+")[0]
    GetTime = datetime.datetime.strptime(GetTime, "%Y-%m-%dT%H:%M:%S")
    UTC8 = (GetTime + datetime.timedelta(hours=8)).strftime("%Y-%m-%d %H:%M:%S")
    return UTC8


# 获取开播时间(理论)
def GetWaitTime(LiveUrl):
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


def main():
    DDJson = '{"channel": ['
    for i in GetVtb():
        # 判断频道ID格式
        if i["isC"] == 0:
            ChannelUrl = "https://www.youtube.com/channel/" + i["Cid"]
        elif i["isC"] == 1:
            ChannelUrl = "https://www.youtube.com/c/" + i["Cid"]
        else:
            ChannelUrl = "https://www.youtube.com/user/" + i["Cid"]
        # 将值传入主页面判断
        LiveUrl = IsLiveYT(ChannelUrl, i["en"])
        # 是否正在直播，在就获取直播时间，不在就直接返回
        if not LiveUrl == "null":
            StartTime = ConversionTime(LiveUrl)
            DDJson = DDJson + '{"on":"' + i["on"] + '","en":"' + i["en"] + '","cn":"' + i[
                "cn"] + '","live":true,"start_time":"' + StartTime + '","live_url":"' + LiveUrl + '"},'
        else:
            DDJson = DDJson + '{"on":"' + i["on"] + '","en":"' + i["en"] + '","cn":"' + i[
                "cn"] + '","live":false,"start_time":null,"live_url":null},'
    # 出循环，结尾json
    DDJson = DDJson[:-1] + "]}"
    print(DDJson)


if __name__ == "__main__":
    main()
