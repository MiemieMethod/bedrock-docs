# <!-- md:samp ResourcePackChunkRequestPacket -->

> 文档版本：r/20_u8<br/>协议版本：671

<!-- md:samp ResourcePackChunkRequestPacket -->数据包，数字ID是`84`。该数据包用于protocol.packet.resourcepackchunkrequestpacket.description

## 结构

```viz
digraph "ResourcePackChunkRequestPacket" {
rankdir = LR
0
0 -> 1
1 -> 2
0 -> 3
3 -> 4

0 [label="ResourcePackChunkRequestPacket",comment="name: \"ResourcePackChunkRequestPacket\", typeName: \"\", id: 0, branchId: 84, recurseId: -1, attributes: 0, notes: \"\""];
1 [label="Resource Name",comment="name: \"Resource Name\", typeName: \"\", id: 1, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
2 [label="string",comment="name: \"string\", typeName: \"\", id: 2, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
3 [label="Chunk",comment="name: \"Chunk\", typeName: \"\", id: 3, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
4 [label="unsigned int",comment="name: \"unsigned int\", typeName: \"\", id: 4, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
{ rank = max;2;4}

}

```

## 字段

```title='ResourcePackChunkRequestPacket'
[resource_name][chunk]
```

/// html | div.result
//// define
Resource Name：[<!-- md:samp string -->](../types/string.md)

- 特殊类型。protocol.packet.resourcepackchunkrequestpacket.resource_name.description


////
//// define
Chunk：<!-- md:samp unsigned int -->

- 基本类型。protocol.packet.resourcepackchunkrequestpacket.chunk.description


////

///

