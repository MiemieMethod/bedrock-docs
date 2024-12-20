# <!-- md:samp DataItem -->

> 文档版本：r/21_u4<br/>协议版本：748

<!-- md:samp DataItem -->类型。该类型用于protocol.type.dataitem.description

## 结构

```viz
digraph "DataItem" {
rankdir = LR
1
1 -> 2
2 -> 3
1 -> 4
4 -> 5
1 -> 6
6 -> 7
7 -> 8
8 -> 9
6 -> 10
10 -> 11
11 -> 12
6 -> 13
13 -> 14
14 -> 15
6 -> 16
16 -> 17
17 -> 18
6 -> 19
19 -> 20
20 -> 21
6 -> 22
22 -> 23
23 -> 24
6 -> 25
25 -> 26
26 -> 27
6 -> 28
28 -> 29
29 -> 30
6 -> 31
31 -> 32
32 -> 33

1 [label="DataItem",comment="name: \"DataItem\", typeName: \"\", id: 1, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
2 [label="ID",comment="name: \"ID\", typeName: \"\", id: 2, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
3 [label="unsigned varint",comment="name: \"unsigned varint\", typeName: \"\", id: 3, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
4 [label="Type",comment="name: \"Type\", typeName: \"\", id: 4, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
5 [label="unsigned varint",comment="name: \"unsigned varint\", typeName: \"\", id: 5, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
6 [label="Dependency on 'Type'",shape=note,comment="name: \"Dependency on 'Type'\", typeName: \"\", id: 6, branchId: 0, recurseId: -1, attributes: 2, notes: \"\""];
7 [label="if (0)",shape=diamond,comment="name: \"if (0)\", typeName: \"\", id: 7, branchId: 0, recurseId: -1, attributes: 4, notes: \"\""];
8 [label="Value",comment="name: \"Value\", typeName: \"\", id: 8, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
9 [label="byte",comment="name: \"byte\", typeName: \"\", id: 9, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
10 [label="if (1)",shape=diamond,comment="name: \"if (1)\", typeName: \"\", id: 10, branchId: 1, recurseId: -1, attributes: 4, notes: \"\""];
11 [label="Value",comment="name: \"Value\", typeName: \"\", id: 11, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
12 [label="short",comment="name: \"short\", typeName: \"\", id: 12, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
13 [label="if (2)",shape=diamond,comment="name: \"if (2)\", typeName: \"\", id: 13, branchId: 2, recurseId: -1, attributes: 4, notes: \"\""];
14 [label="Value",comment="name: \"Value\", typeName: \"\", id: 14, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
15 [label="varint",comment="name: \"varint\", typeName: \"\", id: 15, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
16 [label="if (3)",shape=diamond,comment="name: \"if (3)\", typeName: \"\", id: 16, branchId: 3, recurseId: -1, attributes: 4, notes: \"\""];
17 [label="Value",comment="name: \"Value\", typeName: \"\", id: 17, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
18 [label="float",comment="name: \"float\", typeName: \"\", id: 18, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
19 [label="if (4)",shape=diamond,comment="name: \"if (4)\", typeName: \"\", id: 19, branchId: 4, recurseId: -1, attributes: 4, notes: \"\""];
20 [label="Value",comment="name: \"Value\", typeName: \"\", id: 20, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
21 [label="string",comment="name: \"string\", typeName: \"\", id: 21, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
22 [label="if (5)",shape=diamond,comment="name: \"if (5)\", typeName: \"\", id: 22, branchId: 5, recurseId: -1, attributes: 4, notes: \"\""];
23 [label="Value",comment="name: \"Value\", typeName: \"\", id: 23, branchId: 0, recurseId: -1, attributes: 256, notes: \"\""];
24 [label="CompoundTag",comment="name: \"CompoundTag\", typeName: \"\", id: 24, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
25 [label="if (6)",shape=diamond,comment="name: \"if (6)\", typeName: \"\", id: 25, branchId: 6, recurseId: -1, attributes: 4, notes: \"\""];
26 [label="Value",comment="name: \"Value\", typeName: \"\", id: 26, branchId: 0, recurseId: -1, attributes: 256, notes: \"\""];
27 [label="BlockPos",comment="name: \"BlockPos\", typeName: \"\", id: 27, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
28 [label="if (7)",shape=diamond,comment="name: \"if (7)\", typeName: \"\", id: 28, branchId: 7, recurseId: -1, attributes: 4, notes: \"\""];
29 [label="Value",comment="name: \"Value\", typeName: \"\", id: 29, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
30 [label="varint64",comment="name: \"varint64\", typeName: \"\", id: 30, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
31 [label="if (8)",shape=diamond,comment="name: \"if (8)\", typeName: \"\", id: 31, branchId: 8, recurseId: -1, attributes: 4, notes: \"\""];
32 [label="Value",comment="name: \"Value\", typeName: \"\", id: 32, branchId: 0, recurseId: -1, attributes: 256, notes: \"\""];
33 [label="Vec3",comment="name: \"Vec3\", typeName: \"\", id: 33, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
{ rank = max;3;5;9;12;15;18;21;24;27;30;33}

}

```

## 字段

```title='DataItem'
[id][type][dependency_on_type]
```

/// html | div.result
//// define
ID：<!-- md:samp unsigned varint -->

- 基本类型。protocol.type.dataitem.id.description


////
//// define
Type：<!-- md:samp unsigned varint -->

- 基本类型枚举。protocol.type.dataitem.type.description枚举值如下：

  |键|值|描述|
  |---|---|---|
  |`Byte`|`0`|protocol.enum.byte|
  |`Short`|`1`|protocol.enum.short|
  |`Int`|`2`|protocol.enum.int|
  |`Float`|`3`|protocol.enum.float|
  |`String`|`4`|protocol.enum.string|
  |`CompoundTag`|`5`|protocol.enum.compoundtag|
  |`Pos`|`6`|protocol.enum.pos|
  |`Int64`|`7`|protocol.enum.int64|
  |`Vec3`|`8`|protocol.enum.vec3|
  |`Unknown`|`9`|protocol.enum.unknown|



////
> 依赖于`Type`

///// tab | `Type`如果为`0`
```title='if (0)'
[value]
```

////// html | div.result
/////// define
Value：<!-- md:samp byte -->

- 基本类型。protocol.type.dataitem.dependency_on_type.if_0.value.description


///////

//////

/////

///// tab | `Type`如果为`1`
```title='if (1)'
[value]
```

////// html | div.result
/////// define
Value：<!-- md:samp short -->

- 基本类型。protocol.type.dataitem.dependency_on_type.if_1.value.description


///////

//////

/////

///// tab | `Type`如果为`2`
```title='if (2)'
[value]
```

////// html | div.result
/////// define
Value：<!-- md:samp varint -->

- 基本类型。protocol.type.dataitem.dependency_on_type.if_2.value.description


///////

//////

/////

///// tab | `Type`如果为`3`
```title='if (3)'
[value]
```

////// html | div.result
/////// define
Value：<!-- md:samp float -->

- 基本类型。protocol.type.dataitem.dependency_on_type.if_3.value.description


///////

//////

/////

///// tab | `Type`如果为`4`
```title='if (4)'
[value]
```

////// html | div.result
/////// define
Value：[<!-- md:samp string -->](../types/string.md)

- 特殊类型。protocol.type.dataitem.dependency_on_type.if_4.value.description


///////

//////

/////

///// tab | `Type`如果为`5`
```title='if (5)'
[value]
```

////// html | div.result
/////// define
Value：[<!-- md:samp CompoundTag -->](../types/compoundtag.md)

- 特殊类型。protocol.type.dataitem.dependency_on_type.if_5.value.description


///////

//////

/////

///// tab | `Type`如果为`6`
```title='if (6)'
[value]
```

////// html | div.result
/////// define
Value：[<!-- md:samp BlockPos -->](../types/blockpos.md)

- 特殊类型。protocol.type.dataitem.dependency_on_type.if_6.value.description


///////

//////

/////

///// tab | `Type`如果为`7`
```title='if (7)'
[value]
```

////// html | div.result
/////// define
Value：<!-- md:samp varint64 -->

- 基本类型。protocol.type.dataitem.dependency_on_type.if_7.value.description


///////

//////

/////

///// tab | `Type`如果为`8`
```title='if (8)'
[value]
```

////// html | div.result
/////// define
Value：[<!-- md:samp Vec3 -->](../types/vec3.md)

- 特殊类型。protocol.type.dataitem.dependency_on_type.if_8.value.description


///////

//////

/////

///

