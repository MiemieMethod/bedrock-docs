# <!-- md:samp RequestChunkRadiusPacket -->

> 文档版本：r/21_u4<br/>协议版本：748

<!-- md:samp RequestChunkRadiusPacket -->数据包，数字ID是`69`。该数据包用于protocol.packet.requestchunkradiuspacket.description

## 结构

```viz
digraph "RequestChunkRadiusPacket" {
rankdir = LR
0
0 -> 1
1 -> 2
0 -> 3
3 -> 4

0 [label="RequestChunkRadiusPacket",comment="name: \"RequestChunkRadiusPacket\", typeName: \"\", id: 0, branchId: 69, recurseId: -1, attributes: 0, notes: \"\""];
1 [label="Chunk Radius",comment="name: \"Chunk Radius\", typeName: \"\", id: 1, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
2 [label="varint",comment="name: \"varint\", typeName: \"\", id: 2, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
3 [label="Max ChunkRadius",comment="name: \"Max ChunkRadius\", typeName: \"\", id: 3, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
4 [label="byte",comment="name: \"byte\", typeName: \"\", id: 4, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
{ rank = max;2;4}

}

```

## 字段

```title='RequestChunkRadiusPacket'
[chunk_radius][max_chunkradius]
```

/// html | div.result
//// define
Chunk Radius：<!-- md:samp varint -->

- 基本类型。protocol.packet.requestchunkradiuspacket.chunk_radius.description


////
//// define
Max ChunkRadius：<!-- md:samp byte -->

- 基本类型。protocol.packet.requestchunkradiuspacket.max_chunkradius.description


////

///

