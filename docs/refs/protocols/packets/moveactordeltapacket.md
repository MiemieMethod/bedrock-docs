# <!-- md:samp MoveActorDeltaPacket -->

> 文档版本：r/21_u4<br/>协议版本：748

<!-- md:samp MoveActorDeltaPacket -->数据包，数字ID是`111`。该数据包用于protocol.packet.moveactordeltapacket.description

## 结构

```viz
digraph "MoveActorDeltaPacket" {
rankdir = LR
0
0 -> 1
1 -> 19

0 [label="MoveActorDeltaPacket",comment="name: \"MoveActorDeltaPacket\", typeName: \"\", id: 0, branchId: 111, recurseId: -1, attributes: 0, notes: \"\""];
1 [label="Move Data",comment="name: \"Move Data\", typeName: \"MoveActorDeltaData\", id: 1, branchId: 0, recurseId: -1, attributes: 256, notes: \"\""];
19 [label="MoveActorDeltaData",comment="name: \"MoveActorDeltaData\", typeName: \"\", id: 19, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
{ rank = max;19}

}

```

## 字段

```title='MoveActorDeltaPacket'
[move_data]
```

/// html | div.result
//// define
Move Data：[<!-- md:samp MoveActorDeltaData -->](../types/moveactordeltadata.md)

- 特殊类型。protocol.packet.moveactordeltapacket.move_data.description


////

///

