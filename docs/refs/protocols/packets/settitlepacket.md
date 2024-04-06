# <!-- md:samp SetTitlePacket -->

> 文档版本：r/20_u7<br/>协议版本：662

<!-- md:samp SetTitlePacket -->数据包，数字ID是`88`。

## 结构

```viz
digraph "SetTitlePacket" {
rankdir = LR
0
0 -> 1
1 -> 2
0 -> 3
3 -> 4
0 -> 5
5 -> 6
0 -> 7
7 -> 8
0 -> 9
9 -> 10
0 -> 11
11 -> 12
0 -> 13
13 -> 14

0 [label="SetTitlePacket",comment="name: \"SetTitlePacket\", typeName: \"\", id: 0, branchId: 88, recurseId: -1, attributes: 0, notes: \"\""];
1 [label="Title Type",comment="name: \"Title Type\", typeName: \"\", id: 1, branchId: 0, recurseId: -1, attributes: 0, notes: \"enumeration: SetTitlePacket::TitleType\""];
2 [label="varint",comment="name: \"varint\", typeName: \"\", id: 2, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
3 [label="Title Text",comment="name: \"Title Text\", typeName: \"\", id: 3, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
4 [label="string",comment="name: \"string\", typeName: \"\", id: 4, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
5 [label="Fade In Time",comment="name: \"Fade In Time\", typeName: \"\", id: 5, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
6 [label="varint",comment="name: \"varint\", typeName: \"\", id: 6, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
7 [label="Stay Time",comment="name: \"Stay Time\", typeName: \"\", id: 7, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
8 [label="varint",comment="name: \"varint\", typeName: \"\", id: 8, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
9 [label="Fade Out Time",comment="name: \"Fade Out Time\", typeName: \"\", id: 9, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
10 [label="varint",comment="name: \"varint\", typeName: \"\", id: 10, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
11 [label="Xuid",comment="name: \"Xuid\", typeName: \"\", id: 11, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
12 [label="string",comment="name: \"string\", typeName: \"\", id: 12, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
13 [label="Platform Online Id",comment="name: \"Platform Online Id\", typeName: \"\", id: 13, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
14 [label="string",comment="name: \"string\", typeName: \"\", id: 14, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
{ rank = max;2;4;6;8;10;12;14}

}

```

## 字段

```title='SetTitlePacket'
[title_type][title_text][fade_in_time][stay_time][fade_out_time][xuid][platform_online_id]
```

/// html | div.result
//// define
Title Type：<!-- md:samp varint -->

- 基本类型枚举。枚举值如下：

  |键|值|描述|
  |---|---|---|
  |`Clear`|`0`||
  |`Reset`|`1`||
  |`Title`|`2`||
  |`Subtitle`|`3`||
  |`Actionbar`|`4`||
  |`Times`|`5`||
  |`TitleTextObject`|`6`||
  |`SubtitleTextObject`|`7`||
  |`ActionbarTextObject`|`8`||



////
//// define
Title Text：[<!-- md:samp string -->](../types/string.md)

- 特殊类型。


////
//// define
Fade In Time：<!-- md:samp varint -->

- 基本类型。


////
//// define
Stay Time：<!-- md:samp varint -->

- 基本类型。


////
//// define
Fade Out Time：<!-- md:samp varint -->

- 基本类型。


////
//// define
Xuid：[<!-- md:samp string -->](../types/string.md)

- 特殊类型。


////
//// define
Platform Online Id：[<!-- md:samp string -->](../types/string.md)

- 特殊类型。


////

///
