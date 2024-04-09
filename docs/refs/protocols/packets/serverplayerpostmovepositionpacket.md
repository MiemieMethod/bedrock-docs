# <!-- md:samp ServerPlayerPostMovePositionPacket -->

> 文档版本：r/20_u7<br/>协议版本：662

<!-- md:samp ServerPlayerPostMovePositionPacket -->数据包，数字ID是`16`。该数据包用于protocol.packet.serverplayerpostmovepositionpacket.description

## 结构

```viz
digraph "ServerPlayerPostMovePositionPacket" {
rankdir = LR
0
0 -> 1
1 -> 2

0 [label="ServerPlayerPostMovePositionPacket",comment="name: \"ServerPlayerPostMovePositionPacket\", typeName: \"\", id: 0, branchId: 16, recurseId: -1, attributes: 0, notes: \"\""];
1 [label="Pos",comment="name: \"Pos\", typeName: \"Vec3\", id: 1, branchId: 0, recurseId: -1, attributes: 256, notes: \"\""];
2 [label="Vec3",comment="name: \"Vec3\", typeName: \"\", id: 2, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
{ rank = max;2}

}

```

## 字段

```title='ServerPlayerPostMovePositionPacket'
[pos]
```

/// html | div.result
//// define
Pos：[<!-- md:samp Vec3 -->](../types/vec3.md)

- 特殊类型。protocol.packet.serverplayerpostmovepositionpacket.pos.description


////

///

