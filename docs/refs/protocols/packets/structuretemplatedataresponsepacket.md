# <!-- md:samp StructureTemplateDataResponsePacket -->

> 文档版本：r/20_u7<br/>协议版本：662

<!-- md:samp StructureTemplateDataResponsePacket -->数据包，数字ID是`133`。

## 结构

```viz
digraph "StructureTemplateDataResponsePacket" {
rankdir = LR
0
0 -> 1
1 -> 2
0 -> 3
3 -> 4
4 -> 5
5 -> 6
4 -> 7
7 -> 8
3 -> 9
9 -> 10
10 -> 11
9 -> 12
12 -> 13
9 -> 14
14 -> 15

0 [label="StructureTemplateDataResponsePacket",comment="name: \"StructureTemplateDataResponsePacket\", typeName: \"\", id: 0, branchId: 133, recurseId: -1, attributes: 0, notes: \"\""];
1 [label="Structure Name",comment="name: \"Structure Name\", typeName: \"\", id: 1, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
2 [label="string",comment="name: \"string\", typeName: \"\", id: 2, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
3 [label="Dependency on 'Requested structure exists?'",shape=note,comment="name: \"Dependency on 'Requested structure exists?'\", typeName: \"\", id: 3, branchId: 0, recurseId: -1, attributes: 2, notes: \"\""];
4 [label="if (0)",shape=diamond,comment="name: \"if (0)\", typeName: \"\", id: 4, branchId: 0, recurseId: -1, attributes: 4, notes: \"\""];
5 [label="Failure",comment="name: \"Failure\", typeName: \"\", id: 5, branchId: 0, recurseId: -1, attributes: 0, notes: \"Bool set to false, indicating the requested structure didn't exist.\""];
6 [label="bool",comment="name: \"bool\", typeName: \"\", id: 6, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
7 [label="Response Type",comment="name: \"Response Type\", typeName: \"\", id: 7, branchId: 0, recurseId: -1, attributes: 0, notes: \"enumeration: StructureTemplateResponseType\""];
8 [label="byte",comment="name: \"byte\", typeName: \"\", id: 8, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
9 [label="if (1)",shape=diamond,comment="name: \"if (1)\", typeName: \"\", id: 9, branchId: 1, recurseId: -1, attributes: 4, notes: \"\""];
10 [label="Success",comment="name: \"Success\", typeName: \"\", id: 10, branchId: 0, recurseId: -1, attributes: 0, notes: \"Bool set to true, indicating success.\""];
11 [label="bool",comment="name: \"bool\", typeName: \"\", id: 11, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
12 [label="Structure's NBT",comment="name: \"Structure's NBT\", typeName: \"CompoundTag\", id: 12, branchId: 0, recurseId: -1, attributes: 256, notes: \"\""];
13 [label="CompoundTag",comment="name: \"CompoundTag\", typeName: \"\", id: 13, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
14 [label="Response Type",comment="name: \"Response Type\", typeName: \"\", id: 14, branchId: 0, recurseId: -1, attributes: 0, notes: \"enumeration: StructureTemplateResponseType\""];
15 [label="byte",comment="name: \"byte\", typeName: \"\", id: 15, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
{ rank = max;2;6;8;11;13;15}

}

```

## 字段

/// define
StructureTemplateDataResponsePacket

Structure Name：<!-- md:samp string -->

- 类型：string。

Dependency on 'Requested structure exists?'

//// tab | if (0)
///// define
if (0)

Failure：<!-- md:samp bool -->

- 类型：bool。Bool set to false, indicating the requested structure d'id'n't exist.

Response Type：<!-- md:samp byte -->

- 类型：byte。enumeration: StructureTemplateResponseType


/////

////

//// tab | if (1)
///// define
if (1)

Success：<!-- md:samp bool -->

- 类型：bool。Bool set to true, indicating success.

Structure's NBT：[<!-- md:samp CompoundTag -->](../types/compoundtag.md)

- 类型：CompoundTag。

Response Type：<!-- md:samp byte -->

- 类型：byte。enumeration: StructureTemplateResponseType


/////

////



///
