# <!-- md:samp BlockPos -->

> 文档版本：r/20_u7<br/>协议版本：662

<!-- md:samp BlockPos -->类型。

## 结构

```viz
digraph "BlockPos" {
rankdir = LR
8
8 -> 9
9 -> 10
8 -> 11
11 -> 12
8 -> 13
13 -> 14

8 [label="BlockPos",comment="name: \"BlockPos\", typeName: \"\", id: 8, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
9 [label="X",comment="name: \"X\", typeName: \"\", id: 9, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
10 [label="varint",comment="name: \"varint\", typeName: \"\", id: 10, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
11 [label="Y",comment="name: \"Y\", typeName: \"\", id: 11, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
12 [label="varint",comment="name: \"varint\", typeName: \"\", id: 12, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
13 [label="Z",comment="name: \"Z\", typeName: \"\", id: 13, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
14 [label="varint",comment="name: \"varint\", typeName: \"\", id: 14, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
{ rank = max;10;12;14}

}

```

## 字段

```title='BlockPos'
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
