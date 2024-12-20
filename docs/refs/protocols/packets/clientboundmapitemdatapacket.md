# <!-- md:samp ClientboundMapItemDataPacket -->

> 文档版本：r/21_u4<br/>协议版本：748

<!-- md:samp ClientboundMapItemDataPacket -->数据包，数字ID是`67`。该数据包用于protocol.packet.clientboundmapitemdatapacket.description

## 结构

```viz
digraph "ClientboundMapItemDataPacket" {
rankdir = LR
0
0 -> 1
1 -> 2
0 -> 3
3 -> 4
0 -> 5
5 -> 6
0 -> 7
7 -> 8
0 -> 9
9 -> 10
0 -> 11
11 -> 12
12 -> 13
13 -> 14
14 -> 15
13 -> 16
16 -> 17
17 -> 18
16 -> 19
19 -> 20
11 -> 21
21 -> 22
0 -> 23
23 -> 24
24 -> 25
25 -> 26
23 -> 27
27 -> 28
28 -> 29
23 -> 30
30 -> 31
31 -> 32
23 -> 33
33 -> 34
0 -> 35
35 -> 36
36 -> 37
37 -> 38
38 -> 39
37 -> 40
40 -> 41
41 -> 54
36 -> 55
55 -> 56
56 -> 57
55 -> 58
58 -> 59
59 -> 73
35 -> 74
74 -> 75
0 -> 76
76 -> 77
77 -> 78
78 -> 79
77 -> 80
80 -> 81
77 -> 82
82 -> 83
77 -> 84
84 -> 85
77 -> 86
86 -> 87
87 -> 88
86 -> 89
89 -> 90
90 -> 91
76 -> 92
92 -> 93

0 [label="ClientboundMapItemDataPacket",comment="name: \"ClientboundMapItemDataPacket\", typeName: \"\", id: 0, branchId: 67, recurseId: -1, attributes: 0, notes: \"\""];
1 [label="Map ID",comment="name: \"Map ID\", typeName: \"ActorUniqueID\", id: 1, branchId: 0, recurseId: -1, attributes: 256, notes: \"\""];
2 [label="ActorUniqueID",comment="name: \"ActorUniqueID\", typeName: \"\", id: 2, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
3 [label="Type Flags",comment="name: \"Type Flags\", typeName: \"\", id: 3, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
4 [label="unsigned varint",comment="name: \"unsigned varint\", typeName: \"\", id: 4, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
5 [label="Dimension",comment="name: \"Dimension\", typeName: \"\", id: 5, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
6 [label="byte",comment="name: \"byte\", typeName: \"\", id: 6, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
7 [label="Is Locked Map?",comment="name: \"Is Locked Map?\", typeName: \"\", id: 7, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
8 [label="bool",comment="name: \"bool\", typeName: \"\", id: 8, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
9 [label="Map Origin",comment="name: \"Map Origin\", typeName: \"BlockPos\", id: 9, branchId: 0, recurseId: -1, attributes: 256, notes: \"\""];
10 [label="BlockPos",comment="name: \"BlockPos\", typeName: \"\", id: 10, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
11 [label="Dependency on 'Creation Bit Field'",shape=note,comment="name: \"Dependency on 'Creation Bit Field'\", typeName: \"\", id: 11, branchId: 0, recurseId: -1, attributes: 2, notes: \"\""];
12 [label="if (8)",shape=diamond,comment="name: \"if (8)\", typeName: \"\", id: 12, branchId: 8, recurseId: -1, attributes: 4, notes: \"\""];
13 [label="Map ID List",comment="name: \"Map ID List\", typeName: \"\", id: 13, branchId: 0, recurseId: -1, attributes: 8, notes: \"\""];
14 [label="Array Size",comment="name: \"Array Size\", typeName: \"\", id: 14, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
15 [label="unsigned varint",comment="name: \"unsigned varint\", typeName: \"\", id: 15, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
16 [label="example element",style=dotted,comment="name: \"example element\", typeName: \"\", id: 16, branchId: 0, recurseId: -1, attributes: 16, notes: \"\""];
17 [label="Map ID entry",comment="name: \"Map ID entry\", typeName: \"ActorUniqueID\", id: 17, branchId: 0, recurseId: -1, attributes: 256, notes: \"\""];
18 [label="ActorUniqueID",comment="name: \"ActorUniqueID\", typeName: \"\", id: 18, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
19 [label="Map ID entry",comment="name: \"Map ID entry\", typeName: \"ActorUniqueID\", id: 19, branchId: 0, recurseId: -1, attributes: 256, notes: \"\""];
20 [label="ActorUniqueID",comment="name: \"ActorUniqueID\", typeName: \"\", id: 20, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
21 [label="if (0)",shape=diamond,comment="name: \"if (0)\", typeName: \"\", id: 21, branchId: 0, recurseId: -1, attributes: 4, notes: \"\""];
22 [label="[No Data]",comment="name: \"[No Data]\", typeName: \"\", id: 22, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
23 [label="Dependency on 'DecorationUpdate, TextureUpdate, or Creation Bit Field'",shape=note,comment="name: \"Dependency on 'DecorationUpdate, TextureUpdate, or Creation Bit Field'\", typeName: \"\", id: 23, branchId: 0, recurseId: -1, attributes: 2, notes: \"\""];
24 [label="if (2)",shape=diamond,comment="name: \"if (2)\", typeName: \"\", id: 24, branchId: 2, recurseId: -1, attributes: 4, notes: \"\""];
25 [label="Scale",comment="name: \"Scale\", typeName: \"\", id: 25, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
26 [label="byte",comment="name: \"byte\", typeName: \"\", id: 26, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
27 [label="if (4)",shape=diamond,comment="name: \"if (4)\", typeName: \"\", id: 27, branchId: 4, recurseId: -1, attributes: 4, notes: \"\""];
28 [label="Scale",comment="name: \"Scale\", typeName: \"\", id: 28, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
29 [label="byte",comment="name: \"byte\", typeName: \"\", id: 29, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
30 [label="if (8)",shape=diamond,comment="name: \"if (8)\", typeName: \"\", id: 30, branchId: 8, recurseId: -1, attributes: 4, notes: \"\""];
31 [label="Scale",comment="name: \"Scale\", typeName: \"\", id: 31, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
32 [label="byte",comment="name: \"byte\", typeName: \"\", id: 32, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
33 [label="if (0)",shape=diamond,comment="name: \"if (0)\", typeName: \"\", id: 33, branchId: 0, recurseId: -1, attributes: 4, notes: \"\""];
34 [label="[No Data]",comment="name: \"[No Data]\", typeName: \"\", id: 34, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
35 [label="Dependency on 'DecorationUpdate Bit Field'",shape=note,comment="name: \"Dependency on 'DecorationUpdate Bit Field'\", typeName: \"\", id: 35, branchId: 0, recurseId: -1, attributes: 2, notes: \"\""];
36 [label="if (4)",shape=diamond,comment="name: \"if (4)\", typeName: \"\", id: 36, branchId: 4, recurseId: -1, attributes: 4, notes: \"\""];
37 [label="Actor IDs",comment="name: \"Actor IDs\", typeName: \"\", id: 37, branchId: 0, recurseId: -1, attributes: 8, notes: \"\""];
38 [label="Array Size",comment="name: \"Array Size\", typeName: \"\", id: 38, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
39 [label="unsigned varint",comment="name: \"unsigned varint\", typeName: \"\", id: 39, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
40 [label="example element",style=dotted,comment="name: \"example element\", typeName: \"\", id: 40, branchId: 0, recurseId: -1, attributes: 16, notes: \"\""];
41 [label="MapItemTrackedActor ID",comment="name: \"MapItemTrackedActor ID\", typeName: \"MapItemTrackedActor::UniqueId\", id: 41, branchId: 0, recurseId: -1, attributes: 256, notes: \"\""];
54 [label="MapItemTrackedActor::UniqueId",comment="name: \"MapItemTrackedActor::UniqueId\", typeName: \"\", id: 54, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
55 [label="Decoration List",comment="name: \"Decoration List\", typeName: \"\", id: 55, branchId: 0, recurseId: -1, attributes: 8, notes: \"\""];
56 [label="Array Size",comment="name: \"Array Size\", typeName: \"\", id: 56, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
57 [label="unsigned varint",comment="name: \"unsigned varint\", typeName: \"\", id: 57, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
58 [label="example element",style=dotted,comment="name: \"example element\", typeName: \"\", id: 58, branchId: 0, recurseId: -1, attributes: 16, notes: \"\""];
59 [label="Map Decoration",comment="name: \"Map Decoration\", typeName: \"MapDecoration\", id: 59, branchId: 0, recurseId: -1, attributes: 256, notes: \"\""];
73 [label="MapDecoration",comment="name: \"MapDecoration\", typeName: \"\", id: 73, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
74 [label="if (0)",shape=diamond,comment="name: \"if (0)\", typeName: \"\", id: 74, branchId: 0, recurseId: -1, attributes: 4, notes: \"\""];
75 [label="[No Data]",comment="name: \"[No Data]\", typeName: \"\", id: 75, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
76 [label="Dependency on 'TextureUpdate Bit Field'",shape=note,comment="name: \"Dependency on 'TextureUpdate Bit Field'\", typeName: \"\", id: 76, branchId: 0, recurseId: -1, attributes: 2, notes: \"\""];
77 [label="if (2)",shape=diamond,comment="name: \"if (2)\", typeName: \"\", id: 77, branchId: 2, recurseId: -1, attributes: 4, notes: \"\""];
78 [label="Texture Width",comment="name: \"Texture Width\", typeName: \"\", id: 78, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
79 [label="varint",comment="name: \"varint\", typeName: \"\", id: 79, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
80 [label="Texture Height",comment="name: \"Texture Height\", typeName: \"\", id: 80, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
81 [label="varint",comment="name: \"varint\", typeName: \"\", id: 81, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
82 [label="X-TexCoordinate",comment="name: \"X-TexCoordinate\", typeName: \"\", id: 82, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
83 [label="varint",comment="name: \"varint\", typeName: \"\", id: 83, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
84 [label="Y-TexCoordinate",comment="name: \"Y-TexCoordinate\", typeName: \"\", id: 84, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
85 [label="varint",comment="name: \"varint\", typeName: \"\", id: 85, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
86 [label="Pixels",comment="name: \"Pixels\", typeName: \"\", id: 86, branchId: 0, recurseId: -1, attributes: 8, notes: \"\""];
87 [label="Array Size",comment="name: \"Array Size\", typeName: \"\", id: 87, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
88 [label="unsigned varint",comment="name: \"unsigned varint\", typeName: \"\", id: 88, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
89 [label="example element",style=dotted,comment="name: \"example element\", typeName: \"\", id: 89, branchId: 0, recurseId: -1, attributes: 16, notes: \"\""];
90 [label="Pixel",comment="name: \"Pixel\", typeName: \"\", id: 90, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
91 [label="unsigned varint",comment="name: \"unsigned varint\", typeName: \"\", id: 91, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
92 [label="if (0)",shape=diamond,comment="name: \"if (0)\", typeName: \"\", id: 92, branchId: 0, recurseId: -1, attributes: 4, notes: \"\""];
93 [label="[No Data]",comment="name: \"[No Data]\", typeName: \"\", id: 93, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
{ rank = max;2;4;6;8;10;15;18;20;22;26;29;32;34;39;54;57;73;75;79;81;83;85;88;91;93}

}

```

## 字段

```title='ClientboundMapItemDataPacket'
[map_id][type_flags][dimension][is_locked_map][map_origin][dependency_on_creation_bit_field][dependency_on_decorationupdate_textureupdate_or_creation_bit_field][dependency_on_decorationupdate_bit_field][dependency_on_textureupdate_bit_field]
```

/// html | div.result
//// define
Map ID：[<!-- md:samp ActorUniqueID -->](../types/actoruniqueid.md)

- 特殊类型。protocol.packet.clientboundmapitemdatapacket.map_id.description


////
//// define
Type Flags：<!-- md:samp unsigned varint -->

- 基本类型枚举。protocol.packet.clientboundmapitemdatapacket.type_flags.description枚举值如下：

  |键|值|描述|
  |---|---|---|
  |`Invalid`|`0`|protocol.enum.invalid|
  |`TextureUpdate`|`1 << 1`|protocol.enum.textureupdate|
  |`DecorationUpdate`|`1 << 2`|protocol.enum.decorationupdate|
  |`Creation`|`1 << 3`|protocol.enum.creation|



////
//// define
Dimension：<!-- md:samp byte -->

- 基本类型。protocol.packet.clientboundmapitemdatapacket.dimension.description


////
//// define
Is Locked Map?：<!-- md:samp bool -->

- 基本类型。protocol.packet.clientboundmapitemdatapacket.is_locked_map.description


////
//// define
Map Origin：[<!-- md:samp BlockPos -->](../types/blockpos.md)

- 特殊类型。protocol.packet.clientboundmapitemdatapacket.map_origin.description


////
> 依赖于`Creation Bit Field`

///// tab | `Creation Bit Field`如果为`8`
```title='if (8)'
[map_id_list]
```

////// html | div.result
```title='Map ID List'
[array_size][[example_element]..]
```

/////// html | div.result
//////// define
数组大小：<!-- md:samp unsigned varint -->

- 基本类型。protocol.packet.clientboundmapitemdatapacket.dependency_on_creation_bit_field.if_8.map_id_list.array_size.description


////////
```title='示例元素'
[map_id_entry][map_id_entry]
```

//////// html | div.result
///////// define
Map ID entry：[<!-- md:samp ActorUniqueID -->](../types/actoruniqueid.md)

- 特殊类型。protocol.packet.clientboundmapitemdatapacket.dependency_on_creation_bit_field.if_8.map_id_list.example_element.map_id_entry.description


/////////
///////// define
Map ID entry：[<!-- md:samp ActorUniqueID -->](../types/actoruniqueid.md)

- 特殊类型。protocol.packet.clientboundmapitemdatapacket.dependency_on_creation_bit_field.if_8.map_id_list.example_element.map_id_entry.description


/////////

////////

///////

//////

/////

///// tab | `Creation Bit Field`如果为`0`
////// define
if (0)：<!-- md:samp [No Data] -->

- 无数据


//////

/////
> 依赖于`DecorationUpdate, TextureUpdate, or Creation Bit Field`

///// tab | `DecorationUpdate, TextureUpdate, or Creation Bit Field`如果为`2`
```title='if (2)'
[scale]
```

////// html | div.result
/////// define
Scale：<!-- md:samp byte -->

- 基本类型。protocol.packet.clientboundmapitemdatapacket.dependency_on_decorationupdate_textureupdate_or_creation_bit_field.if_2.scale.description


///////

//////

/////

///// tab | `DecorationUpdate, TextureUpdate, or Creation Bit Field`如果为`4`
```title='if (4)'
[scale]
```

////// html | div.result
/////// define
Scale：<!-- md:samp byte -->

- 基本类型。protocol.packet.clientboundmapitemdatapacket.dependency_on_decorationupdate_textureupdate_or_creation_bit_field.if_4.scale.description


///////

//////

/////

///// tab | `DecorationUpdate, TextureUpdate, or Creation Bit Field`如果为`8`
```title='if (8)'
[scale]
```

////// html | div.result
/////// define
Scale：<!-- md:samp byte -->

- 基本类型。protocol.packet.clientboundmapitemdatapacket.dependency_on_decorationupdate_textureupdate_or_creation_bit_field.if_8.scale.description


///////

//////

/////

///// tab | `DecorationUpdate, TextureUpdate, or Creation Bit Field`如果为`0`
////// define
if (0)：<!-- md:samp [No Data] -->

- 无数据


//////

/////
> 依赖于`DecorationUpdate Bit Field`

///// tab | `DecorationUpdate Bit Field`如果为`4`
```title='if (4)'
[actor_ids][decoration_list]
```

////// html | div.result
```title='Actor IDs'
[array_size][[example_element]..]
```

/////// html | div.result
//////// define
数组大小：<!-- md:samp unsigned varint -->

- 基本类型。protocol.packet.clientboundmapitemdatapacket.dependency_on_decorationupdate_bit_field.if_4.actor_ids.array_size.description


////////
```title='示例元素'
[mapitemtrackedactor_id]
```

//////// html | div.result
///////// define
MapItemTrackedActor ID：[<!-- md:samp MapItemTrackedActor::UniqueId -->](../types/mapitemtrackedactor__uniqueid.md)

- 特殊类型。protocol.packet.clientboundmapitemdatapacket.dependency_on_decorationupdate_bit_field.if_4.actor_ids.example_element.mapitemtrackedactor_id.description


/////////

////////

///////
```title='Decoration List'
[array_size][[example_element]..]
```

/////// html | div.result
//////// define
数组大小：<!-- md:samp unsigned varint -->

- 基本类型。protocol.packet.clientboundmapitemdatapacket.dependency_on_decorationupdate_bit_field.if_4.decoration_list.array_size.description


////////
```title='示例元素'
[map_decoration]
```

//////// html | div.result
///////// define
Map Decoration：[<!-- md:samp MapDecoration -->](../types/mapdecoration.md)

- 特殊类型。protocol.packet.clientboundmapitemdatapacket.dependency_on_decorationupdate_bit_field.if_4.decoration_list.example_element.map_decoration.description


/////////

////////

///////

//////

/////

///// tab | `DecorationUpdate Bit Field`如果为`0`
////// define
if (0)：<!-- md:samp [No Data] -->

- 无数据


//////

/////
> 依赖于`TextureUpdate Bit Field`

///// tab | `TextureUpdate Bit Field`如果为`2`
```title='if (2)'
[texture_width][texture_height][x-texcoordinate][y-texcoordinate][pixels]
```

////// html | div.result
/////// define
Texture Width：<!-- md:samp varint -->

- 基本类型。protocol.packet.clientboundmapitemdatapacket.dependency_on_textureupdate_bit_field.if_2.texture_width.description


///////
/////// define
Texture Height：<!-- md:samp varint -->

- 基本类型。protocol.packet.clientboundmapitemdatapacket.dependency_on_textureupdate_bit_field.if_2.texture_height.description


///////
/////// define
X-TexCoordinate：<!-- md:samp varint -->

- 基本类型。protocol.packet.clientboundmapitemdatapacket.dependency_on_textureupdate_bit_field.if_2.x-texcoordinate.description


///////
/////// define
Y-TexCoordinate：<!-- md:samp varint -->

- 基本类型。protocol.packet.clientboundmapitemdatapacket.dependency_on_textureupdate_bit_field.if_2.y-texcoordinate.description


///////
```title='Pixels'
[array_size][[example_element]..]
```

/////// html | div.result
//////// define
数组大小：<!-- md:samp unsigned varint -->

- 基本类型。protocol.packet.clientboundmapitemdatapacket.dependency_on_textureupdate_bit_field.if_2.pixels.array_size.description


////////
```title='示例元素'
[pixel]
```

//////// html | div.result
///////// define
Pixel：<!-- md:samp unsigned varint -->

- 基本类型。protocol.packet.clientboundmapitemdatapacket.dependency_on_textureupdate_bit_field.if_2.pixels.example_element.pixel.description


/////////

////////

///////

//////

/////

///// tab | `TextureUpdate Bit Field`如果为`0`
////// define
if (0)：<!-- md:samp [No Data] -->

- 无数据


//////

/////

///

