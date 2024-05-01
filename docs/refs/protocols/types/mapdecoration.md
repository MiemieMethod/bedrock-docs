# <!-- md:samp MapDecoration -->

> 文档版本：r/20_u8<br/>协议版本：671

<!-- md:samp MapDecoration -->类型。该类型用于protocol.type.mapdecoration.description

## 结构

```viz
digraph "MapDecoration" {
rankdir = LR
60
60 -> 61
61 -> 62
60 -> 63
63 -> 64
60 -> 65
65 -> 66
60 -> 67
67 -> 68
60 -> 69
69 -> 70
60 -> 71
71 -> 72

60 [label="MapDecoration",comment="name: \"MapDecoration\", typeName: \"\", id: 60, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
61 [label="Map Decoration Type",comment="name: \"Map Decoration Type\", typeName: \"\", id: 61, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
62 [label="byte",comment="name: \"byte\", typeName: \"\", id: 62, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
63 [label="Rotation",comment="name: \"Rotation\", typeName: \"\", id: 63, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
64 [label="byte",comment="name: \"byte\", typeName: \"\", id: 64, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
65 [label="X",comment="name: \"X\", typeName: \"\", id: 65, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
66 [label="byte",comment="name: \"byte\", typeName: \"\", id: 66, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
67 [label="Y",comment="name: \"Y\", typeName: \"\", id: 67, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
68 [label="byte",comment="name: \"byte\", typeName: \"\", id: 68, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
69 [label="Label",comment="name: \"Label\", typeName: \"\", id: 69, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
70 [label="string",comment="name: \"string\", typeName: \"\", id: 70, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
71 [label="Color - ARGB",comment="name: \"Color - ARGB\", typeName: \"\", id: 71, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
72 [label="unsigned varint",comment="name: \"unsigned varint\", typeName: \"\", id: 72, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
{ rank = max;62;64;66;68;70;72}

}

```

## 字段

```title='MapDecoration'
[map_decoration_type][rotation][x][y][label][color_argb]
```

/// html | div.result
//// define
Map Decoration Type：<!-- md:samp byte -->

- 基本类型。protocol.type.mapdecoration.map_decoration_type.description


////
//// define
Rotation：<!-- md:samp byte -->

- 基本类型。protocol.type.mapdecoration.rotation.description


////
//// define
X：<!-- md:samp byte -->

- 基本类型。protocol.type.mapdecoration.x.description


////
//// define
Y：<!-- md:samp byte -->

- 基本类型。protocol.type.mapdecoration.y.description


////
//// define
Label：[<!-- md:samp string -->](../types/string.md)

- 特殊类型。protocol.type.mapdecoration.label.description


////
//// define
Color - ARGB：<!-- md:samp unsigned varint -->

- 基本类型。protocol.type.mapdecoration.color_argb.description


////

///

