# <!-- md:samp LabTablePacket -->

> 文档版本：r/20_u8<br/>协议版本：671

<!-- md:samp LabTablePacket -->数据包，数字ID是`109`。该数据包用于protocol.packet.labtablepacket.description

## 结构

```viz
digraph "LabTablePacket" {
rankdir = LR
0
0 -> 1
1 -> 2
0 -> 3
3 -> 4
0 -> 5
5 -> 6

0 [label="LabTablePacket",comment="name: \"LabTablePacket\", typeName: \"\", id: 0, branchId: 109, recurseId: -1, attributes: 0, notes: \"\""];
1 [label="Type",comment="name: \"Type\", typeName: \"\", id: 1, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
2 [label="byte",comment="name: \"byte\", typeName: \"\", id: 2, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
3 [label="Position",comment="name: \"Position\", typeName: \"BlockPos\", id: 3, branchId: 0, recurseId: -1, attributes: 256, notes: \"\""];
4 [label="BlockPos",comment="name: \"BlockPos\", typeName: \"\", id: 4, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
5 [label="Reaction",comment="name: \"Reaction\", typeName: \"\", id: 5, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
6 [label="byte",comment="name: \"byte\", typeName: \"\", id: 6, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
{ rank = max;2;4;6}

}

```

## 字段

```title='LabTablePacket'
[type][position][reaction]
```

/// html | div.result
//// define
Type：<!-- md:samp byte -->

- 基本类型。protocol.packet.labtablepacket.type.description


////
//// define
Position：[<!-- md:samp BlockPos -->](../types/blockpos.md)

- 特殊类型。protocol.packet.labtablepacket.position.description


////
//// define
Reaction：<!-- md:samp byte -->

- 基本类型。protocol.packet.labtablepacket.reaction.description


////

///

