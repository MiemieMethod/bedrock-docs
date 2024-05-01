# <!-- md:samp MultiplayerSettingsPacket -->

> 文档版本：r/20_u8<br/>协议版本：671

<!-- md:samp MultiplayerSettingsPacket -->数据包，数字ID是`139`。该数据包用于protocol.packet.multiplayersettingspacket.description

## 结构

```viz
digraph "MultiplayerSettingsPacket" {
rankdir = LR
0
0 -> 1
1 -> 2

0 [label="MultiplayerSettingsPacket",comment="name: \"MultiplayerSettingsPacket\", typeName: \"\", id: 0, branchId: 139, recurseId: -1, attributes: 0, notes: \"\""];
1 [label="Type",comment="name: \"Type\", typeName: \"\", id: 1, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
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

- 基本类型。protocol.packet.multiplayersettingspacket.type.description


////

///

