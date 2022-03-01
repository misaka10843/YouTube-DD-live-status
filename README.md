# YouTube-DD-live-status
## 简介

此仓库是整合了一些YouTube上的虚拟主播的直播状态

暂且准备是每10分钟更新一次

（毕竟不能一直更新嘛,本来是想用cf的worker，但是发现逻辑不好写，所以转到了GitHub actions）

您可以在`DD.json`中按照规范来添加你想要的V（虽然还没有实现www）

作者正在全力开发中，还请点个star✨吧qwq

## 如何使用

因为这是个自动发布的仓库，所以还请最好使用反代站(对于大陆来说)，或者直接github

您可以点击[这里](https://github.com/misaka10843/YouTube-DD-live-status/blob/main/DDLive.json) 查看文件

`https://github.com/misaka10843/YouTube-DD-live-status/raw/main/DDLive.json` 

这个是文件源码，每10mins更新一次（但是github只能随缘运行了www）

如果发现json的更新时间过早，可能是因为并没有啥更新的，放心用就可了（还不放心可以看看action）

现在大概框架已经做好，以下为`DDLive.json`的示例代码

```json
{
  "channel": [
    {
      "on": "カグラナナ",
      "en": "Kaguranana",
      "cn": "神楽七奈",
      "live": false,
      "start_time": null,
      "live_url": null
    },
    {
      "on": "しぐれうい",
      "en": "Shigureui",
      "cn": "时雨羽衣",
      "live": false,
      "start_time": null,
      "live_url": null
    },
    {
      "on": "白上フブキ",
      "en": "Shirakamifubuki",
      "cn": "白上吹雪",
      "live": true,
      "start_time": "2022-03-01 20:00:31",
      "live_url": "https://www.youtube.com/watch?v=emFwdMNPg_A"
    }
  ]
}
```

其中：

·`on`:为Vtb的原名(与DD.json绑定)

·`en`:为Vtb的英语/罗马音名(与DD.json绑定)

·`cn`:为Vtb的中文名(与DD.json绑定)

·`live`:bool值，`true`为直播中，`fasle`为下播ing

·`start_time`:开播/预计开播的时间，未开播(没有开预约)即为`null`

·`live_url`:直播间的地址，未开播(没有开预约)为`null`

## DD.json编写规范

[文件在此](https://github.com/misaka10843/YouTube-DD-live-status/blob/main/DD.json)

先看示例json

```json
{
  "channel": [
    {
      "en": "Kaguranana",
      "on": "カグラナナ",
      "cn": "神楽七奈",
      "isC": 1,
      "Cid": "かぐらななななかぐ辛党Ch"
    },
    {
      "en": "Shigureui",
      "on": "しぐれうい",
      "cn": "时雨羽衣",
      "isC": 0,
      "Cid": "UCt30jJgChL8qeT9VPadidSw"
    }
  ]
}
```

· `en`:代表这个V的名字的罗马音或者英文

· `on`:代表这个V的原名

· `cn`:代表这个V的中文名

· `isC`:因为防止有些V的主页链接不是像`https://www.youtube.com/channel/UCt30jJgChL8qeT9VPadidSw`

这种的所以就需要判断是否是`www.youtube.com/c/かぐらななななかぐ辛党Ch` 这种的

(`c = 1,user = 2,channel = 0`)

· `Cid`:频道的ID

如`www.youtube.com/c/かぐらななななかぐ辛党Ch` 中的`かぐらななななかぐ辛党Ch`

和 `www.youtube.com/channel/UCt30jJgChL8qeT9VPadidSw` 中的`UCt30jJgChL8qeT9VPadidSw`

## 仓库基本情况

![Alt](https://repobeats.axiom.co/api/embed/2e473654161f51946ba290542ecf3ed87ff2b75b.svg "Repobeats analytics image")
