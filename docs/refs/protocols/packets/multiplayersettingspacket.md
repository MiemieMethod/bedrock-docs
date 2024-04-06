# <!-- md:samp MultiplayerSettingsPacket -->

> 文档版本：r/20_u7<br/>协议版本：662

<!-- md:samp MultiplayerSettingsPacket -->数据包，数字ID是`139`。

## 结构

```viz
digraph "MultiplayerSettingsPacket" {
rankdir = LR
0
0 -> 1
1 -> 2

0 [label="MultiplayerSettingsPacket",comment="name: \"MultiplayerSettingsPacket\", typeName: \"\", id: 0, branchId: 139, recurseId: -1, attributes: 0, notes: \"\""];
1 [label="Type",comment="name: \"Type\", typeName: \"\", id: 1, branchId: 0, recurseId: -1, attributes: 0, notes: \"enumeration: MultiplayerSettingsPacketType\""];
2 [label="varint",comment="name: \"varint\", typeName: \"\", id: 2, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
{ rank = max;2}

}

```

## 字段

```title='MultiplayerSettingsPacket'
[type]
```

/// html | div.result
//// define
Type：<!-- md:samp varint -->

- <!-- md:samp varint -->类型枚举。枚举值如下：

  |键|值|描述|
  |---|---|---|
  |`EnableMultiplayer`|`0`||
  |`DisableMultiplayer`|`1`||
  |`RefreshJoincode`|`2`||



////

///

