# <!-- md:samp ResourcePackChunkDataPacket -->

> 文档版本：r/21_u4<br/>协议版本：748

<!-- md:samp ResourcePackChunkDataPacket -->数据包，数字ID是`83`。该数据包用于protocol.packet.resourcepackchunkdatapacket.description

## 结构

```viz
digraph "ResourcePackChunkDataPacket" {
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

0 [label="ResourcePackChunkDataPacket",comment="name: \"ResourcePackChunkDataPacket\", typeName: \"\", id: 0, branchId: 83, recurseId: -1, attributes: 0, notes: \"\""];
1 [label="Resource Name",comment="name: \"Resource Name\", typeName: \"\", id: 1, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
2 [label="string",comment="name: \"string\", typeName: \"\", id: 2, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
3 [label="Chunk ID",comment="name: \"Chunk ID\", typeName: \"\", id: 3, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
4 [label="unsigned int",comment="name: \"unsigned int\", typeName: \"\", id: 4, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
5 [label="Byte Offset",comment="name: \"Byte Offset\", typeName: \"\", id: 5, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
6 [label="unsigned int64",comment="name: \"unsigned int64\", typeName: \"\", id: 6, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
7 [label="Chunk Data",comment="name: \"Chunk Data\", typeName: \"\", id: 7, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
8 [label="string",comment="name: \"string\", typeName: \"\", id: 8, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
{ rank = max;2;4;6;8}

}

```

## 字段

```title='ResourcePackChunkDataPacket'
[resource_name][chunk_id][byte_offset][chunk_data]
```

/// html | div.result
//// define
Resource Name：[<!-- md:samp string -->](../types/string.md)

- 特殊类型。protocol.packet.resourcepackchunkdatapacket.resource_name.description


////
//// define
Chunk ID：<!-- md:samp unsigned int -->

- 基本类型。protocol.packet.resourcepackchunkdatapacket.chunk_id.description


////
//// define
Byte Offset：<!-- md:samp unsigned int64 -->

- 基本类型。protocol.packet.resourcepackchunkdatapacket.byte_offset.description


////
//// define
Chunk Data：[<!-- md:samp string -->](../types/string.md)

- 特殊类型。protocol.packet.resourcepackchunkdatapacket.chunk_data.description


////

///

