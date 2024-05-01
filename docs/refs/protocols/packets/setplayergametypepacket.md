# <!-- md:samp SetPlayerGameTypePacket -->

> 文档版本：r/20_u8<br/>协议版本：671

<!-- md:samp SetPlayerGameTypePacket -->数据包，数字ID是`62`。该数据包用于protocol.packet.setplayergametypepacket.description

## 结构

```viz
digraph "SetPlayerGameTypePacket" {
rankdir = LR
0
0 -> 1
1 -> 2

0 [label="SetPlayerGameTypePacket",comment="name: \"SetPlayerGameTypePacket\", typeName: \"\", id: 0, branchId: 62, recurseId: -1, attributes: 0, notes: \"\""];
1 [label="Player Game Type",comment="name: \"Player Game Type\", typeName: \"\", id: 1, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
2 [label="varint",comment="name: \"varint\", typeName: \"\", id: 2, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
{ rank = max;2}

}

```

## 字段

```title='SetPlayerGameTypePacket'
[player_game_type]
```

/// html | div.result
//// define
Player Game Type：<!-- md:samp varint -->

- 基本类型。protocol.packet.setplayergametypepacket.player_game_type.description


////

///

