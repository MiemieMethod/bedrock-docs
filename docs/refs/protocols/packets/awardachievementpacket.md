# <!-- md:samp AwardAchievementPacket -->

> 文档版本：r/21_u4<br/>协议版本：748

<!-- md:samp AwardAchievementPacket -->数据包，数字ID是`309`。该数据包用于protocol.packet.awardachievementpacket.description

## 结构

```viz
digraph "AwardAchievementPacket" {
rankdir = LR
0
0 -> 1
1 -> 2

0 [label="AwardAchievementPacket",comment="name: \"AwardAchievementPacket\", typeName: \"\", id: 0, branchId: 309, recurseId: -1, attributes: 0, notes: \"\""];
1 [label="AchievementID",comment="name: \"AchievementID\", typeName: \"\", id: 1, branchId: 0, recurseId: -1, attributes: 0, notes: \"Achievement ID\""];
2 [label="int",comment="name: \"int\", typeName: \"\", id: 2, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
{ rank = max;2}

}

```

## 字段

```title='AwardAchievementPacket'
[achievementid]
```

/// html | div.result
//// define
AchievementID：<!-- md:samp int -->

- 基本类型。protocol.packet.awardachievementpacket.achievementid.descriptionAchievement ID


////

///

