# <!-- md:samp LabTablePacket -->

> 文档版本：r/20_u7<br/>协议版本：662

<!-- md:samp LabTablePacket -->数据包，数字ID是`109`。

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
1 [label="Type",comment="name: \"Type\", typeName: \"\", id: 1, branchId: 0, recurseId: -1, attributes: 0, notes: \"enumeration: LabTablePacket::Type\""];
2 [label="byte",comment="name: \"byte\", typeName: \"\", id: 2, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
3 [label="Position",comment="name: \"Position\", typeName: \"BlockPos\", id: 3, branchId: 0, recurseId: -1, attributes: 256, notes: \"\""];
4 [label="BlockPos",comment="name: \"BlockPos\", typeName: \"\", id: 4, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
5 [label="Reaction",comment="name: \"Reaction\", typeName: \"\", id: 5, branchId: 0, recurseId: -1, attributes: 0, notes: \"enumeration: LabTableReactionType\""];
6 [label="byte",comment="name: \"byte\", typeName: \"\", id: 6, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
{ rank = max;2;4;6}

}

```

## 字段

/// define
LabTablePacket

Type：<!-- md:samp byte -->

- 类型：byte。enumeration: LabTablePacket::Type

Position：[<!-- md:samp BlockPos -->](../types/blockpos.md)

- 类型：BlockPos。

Reaction：<!-- md:samp byte -->

- 类型：byte。enumeration: LabTableReactionType


///
