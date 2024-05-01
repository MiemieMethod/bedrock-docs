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

- 基本类型枚举。protocol.packet.setplayergametypepacket.player_game_type.description枚举值如下：

  |键|值|描述|
  |---|---|---|
  |`Undefined`|`-1`|protocol.enum.undefined|
  |`Survival`|`0`|protocol.enum.survival|
  |`Creative`|`1`|protocol.enum.creative|
  |`Adventure`|`2`|protocol.enum.adventure|
  |`Default`|`5`|protocol.enum.default|
  |`Spectator`|`6`|protocol.enum.spectator|
  |`WorldDefault`|`Survival`|protocol.enum.worlddefault|



////

///

