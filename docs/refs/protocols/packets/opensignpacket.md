# <!-- md:samp OpenSignPacket -->

> 文档版本：r/21_u4<br/>协议版本：748

<!-- md:samp OpenSignPacket -->数据包，数字ID是`303`。该数据包用于protocol.packet.opensignpacket.description

## 结构

```viz
digraph "OpenSignPacket" {
rankdir = LR
0
0 -> 1
1 -> 2
0 -> 3
3 -> 4

0 [label="OpenSignPacket",comment="name: \"OpenSignPacket\", typeName: \"\", id: 0, branchId: 303, recurseId: -1, attributes: 0, notes: \"\""];
1 [label="Pos",comment="name: \"Pos\", typeName: \"NetworkBlockPosition\", id: 1, branchId: 0, recurseId: -1, attributes: 256, notes: \"\""];
2 [label="NetworkBlockPosition",comment="name: \"NetworkBlockPosition\", typeName: \"\", id: 2, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
3 [label="Is Front Side",comment="name: \"Is Front Side\", typeName: \"\", id: 3, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
4 [label="bool",comment="name: \"bool\", typeName: \"\", id: 4, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
{ rank = max;2;4}

}

```

## 字段

```title='OpenSignPacket'
[pos][is_front_side]
```

/// html | div.result
//// define
Pos：[<!-- md:samp NetworkBlockPosition -->](../types/networkblockposition.md)

- 特殊类型。protocol.packet.opensignpacket.pos.description


////
//// define
Is Front Side：<!-- md:samp bool -->

- 基本类型。protocol.packet.opensignpacket.is_front_side.description


////

///

