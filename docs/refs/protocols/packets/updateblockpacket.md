# <!-- md:samp UpdateBlockPacket -->

> 文档版本：r/21_u4<br/>协议版本：748

<!-- md:samp UpdateBlockPacket -->数据包，数字ID是`21`。该数据包用于protocol.packet.updateblockpacket.description

## 结构

```viz
digraph "UpdateBlockPacket" {
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

0 [label="UpdateBlockPacket",comment="name: \"UpdateBlockPacket\", typeName: \"\", id: 0, branchId: 21, recurseId: -1, attributes: 0, notes: \"\""];
1 [label="Block Position",comment="name: \"Block Position\", typeName: \"NetworkBlockPosition\", id: 1, branchId: 0, recurseId: -1, attributes: 256, notes: \"\""];
2 [label="NetworkBlockPosition",comment="name: \"NetworkBlockPosition\", typeName: \"\", id: 2, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
3 [label="Block Runtime ID",comment="name: \"Block Runtime ID\", typeName: \"\", id: 3, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
4 [label="unsigned varint",comment="name: \"unsigned varint\", typeName: \"\", id: 4, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
5 [label="Flags",comment="name: \"Flags\", typeName: \"\", id: 5, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
6 [label="unsigned varint",comment="name: \"unsigned varint\", typeName: \"\", id: 6, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
7 [label="Layer",comment="name: \"Layer\", typeName: \"\", id: 7, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
8 [label="unsigned varint",comment="name: \"unsigned varint\", typeName: \"\", id: 8, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
{ rank = max;2;4;6;8}

}

```

## 字段

```title='UpdateBlockPacket'
[block_position][block_runtime_id][flags][layer]
```

/// html | div.result
//// define
Block Position：[<!-- md:samp NetworkBlockPosition -->](../types/networkblockposition.md)

- 特殊类型。protocol.packet.updateblockpacket.block_position.description


////
//// define
Block Runtime ID：<!-- md:samp unsigned varint -->

- 基本类型。protocol.packet.updateblockpacket.block_runtime_id.description


////
//// define
Flags：<!-- md:samp unsigned varint -->

- 基本类型。protocol.packet.updateblockpacket.flags.description


////
//// define
Layer：<!-- md:samp unsigned varint -->

- 基本类型。protocol.packet.updateblockpacket.layer.description


////

///

