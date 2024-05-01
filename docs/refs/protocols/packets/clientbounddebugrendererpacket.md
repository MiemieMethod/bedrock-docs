# <!-- md:samp ClientboundDebugRendererPacket -->

> 文档版本：r/20_u8<br/>协议版本：671

<!-- md:samp ClientboundDebugRendererPacket -->数据包，数字ID是`164`。该数据包用于protocol.packet.clientbounddebugrendererpacket.description

## 结构

```viz
digraph "ClientboundDebugRendererPacket" {
rankdir = LR
0
0 -> 1
1 -> 2
0 -> 3
3 -> 4
4 -> 5
3 -> 6
6 -> 7
3 -> 8
8 -> 9
9 -> 10
8 -> 11
11 -> 12
8 -> 13
13 -> 14
8 -> 15
15 -> 16
8 -> 17
17 -> 18
8 -> 19
19 -> 20
8 -> 21
21 -> 22

0 [label="ClientboundDebugRendererPacket",comment="name: \"ClientboundDebugRendererPacket\", typeName: \"\", id: 0, branchId: 164, recurseId: -1, attributes: 0, notes: \"\""];
1 [label="Debug Marker Type",comment="name: \"Debug Marker Type\", typeName: \"\", id: 1, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
2 [label="unsigned int",comment="name: \"unsigned int\", typeName: \"\", id: 2, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
3 [label="Dependency on 'Debug Marker Type'",shape=note,comment="name: \"Dependency on 'Debug Marker Type'\", typeName: \"\", id: 3, branchId: 0, recurseId: -1, attributes: 2, notes: \"\""];
4 [label="if (0)",shape=diamond,comment="name: \"if (0)\", typeName: \"\", id: 4, branchId: 0, recurseId: -1, attributes: 4, notes: \"\""];
5 [label="[No Data]",comment="name: \"[No Data]\", typeName: \"\", id: 5, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
6 [label="if (1)",shape=diamond,comment="name: \"if (1)\", typeName: \"\", id: 6, branchId: 1, recurseId: -1, attributes: 4, notes: \"\""];
7 [label="[No Data]",comment="name: \"[No Data]\", typeName: \"\", id: 7, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
8 [label="if (2)",shape=diamond,comment="name: \"if (2)\", typeName: \"\", id: 8, branchId: 2, recurseId: -1, attributes: 4, notes: \"\""];
9 [label="Debug Marker Text",comment="name: \"Debug Marker Text\", typeName: \"\", id: 9, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
10 [label="string",comment="name: \"string\", typeName: \"\", id: 10, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
11 [label="Debug Marker Position",comment="name: \"Debug Marker Position\", typeName: \"Vec3\", id: 11, branchId: 0, recurseId: -1, attributes: 256, notes: \"\""];
12 [label="Vec3",comment="name: \"Vec3\", typeName: \"\", id: 12, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
13 [label="Debug Marker Color red",comment="name: \"Debug Marker Color red\", typeName: \"\", id: 13, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
14 [label="float",comment="name: \"float\", typeName: \"\", id: 14, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
15 [label="Debug Marker Color green",comment="name: \"Debug Marker Color green\", typeName: \"\", id: 15, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
16 [label="float",comment="name: \"float\", typeName: \"\", id: 16, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
17 [label="Debug Marker Color blue",comment="name: \"Debug Marker Color blue\", typeName: \"\", id: 17, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
18 [label="float",comment="name: \"float\", typeName: \"\", id: 18, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
19 [label="Debug Marker Color alpha",comment="name: \"Debug Marker Color alpha\", typeName: \"\", id: 19, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
20 [label="float",comment="name: \"float\", typeName: \"\", id: 20, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
21 [label="Debug Marker Duration Milliseconds",comment="name: \"Debug Marker Duration Milliseconds\", typeName: \"\", id: 21, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
22 [label="unsigned int64",comment="name: \"unsigned int64\", typeName: \"\", id: 22, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
{ rank = max;2;5;7;10;12;14;16;18;20;22}

}

```

## 字段

```title='ClientboundDebugRendererPacket'
[debug_marker_type][dependency_on_debug_marker_type]
```

/// html | div.result
//// define
Debug Marker Type：<!-- md:samp unsigned int -->

- 基本类型枚举。protocol.packet.clientbounddebugrendererpacket.debug_marker_type.description枚举值如下：

  |键|值|描述|
  |---|---|---|
  |`Invalid`|`0`|protocol.enum.invalid|
  |`ClearDebugMarkers`|`1`|protocol.enum.cleardebugmarkers|
  |`AddDebugMarkerCube`|`2`|protocol.enum.adddebugmarkercube|



////
> 依赖于`Debug Marker Type`

///// tab | `Debug Marker Type`如果为`0`
////// define
if (0)：<!-- md:samp [No Data] -->

- 无数据


//////

/////

///// tab | `Debug Marker Type`如果为`1`
////// define
if (1)：<!-- md:samp [No Data] -->

- 无数据


//////

/////

///// tab | `Debug Marker Type`如果为`2`
```title='if (2)'
[debug_marker_text][debug_marker_position][debug_marker_color_red][debug_marker_color_green][debug_marker_color_blue][debug_marker_color_alpha][debug_marker_duration_milliseconds]
```

////// html | div.result
/////// define
Debug Marker Text：[<!-- md:samp string -->](../types/string.md)

- 特殊类型。protocol.packet.clientbounddebugrendererpacket.dependency_on_debug_marker_type.if_2.debug_marker_text.description


///////
/////// define
Debug Marker Position：[<!-- md:samp Vec3 -->](../types/vec3.md)

- 特殊类型。protocol.packet.clientbounddebugrendererpacket.dependency_on_debug_marker_type.if_2.debug_marker_position.description


///////
/////// define
Debug Marker Color red：<!-- md:samp float -->

- 基本类型。protocol.packet.clientbounddebugrendererpacket.dependency_on_debug_marker_type.if_2.debug_marker_color_red.description


///////
/////// define
Debug Marker Color green：<!-- md:samp float -->

- 基本类型。protocol.packet.clientbounddebugrendererpacket.dependency_on_debug_marker_type.if_2.debug_marker_color_green.description


///////
/////// define
Debug Marker Color blue：<!-- md:samp float -->

- 基本类型。protocol.packet.clientbounddebugrendererpacket.dependency_on_debug_marker_type.if_2.debug_marker_color_blue.description


///////
/////// define
Debug Marker Color alpha：<!-- md:samp float -->

- 基本类型。protocol.packet.clientbounddebugrendererpacket.dependency_on_debug_marker_type.if_2.debug_marker_color_alpha.description


///////
/////// define
Debug Marker Duration Milliseconds：<!-- md:samp unsigned int64 -->

- 基本类型。protocol.packet.clientbounddebugrendererpacket.dependency_on_debug_marker_type.if_2.debug_marker_duration_milliseconds.description


///////

//////

/////

///

