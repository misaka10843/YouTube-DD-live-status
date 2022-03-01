# YouTube-DD-live-status
## 简介

此仓库是整合了一些YouTube上的虚拟主播的直播状态

暂且准备是每10分钟更新一次

（毕竟不能一直更新嘛,本来是想用cf的worker，但是发现逻辑不好写，所以转到了GitHub actions）

您可以在`DD.json`中按照规范来添加你想要的V（虽然还没有实现www）

作者正在全力开发中，还请点个star✨吧qwq

## DD.json编写规范

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