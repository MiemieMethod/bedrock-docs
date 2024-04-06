# <!-- md:samp SetScoreboardIdentityPacket -->

> 文档版本：r/20_u7<br/>协议版本：662

<!-- md:samp SetScoreboardIdentityPacket -->数据包，数字ID是`112`。

## 结构

```viz
digraph "SetScoreboardIdentityPacket" {
rankdir = LR
0
0 -> 1
1 -> 2
0 -> 3
3 -> 4
4 -> 5
3 -> 6
6 -> 7
7 -> 8
6 -> 9
9 -> 10
10 -> 11
9 -> 12
12 -> 13
13 -> 14

0 [label="SetScoreboardIdentityPacket",comment="name: \"SetScoreboardIdentityPacket\", typeName: \"\", id: 0, branchId: 112, recurseId: -1, attributes: 0, notes: \"\""];
1 [label="Scoreboard Identity Packet Type",comment="name: \"Scoreboard Identity Packet Type\", typeName: \"\", id: 1, branchId: 0, recurseId: -1, attributes: 0, notes: \"enumeration: ScoreboardIdentityPacketType\""];
2 [label="byte",comment="name: \"byte\", typeName: \"\", id: 2, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
3 [label="Identity Info",comment="name: \"Identity Info\", typeName: \"\", id: 3, branchId: 0, recurseId: -1, attributes: 8, notes: \"\""];
4 [label="Array Size",comment="name: \"Array Size\", typeName: \"\", id: 4, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
5 [label="unsigned varint",comment="name: \"unsigned varint\", typeName: \"\", id: 5, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
6 [label="example element",style=dotted,comment="name: \"example element\", typeName: \"\", id: 6, branchId: 0, recurseId: -1, attributes: 16, notes: \"\""];
7 [label="Scoreboard Id",comment="name: \"Scoreboard Id\", typeName: \"ScoreboardId\", id: 7, branchId: 0, recurseId: -1, attributes: 256, notes: \"\""];
8 [label="ScoreboardId",comment="name: \"ScoreboardId\", typeName: \"\", id: 8, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
9 [label="Dependency on 'Is Update Type'",shape=note,comment="name: \"Dependency on 'Is Update Type'\", typeName: \"\", id: 9, branchId: 0, recurseId: -1, attributes: 2, notes: \"\""];
10 [label="if (0)",shape=diamond,comment="name: \"if (0)\", typeName: \"\", id: 10, branchId: 0, recurseId: -1, attributes: 4, notes: \"\""];
11 [label="[No Data]",comment="name: \"[No Data]\", typeName: \"\", id: 11, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
12 [label="if (1)",shape=diamond,comment="name: \"if (1)\", typeName: \"\", id: 12, branchId: 1, recurseId: -1, attributes: 4, notes: \"\""];
13 [label="Player Unique Id",comment="name: \"Player Unique Id\", typeName: \"\", id: 13, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
14 [label="varint64",comment="name: \"varint64\", typeName: \"\", id: 14, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
{ rank = max;2;5;8;11;14}

}

```

## 字段

```title='SetScoreboardIdentityPacket'
[scoreboard_identity_packet_type][identity_info]
```

/// html | div.result
//// define
Scoreboard Identity Packet Type：<!-- md:samp byte -->

- 类型：<!-- md:samp byte -->。枚举值如下：

  |键|值|描述|
  |---|---|---|
  |`Update`|`0`||
  |`Remove`|`1`||



////
```title='Identity Info'
[array_size][[example_element]..]
```

//// html | div.result
///// define
数组大小：<!-- md:samp unsigned varint -->

- 类型：<!-- md:samp unsigned varint -->。


/////
```title='示例元素'
[scoreboard_id][dependency_on_'is_update_type']
```

///// html | div.result
////// define
Scoreboard Id：[<!-- md:samp ScoreboardId -->](../types/scoreboardid.md)

- 类型：<!-- md:samp ScoreboardId -->。


//////
> 依赖于`Is Update Type`

/////// tab | `Is Update Type`如果为`0`
//////// define
if (0)：<!-- md:samp [No Data] -->

- 无数据。


////////

///////

/////// tab | `Is Update Type`如果为`1`
```title='if (1)'
[player_unique_id]
```

//////// html | div.result
///////// define
Player Unique Id：<!-- md:samp varint64 -->

- 类型：<!-- md:samp varint64 -->。


/////////

////////

///////

/////

////

///

