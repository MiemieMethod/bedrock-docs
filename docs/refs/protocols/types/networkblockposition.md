# <!-- md:samp NetworkBlockPosition -->

> 文档版本：r/20_u7<br/>协议版本：662

<!-- md:samp NetworkBlockPosition -->类型。

## 结构

```viz
digraph "NetworkBlockPosition" {
rankdir = LR
42
42 -> 43
43 -> 44
42 -> 45
45 -> 46
42 -> 47
47 -> 48

42 [label="NetworkBlockPosition",comment="name: \"NetworkBlockPosition\", typeName: \"\", id: 42, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
43 [label="X",comment="name: \"X\", typeName: \"\", id: 43, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
44 [label="varint",comment="name: \"varint\", typeName: \"\", id: 44, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
45 [label="Y",comment="name: \"Y\", typeName: \"\", id: 45, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
46 [label="unsigned varint",comment="name: \"unsigned varint\", typeName: \"\", id: 46, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
47 [label="Z",comment="name: \"Z\", typeName: \"\", id: 47, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
48 [label="varint",comment="name: \"varint\", typeName: \"\", id: 48, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
{ rank = max;44;46;48}

}

```

## 字段

/// define
NetworkBlockPosition

X：<!-- md:samp varint -->

- 类型：varint。

Y：<!-- md:samp unsigned varint -->

- 类型：unsigned varint。

Z：<!-- md:samp varint -->

- 类型：varint。


///
