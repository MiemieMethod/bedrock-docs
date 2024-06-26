# <!-- md:samp PlayerAuthInputPacket -->

> 文档版本：r/20_u8<br/>协议版本：671

<!-- md:samp PlayerAuthInputPacket -->数据包，数字ID是`144`。该数据包用于protocol.packet.playerauthinputpacket.description

## 结构

```viz
digraph "PlayerAuthInputPacket" {
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
0 -> 23
23 -> 24
0 -> 25
25 -> 26
0 -> 27
27 -> 28
28 -> 29
27 -> 30
30 -> 31
31 -> 76
0 -> 77
77 -> 78
78 -> 79
77 -> 80
80 -> 81
81 -> 85
80 -> 86
86 -> 87
87 -> 88
86 -> 89
89 -> 90
90 -> 91
89 -> 92
92 -> 93
89 -> 94
94 -> 102
89 -> 103
103 -> 104
80 -> 105
105 -> 106
106 -> 107
105 -> 108
108 -> 109
109 -> 110
80 -> 111
111 -> 112
0 -> 113
113 -> 114
114 -> 115
113 -> 116
116 -> 117
117 -> 159
0 -> 160
160 -> 161
161 -> 162
160 -> 163
163 -> 164
164 -> 165
163 -> 166
166 -> 167
0 -> 168
168 -> 169

0 [label="PlayerAuthInputPacket",comment="name: \"PlayerAuthInputPacket\", typeName: \"\", id: 0, branchId: 144, recurseId: -1, attributes: 0, notes: \"\""];
1 [label="Player Rotation",comment="name: \"Player Rotation\", typeName: \"Vec2\", id: 1, branchId: 0, recurseId: -1, attributes: 256, notes: \"\""];
2 [label="Vec2",comment="name: \"Vec2\", typeName: \"\", id: 2, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
3 [label="Player Position",comment="name: \"Player Position\", typeName: \"Vec3\", id: 3, branchId: 0, recurseId: -1, attributes: 256, notes: \"\""];
4 [label="Vec3",comment="name: \"Vec3\", typeName: \"\", id: 4, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
5 [label="Move Vector",comment="name: \"Move Vector\", typeName: \"Vec2\", id: 5, branchId: 0, recurseId: -1, attributes: 256, notes: \"\""];
6 [label="Vec2",comment="name: \"Vec2\", typeName: \"\", id: 6, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
7 [label="Player's Head Rotation",comment="name: \"Player's Head Rotation\", typeName: \"\", id: 7, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
8 [label="float",comment="name: \"float\", typeName: \"\", id: 8, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
9 [label="Input Data",comment="name: \"Input Data\", typeName: \"\", id: 9, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
10 [label="unsigned varint64",comment="name: \"unsigned varint64\", typeName: \"\", id: 10, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
11 [label="Input Mode",comment="name: \"Input Mode\", typeName: \"\", id: 11, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
12 [label="unsigned varint",comment="name: \"unsigned varint\", typeName: \"\", id: 12, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
13 [label="Play Mode",comment="name: \"Play Mode\", typeName: \"\", id: 13, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
14 [label="unsigned varint",comment="name: \"unsigned varint\", typeName: \"\", id: 14, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
15 [label="New Interaction Model",comment="name: \"New Interaction Model\", typeName: \"\", id: 15, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
16 [label="unsigned varint",comment="name: \"unsigned varint\", typeName: \"\", id: 16, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
17 [label="Dependency on 'Play Mode == ClientPlayMode::Reality'",shape=note,comment="name: \"Dependency on 'Play Mode == ClientPlayMode::Reality'\", typeName: \"\", id: 17, branchId: 0, recurseId: -1, attributes: 2, notes: \"\""];
18 [label="if (0)",shape=diamond,comment="name: \"if (0)\", typeName: \"\", id: 18, branchId: 0, recurseId: -1, attributes: 4, notes: \"\""];
19 [label="[No Data]",comment="name: \"[No Data]\", typeName: \"\", id: 19, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
20 [label="if (1)",shape=diamond,comment="name: \"if (1)\", typeName: \"\", id: 20, branchId: 1, recurseId: -1, attributes: 4, notes: \"\""];
21 [label="VR Gaze Direction",comment="name: \"VR Gaze Direction\", typeName: \"Vec3\", id: 21, branchId: 0, recurseId: -1, attributes: 256, notes: \"\""];
22 [label="Vec3",comment="name: \"Vec3\", typeName: \"\", id: 22, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
23 [label="Client tick",comment="name: \"Client tick\", typeName: \"\", id: 23, branchId: 0, recurseId: -1, attributes: 0, notes: \"Which simulation frame client is on. Used to match corrections\""];
24 [label="unsigned varint64",comment="name: \"unsigned varint64\", typeName: \"\", id: 24, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
25 [label="Pos Delta",comment="name: \"Pos Delta\", typeName: \"Vec3\", id: 25, branchId: 0, recurseId: -1, attributes: 256, notes: \"Velocity\""];
26 [label="Vec3",comment="name: \"Vec3\", typeName: \"\", id: 26, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
27 [label="Dependency on 'ItemUseTransaction and PerformItemInteraction bit set'",shape=note,comment="name: \"Dependency on 'ItemUseTransaction and PerformItemInteraction bit set'\", typeName: \"\", id: 27, branchId: 0, recurseId: -1, attributes: 2, notes: \"\""];
28 [label="if (0)",shape=diamond,comment="name: \"if (0)\", typeName: \"\", id: 28, branchId: 0, recurseId: -1, attributes: 4, notes: \"\""];
29 [label="[No Data]",comment="name: \"[No Data]\", typeName: \"\", id: 29, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
30 [label="if (1)",shape=diamond,comment="name: \"if (1)\", typeName: \"\", id: 30, branchId: 1, recurseId: -1, attributes: 4, notes: \"\""];
31 [label="Item Use Transaction",comment="name: \"Item Use Transaction\", typeName: \"PackedItemUseLegacyInventoryTransaction\", id: 31, branchId: 0, recurseId: -1, attributes: 256, notes: \"\""];
76 [label="PackedItemUseLegacyInventoryTransaction",comment="name: \"PackedItemUseLegacyInventoryTransaction\", typeName: \"\", id: 76, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
77 [label="Dependency on 'ItemStackRequest and PerformItemStackRequest bit set'",shape=note,comment="name: \"Dependency on 'ItemStackRequest and PerformItemStackRequest bit set'\", typeName: \"\", id: 77, branchId: 0, recurseId: -1, attributes: 2, notes: \"\""];
78 [label="if (0)",shape=diamond,comment="name: \"if (0)\", typeName: \"\", id: 78, branchId: 0, recurseId: -1, attributes: 4, notes: \"\""];
79 [label="[No Data]",comment="name: \"[No Data]\", typeName: \"\", id: 79, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
80 [label="if (1)",shape=diamond,comment="name: \"if (1)\", typeName: \"\", id: 80, branchId: 1, recurseId: -1, attributes: 4, notes: \"\""];
81 [label="Client Request Id",comment="name: \"Client Request Id\", typeName: \"TypedClientNetId<struct ItemStackRequestIdTag,int,0>\", id: 81, branchId: 0, recurseId: -1, attributes: 256, notes: \"\""];
85 [label="TypedClientNetId<struct ItemStackRequestIdTag,int,0>",comment="name: \"TypedClientNetId<struct ItemStackRequestIdTag,int,0>\", typeName: \"\", id: 85, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
86 [label="Actions",comment="name: \"Actions\", typeName: \"\", id: 86, branchId: 0, recurseId: -1, attributes: 8, notes: \"There are a variety of possible actions each with their own schema; this (Take) is just one example. Refer to the Item Stack Net Manager documentation.\""];
87 [label="Array Size",comment="name: \"Array Size\", typeName: \"\", id: 87, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
88 [label="unsigned varint",comment="name: \"unsigned varint\", typeName: \"\", id: 88, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
89 [label="example element",style=dotted,comment="name: \"example element\", typeName: \"\", id: 89, branchId: 0, recurseId: -1, attributes: 16, notes: \"\""];
90 [label="Action type",comment="name: \"Action type\", typeName: \"\", id: 90, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
91 [label="byte",comment="name: \"byte\", typeName: \"\", id: 91, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
92 [label="Amount",comment="name: \"Amount\", typeName: \"\", id: 92, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
93 [label="byte",comment="name: \"byte\", typeName: \"\", id: 93, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
94 [label="Source",comment="name: \"Source\", typeName: \"ItemStackRequestSlotInfo\", id: 94, branchId: 0, recurseId: -1, attributes: 256, notes: \"\""];
102 [label="ItemStackRequestSlotInfo",comment="name: \"ItemStackRequestSlotInfo\", typeName: \"\", id: 102, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
103 [label="Destination",comment="name: \"Destination\", typeName: \"ItemStackRequestSlotInfo\", id: 103, branchId: 0, recurseId: -1, attributes: 256, notes: \"\""];
104 [label="ItemStackRequestSlotInfo",comment="name: \"ItemStackRequestSlotInfo\", typeName: \"\", id: 104, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
105 [label="Strings To Filter",comment="name: \"Strings To Filter\", typeName: \"\", id: 105, branchId: 0, recurseId: -1, attributes: 8, notes: \"Array of strings to submit to profanity filtering service\""];
106 [label="Array Size",comment="name: \"Array Size\", typeName: \"\", id: 106, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
107 [label="unsigned varint",comment="name: \"unsigned varint\", typeName: \"\", id: 107, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
108 [label="example element",style=dotted,comment="name: \"example element\", typeName: \"\", id: 108, branchId: 0, recurseId: -1, attributes: 16, notes: \"\""];
109 [label="String To Filter",comment="name: \"String To Filter\", typeName: \"\", id: 109, branchId: 0, recurseId: -1, attributes: 0, notes: \"Indivdiual string that needs checking\""];
110 [label="string",comment="name: \"string\", typeName: \"\", id: 110, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
111 [label="StringsToFilterOrigin",comment="name: \"StringsToFilterOrigin\", typeName: \"\", id: 111, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
112 [label="int",comment="name: \"int\", typeName: \"\", id: 112, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
113 [label="Dependency on 'PerformBlockActions bit set'",shape=note,comment="name: \"Dependency on 'PerformBlockActions bit set'\", typeName: \"\", id: 113, branchId: 0, recurseId: -1, attributes: 2, notes: \"\""];
114 [label="if (0)",shape=diamond,comment="name: \"if (0)\", typeName: \"\", id: 114, branchId: 0, recurseId: -1, attributes: 4, notes: \"\""];
115 [label="[No Data]",comment="name: \"[No Data]\", typeName: \"\", id: 115, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
116 [label="if (1)",shape=diamond,comment="name: \"if (1)\", typeName: \"\", id: 116, branchId: 1, recurseId: -1, attributes: 4, notes: \"\""];
117 [label="Player Block Actions",comment="name: \"Player Block Actions\", typeName: \"PlayerBlockActions\", id: 117, branchId: 0, recurseId: -1, attributes: 256, notes: \"\""];
159 [label="PlayerBlockActions",comment="name: \"PlayerBlockActions\", typeName: \"\", id: 159, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
160 [label="Dependency on 'IsInClientPredictedVehicle bit set'",shape=note,comment="name: \"Dependency on 'IsInClientPredictedVehicle bit set'\", typeName: \"\", id: 160, branchId: 0, recurseId: -1, attributes: 2, notes: \"\""];
161 [label="if (0)",shape=diamond,comment="name: \"if (0)\", typeName: \"\", id: 161, branchId: 0, recurseId: -1, attributes: 4, notes: \"\""];
162 [label="[No Data]",comment="name: \"[No Data]\", typeName: \"\", id: 162, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
163 [label="if (1)",shape=diamond,comment="name: \"if (1)\", typeName: \"\", id: 163, branchId: 1, recurseId: -1, attributes: 4, notes: \"\""];
164 [label="Vehicle Rotation",comment="name: \"Vehicle Rotation\", typeName: \"Vec2\", id: 164, branchId: 0, recurseId: -1, attributes: 256, notes: \"\""];
165 [label="Vec2",comment="name: \"Vec2\", typeName: \"\", id: 165, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
166 [label="Client Predicted Vehicle",comment="name: \"Client Predicted Vehicle\", typeName: \"ActorUniqueID\", id: 166, branchId: 0, recurseId: -1, attributes: 256, notes: \"\""];
167 [label="ActorUniqueID",comment="name: \"ActorUniqueID\", typeName: \"\", id: 167, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
168 [label="Analog MoveVector",comment="name: \"Analog MoveVector\", typeName: \"Vec2\", id: 168, branchId: 0, recurseId: -1, attributes: 256, notes: \"\""];
169 [label="Vec2",comment="name: \"Vec2\", typeName: \"\", id: 169, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
{ rank = max;2;4;6;8;10;12;14;16;19;22;24;26;29;76;79;85;88;91;93;102;104;107;110;112;115;159;162;165;167;169}

}

```

## 字段

```title='PlayerAuthInputPacket'
[player_rotation][player_position][move_vector][players_head_rotation][input_data][input_mode][play_mode][new_interaction_model][dependency_on_play_mode_is_clientplaymode::reality][client_tick][pos_delta][dependency_on_itemusetransaction_and_performiteminteraction_bit_set][dependency_on_itemstackrequest_and_performitemstackrequest_bit_set][dependency_on_performblockactions_bit_set][dependency_on_isinclientpredictedvehicle_bit_set][analog_movevector]
```

/// html | div.result
//// define
Player Rotation：[<!-- md:samp Vec2 -->](../types/vec2.md)

- 特殊类型。protocol.packet.playerauthinputpacket.player_rotation.description


////
//// define
Player Position：[<!-- md:samp Vec3 -->](../types/vec3.md)

- 特殊类型。protocol.packet.playerauthinputpacket.player_position.description


////
//// define
Move Vector：[<!-- md:samp Vec2 -->](../types/vec2.md)

- 特殊类型。protocol.packet.playerauthinputpacket.move_vector.description


////
//// define
Player's Head Rotation：<!-- md:samp float -->

- 基本类型。protocol.packet.playerauthinputpacket.players_head_rotation.description


////
//// define
Input Data：<!-- md:samp unsigned varint64 -->

- 基本类型。protocol.packet.playerauthinputpacket.input_data.description


////
//// define
Input Mode：<!-- md:samp unsigned varint -->

- 基本类型枚举。protocol.packet.playerauthinputpacket.input_mode.description枚举值如下：

  |键|值|描述|
  |---|---|---|
  |`Undefined`|`0`|protocol.enum.undefined|
  |`Mouse`|`1`|protocol.enum.mouse|
  |`Touch`|`2`|protocol.enum.touch|
  |`GamePad`|`3`|protocol.enum.gamepad|
  |`MotionController`|`4`|protocol.enum.motioncontroller|
  |`Count`|`5`|protocol.enum.count|



////
//// define
Play Mode：<!-- md:samp unsigned varint -->

- 基本类型枚举。protocol.packet.playerauthinputpacket.play_mode.description枚举值如下：

  |键|值|描述|
  |---|---|---|
  |`Normal`|`0`|protocol.enum.normal|
  |`Teaser`|`1`|protocol.enum.teaser|
  |`Screen`|`2`|protocol.enum.screen|
  |`Viewer`|`3`|protocol.enum.viewer|
  |`Reality`|`4`|protocol.enum.reality|
  |`Placement`|`5`|protocol.enum.placement|
  |`LivingRoom`|`6`|protocol.enum.livingroom|
  |`ExitLevel`|`7`|protocol.enum.exitlevel|
  |`ExitLevelLivingRoom`|`8`|protocol.enum.exitlevellivingroom|
  |`NumModes`|`9`|protocol.enum.nummodes|



////
//// define
New Interaction Model：<!-- md:samp unsigned varint -->

- 基本类型枚举。protocol.packet.playerauthinputpacket.new_interaction_model.description枚举值如下：

  |键|值|描述|
  |---|---|---|
  |`Touch`|`0`|protocol.enum.touch|
  |`Crosshair`|`1`|protocol.enum.crosshair|
  |`Classic`|`2`|protocol.enum.classic|
  |`Count`|`3`|protocol.enum.count|



////
> 依赖于`Play Mode == ClientPlayMode::Reality`

///// tab | `Play Mode == ClientPlayMode::Reality`如果为`0`
////// define
if (0)：<!-- md:samp [No Data] -->

- 无数据


//////

/////

///// tab | `Play Mode == ClientPlayMode::Reality`如果为`1`
```title='if (1)'
[vr_gaze_direction]
```

////// html | div.result
/////// define
VR Gaze Direction：[<!-- md:samp Vec3 -->](../types/vec3.md)

- 特殊类型。protocol.packet.playerauthinputpacket.dependency_on_play_mode_is_clientplaymode::reality.if_1.vr_gaze_direction.description


///////

//////

/////
//// define
Client tick：<!-- md:samp unsigned varint64 -->

- 基本类型。protocol.packet.playerauthinputpacket.client_tick.descriptionWhich simulation frame client is on. Used to match corrections


////
//// define
Pos Delta：[<!-- md:samp Vec3 -->](../types/vec3.md)

- 特殊类型。protocol.packet.playerauthinputpacket.pos_delta.descriptionVelocity


////
> 依赖于`ItemUseTransaction and PerformItemInteraction bit set`

///// tab | `ItemUseTransaction and PerformItemInteraction bit set`如果为`0`
////// define
if (0)：<!-- md:samp [No Data] -->

- 无数据


//////

/////

///// tab | `ItemUseTransaction and PerformItemInteraction bit set`如果为`1`
```title='if (1)'
[item_use_transaction]
```

////// html | div.result
/////// define
Item Use Transaction：[<!-- md:samp PackedItemUseLegacyInventoryTransaction -->](../types/packeditemuselegacyinventorytransaction.md)

- 特殊类型。protocol.packet.playerauthinputpacket.dependency_on_itemusetransaction_and_performiteminteraction_bit_set.if_1.item_use_transaction.description


///////

//////

/////
> 依赖于`ItemStackRequest and PerformItemStackRequest bit set`

///// tab | `ItemStackRequest and PerformItemStackRequest bit set`如果为`0`
////// define
if (0)：<!-- md:samp [No Data] -->

- 无数据


//////

/////

///// tab | `ItemStackRequest and PerformItemStackRequest bit set`如果为`1`
```title='if (1)'
[client_request_id][actions][strings_to_filter][stringstofilterorigin]
```

////// html | div.result
/////// define
Client Request Id：[<!-- md:samp TypedClientNetId&lt;struct ItemStackRequestIdTag,int,0&gt; -->](../types/typedclientnetid_struct_itemstackrequestidtag,int,0_.md)

- 特殊类型。protocol.packet.playerauthinputpacket.dependency_on_itemstackrequest_and_performitemstackrequest_bit_set.if_1.client_request_id.description


///////
```title='Actions'
[array_size][[example_element]..]
```

/////// html | div.result
//////// define
数组大小：<!-- md:samp unsigned varint -->

- 基本类型。protocol.packet.playerauthinputpacket.dependency_on_itemstackrequest_and_performitemstackrequest_bit_set.if_1.actions.array_size.description


////////
```title='示例元素'
[action_type][amount][source][destination]
```

//////// html | div.result
///////// define
Action type：<!-- md:samp byte -->

- 基本类型枚举。protocol.packet.playerauthinputpacket.dependency_on_itemstackrequest_and_performitemstackrequest_bit_set.if_1.actions.example_element.action_type.description枚举值如下：

  |键|值|描述|
  |---|---|---|
  |`Take`|`0`|protocol.enum.take|
  |`Place`|`1`|protocol.enum.place|
  |`Swap`|`2`|protocol.enum.swap|
  |`Drop`|`3`|protocol.enum.drop|
  |`Destroy`|`4`|protocol.enum.destroy|
  |`Consume`|`5`|protocol.enum.consume|
  |`Create`|`6`|protocol.enum.create|
  |`PlaceInItemContainer`|`7`|protocol.enum.placeinitemcontainer|
  |`TakeFromItemContainer`|`8`|protocol.enum.takefromitemcontainer|
  |`ScreenLabTableCombine`|`9`|protocol.enum.screenlabtablecombine|
  |`ScreenBeaconPayment`|`10`|protocol.enum.screenbeaconpayment|
  |`ScreenHUDMineBlock`|`11`|protocol.enum.screenhudmineblock|
  |`CraftRecipe`|`12`|protocol.enum.craftrecipe|
  |`CraftRecipeAuto`|`13`|protocol.enum.craftrecipeauto|
  |`CraftCreative`|`14`|protocol.enum.craftcreative|
  |`CraftRecipeOptional`|`15`|protocol.enum.craftrecipeoptional|
  |`CraftRepairAndDisenchant`|`16`|protocol.enum.craftrepairanddisenchant|
  |`CraftLoom`|`17`|protocol.enum.craftloom|
  |`CraftNonImplemented_DEPRECATEDASKTYLAING`|`18`|protocol.enum.craftnonimplemented_deprecatedasktylaing|
  |`CraftResults_DEPRECATEDASKTYLAING`|`19`|protocol.enum.craftresults_deprecatedasktylaing|
  |`ifdef`|`20`|protocol.enum.ifdef|
  |`TEST_INFRASTRUCTURE_ENABLED`|`21`|protocol.enum.test_infrastructure_enabled|
  |`Test`|`22`|protocol.enum.test|
  |`endif`|`23`|protocol.enum.endif|



/////////
///////// define
Amount：<!-- md:samp byte -->

- 基本类型。protocol.packet.playerauthinputpacket.dependency_on_itemstackrequest_and_performitemstackrequest_bit_set.if_1.actions.example_element.amount.description


/////////
///////// define
Source：[<!-- md:samp ItemStackRequestSlotInfo -->](../types/itemstackrequestslotinfo.md)

- 特殊类型。protocol.packet.playerauthinputpacket.dependency_on_itemstackrequest_and_performitemstackrequest_bit_set.if_1.actions.example_element.source.description


/////////
///////// define
Destination：[<!-- md:samp ItemStackRequestSlotInfo -->](../types/itemstackrequestslotinfo.md)

- 特殊类型。protocol.packet.playerauthinputpacket.dependency_on_itemstackrequest_and_performitemstackrequest_bit_set.if_1.actions.example_element.destination.description


/////////

////////

///////
```title='Strings To Filter'
[array_size][[example_element]..]
```

/////// html | div.result
//////// define
数组大小：<!-- md:samp unsigned varint -->

- 基本类型。protocol.packet.playerauthinputpacket.dependency_on_itemstackrequest_and_performitemstackrequest_bit_set.if_1.strings_to_filter.array_size.description


////////
```title='示例元素'
[string_to_filter]
```

//////// html | div.result
///////// define
String To Filter：[<!-- md:samp string -->](../types/string.md)

- 特殊类型。protocol.packet.playerauthinputpacket.dependency_on_itemstackrequest_and_performitemstackrequest_bit_set.if_1.strings_to_filter.example_element.string_to_filter.descriptionIndivdiual string that needs checking


/////////

////////

///////
/////// define
StringsToFilterOrigin：<!-- md:samp int -->

- 基本类型枚举。protocol.packet.playerauthinputpacket.dependency_on_itemstackrequest_and_performitemstackrequest_bit_set.if_1.stringstofilterorigin.description枚举值如下：

  |键|值|描述|
  |---|---|---|
  |`unknown`|`-1`|protocol.enum.unknown|
  |`ServerChatPublic`|`0`|protocol.enum.serverchatpublic|
  |`ServerChatWhisper`|`1`|protocol.enum.serverchatwhisper|
  |`SignText`|`2`|protocol.enum.signtext|
  |`AnvilText`|`3`|protocol.enum.anviltext|
  |`BookAndQuillText`|`4`|protocol.enum.bookandquilltext|
  |`CommandBlockText`|`5`|protocol.enum.commandblocktext|
  |`BlockActorDataText`|`6`|protocol.enum.blockactordatatext|
  |`JoinEventText`|`7`|protocol.enum.joineventtext|
  |`LeaveEventText`|`8`|protocol.enum.leaveeventtext|
  |`SlashCommandChat`|`9`|protocol.enum.slashcommandchat|
  |`CartographyText`|`10`|protocol.enum.cartographytext|
  |`KickCommand`|`11`|protocol.enum.kickcommand|
  |`TitleCommand`|`12`|protocol.enum.titlecommand|
  |`SummonCommand`|`13`|protocol.enum.summoncommand|
  |`ServerForm`|`14`|protocol.enum.serverform|
  |`COUNT`|`15`|protocol.enum.count|



///////

//////

/////
> 依赖于`PerformBlockActions bit set`

///// tab | `PerformBlockActions bit set`如果为`0`
////// define
if (0)：<!-- md:samp [No Data] -->

- 无数据


//////

/////

///// tab | `PerformBlockActions bit set`如果为`1`
```title='if (1)'
[player_block_actions]
```

////// html | div.result
/////// define
Player Block Actions：[<!-- md:samp PlayerBlockActions -->](../types/playerblockactions.md)

- 特殊类型。protocol.packet.playerauthinputpacket.dependency_on_performblockactions_bit_set.if_1.player_block_actions.description


///////

//////

/////
> 依赖于`IsInClientPredictedVehicle bit set`

///// tab | `IsInClientPredictedVehicle bit set`如果为`0`
////// define
if (0)：<!-- md:samp [No Data] -->

- 无数据


//////

/////

///// tab | `IsInClientPredictedVehicle bit set`如果为`1`
```title='if (1)'
[vehicle_rotation][client_predicted_vehicle]
```

////// html | div.result
/////// define
Vehicle Rotation：[<!-- md:samp Vec2 -->](../types/vec2.md)

- 特殊类型。protocol.packet.playerauthinputpacket.dependency_on_isinclientpredictedvehicle_bit_set.if_1.vehicle_rotation.description


///////
/////// define
Client Predicted Vehicle：[<!-- md:samp ActorUniqueID -->](../types/actoruniqueid.md)

- 特殊类型。protocol.packet.playerauthinputpacket.dependency_on_isinclientpredictedvehicle_bit_set.if_1.client_predicted_vehicle.description


///////

//////

/////
//// define
Analog MoveVector：[<!-- md:samp Vec2 -->](../types/vec2.md)

- 特殊类型。protocol.packet.playerauthinputpacket.analog_movevector.description


////

///

