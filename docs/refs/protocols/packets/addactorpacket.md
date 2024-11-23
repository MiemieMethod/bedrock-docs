# <!-- md:samp AddActorPacket -->

> 文档版本：r/21_u4<br/>协议版本：748

<!-- md:samp AddActorPacket -->数据包，数字ID是`13`。该数据包用于protocol.packet.addactorpacket.description

## 结构

```viz
digraph "AddActorPacket" {
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
0 -> 13
13 -> 14
0 -> 15
15 -> 16
0 -> 17
17 -> 18
18 -> 19
17 -> 20
20 -> 21
21 -> 22
20 -> 23
23 -> 24
20 -> 25
25 -> 26
20 -> 27
27 -> 28
0 -> 29
29 -> 30
0 -> 31
31 -> 32
0 -> 33
33 -> 34
34 -> 35
33 -> 36
36 -> 37
37 -> 38

0 [label="AddActorPacket",comment="name: \"AddActorPacket\", typeName: \"\", id: 0, branchId: 13, recurseId: -1, attributes: 0, notes: \"\""];
1 [label="Target Actor ID",comment="name: \"Target Actor ID\", typeName: \"ActorUniqueID\", id: 1, branchId: 0, recurseId: -1, attributes: 256, notes: \"\""];
2 [label="ActorUniqueID",comment="name: \"ActorUniqueID\", typeName: \"\", id: 2, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
3 [label="Target Runtime ID",comment="name: \"Target Runtime ID\", typeName: \"ActorRuntimeID\", id: 3, branchId: 0, recurseId: -1, attributes: 256, notes: \"\""];
4 [label="ActorRuntimeID",comment="name: \"ActorRuntimeID\", typeName: \"\", id: 4, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
5 [label="Actor Type",comment="name: \"Actor Type\", typeName: \"\", id: 5, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
6 [label="string",comment="name: \"string\", typeName: \"\", id: 6, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
7 [label="Position",comment="name: \"Position\", typeName: \"Vec3\", id: 7, branchId: 0, recurseId: -1, attributes: 256, notes: \"\""];
8 [label="Vec3",comment="name: \"Vec3\", typeName: \"\", id: 8, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
9 [label="Velocity",comment="name: \"Velocity\", typeName: \"Vec3\", id: 9, branchId: 0, recurseId: -1, attributes: 256, notes: \"\""];
10 [label="Vec3",comment="name: \"Vec3\", typeName: \"\", id: 10, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
11 [label="Rotation",comment="name: \"Rotation\", typeName: \"Vec2\", id: 11, branchId: 0, recurseId: -1, attributes: 256, notes: \"\""];
12 [label="Vec2",comment="name: \"Vec2\", typeName: \"\", id: 12, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
13 [label="Y Head Rotation",comment="name: \"Y Head Rotation\", typeName: \"\", id: 13, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
14 [label="float",comment="name: \"float\", typeName: \"\", id: 14, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
15 [label="Y Body Rotation",comment="name: \"Y Body Rotation\", typeName: \"\", id: 15, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
16 [label="float",comment="name: \"float\", typeName: \"\", id: 16, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
17 [label="Attributes List",comment="name: \"Attributes List\", typeName: \"\", id: 17, branchId: 0, recurseId: -1, attributes: 8, notes: \"\""];
18 [label="Array Size",comment="name: \"Array Size\", typeName: \"\", id: 18, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
19 [label="unsigned varint",comment="name: \"unsigned varint\", typeName: \"\", id: 19, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
20 [label="example element",style=dotted,comment="name: \"example element\", typeName: \"\", id: 20, branchId: 0, recurseId: -1, attributes: 16, notes: \"\""];
21 [label="Attribute Name",comment="name: \"Attribute Name\", typeName: \"\", id: 21, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
22 [label="string",comment="name: \"string\", typeName: \"\", id: 22, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
23 [label="Min Value",comment="name: \"Min Value\", typeName: \"\", id: 23, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
24 [label="float",comment="name: \"float\", typeName: \"\", id: 24, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
25 [label="Current Value",comment="name: \"Current Value\", typeName: \"\", id: 25, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
26 [label="float",comment="name: \"float\", typeName: \"\", id: 26, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
27 [label="Max Value",comment="name: \"Max Value\", typeName: \"\", id: 27, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
28 [label="float",comment="name: \"float\", typeName: \"\", id: 28, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
29 [label="Actor Data",comment="name: \"Actor Data\", typeName: \"std::vector<class std::unique_ptr<class DataItem,struct std::default_delete<class DataItem> >,class std::allocator<class std::unique_ptr<class DataItem,struct std::default_delete<class DataItem> > > >\", id: 29, branchId: 0, recurseId: -1, attributes: 256, notes: \"\""];
30 [label="std::vector<class std::unique_ptr<class DataItem,struct std::default_delete<class DataItem> >,class std::allocator<class std::unique_ptr<class DataItem,struct std::default_delete<class DataItem> > > >",comment="name: \"std::vector<class std::unique_ptr<class DataItem,struct std::default_delete<class DataItem> >,class std::allocator<class std::unique_ptr<class DataItem,struct std::default_delete<class DataItem> > > >\", typeName: \"\", id: 30, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
31 [label="Synched Properties",comment="name: \"Synched Properties\", typeName: \"PropertySyncData\", id: 31, branchId: 0, recurseId: -1, attributes: 256, notes: \"\""];
32 [label="PropertySyncData",comment="name: \"PropertySyncData\", typeName: \"\", id: 32, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
33 [label="Actor Links",comment="name: \"Actor Links\", typeName: \"\", id: 33, branchId: 0, recurseId: -1, attributes: 8, notes: \"\""];
34 [label="Array Size",comment="name: \"Array Size\", typeName: \"\", id: 34, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
35 [label="unsigned varint",comment="name: \"unsigned varint\", typeName: \"\", id: 35, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
36 [label="example element",style=dotted,comment="name: \"example element\", typeName: \"\", id: 36, branchId: 0, recurseId: -1, attributes: 16, notes: \"\""];
37 [label="Link",comment="name: \"Link\", typeName: \"ActorLink\", id: 37, branchId: 0, recurseId: -1, attributes: 256, notes: \"\""];
38 [label="ActorLink",comment="name: \"ActorLink\", typeName: \"\", id: 38, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
{ rank = max;2;4;6;8;10;12;14;16;19;22;24;26;28;30;32;35;38}

}

```

## 字段

```title='AddActorPacket'
[target_actor_id][target_runtime_id][actor_type][position][velocity][rotation][y_head_rotation][y_body_rotation][attributes_list][actor_data][synched_properties][actor_links]
```

/// html | div.result
//// define
Target Actor ID：[<!-- md:samp ActorUniqueID -->](../types/actoruniqueid.md)

- 特殊类型。protocol.packet.addactorpacket.target_actor_id.description


////
//// define
Target Runtime ID：[<!-- md:samp ActorRuntimeID -->](../types/actorruntimeid.md)

- 特殊类型。protocol.packet.addactorpacket.target_runtime_id.description


////
//// define
Actor Type：[<!-- md:samp string -->](../types/string.md)

- 特殊类型。protocol.packet.addactorpacket.actor_type.description


////
//// define
Position：[<!-- md:samp Vec3 -->](../types/vec3.md)

- 特殊类型。protocol.packet.addactorpacket.position.description


////
//// define
Velocity：[<!-- md:samp Vec3 -->](../types/vec3.md)

- 特殊类型。protocol.packet.addactorpacket.velocity.description


////
//// define
Rotation：[<!-- md:samp Vec2 -->](../types/vec2.md)

- 特殊类型。protocol.packet.addactorpacket.rotation.description


////
//// define
Y Head Rotation：<!-- md:samp float -->

- 基本类型。protocol.packet.addactorpacket.y_head_rotation.description


////
//// define
Y Body Rotation：<!-- md:samp float -->

- 基本类型。protocol.packet.addactorpacket.y_body_rotation.description


////
```title='Attributes List'
[array_size][[example_element]..]
```

//// html | div.result
///// define
数组大小：<!-- md:samp unsigned varint -->

- 基本类型。protocol.packet.addactorpacket.attributes_list.array_size.description


/////
```title='示例元素'
[attribute_name][min_value][current_value][max_value]
```

///// html | div.result
////// define
Attribute Name：[<!-- md:samp string -->](../types/string.md)

- 特殊类型。protocol.packet.addactorpacket.attributes_list.example_element.attribute_name.description


//////
////// define
Min Value：<!-- md:samp float -->

- 基本类型。protocol.packet.addactorpacket.attributes_list.example_element.min_value.description


//////
////// define
Current Value：<!-- md:samp float -->

- 基本类型。protocol.packet.addactorpacket.attributes_list.example_element.current_value.description


//////
////// define
Max Value：<!-- md:samp float -->

- 基本类型。protocol.packet.addactorpacket.attributes_list.example_element.max_value.description


//////

/////

////
//// define
Actor Data：[<!-- md:samp std::vector&lt;std::unique_ptr&lt;DataItem&gt;&gt; -->](../types/std__vector_class_std__unique_ptr_class_dataitem,struct_std__default_delete_class_dataitem___,class_std__allocator_class_std__u.md)

- 特殊类型。protocol.packet.addactorpacket.actor_data.description


////
//// define
Synched Properties：[<!-- md:samp PropertySyncData -->](../types/propertysyncdata.md)

- 特殊类型。protocol.packet.addactorpacket.synched_properties.description


////
```title='Actor Links'
[array_size][[example_element]..]
```

//// html | div.result
///// define
数组大小：<!-- md:samp unsigned varint -->

- 基本类型。protocol.packet.addactorpacket.actor_links.array_size.description


/////
```title='示例元素'
[link]
```

///// html | div.result
////// define
Link：[<!-- md:samp ActorLink -->](../types/actorlink.md)

- 特殊类型。protocol.packet.addactorpacket.actor_links.example_element.link.description


//////

/////

////

///

