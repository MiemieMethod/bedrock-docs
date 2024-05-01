# <!-- md:samp ChunkRadiusUpdatedPacket -->

> 文档版本：r/20_u8<br/>协议版本：671

<!-- md:samp ChunkRadiusUpdatedPacket -->数据包，数字ID是`70`。该数据包用于protocol.packet.chunkradiusupdatedpacket.description

## 结构

```viz
digraph "ChunkRadiusUpdatedPacket" {
rankdir = LR
0
0 -> 1
1 -> 2

0 [label="ChunkRadiusUpdatedPacket",comment="name: \"ChunkRadiusUpdatedPacket\", typeName: \"\", id: 0, branchId: 70, recurseId: -1, attributes: 0, notes: \"\""];
1 [label="Chunk Radius",comment="name: \"Chunk Radius\", typeName: \"\", id: 1, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
2 [label="varint",comment="name: \"varint\", typeName: \"\", id: 2, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
{ rank = max;2}

}

```

## 字段

```title='ChunkRadiusUpdatedPacket'
[chunk_radius]
```

/// html | div.result
//// define
Chunk Radius：<!-- md:samp varint -->

- 基本类型。protocol.packet.chunkradiusupdatedpacket.chunk_radius.description


////

///

