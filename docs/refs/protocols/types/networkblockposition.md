# <!-- md:samp NetworkBlockPosition -->

> 文档版本：r/21_u3<br/>协议版本：729

<!-- md:samp NetworkBlockPosition -->类型。该类型用于protocol.type.networkblockposition.description

## 结构

```viz
digraph "NetworkBlockPosition" {
rankdir = LR
44
44 -> 45
45 -> 46
44 -> 47
47 -> 48
44 -> 49
49 -> 50

44 [label="NetworkBlockPosition",comment="name: \"NetworkBlockPosition\", typeName: \"\", id: 44, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
45 [label="X",comment="name: \"X\", typeName: \"\", id: 45, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
46 [label="varint",comment="name: \"varint\", typeName: \"\", id: 46, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
47 [label="Y",comment="name: \"Y\", typeName: \"\", id: 47, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
48 [label="unsigned varint",comment="name: \"unsigned varint\", typeName: \"\", id: 48, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
49 [label="Z",comment="name: \"Z\", typeName: \"\", id: 49, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
50 [label="varint",comment="name: \"varint\", typeName: \"\", id: 50, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
{ rank = max;46;48;50}

}

```

## 字段

```title='NetworkBlockPosition'
[x][y][z]
```

/// html | div.result
//// define
X：<!-- md:samp varint -->

- 基本类型。protocol.type.networkblockposition.x.description


////
//// define
Y：<!-- md:samp unsigned varint -->

- 基本类型。protocol.type.networkblockposition.y.description


////
//// define
Z：<!-- md:samp varint -->

- 基本类型。protocol.type.networkblockposition.z.description


////

///

