# <!-- md:samp SubChunkPos -->

> 文档版本：r/20_u7<br/>协议版本：662

<!-- md:samp SubChunkPos -->类型。

## 结构

```viz
digraph "SubChunkPos" {
rankdir = LR
6
6 -> 7
7 -> 8
6 -> 9
9 -> 10
6 -> 11
11 -> 12

6 [label="SubChunkPos",comment="name: \"SubChunkPos\", typeName: \"\", id: 6, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
7 [label="X",comment="name: \"X\", typeName: \"\", id: 7, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
8 [label="varint",comment="name: \"varint\", typeName: \"\", id: 8, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
9 [label="Y",comment="name: \"Y\", typeName: \"\", id: 9, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
10 [label="varint",comment="name: \"varint\", typeName: \"\", id: 10, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
11 [label="Z",comment="name: \"Z\", typeName: \"\", id: 11, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
12 [label="varint",comment="name: \"varint\", typeName: \"\", id: 12, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
{ rank = max;8;10;12}

}

```

## 字段

```title='SubChunkPos'
[x][y][z]
```

/// html | div.result
//// define
X：<!-- md:samp varint -->

- 基本类型。


////
//// define
Y：<!-- md:samp varint -->

- 基本类型。


////
//// define
Z：<!-- md:samp varint -->

- 基本类型。


////

///

