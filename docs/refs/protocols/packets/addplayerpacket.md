# <!-- md:samp AddPlayerPacket -->

> 文档版本：r/21_u3<br/>协议版本：729

<!-- md:samp AddPlayerPacket -->数据包，数字ID是`12`。该数据包用于protocol.packet.addplayerpacket.description

## 结构

```viz
digraph "AddPlayerPacket" {
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
17 -> 45
0 -> 46
46 -> 47
0 -> 48
48 -> 49
49 -> 50
50 -> 56
48 -> 57
57 -> 58
58 -> 59
0 -> 60
60 -> 78
0 -> 79
79 -> 104
0 -> 105
105 -> 106
106 -> 107
105 -> 108
108 -> 109
109 -> 123
0 -> 124
124 -> 125
0 -> 126
126 -> 127

0 [label="AddPlayerPacket",comment="name: \"AddPlayerPacket\", typeName: \"\", id: 0, branchId: 12, recurseId: -1, attributes: 0, notes: \"\""];
1 [label="UUID",comment="name: \"UUID\", typeName: \"mce::UUID\", id: 1, branchId: 0, recurseId: -1, attributes: 256, notes: \"\""];
2 [label="mce::UUID",comment="name: \"mce::UUID\", typeName: \"\", id: 2, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
3 [label="Player Name",comment="name: \"Player Name\", typeName: \"\", id: 3, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
4 [label="string",comment="name: \"string\", typeName: \"\", id: 4, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
5 [label="Target Runtime ID",comment="name: \"Target Runtime ID\", typeName: \"ActorRuntimeID\", id: 5, branchId: 0, recurseId: -1, attributes: 256, notes: \"\""];
6 [label="ActorRuntimeID",comment="name: \"ActorRuntimeID\", typeName: \"\", id: 6, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
7 [label="Platform Chat Id",comment="name: \"Platform Chat Id\", typeName: \"\", id: 7, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
8 [label="string",comment="name: \"string\", typeName: \"\", id: 8, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
9 [label="Position",comment="name: \"Position\", typeName: \"Vec3\", id: 9, branchId: 0, recurseId: -1, attributes: 256, notes: \"\""];
10 [label="Vec3",comment="name: \"Vec3\", typeName: \"\", id: 10, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
11 [label="Velocity",comment="name: \"Velocity\", typeName: \"Vec3\", id: 11, branchId: 0, recurseId: -1, attributes: 256, notes: \"\""];
12 [label="Vec3",comment="name: \"Vec3\", typeName: \"\", id: 12, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
13 [label="Rotation",comment="name: \"Rotation\", typeName: \"Vec2\", id: 13, branchId: 0, recurseId: -1, attributes: 256, notes: \"\""];
14 [label="Vec2",comment="name: \"Vec2\", typeName: \"\", id: 14, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
15 [label="Y-Head Rotation",comment="name: \"Y-Head Rotation\", typeName: \"\", id: 15, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
16 [label="float",comment="name: \"float\", typeName: \"\", id: 16, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
17 [label="Carried Item",comment="name: \"Carried Item\", typeName: \"NetworkItemStackDescriptor\", id: 17, branchId: 0, recurseId: -1, attributes: 256, notes: \"\""];
45 [label="NetworkItemStackDescriptor",comment="name: \"NetworkItemStackDescriptor\", typeName: \"\", id: 45, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
46 [label="Player Game Type",comment="name: \"Player Game Type\", typeName: \"\", id: 46, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
47 [label="varint",comment="name: \"varint\", typeName: \"\", id: 47, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
48 [label="Dependency on 'SynchedActorDataEntityWrapper exist?'",shape=note,comment="name: \"Dependency on 'SynchedActorDataEntityWrapper exist?'\", typeName: \"\", id: 48, branchId: 0, recurseId: -1, attributes: 2, notes: \"\""];
49 [label="if (0)",shape=diamond,comment="name: \"if (0)\", typeName: \"\", id: 49, branchId: 0, recurseId: -1, attributes: 4, notes: \"\""];
50 [label="Unpack",comment="name: \"Unpack\", typeName: \"std::vector<class std::unique_ptr<class DataItem,struct std::default_delete<class DataItem> >,class std::allocator<class std::unique_ptr<class DataItem,struct std::default_delete<class DataItem> > > >\", id: 50, branchId: 0, recurseId: -1, attributes: 256, notes: \"std::vector<std::unique_ptr<DataItem>>\""];
56 [label="std::vector<class std::unique_ptr<class DataItem,struct std::default_delete<class DataItem> >,class std::allocator<class std::unique_ptr<class DataItem,struct std::default_delete<class DataItem> > > >",comment="name: \"std::vector<class std::unique_ptr<class DataItem,struct std::default_delete<class DataItem> >,class std::allocator<class std::unique_ptr<class DataItem,struct std::default_delete<class DataItem> > > >\", typeName: \"\", id: 56, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
57 [label="if (1)",shape=diamond,comment="name: \"if (1)\", typeName: \"\", id: 57, branchId: 1, recurseId: -1, attributes: 4, notes: \"\""];
58 [label="Entity Data PackAll",comment="name: \"Entity Data PackAll\", typeName: \"std::vector<class std::unique_ptr<class DataItem,struct std::default_delete<class DataItem> >,class std::allocator<class std::unique_ptr<class DataItem,struct std::default_delete<class DataItem> > > >\", id: 58, branchId: 0, recurseId: -1, attributes: 256, notes: \"std::vector<std::unique_ptr<DataItem>>\""];
59 [label="std::vector<class std::unique_ptr<class DataItem,struct std::default_delete<class DataItem> >,class std::allocator<class std::unique_ptr<class DataItem,struct std::default_delete<class DataItem> > > >",comment="name: \"std::vector<class std::unique_ptr<class DataItem,struct std::default_delete<class DataItem> >,class std::allocator<class std::unique_ptr<class DataItem,struct std::default_delete<class DataItem> > > >\", typeName: \"\", id: 59, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
60 [label="Synched Properties",comment="name: \"Synched Properties\", typeName: \"PropertySyncData\", id: 60, branchId: 0, recurseId: -1, attributes: 256, notes: \"\""];
78 [label="PropertySyncData",comment="name: \"PropertySyncData\", typeName: \"\", id: 78, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
79 [label="AbilitiesData",comment="name: \"AbilitiesData\", typeName: \"SerializedAbilitiesData\", id: 79, branchId: 0, recurseId: -1, attributes: 256, notes: \"\""];
104 [label="SerializedAbilitiesData",comment="name: \"SerializedAbilitiesData\", typeName: \"\", id: 104, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
105 [label="Actor Links",comment="name: \"Actor Links\", typeName: \"\", id: 105, branchId: 0, recurseId: -1, attributes: 8, notes: \"\""];
106 [label="Array Size",comment="name: \"Array Size\", typeName: \"\", id: 106, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
107 [label="unsigned varint",comment="name: \"unsigned varint\", typeName: \"\", id: 107, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
108 [label="example element",style=dotted,comment="name: \"example element\", typeName: \"\", id: 108, branchId: 0, recurseId: -1, attributes: 16, notes: \"\""];
109 [label="Link",comment="name: \"Link\", typeName: \"ActorLink\", id: 109, branchId: 0, recurseId: -1, attributes: 256, notes: \"\""];
123 [label="ActorLink",comment="name: \"ActorLink\", typeName: \"\", id: 123, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
124 [label="Device Id",comment="name: \"Device Id\", typeName: \"\", id: 124, branchId: 0, recurseId: -1, attributes: 0, notes: \"A unique device id obtained from the connection request.\""];
125 [label="string",comment="name: \"string\", typeName: \"\", id: 125, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
126 [label="Build Platform",comment="name: \"Build Platform\", typeName: \"\", id: 126, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
127 [label="int",comment="name: \"int\", typeName: \"\", id: 127, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
{ rank = max;2;4;6;8;10;12;14;16;45;47;56;59;78;104;107;123;125;127}

}

```

## 字段

```title='AddPlayerPacket'
[uuid][player_name][target_runtime_id][platform_chat_id][position][velocity][rotation][y-head_rotation][carried_item][player_game_type][dependency_on_synchedactordataentitywrapper_exist][synched_properties][abilitiesdata][actor_links][device_id][build_platform]
```

/// html | div.result
//// define
UUID：[<!-- md:samp mce::UUID -->](../types/mce__uuid.md)

- 特殊类型。protocol.packet.addplayerpacket.uuid.description


////
//// define
Player Name：[<!-- md:samp string -->](../types/string.md)

- 特殊类型。protocol.packet.addplayerpacket.player_name.description


////
//// define
Target Runtime ID：[<!-- md:samp ActorRuntimeID -->](../types/actorruntimeid.md)

- 特殊类型。protocol.packet.addplayerpacket.target_runtime_id.description


////
//// define
Platform Chat Id：[<!-- md:samp string -->](../types/string.md)

- 特殊类型。protocol.packet.addplayerpacket.platform_chat_id.description


////
//// define
Position：[<!-- md:samp Vec3 -->](../types/vec3.md)

- 特殊类型。protocol.packet.addplayerpacket.position.description


////
//// define
Velocity：[<!-- md:samp Vec3 -->](../types/vec3.md)

- 特殊类型。protocol.packet.addplayerpacket.velocity.description


////
//// define
Rotation：[<!-- md:samp Vec2 -->](../types/vec2.md)

- 特殊类型。protocol.packet.addplayerpacket.rotation.description


////
//// define
Y-Head Rotation：<!-- md:samp float -->

- 基本类型。protocol.packet.addplayerpacket.y-head_rotation.description


////
//// define
Carried Item：[<!-- md:samp NetworkItemStackDescriptor -->](../types/networkitemstackdescriptor.md)

- 特殊类型。protocol.packet.addplayerpacket.carried_item.description


////
//// define
Player Game Type：<!-- md:samp varint -->

- 基本类型枚举。protocol.packet.addplayerpacket.player_game_type.description枚举值如下：

  |键|值|描述|
  |---|---|---|
  |`Undefined`|`-1`|protocol.enum.undefined|
  |`Survival`|`0`|protocol.enum.survival|
  |`Creative`|`1`|protocol.enum.creative|
  |`Adventure`|`2`|protocol.enum.adventure|
  |`Default`|`5`|protocol.enum.default|
  |`Spectator`|`6`|protocol.enum.spectator|
  |`WorldDefault`|`Survival`|protocol.enum.worlddefault|



////
> 依赖于`SynchedActorDataEntityWrapper exist?`

///// tab | `SynchedActorDataEntityWrapper exist?`如果为`0`
```title='if (0)'
[unpack]
```

////// html | div.result
/////// define
Unpack：[<!-- md:samp std::vector&lt;std::unique_ptr&lt;DataItem&gt;&gt; -->](../types/std__vector_class_std__unique_ptr_class_dataitem,struct_std__default_delete_class_dataitem___,class_std__allocator_class_std__u.md)

- 特殊类型。protocol.packet.addplayerpacket.dependency_on_synchedactordataentitywrapper_exist.if_0.unpack.descriptionstd::vector<std::unique_ptr<DataItem>>


///////

//////

/////

///// tab | `SynchedActorDataEntityWrapper exist?`如果为`1`
```title='if (1)'
[entity_data_packall]
```

////// html | div.result
/////// define
Entity Data PackAll：[<!-- md:samp std::vector&lt;std::unique_ptr&lt;DataItem&gt;&gt; -->](../types/std__vector_class_std__unique_ptr_class_dataitem,struct_std__default_delete_class_dataitem___,class_std__allocator_class_std__u.md)

- 特殊类型。protocol.packet.addplayerpacket.dependency_on_synchedactordataentitywrapper_exist.if_1.entity_data_packall.descriptionstd::vector<std::unique_ptr<DataItem>>


///////

//////

/////
//// define
Synched Properties：[<!-- md:samp PropertySyncData -->](../types/propertysyncdata.md)

- 特殊类型。protocol.packet.addplayerpacket.synched_properties.description


////
//// define
AbilitiesData：[<!-- md:samp SerializedAbilitiesData -->](../types/serializedabilitiesdata.md)

- 特殊类型。protocol.packet.addplayerpacket.abilitiesdata.description


////
```title='Actor Links'
[array_size][[example_element]..]
```

//// html | div.result
///// define
数组大小：<!-- md:samp unsigned varint -->

- 基本类型。protocol.packet.addplayerpacket.actor_links.array_size.description


/////
```title='示例元素'
[link]
```

///// html | div.result
////// define
Link：[<!-- md:samp ActorLink -->](../types/actorlink.md)

- 特殊类型。protocol.packet.addplayerpacket.actor_links.example_element.link.description


//////

/////

////
//// define
Device Id：[<!-- md:samp string -->](../types/string.md)

- 特殊类型。protocol.packet.addplayerpacket.device_id.descriptionA unique device 'id' obtained from the connection request.


////
//// define
Build Platform：<!-- md:samp int -->

- 基本类型枚举。protocol.packet.addplayerpacket.build_platform.description枚举值如下：

  |键|值|描述|
  |---|---|---|
  |`Google`|`1`|protocol.enum.google|
  |`iOS`|`2`|protocol.enum.ios|
  |`OSX`|`3`|protocol.enum.osx|
  |`Amazon`|`4`|protocol.enum.amazon|
  |`GearVR`|`5`|protocol.enum.gearvr|
  |`UWP`|`7`|protocol.enum.uwp|
  |`Win32`|`8`|protocol.enum.win32|
  |`Dedicated`|`9`|protocol.enum.dedicated|
  |`tvOS_Deprecated`|`10`|protocol.enum.tvos_deprecated|
  |`Sony`|`11`|protocol.enum.sony|
  |`Nx`|`12`|protocol.enum.nx|
  |`Xbox`|`13`|protocol.enum.xbox|
  |`WindowsPhone_Deprecated`|`14`|protocol.enum.windowsphone_deprecated|
  |`Linux`|`15`|protocol.enum.linux|
  |`Unknown`|`-1`|protocol.enum.unknown|



////

///

