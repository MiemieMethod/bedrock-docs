# <!-- md:samp MoveActorAbsolutePacket -->

> 文档版本：r/21_u4<br/>协议版本：748

<!-- md:samp MoveActorAbsolutePacket -->数据包，数字ID是`18`。该数据包用于protocol.packet.moveactorabsolutepacket.description

## 结构

```viz
digraph "MoveActorAbsolutePacket" {
rankdir = LR
0
0 -> 1
1 -> 15

0 [label="MoveActorAbsolutePacket",comment="name: \"MoveActorAbsolutePacket\", typeName: \"\", id: 0, branchId: 18, recurseId: -1, attributes: 0, notes: \"\""];
1 [label="Move Data",comment="name: \"Move Data\", typeName: \"MoveActorAbsoluteData\", id: 1, branchId: 0, recurseId: -1, attributes: 256, notes: \"This is used in legacy client authoritative movement mode to move a client predicted vehicle that the client is in control of. In any other case this is client bound for normal actor motion updates.\""];
15 [label="MoveActorAbsoluteData",comment="name: \"MoveActorAbsoluteData\", typeName: \"\", id: 15, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
{ rank = max;15}

}

```

## 字段

```title='MoveActorAbsolutePacket'
[move_data]
```

/// html | div.result
//// define
Move Data：[<!-- md:samp MoveActorAbsoluteData -->](../types/moveactorabsolutedata.md)

- 特殊类型。protocol.packet.moveactorabsolutepacket.move_data.descriptionThis is used in legacy client authoritative movement mode to move a client predicted vehicle that the client is in control of. In any other case this is client bound for normal actor motion updates.


////

///

