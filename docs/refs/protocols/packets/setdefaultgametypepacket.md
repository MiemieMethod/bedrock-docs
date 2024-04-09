# <!-- md:samp SetDefaultGameTypePacket -->

> 文档版本：r/20_u7<br/>协议版本：662

<!-- md:samp SetDefaultGameTypePacket -->数据包，数字ID是`105`。该数据包用于protocol.packet.setdefaultgametypepacket.description

## 结构

```viz
digraph "SetDefaultGameTypePacket" {
rankdir = LR
0
0 -> 1
1 -> 2

0 [label="SetDefaultGameTypePacket",comment="name: \"SetDefaultGameTypePacket\", typeName: \"\", id: 0, branchId: 105, recurseId: -1, attributes: 0, notes: \"\""];
1 [label="Default Game Type",comment="name: \"Default Game Type\", typeName: \"\", id: 1, branchId: 0, recurseId: -1, attributes: 0, notes: \"enumeration: GameType\""];
2 [label="varint",comment="name: \"varint\", typeName: \"\", id: 2, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
{ rank = max;2}

}

```

## 字段

```title='SetDefaultGameTypePacket'
[default_game_type]
```

/// html | div.result
//// define
Default Game Type：<!-- md:samp varint -->

- 基本类型枚举。protocol.packet.setdefaultgametypepacket.default_game_type.description枚举值如下：

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

