# <!-- md:samp MapInfoRequestPacket -->

> 文档版本：r/21_u4<br/>协议版本：748

<!-- md:samp MapInfoRequestPacket -->数据包，数字ID是`68`。该数据包用于protocol.packet.mapinforequestpacket.description

## 结构

```viz
digraph "MapInfoRequestPacket" {
rankdir = LR
0
0 -> 1
1 -> 2
0 -> 3
3 -> 4
4 -> 5
3 -> 6
6 -> 7
7 -> 8
8 -> 9
7 -> 10
10 -> 11
11 -> 12
10 -> 13
13 -> 14

0 [label="MapInfoRequestPacket",comment="name: \"MapInfoRequestPacket\", typeName: \"\", id: 0, branchId: 68, recurseId: -1, attributes: 0, notes: \"\""];
1 [label="Map Unique ID",comment="name: \"Map Unique ID\", typeName: \"ActorUniqueID\", id: 1, branchId: 0, recurseId: -1, attributes: 256, notes: \"\""];
2 [label="ActorUniqueID",comment="name: \"ActorUniqueID\", typeName: \"\", id: 2, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
3 [label="Dependency on 'mClientPixels.size() > 0 ?'",shape=note,comment="name: \"Dependency on 'mClientPixels.size() > 0 ?'\", typeName: \"\", id: 3, branchId: 0, recurseId: -1, attributes: 2, notes: \"\""];
4 [label="if (0)",shape=diamond,comment="name: \"if (0)\", typeName: \"\", id: 4, branchId: 0, recurseId: -1, attributes: 4, notes: \"\""];
5 [label="[No Data]",comment="name: \"[No Data]\", typeName: \"\", id: 5, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
6 [label="if (1)",shape=diamond,comment="name: \"if (1)\", typeName: \"\", id: 6, branchId: 1, recurseId: -1, attributes: 4, notes: \"\""];
7 [label="Client Pixels List",comment="name: \"Client Pixels List\", typeName: \"\", id: 7, branchId: 0, recurseId: -1, attributes: 8, notes: \"These are sent from the client to tell the Server map about terrain pixels it doesn't know about\""];
8 [label="Client Pixels List Size",comment="name: \"Client Pixels List Size\", typeName: \"\", id: 8, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
9 [label="unsigned int",comment="name: \"unsigned int\", typeName: \"\", id: 9, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
10 [label="example element",style=dotted,comment="name: \"example element\", typeName: \"\", id: 10, branchId: 0, recurseId: -1, attributes: 16, notes: \"\""];
11 [label="pixel",comment="name: \"pixel\", typeName: \"\", id: 11, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
12 [label="unsigned int",comment="name: \"unsigned int\", typeName: \"\", id: 12, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
13 [label="index",comment="name: \"index\", typeName: \"\", id: 13, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
14 [label="unsigned short",comment="name: \"unsigned short\", typeName: \"\", id: 14, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
{ rank = max;2;5;9;12;14}

}

```

## 字段

```title='MapInfoRequestPacket'
[map_unique_id][dependency_on_mclientpixels.size()_g_0]
```

/// html | div.result
//// define
Map Unique ID：[<!-- md:samp ActorUniqueID -->](../types/actoruniqueid.md)

- 特殊类型。protocol.packet.mapinforequestpacket.map_unique_id.description


////
> 依赖于`mClientPixels.size() > 0 ?`

///// tab | `mClientPixels.size() > 0 ?`如果为`0`
////// define
if (0)：<!-- md:samp [No Data] -->

- 无数据


//////

/////

///// tab | `mClientPixels.size() > 0 ?`如果为`1`
```title='if (1)'
[client_pixels_list]
```

////// html | div.result
```title='Client Pixels List'
[client_pixels_list_size][[example_element]..]
```

/////// html | div.result
//////// define
Client Pixels List Size：<!-- md:samp unsigned int -->

- 基本类型。protocol.packet.mapinforequestpacket.dependency_on_mclientpixels.size()_g_0.if_1.client_pixels_list.client_pixels_list_size.description


////////
```title='示例元素'
[pixel][index]
```

//////// html | div.result
///////// define
pixel：<!-- md:samp unsigned int -->

- 基本类型。protocol.packet.mapinforequestpacket.dependency_on_mclientpixels.size()_g_0.if_1.client_pixels_list.example_element.pixel.description


/////////
///////// define
index：<!-- md:samp unsigned short -->

- 基本类型。protocol.packet.mapinforequestpacket.dependency_on_mclientpixels.size()_g_0.if_1.client_pixels_list.example_element.index.description


/////////

////////

///////

//////

/////

///

