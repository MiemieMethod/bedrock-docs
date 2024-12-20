# <!-- md:samp StructureTemplateDataResponsePacket -->

> 文档版本：r/21_u4<br/>协议版本：748

<!-- md:samp StructureTemplateDataResponsePacket -->数据包，数字ID是`133`。该数据包用于protocol.packet.structuretemplatedataresponsepacket.description

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
7 [label="Response Type",comment="name: \"Response Type\", typeName: \"\", id: 7, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
8 [label="byte",comment="name: \"byte\", typeName: \"\", id: 8, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
9 [label="if (1)",shape=diamond,comment="name: \"if (1)\", typeName: \"\", id: 9, branchId: 1, recurseId: -1, attributes: 4, notes: \"\""];
10 [label="Success",comment="name: \"Success\", typeName: \"\", id: 10, branchId: 0, recurseId: -1, attributes: 0, notes: \"Bool set to true, indicating success.\""];
11 [label="bool",comment="name: \"bool\", typeName: \"\", id: 11, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
12 [label="Structure's NBT",comment="name: \"Structure's NBT\", typeName: \"CompoundTag\", id: 12, branchId: 0, recurseId: -1, attributes: 256, notes: \"\""];
13 [label="CompoundTag",comment="name: \"CompoundTag\", typeName: \"\", id: 13, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
14 [label="Response Type",comment="name: \"Response Type\", typeName: \"\", id: 14, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
15 [label="byte",comment="name: \"byte\", typeName: \"\", id: 15, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
{ rank = max;2;6;8;11;13;15}

}

```

## 字段

```title='StructureTemplateDataResponsePacket'
[structure_name][dependency_on_requested_structure_exists]
```

/// html | div.result
//// define
Structure Name：[<!-- md:samp string -->](../types/string.md)

- 特殊类型。protocol.packet.structuretemplatedataresponsepacket.structure_name.description


////
> 依赖于`Requested structure exists?`

///// tab | `Requested structure exists?`如果为`0`
```title='if (0)'
[failure][response_type]
```

////// html | div.result
/////// define
Failure：<!-- md:samp bool -->

- 基本类型。protocol.packet.structuretemplatedataresponsepacket.dependency_on_requested_structure_exists.if_0.failure.descriptionBool set to false, indicating the requested structure d'id'n't exist.


///////
/////// define
Response Type：<!-- md:samp byte -->

- 基本类型枚举。protocol.packet.structuretemplatedataresponsepacket.dependency_on_requested_structure_exists.if_0.response_type.description枚举值如下：

  |键|值|描述|
  |---|---|---|
  |`None`|`0`|无|
  |`Export`|`1`|protocol.enum.export|
  |`Query`|`2`|protocol.enum.query|



///////

//////

/////

///// tab | `Requested structure exists?`如果为`1`
```title='if (1)'
[success][structures_nbt][response_type]
```

////// html | div.result
/////// define
Success：<!-- md:samp bool -->

- 基本类型。protocol.packet.structuretemplatedataresponsepacket.dependency_on_requested_structure_exists.if_1.success.descriptionBool set to true, indicating success.


///////
/////// define
Structure's NBT：[<!-- md:samp CompoundTag -->](../types/compoundtag.md)

- 特殊类型。protocol.packet.structuretemplatedataresponsepacket.dependency_on_requested_structure_exists.if_1.structures_nbt.description


///////
/////// define
Response Type：<!-- md:samp byte -->

- 基本类型枚举。protocol.packet.structuretemplatedataresponsepacket.dependency_on_requested_structure_exists.if_1.response_type.description枚举值如下：

  |键|值|描述|
  |---|---|---|
  |`None`|`0`|无|
  |`Export`|`1`|protocol.enum.export|
  |`Query`|`2`|protocol.enum.query|



///////

//////

/////

///

