# <!-- md:samp PhotoTransferPacket -->

> 文档版本：r/20_u7<br/>协议版本：662

<!-- md:samp PhotoTransferPacket -->数据包，数字ID是`99`。该数据包用于protocol.packet.phototransferpacket.description

## 结构

```viz
digraph "PhotoTransferPacket" {
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
0 -> 9
9 -> 10
0 -> 11
11 -> 12
0 -> 13
13 -> 14

0 [label="PhotoTransferPacket",comment="name: \"PhotoTransferPacket\", typeName: \"\", id: 0, branchId: 99, recurseId: -1, attributes: 0, notes: \"\""];
1 [label="Photo Name",comment="name: \"Photo Name\", typeName: \"\", id: 1, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
2 [label="string",comment="name: \"string\", typeName: \"\", id: 2, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
3 [label="Photo Data",comment="name: \"Photo Data\", typeName: \"\", id: 3, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
4 [label="string",comment="name: \"string\", typeName: \"\", id: 4, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
5 [label="Book ID",comment="name: \"Book ID\", typeName: \"\", id: 5, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
6 [label="string",comment="name: \"string\", typeName: \"\", id: 6, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
7 [label="Type",comment="name: \"Type\", typeName: \"\", id: 7, branchId: 0, recurseId: -1, attributes: 0, notes: \"enumeration: PhotoType\""];
8 [label="byte",comment="name: \"byte\", typeName: \"\", id: 8, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
9 [label="Source Type",comment="name: \"Source Type\", typeName: \"\", id: 9, branchId: 0, recurseId: -1, attributes: 0, notes: \"enumeration: PhotoType\""];
10 [label="byte",comment="name: \"byte\", typeName: \"\", id: 10, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
11 [label="Owner ID",comment="name: \"Owner ID\", typeName: \"\", id: 11, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
12 [label="int64",comment="name: \"int64\", typeName: \"\", id: 12, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
13 [label="New Photo Name",comment="name: \"New Photo Name\", typeName: \"\", id: 13, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
14 [label="string",comment="name: \"string\", typeName: \"\", id: 14, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
{ rank = max;2;4;6;8;10;12;14}

}

```

## 字段

```title='PhotoTransferPacket'
[photo_name][photo_data][book_id][type][source_type][owner_id][new_photo_name]
```

/// html | div.result
//// define
Photo Name：[<!-- md:samp string -->](../types/string.md)

- 特殊类型。protocol.packet.phototransferpacket.photo_name.description


////
//// define
Photo Data：[<!-- md:samp string -->](../types/string.md)

- 特殊类型。protocol.packet.phototransferpacket.photo_data.description


////
//// define
Book ID：[<!-- md:samp string -->](../types/string.md)

- 特殊类型。protocol.packet.phototransferpacket.book_id.description


////
//// define
Type：<!-- md:samp byte -->

- 基本类型枚举。protocol.packet.phototransferpacket.type.description枚举值如下：

  |键|值|描述|
  |---|---|---|
  |`Portfolio`|`0`|protocol.enum.portfolio|
  |`PhotoItem`|`1`|protocol.enum.photoitem|
  |`Book`|`2`|protocol.enum.book|



////
//// define
Source Type：<!-- md:samp byte -->

- 基本类型枚举。protocol.packet.phototransferpacket.source_type.description枚举值如下：

  |键|值|描述|
  |---|---|---|
  |`Portfolio`|`0`|protocol.enum.portfolio|
  |`PhotoItem`|`1`|protocol.enum.photoitem|
  |`Book`|`2`|protocol.enum.book|



////
//// define
Owner ID：<!-- md:samp int64 -->

- 基本类型。protocol.packet.phototransferpacket.owner_id.description


////
//// define
New Photo Name：[<!-- md:samp string -->](../types/string.md)

- 特殊类型。protocol.packet.phototransferpacket.new_photo_name.description


////

///

