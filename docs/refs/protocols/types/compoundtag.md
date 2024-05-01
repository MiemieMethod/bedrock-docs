# <!-- md:samp CompoundTag -->

> 文档版本：r/20_u8<br/>协议版本：671

<!-- md:samp CompoundTag -->类型。该类型用于protocol.type.compoundtag.description

## 结构

```viz
digraph "CompoundTag" {
rankdir = LR
0
0 -> 1
1 -> 2
0 -> 3
3 -> 4
4 -> 5
5 -> 6
4 -> 7
7 -> 8
8 -> 9
7 -> 10
10 -> 11
11 -> 12
7 -> 13
13 -> 14
14 -> 15
7 -> 16
16 -> 17
17 -> 18
7 -> 19
19 -> 20
20 -> 21
7 -> 22
22 -> 23
23 -> 24
7 -> 25
25 -> 26
26 -> 27
7 -> 28
28 -> 29
29 -> 30
30 -> 31
29 -> 32
32 -> 33
33 -> 34
7 -> 35
35 -> 36
36 -> 37
7 -> 38
38 -> 39
39 -> 40
40 -> 41
41 -> 42
39 -> 43
43 -> 44
44 -> 45
38 -> 46
46 -> 47
47 -> 48
46 -> 49
49 -> 50
50 -> 58
7 -> 59
59 -> 60
60 -> 61
61 -> 62
62 -> 63
59 -> 64
64 -> 65
7 -> 66
66 -> 67
67 -> 68
68 -> 69
67 -> 70
70 -> 71
71 -> 72
3 -> 73
73 -> 74

0 [label="CompoundTag",comment="name: \"CompoundTag\", typeName: \"\", id: 0, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
1 [label="Tag Type",comment="name: \"Tag Type\", typeName: \"\", id: 1, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
2 [label="byte",comment="name: \"byte\", typeName: \"\", id: 2, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
3 [label="Dependency on 'if 'Tag Type' is 0'",shape=note,comment="name: \"Dependency on 'if 'Tag Type' is 0'\", typeName: \"\", id: 3, branchId: 0, recurseId: -1, attributes: 2, notes: \"\""];
4 [label="if (0)",shape=diamond,comment="name: \"if (0)\", typeName: \"\", id: 4, branchId: 0, recurseId: -1, attributes: 4, notes: \"\""];
5 [label="Tag Name",comment="name: \"Tag Name\", typeName: \"\", id: 5, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
6 [label="string",comment="name: \"string\", typeName: \"\", id: 6, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
7 [label="Dependency on 'Tag Type'",shape=note,comment="name: \"Dependency on 'Tag Type'\", typeName: \"\", id: 7, branchId: 0, recurseId: -1, attributes: 2, notes: \"\""];
8 [label="if (0)",shape=diamond,comment="name: \"if (0)\", typeName: \"\", id: 8, branchId: 0, recurseId: -1, attributes: 4, notes: \"\""];
9 [label="[No Data]",comment="name: \"[No Data]\", typeName: \"\", id: 9, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
10 [label="if (1)",shape=diamond,comment="name: \"if (1)\", typeName: \"\", id: 10, branchId: 1, recurseId: -1, attributes: 4, notes: \"\""];
11 [label="Tag Value",comment="name: \"Tag Value\", typeName: \"\", id: 11, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
12 [label="byte",comment="name: \"byte\", typeName: \"\", id: 12, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
13 [label="if (2)",shape=diamond,comment="name: \"if (2)\", typeName: \"\", id: 13, branchId: 2, recurseId: -1, attributes: 4, notes: \"\""];
14 [label="Tag Value",comment="name: \"Tag Value\", typeName: \"\", id: 14, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
15 [label="short",comment="name: \"short\", typeName: \"\", id: 15, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
16 [label="if (3)",shape=diamond,comment="name: \"if (3)\", typeName: \"\", id: 16, branchId: 3, recurseId: -1, attributes: 4, notes: \"\""];
17 [label="Tag Value",comment="name: \"Tag Value\", typeName: \"\", id: 17, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
18 [label="varint",comment="name: \"varint\", typeName: \"\", id: 18, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
19 [label="if (4)",shape=diamond,comment="name: \"if (4)\", typeName: \"\", id: 19, branchId: 4, recurseId: -1, attributes: 4, notes: \"\""];
20 [label="Tag Value",comment="name: \"Tag Value\", typeName: \"\", id: 20, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
21 [label="varint64",comment="name: \"varint64\", typeName: \"\", id: 21, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
22 [label="if (5)",shape=diamond,comment="name: \"if (5)\", typeName: \"\", id: 22, branchId: 5, recurseId: -1, attributes: 4, notes: \"\""];
23 [label="Tag Value",comment="name: \"Tag Value\", typeName: \"\", id: 23, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
24 [label="float",comment="name: \"float\", typeName: \"\", id: 24, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
25 [label="if (6)",shape=diamond,comment="name: \"if (6)\", typeName: \"\", id: 25, branchId: 6, recurseId: -1, attributes: 4, notes: \"\""];
26 [label="Tag Value",comment="name: \"Tag Value\", typeName: \"\", id: 26, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
27 [label="double",comment="name: \"double\", typeName: \"\", id: 27, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
28 [label="if (7)",shape=diamond,comment="name: \"if (7)\", typeName: \"\", id: 28, branchId: 7, recurseId: -1, attributes: 4, notes: \"\""];
29 [label="Byte Array",comment="name: \"Byte Array\", typeName: \"\", id: 29, branchId: 0, recurseId: -1, attributes: 8, notes: \"\""];
30 [label="Array Size",comment="name: \"Array Size\", typeName: \"\", id: 30, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
31 [label="varint",comment="name: \"varint\", typeName: \"\", id: 31, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
32 [label="example element",style=dotted,comment="name: \"example element\", typeName: \"\", id: 32, branchId: 0, recurseId: -1, attributes: 16, notes: \"\""];
33 [label="Byte Data",comment="name: \"Byte Data\", typeName: \"\", id: 33, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
34 [label="byte",comment="name: \"byte\", typeName: \"\", id: 34, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
35 [label="if (8)",shape=diamond,comment="name: \"if (8)\", typeName: \"\", id: 35, branchId: 8, recurseId: -1, attributes: 4, notes: \"\""];
36 [label="Tag Value",comment="name: \"Tag Value\", typeName: \"\", id: 36, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
37 [label="string",comment="name: \"string\", typeName: \"\", id: 37, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
38 [label="if (9)",shape=diamond,comment="name: \"if (9)\", typeName: \"\", id: 38, branchId: 9, recurseId: -1, attributes: 4, notes: \"\""];
39 [label="Dependency on 'if empty list'",shape=note,comment="name: \"Dependency on 'if empty list'\", typeName: \"\", id: 39, branchId: 0, recurseId: -1, attributes: 2, notes: \"\""];
40 [label="if (0)",shape=diamond,comment="name: \"if (0)\", typeName: \"\", id: 40, branchId: 0, recurseId: -1, attributes: 4, notes: \"\""];
41 [label="Tag Type for list",comment="name: \"Tag Type for list\", typeName: \"\", id: 41, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
42 [label="byte",comment="name: \"byte\", typeName: \"\", id: 42, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
43 [label="if (1)",shape=diamond,comment="name: \"if (1)\", typeName: \"\", id: 43, branchId: 1, recurseId: -1, attributes: 4, notes: \"\""];
44 [label="Tag Type (must be 1)",comment="name: \"Tag Type (must be 1)\", typeName: \"\", id: 44, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
45 [label="byte",comment="name: \"byte\", typeName: \"\", id: 45, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
46 [label="Tag Array",comment="name: \"Tag Array\", typeName: \"\", id: 46, branchId: 0, recurseId: -1, attributes: 8, notes: \"\""];
47 [label="Array Size",comment="name: \"Array Size\", typeName: \"\", id: 47, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
48 [label="varint",comment="name: \"varint\", typeName: \"\", id: 48, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
49 [label="example element",style=dotted,comment="name: \"example element\", typeName: \"\", id: 49, branchId: 0, recurseId: -1, attributes: 16, notes: \"\""];
50 [label="Tag (Recursive)",comment="name: \"Tag (Recursive)\", typeName: \"CompoundTag\", id: 50, branchId: 0, recurseId: -1, attributes: 256, notes: \"\""];
58 [label="CompoundTag",comment="name: \"CompoundTag\", typeName: \"\", id: 58, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
59 [label="if (10)",shape=diamond,comment="name: \"if (10)\", typeName: \"\", id: 59, branchId: 10, recurseId: -1, attributes: 4, notes: \"\""];
60 [label="Tag Array",comment="name: \"Tag Array\", typeName: \"\", id: 60, branchId: 0, recurseId: -1, attributes: 8, notes: \"\""];
61 [label="example element",style=dotted,comment="name: \"example element\", typeName: \"\", id: 61, branchId: 0, recurseId: -1, attributes: 16, notes: \"\""];
62 [label="Tag (Recursive)",comment="name: \"Tag (Recursive)\", typeName: \"CompoundTag\", id: 62, branchId: 0, recurseId: -1, attributes: 256, notes: \"\""];
63 [label="CompoundTag",comment="name: \"CompoundTag\", typeName: \"\", id: 63, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
64 [label="End (must be 0)",comment="name: \"End (must be 0)\", typeName: \"\", id: 64, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
65 [label="byte",comment="name: \"byte\", typeName: \"\", id: 65, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
66 [label="if (11)",shape=diamond,comment="name: \"if (11)\", typeName: \"\", id: 66, branchId: 11, recurseId: -1, attributes: 4, notes: \"\""];
67 [label="Int Array",comment="name: \"Int Array\", typeName: \"\", id: 67, branchId: 0, recurseId: -1, attributes: 8, notes: \"\""];
68 [label="Array Size",comment="name: \"Array Size\", typeName: \"\", id: 68, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
69 [label="varint",comment="name: \"varint\", typeName: \"\", id: 69, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
70 [label="example element",style=dotted,comment="name: \"example element\", typeName: \"\", id: 70, branchId: 0, recurseId: -1, attributes: 16, notes: \"\""];
71 [label="Int Data",comment="name: \"Int Data\", typeName: \"\", id: 71, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
72 [label="varint",comment="name: \"varint\", typeName: \"\", id: 72, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
73 [label="if (1)",shape=diamond,comment="name: \"if (1)\", typeName: \"\", id: 73, branchId: 1, recurseId: -1, attributes: 4, notes: \"\""];
74 [label="[No Data]",comment="name: \"[No Data]\", typeName: \"\", id: 74, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
{ rank = max;2;6;9;12;15;18;21;24;27;31;34;37;42;45;48;58;63;65;69;72;74}

}

```

## 字段

```title='CompoundTag'
[tag_type][dependency_on_if_tag_type_is_0]
```

/// html | div.result
//// define
Tag Type：<!-- md:samp byte -->

- 基本类型枚举。protocol.type.compoundtag.tag_type.description枚举值如下：

  |键|值|描述|
  |---|---|---|
  |`End`|`0`|protocol.enum.end|
  |`Byte`|`1`|protocol.enum.byte|
  |`Short`|`2`|protocol.enum.short|
  |`Int`|`3`|protocol.enum.int|
  |`Int64`|`4`|protocol.enum.int64|
  |`Float`|`5`|protocol.enum.float|
  |`Double`|`6`|protocol.enum.double|
  |`ByteArray`|`7`|protocol.enum.bytearray|
  |`String`|`8`|protocol.enum.string|
  |`List`|`9`|protocol.enum.list|
  |`Compound`|`10`|protocol.enum.compound|
  |`IntArray`|`11`|protocol.enum.intarray|
  |`NumTagTypes`|`12`|protocol.enum.numtagtypes|



////
> 依赖于`if 'Tag Type' is 0`

///// tab | `if 'Tag Type' is 0`如果为`0`
```title='if (0)'
[tag_name][dependency_on_tag_type]
```

////// html | div.result
/////// define
Tag Name：[<!-- md:samp string -->](../types/string.md)

- 特殊类型。protocol.type.compoundtag.dependency_on_if_tag_type_is_0.if_0.tag_name.description


///////
> 依赖于`Tag Type`

//////// tab | `Tag Type`如果为`0`
///////// define
if (0)：<!-- md:samp [No Data] -->

- 无数据


/////////

////////

//////// tab | `Tag Type`如果为`1`
```title='if (1)'
[tag_value]
```

///////// html | div.result
////////// define
Tag Value：<!-- md:samp byte -->

- 基本类型。protocol.type.compoundtag.dependency_on_if_tag_type_is_0.if_0.dependency_on_tag_type.if_1.tag_value.description


//////////

/////////

////////

//////// tab | `Tag Type`如果为`2`
```title='if (2)'
[tag_value]
```

///////// html | div.result
////////// define
Tag Value：<!-- md:samp short -->

- 基本类型。protocol.type.compoundtag.dependency_on_if_tag_type_is_0.if_0.dependency_on_tag_type.if_2.tag_value.description


//////////

/////////

////////

//////// tab | `Tag Type`如果为`3`
```title='if (3)'
[tag_value]
```

///////// html | div.result
////////// define
Tag Value：<!-- md:samp varint -->

- 基本类型。protocol.type.compoundtag.dependency_on_if_tag_type_is_0.if_0.dependency_on_tag_type.if_3.tag_value.description


//////////

/////////

////////

//////// tab | `Tag Type`如果为`4`
```title='if (4)'
[tag_value]
```

///////// html | div.result
////////// define
Tag Value：<!-- md:samp varint64 -->

- 基本类型。protocol.type.compoundtag.dependency_on_if_tag_type_is_0.if_0.dependency_on_tag_type.if_4.tag_value.description


//////////

/////////

////////

//////// tab | `Tag Type`如果为`5`
```title='if (5)'
[tag_value]
```

///////// html | div.result
////////// define
Tag Value：<!-- md:samp float -->

- 基本类型。protocol.type.compoundtag.dependency_on_if_tag_type_is_0.if_0.dependency_on_tag_type.if_5.tag_value.description


//////////

/////////

////////

//////// tab | `Tag Type`如果为`6`
```title='if (6)'
[tag_value]
```

///////// html | div.result
////////// define
Tag Value：<!-- md:samp double -->

- 基本类型。protocol.type.compoundtag.dependency_on_if_tag_type_is_0.if_0.dependency_on_tag_type.if_6.tag_value.description


//////////

/////////

////////

//////// tab | `Tag Type`如果为`7`
```title='if (7)'
[byte_array]
```

///////// html | div.result
```title='Byte Array'
[array_size][[example_element]..]
```

////////// html | div.result
/////////// define
数组大小：<!-- md:samp varint -->

- 基本类型。protocol.type.compoundtag.dependency_on_if_tag_type_is_0.if_0.dependency_on_tag_type.if_7.byte_array.array_size.description


///////////
```title='示例元素'
[byte_data]
```

/////////// html | div.result
//////////// define
Byte Data：<!-- md:samp byte -->

- 基本类型。protocol.type.compoundtag.dependency_on_if_tag_type_is_0.if_0.dependency_on_tag_type.if_7.byte_array.example_element.byte_data.description


////////////

///////////

//////////

/////////

////////

//////// tab | `Tag Type`如果为`8`
```title='if (8)'
[tag_value]
```

///////// html | div.result
////////// define
Tag Value：[<!-- md:samp string -->](../types/string.md)

- 特殊类型。protocol.type.compoundtag.dependency_on_if_tag_type_is_0.if_0.dependency_on_tag_type.if_8.tag_value.description


//////////

/////////

////////

//////// tab | `Tag Type`如果为`9`
```title='if (9)'
[dependency_on_if_empty_list][tag_array]
```

///////// html | div.result
> 依赖于`if empty list`

/////////// tab | `if empty list`如果为`0`
```title='if (0)'
[tag_type_for_list]
```

//////////// html | div.result
///////////// define
Tag Type for list：<!-- md:samp byte -->

- 基本类型枚举。protocol.type.compoundtag.dependency_on_if_tag_type_is_0.if_0.dependency_on_tag_type.if_9.dependency_on_if_empty_list.if_0.tag_type_for_list.description枚举值如下：

  |键|值|描述|
  |---|---|---|
  |`End`|`0`|protocol.enum.end|
  |`Byte`|`1`|protocol.enum.byte|
  |`Short`|`2`|protocol.enum.short|
  |`Int`|`3`|protocol.enum.int|
  |`Int64`|`4`|protocol.enum.int64|
  |`Float`|`5`|protocol.enum.float|
  |`Double`|`6`|protocol.enum.double|
  |`ByteArray`|`7`|protocol.enum.bytearray|
  |`String`|`8`|protocol.enum.string|
  |`List`|`9`|protocol.enum.list|
  |`Compound`|`10`|protocol.enum.compound|
  |`IntArray`|`11`|protocol.enum.intarray|
  |`NumTagTypes`|`12`|protocol.enum.numtagtypes|



/////////////

////////////

///////////

/////////// tab | `if empty list`如果为`1`
```title='if (1)'
[tag_type]
```

//////////// html | div.result
///////////// define
Tag Type (must be 1)：<!-- md:samp byte -->

- 基本类型枚举。protocol.type.compoundtag.dependency_on_if_tag_type_is_0.if_0.dependency_on_tag_type.if_9.dependency_on_if_empty_list.if_1.tag_type.description枚举值如下：

  |键|值|描述|
  |---|---|---|
  |`End`|`0`|protocol.enum.end|
  |`Byte`|`1`|protocol.enum.byte|
  |`Short`|`2`|protocol.enum.short|
  |`Int`|`3`|protocol.enum.int|
  |`Int64`|`4`|protocol.enum.int64|
  |`Float`|`5`|protocol.enum.float|
  |`Double`|`6`|protocol.enum.double|
  |`ByteArray`|`7`|protocol.enum.bytearray|
  |`String`|`8`|protocol.enum.string|
  |`List`|`9`|protocol.enum.list|
  |`Compound`|`10`|protocol.enum.compound|
  |`IntArray`|`11`|protocol.enum.intarray|
  |`NumTagTypes`|`12`|protocol.enum.numtagtypes|



/////////////

////////////

///////////
```title='Tag Array'
[array_size][[example_element]..]
```

////////// html | div.result
/////////// define
数组大小：<!-- md:samp varint -->

- 基本类型。protocol.type.compoundtag.dependency_on_if_tag_type_is_0.if_0.dependency_on_tag_type.if_9.tag_array.array_size.description


///////////
```title='示例元素'
[tag]
```

/////////// html | div.result
//////////// define
Tag (Recursive)：[<!-- md:samp CompoundTag -->](../types/compoundtag.md)

- 特殊类型。protocol.type.compoundtag.dependency_on_if_tag_type_is_0.if_0.dependency_on_tag_type.if_9.tag_array.example_element.tag.description


////////////

///////////

//////////

/////////

////////

//////// tab | `Tag Type`如果为`10`
```title='if (10)'
[tag_array][end]
```

///////// html | div.result
```title='Tag Array'
[[example_element]..]
```

////////// html | div.result
```title='示例元素'
[tag]
```

/////////// html | div.result
//////////// define
Tag (Recursive)：[<!-- md:samp CompoundTag -->](../types/compoundtag.md)

- 特殊类型。protocol.type.compoundtag.dependency_on_if_tag_type_is_0.if_0.dependency_on_tag_type.if_10.tag_array.example_element.tag.description


////////////

///////////

//////////
////////// define
End (must be 0)：<!-- md:samp byte -->

- 基本类型。protocol.type.compoundtag.dependency_on_if_tag_type_is_0.if_0.dependency_on_tag_type.if_10.end.description


//////////

/////////

////////

//////// tab | `Tag Type`如果为`11`
```title='if (11)'
[int_array]
```

///////// html | div.result
```title='Int Array'
[array_size][[example_element]..]
```

////////// html | div.result
/////////// define
数组大小：<!-- md:samp varint -->

- 基本类型。protocol.type.compoundtag.dependency_on_if_tag_type_is_0.if_0.dependency_on_tag_type.if_11.int_array.array_size.description


///////////
```title='示例元素'
[int_data]
```

/////////// html | div.result
//////////// define
Int Data：<!-- md:samp varint -->

- 基本类型。protocol.type.compoundtag.dependency_on_if_tag_type_is_0.if_0.dependency_on_tag_type.if_11.int_array.example_element.int_data.description


////////////

///////////

//////////

/////////

////////

//////

/////

///// tab | `if 'Tag Type' is 0`如果为`1`
////// define
if (1)：<!-- md:samp [No Data] -->

- 无数据


//////

/////

///

