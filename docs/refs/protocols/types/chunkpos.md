# <!-- md:samp ChunkPos -->

> 文档版本：r/21_u4<br/>协议版本：748

<!-- md:samp ChunkPos -->类型。该类型用于protocol.type.chunkpos.description

## 结构

```viz
digraph "ChunkPos" {
rankdir = LR
2
2 -> 3
3 -> 4
2 -> 5
5 -> 6

2 [label="ChunkPos",comment="name: \"ChunkPos\", typeName: \"\", id: 2, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
3 [label="X",comment="name: \"X\", typeName: \"\", id: 3, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
4 [label="varint",comment="name: \"varint\", typeName: \"\", id: 4, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
5 [label="Z",comment="name: \"Z\", typeName: \"\", id: 5, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
6 [label="varint",comment="name: \"varint\", typeName: \"\", id: 6, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
{ rank = max;4;6}

}

```

## 字段

```title='ChunkPos'
[x][z]
```

/// html | div.result
//// define
X：<!-- md:samp varint -->

- 基本类型。protocol.type.chunkpos.x.description


////
//// define
Z：<!-- md:samp varint -->

- 基本类型。protocol.type.chunkpos.z.description


////

///

