# <!-- md:samp PlayerListPacket -->

> 文档版本：r/21_u4<br/>协议版本：748

<!-- md:samp PlayerListPacket -->数据包，数字ID是`63`。该数据包用于protocol.packet.playerlistpacket.description

## 结构

```viz
digraph "PlayerListPacket" {
rankdir = LR
0
0 -> 1
1 -> 2
0 -> 3
3 -> 4
4 -> 5
5 -> 6
6 -> 7
5 -> 8
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
21 -> 113
8 -> 114
114 -> 115
8 -> 116
116 -> 117
8 -> 118
118 -> 119
4 -> 120
120 -> 121
3 -> 122
122 -> 123
123 -> 124
124 -> 125
123 -> 126
126 -> 127
127 -> 128

0 [label="PlayerListPacket",comment="name: \"PlayerListPacket\", typeName: \"\", id: 0, branchId: 63, recurseId: -1, attributes: 0, notes: \"\""];
1 [label="Action",comment="name: \"Action\", typeName: \"\", id: 1, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
2 [label="byte",comment="name: \"byte\", typeName: \"\", id: 2, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
3 [label="Dependency on 'Action'",shape=note,comment="name: \"Dependency on 'Action'\", typeName: \"\", id: 3, branchId: 0, recurseId: -1, attributes: 2, notes: \"\""];
4 [label="if (0)",shape=diamond,comment="name: \"if (0)\", typeName: \"\", id: 4, branchId: 0, recurseId: -1, attributes: 4, notes: \"\""];
5 [label="Add Player List",comment="name: \"Add Player List\", typeName: \"\", id: 5, branchId: 0, recurseId: -1, attributes: 8, notes: \"\""];
6 [label="Entries Count",comment="name: \"Entries Count\", typeName: \"\", id: 6, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
7 [label="unsigned varint",comment="name: \"unsigned varint\", typeName: \"\", id: 7, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
8 [label="example element",style=dotted,comment="name: \"example element\", typeName: \"\", id: 8, branchId: 0, recurseId: -1, attributes: 16, notes: \"\""];
9 [label="UUID",comment="name: \"UUID\", typeName: \"mce::UUID\", id: 9, branchId: 0, recurseId: -1, attributes: 256, notes: \"\""];
10 [label="mce::UUID",comment="name: \"mce::UUID\", typeName: \"\", id: 10, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
11 [label="Target Actor ID",comment="name: \"Target Actor ID\", typeName: \"ActorUniqueID\", id: 11, branchId: 0, recurseId: -1, attributes: 256, notes: \"\""];
12 [label="ActorUniqueID",comment="name: \"ActorUniqueID\", typeName: \"\", id: 12, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
13 [label="Player Name",comment="name: \"Player Name\", typeName: \"\", id: 13, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
14 [label="string",comment="name: \"string\", typeName: \"\", id: 14, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
15 [label="XBL XUID",comment="name: \"XBL XUID\", typeName: \"\", id: 15, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
16 [label="string",comment="name: \"string\", typeName: \"\", id: 16, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
17 [label="Platform Chat Id",comment="name: \"Platform Chat Id\", typeName: \"\", id: 17, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
18 [label="string",comment="name: \"string\", typeName: \"\", id: 18, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
19 [label="Build Platform",comment="name: \"Build Platform\", typeName: \"\", id: 19, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
20 [label="int",comment="name: \"int\", typeName: \"\", id: 20, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
21 [label="Serialized Skin",comment="name: \"Serialized Skin\", typeName: \"SerializedSkin\", id: 21, branchId: 0, recurseId: -1, attributes: 256, notes: \"\""];
113 [label="SerializedSkin",comment="name: \"SerializedSkin\", typeName: \"\", id: 113, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
114 [label="Is Teacher?",comment="name: \"Is Teacher?\", typeName: \"\", id: 114, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
115 [label="bool",comment="name: \"bool\", typeName: \"\", id: 115, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
116 [label="Is Host?",comment="name: \"Is Host?\", typeName: \"\", id: 116, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
117 [label="bool",comment="name: \"bool\", typeName: \"\", id: 117, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
118 [label="Is SubClient",comment="name: \"Is SubClient\", typeName: \"\", id: 118, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
119 [label="bool",comment="name: \"bool\", typeName: \"\", id: 119, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
120 [label="Is trusted skin",comment="name: \"Is trusted skin\", typeName: \"\", id: 120, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
121 [label="bool",comment="name: \"bool\", typeName: \"\", id: 121, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
122 [label="if (1)",shape=diamond,comment="name: \"if (1)\", typeName: \"\", id: 122, branchId: 1, recurseId: -1, attributes: 4, notes: \"\""];
123 [label="Remove Player List",comment="name: \"Remove Player List\", typeName: \"\", id: 123, branchId: 0, recurseId: -1, attributes: 8, notes: \"\""];
124 [label="Entries Count",comment="name: \"Entries Count\", typeName: \"\", id: 124, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
125 [label="unsigned varint",comment="name: \"unsigned varint\", typeName: \"\", id: 125, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
126 [label="example element",style=dotted,comment="name: \"example element\", typeName: \"\", id: 126, branchId: 0, recurseId: -1, attributes: 16, notes: \"\""];
127 [label="UUID",comment="name: \"UUID\", typeName: \"mce::UUID\", id: 127, branchId: 0, recurseId: -1, attributes: 256, notes: \"\""];
128 [label="mce::UUID",comment="name: \"mce::UUID\", typeName: \"\", id: 128, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
{ rank = max;2;7;10;12;14;16;18;20;113;115;117;119;121;125;128}

}

```

## 字段

```title='PlayerListPacket'
[action][dependency_on_action]
```

/// html | div.result
//// define
Action：<!-- md:samp byte -->

- 基本类型枚举。protocol.packet.playerlistpacket.action.description枚举值如下：

  |键|值|描述|
  |---|---|---|
  |`Add`|`0`|protocol.enum.add|
  |`Remove`|`1`|protocol.enum.remove|



////
> 依赖于`Action`

///// tab | `Action`如果为`0`
```title='if (0)'
[add_player_list][is_trusted_skin]
```

////// html | div.result
```title='Add Player List'
[entries_count][[example_element]..]
```

/////// html | div.result
//////// define
Entries Count：<!-- md:samp unsigned varint -->

- 基本类型。protocol.packet.playerlistpacket.dependency_on_action.if_0.add_player_list.entries_count.description


////////
```title='示例元素'
[uuid][target_actor_id][player_name][xbl_xuid][platform_chat_id][build_platform][serialized_skin][is_teacher][is_host][is_subclient]
```

//////// html | div.result
///////// define
UUID：[<!-- md:samp mce::UUID -->](../types/mce__uuid.md)

- 特殊类型。protocol.packet.playerlistpacket.dependency_on_action.if_0.add_player_list.example_element.uuid.description


/////////
///////// define
Target Actor ID：[<!-- md:samp ActorUniqueID -->](../types/actoruniqueid.md)

- 特殊类型。protocol.packet.playerlistpacket.dependency_on_action.if_0.add_player_list.example_element.target_actor_id.description


/////////
///////// define
Player Name：[<!-- md:samp string -->](../types/string.md)

- 特殊类型。protocol.packet.playerlistpacket.dependency_on_action.if_0.add_player_list.example_element.player_name.description


/////////
///////// define
XBL XUID：[<!-- md:samp string -->](../types/string.md)

- 特殊类型。protocol.packet.playerlistpacket.dependency_on_action.if_0.add_player_list.example_element.xbl_xuid.description


/////////
///////// define
Platform Chat Id：[<!-- md:samp string -->](../types/string.md)

- 特殊类型。protocol.packet.playerlistpacket.dependency_on_action.if_0.add_player_list.example_element.platform_chat_id.description


/////////
///////// define
Build Platform：<!-- md:samp int -->

- 基本类型枚举。protocol.packet.playerlistpacket.dependency_on_action.if_0.add_player_list.example_element.build_platform.description枚举值如下：

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



/////////
///////// define
Serialized Skin：[<!-- md:samp SerializedSkin -->](../types/serializedskin.md)

- 特殊类型。protocol.packet.playerlistpacket.dependency_on_action.if_0.add_player_list.example_element.serialized_skin.description


/////////
///////// define
Is Teacher?：<!-- md:samp bool -->

- 基本类型。protocol.packet.playerlistpacket.dependency_on_action.if_0.add_player_list.example_element.is_teacher.description


/////////
///////// define
Is Host?：<!-- md:samp bool -->

- 基本类型。protocol.packet.playerlistpacket.dependency_on_action.if_0.add_player_list.example_element.is_host.description


/////////
///////// define
Is SubClient：<!-- md:samp bool -->

- 基本类型。protocol.packet.playerlistpacket.dependency_on_action.if_0.add_player_list.example_element.is_subclient.description


/////////

////////

///////
/////// define
Is trusted skin：<!-- md:samp bool -->

- 基本类型。protocol.packet.playerlistpacket.dependency_on_action.if_0.is_trusted_skin.description


///////

//////

/////

///// tab | `Action`如果为`1`
```title='if (1)'
[remove_player_list]
```

////// html | div.result
```title='Remove Player List'
[entries_count][[example_element]..]
```

/////// html | div.result
//////// define
Entries Count：<!-- md:samp unsigned varint -->

- 基本类型。protocol.packet.playerlistpacket.dependency_on_action.if_1.remove_player_list.entries_count.description


////////
```title='示例元素'
[uuid]
```

//////// html | div.result
///////// define
UUID：[<!-- md:samp mce::UUID -->](../types/mce__uuid.md)

- 特殊类型。protocol.packet.playerlistpacket.dependency_on_action.if_1.remove_player_list.example_element.uuid.description


/////////

////////

///////

//////

/////

///

