# <!-- md:samp ChunkPos -->

> 文档版本：r/20_u7<br/>协议版本：662

<!-- md:samp ChunkPos -->类型。

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

- <!-- md:samp varint -->类型。


////
//// define
Z：<!-- md:samp varint -->

- <!-- md:samp varint -->类型。


////

///

