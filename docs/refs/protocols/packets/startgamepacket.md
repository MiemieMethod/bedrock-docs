# <!-- md:samp StartGamePacket -->

> 文档版本：r/21_u4<br/>协议版本：748

<!-- md:samp StartGamePacket -->数据包，数字ID是`11`。该数据包用于protocol.packet.startgamepacket.description

## 结构

```viz
digraph "StartGamePacket" {
rankdir = LR
0
0 -> 1
1 -> 5
0 -> 6
6 -> 10
0 -> 11
11 -> 12
0 -> 13
13 -> 14
0 -> 15
15 -> 21
0 -> 22
22 -> 145
0 -> 146
146 -> 147
0 -> 148
148 -> 149
0 -> 150
150 -> 151
0 -> 152
152 -> 153
0 -> 154
154 -> 162
0 -> 163
163 -> 164
0 -> 165
165 -> 166
0 -> 167
167 -> 168
168 -> 169
167 -> 170
170 -> 171
171 -> 172
170 -> 173
173 -> 174
0 -> 175
175 -> 176
176 -> 177
175 -> 178
178 -> 179
179 -> 187
0 -> 188
188 -> 189
0 -> 190
190 -> 191
0 -> 192
192 -> 193
0 -> 194
194 -> 195
0 -> 196
196 -> 197
0 -> 198
198 -> 199
0 -> 200
200 -> 201
0 -> 202
202 -> 203
0 -> 204
204 -> 208

0 [label="StartGamePacket",comment="name: \"StartGamePacket\", typeName: \"\", id: 0, branchId: 11, recurseId: -1, attributes: 0, notes: \"\""];
1 [label="Target Actor ID",comment="name: \"Target Actor ID\", typeName: \"ActorUniqueID\", id: 1, branchId: 0, recurseId: -1, attributes: 256, notes: \"\""];
5 [label="ActorUniqueID",comment="name: \"ActorUniqueID\", typeName: \"\", id: 5, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
6 [label="Target Runtime ID",comment="name: \"Target Runtime ID\", typeName: \"ActorRuntimeID\", id: 6, branchId: 0, recurseId: -1, attributes: 256, notes: \"\""];
10 [label="ActorRuntimeID",comment="name: \"ActorRuntimeID\", typeName: \"\", id: 10, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
11 [label="Actor Game Type",comment="name: \"Actor Game Type\", typeName: \"\", id: 11, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
12 [label="varint",comment="name: \"varint\", typeName: \"\", id: 12, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
13 [label="Position",comment="name: \"Position\", typeName: \"Vec3\", id: 13, branchId: 0, recurseId: -1, attributes: 256, notes: \"\""];
14 [label="Vec3",comment="name: \"Vec3\", typeName: \"\", id: 14, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
15 [label="Rotation",comment="name: \"Rotation\", typeName: \"Vec2\", id: 15, branchId: 0, recurseId: -1, attributes: 256, notes: \"\""];
21 [label="Vec2",comment="name: \"Vec2\", typeName: \"\", id: 21, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
22 [label="Settings",comment="name: \"Settings\", typeName: \"LevelSettings\", id: 22, branchId: 0, recurseId: -1, attributes: 256, notes: \"\""];
145 [label="LevelSettings",comment="name: \"LevelSettings\", typeName: \"\", id: 145, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
146 [label="Level ID",comment="name: \"Level ID\", typeName: \"\", id: 146, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
147 [label="string",comment="name: \"string\", typeName: \"\", id: 147, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
148 [label="Level Name",comment="name: \"Level Name\", typeName: \"\", id: 148, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
149 [label="string",comment="name: \"string\", typeName: \"\", id: 149, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
150 [label="Template Content Identity",comment="name: \"Template Content Identity\", typeName: \"\", id: 150, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
151 [label="string",comment="name: \"string\", typeName: \"\", id: 151, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
152 [label="Is Trial?",comment="name: \"Is Trial?\", typeName: \"\", id: 152, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
153 [label="bool",comment="name: \"bool\", typeName: \"\", id: 153, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
154 [label="Movement Settings",comment="name: \"Movement Settings\", typeName: \"SyncedPlayerMovementSettings\", id: 154, branchId: 0, recurseId: -1, attributes: 256, notes: \"\""];
162 [label="SyncedPlayerMovementSettings",comment="name: \"SyncedPlayerMovementSettings\", typeName: \"\", id: 162, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
163 [label="Current Level Time",comment="name: \"Current Level Time\", typeName: \"\", id: 163, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
164 [label="unsigned int64",comment="name: \"unsigned int64\", typeName: \"\", id: 164, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
165 [label="Enchantment Seed",comment="name: \"Enchantment Seed\", typeName: \"\", id: 165, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
166 [label="varint",comment="name: \"varint\", typeName: \"\", id: 166, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
167 [label="Block Properties",comment="name: \"Block Properties\", typeName: \"\", id: 167, branchId: 0, recurseId: -1, attributes: 8, notes: \"\""];
168 [label="Array Size",comment="name: \"Array Size\", typeName: \"\", id: 168, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
169 [label="unsigned varint",comment="name: \"unsigned varint\", typeName: \"\", id: 169, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
170 [label="example element",style=dotted,comment="name: \"example element\", typeName: \"\", id: 170, branchId: 0, recurseId: -1, attributes: 16, notes: \"\""];
171 [label="Block Name",comment="name: \"Block Name\", typeName: \"\", id: 171, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
172 [label="string",comment="name: \"string\", typeName: \"\", id: 172, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
173 [label="Block Definition",comment="name: \"Block Definition\", typeName: \"CompoundTag\", id: 173, branchId: 0, recurseId: -1, attributes: 256, notes: \"Map of block states. { key (component name):[label,value] } (Can be left empty.)\""];
174 [label="CompoundTag",comment="name: \"CompoundTag\", typeName: \"\", id: 174, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
175 [label="Item List - every vanilla item must be present",comment="name: \"Item List - every vanilla item must be present\", typeName: \"\", id: 175, branchId: 0, recurseId: -1, attributes: 8, notes: \"\""];
176 [label="Array Size",comment="name: \"Array Size\", typeName: \"\", id: 176, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
177 [label="unsigned varint",comment="name: \"unsigned varint\", typeName: \"\", id: 177, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
178 [label="example element",style=dotted,comment="name: \"example element\", typeName: \"\", id: 178, branchId: 0, recurseId: -1, attributes: 16, notes: \"\""];
179 [label="Item Info",comment="name: \"Item Info\", typeName: \"ItemData\", id: 179, branchId: 0, recurseId: -1, attributes: 256, notes: \"See: ItemData Type\""];
187 [label="ItemData",comment="name: \"ItemData\", typeName: \"\", id: 187, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
188 [label="Multiplayer Correlation Id",comment="name: \"Multiplayer Correlation Id\", typeName: \"\", id: 188, branchId: 0, recurseId: -1, attributes: 0, notes: \"A UUID to identify this multiplayer session.\""];
189 [label="string",comment="name: \"string\", typeName: \"\", id: 189, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
190 [label="Enable Item Stack Net Manager",comment="name: \"Enable Item Stack Net Manager\", typeName: \"\", id: 190, branchId: 0, recurseId: -1, attributes: 0, notes: \"Whether the new item stack net manager is enabled for server authoritative inventory. This will eventually be required.\""];
191 [label="bool",comment="name: \"bool\", typeName: \"\", id: 191, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
192 [label="Server version",comment="name: \"Server version\", typeName: \"\", id: 192, branchId: 0, recurseId: -1, attributes: 0, notes: \"For telemetry purposes - sending your own string with your own server name and version here would be useful for Mojang's telemetry.\""];
193 [label="string",comment="name: \"string\", typeName: \"\", id: 193, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
194 [label="Player Property Data",comment="name: \"Player Property Data\", typeName: \"CompoundTag\", id: 194, branchId: 0, recurseId: -1, attributes: 256, notes: \"like SyncActorPropertyPacket, specifically for minecraft:player properties\""];
195 [label="CompoundTag",comment="name: \"CompoundTag\", typeName: \"\", id: 195, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
196 [label="Server Block Type Registry Checksum",comment="name: \"Server Block Type Registry Checksum\", typeName: \"\", id: 196, branchId: 0, recurseId: -1, attributes: 0, notes: \"Checksum for detecting mismatches in block types between server and client.\""];
197 [label="unsigned int64",comment="name: \"unsigned int64\", typeName: \"\", id: 197, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
198 [label="World Template ID",comment="name: \"World Template ID\", typeName: \"mce::UUID\", id: 198, branchId: 0, recurseId: -1, attributes: 256, notes: \"\""];
199 [label="mce::UUID",comment="name: \"mce::UUID\", typeName: \"\", id: 199, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
200 [label="Server Enabled ClientSide Generation",comment="name: \"Server Enabled ClientSide Generation\", typeName: \"\", id: 200, branchId: 0, recurseId: -1, attributes: 0, notes: \"BiomeComponentFactory needs to know about this toggle before we start parsing BiomeComponents\""];
201 [label="bool",comment="name: \"bool\", typeName: \"\", id: 201, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
202 [label="BlockNetworkIds Are Hashes",comment="name: \"BlockNetworkIds Are Hashes\", typeName: \"\", id: 202, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
203 [label="bool",comment="name: \"bool\", typeName: \"\", id: 203, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
204 [label="NetworkPermissions",comment="name: \"NetworkPermissions\", typeName: \"NetworkPermissions\", id: 204, branchId: 0, recurseId: -1, attributes: 256, notes: \"\""];
208 [label="NetworkPermissions",comment="name: \"NetworkPermissions\", typeName: \"\", id: 208, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
{ rank = max;5;10;12;14;21;145;147;149;151;153;162;164;166;169;172;174;177;187;189;191;193;195;197;199;201;203;208}

}

```

## 字段

```title='StartGamePacket'
[target_actor_id][target_runtime_id][actor_game_type][position][rotation][settings][level_id][level_name][template_content_identity][is_trial][movement_settings][current_level_time][enchantment_seed][block_properties][item_list_every_vanilla_item_must_be_present][multiplayer_correlation_id][enable_item_stack_net_manager][server_version][player_property_data][server_block_type_registry_checksum][world_template_id][server_enabled_clientside_generation][blocknetworkids_are_hashes][networkpermissions]
```

/// html | div.result
//// define
Target Actor ID：[<!-- md:samp ActorUniqueID -->](../types/actoruniqueid.md)

- 特殊类型。protocol.packet.startgamepacket.target_actor_id.description


////
//// define
Target Runtime ID：[<!-- md:samp ActorRuntimeID -->](../types/actorruntimeid.md)

- 特殊类型。protocol.packet.startgamepacket.target_runtime_id.description


////
//// define
Actor Game Type：<!-- md:samp varint -->

- 基本类型枚举。protocol.packet.startgamepacket.actor_game_type.description枚举值如下：

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
//// define
Position：[<!-- md:samp Vec3 -->](../types/vec3.md)

- 特殊类型。protocol.packet.startgamepacket.position.description


////
//// define
Rotation：[<!-- md:samp Vec2 -->](../types/vec2.md)

- 特殊类型。protocol.packet.startgamepacket.rotation.description


////
//// define
Settings：[<!-- md:samp LevelSettings -->](../types/levelsettings.md)

- 特殊类型。protocol.packet.startgamepacket.settings.description


////
//// define
Level ID：[<!-- md:samp string -->](../types/string.md)

- 特殊类型。protocol.packet.startgamepacket.level_id.description


////
//// define
Level Name：[<!-- md:samp string -->](../types/string.md)

- 特殊类型。protocol.packet.startgamepacket.level_name.description


////
//// define
Template Content Identity：[<!-- md:samp string -->](../types/string.md)

- 特殊类型。protocol.packet.startgamepacket.template_content_identity.description


////
//// define
Is Trial?：<!-- md:samp bool -->

- 基本类型。protocol.packet.startgamepacket.is_trial.description


////
//// define
Movement Settings：[<!-- md:samp SyncedPlayerMovementSettings -->](../types/syncedplayermovementsettings.md)

- 特殊类型。protocol.packet.startgamepacket.movement_settings.description


////
//// define
Current Level Time：<!-- md:samp unsigned int64 -->

- 基本类型。protocol.packet.startgamepacket.current_level_time.description


////
//// define
Enchantment Seed：<!-- md:samp varint -->

- 基本类型。protocol.packet.startgamepacket.enchantment_seed.description


////
```title='Block Properties'
[array_size][[example_element]..]
```

//// html | div.result
///// define
数组大小：<!-- md:samp unsigned varint -->

- 基本类型。protocol.packet.startgamepacket.block_properties.array_size.description


/////
```title='示例元素'
[block_name][block_definition]
```

///// html | div.result
////// define
Block Name：[<!-- md:samp string -->](../types/string.md)

- 特殊类型。protocol.packet.startgamepacket.block_properties.example_element.block_name.description


//////
////// define
Block Definition：[<!-- md:samp CompoundTag -->](../types/compoundtag.md)

- 特殊类型。protocol.packet.startgamepacket.block_properties.example_element.block_definition.descriptionMap of block states. { key (component 'name'):[label,value] } (Can be left empty.)


//////

/////

////
```title='Item List - every vanilla item must be present'
[array_size][[example_element]..]
```

//// html | div.result
///// define
数组大小：<!-- md:samp unsigned varint -->

- 基本类型。protocol.packet.startgamepacket.item_list_every_vanilla_item_must_be_present.array_size.description


/////
```title='示例元素'
[item_info]
```

///// html | div.result
////// define
Item Info：[<!-- md:samp ItemData -->](../types/itemdata.md)

- 特殊类型。protocol.packet.startgamepacket.item_list_every_vanilla_item_must_be_present.example_element.item_info.descriptionSee: ItemData Type


//////

/////

////
//// define
Multiplayer Correlation Id：[<!-- md:samp string -->](../types/string.md)

- 特殊类型。protocol.packet.startgamepacket.multiplayer_correlation_id.descriptionA UUID to 'id'entify this multiplayer session.


////
//// define
Enable Item Stack Net Manager：<!-- md:samp bool -->

- 基本类型。protocol.packet.startgamepacket.enable_item_stack_net_manager.descriptionWhether the new item stack net manager is enabled for server authoritative inventory. This will eventually be required.


////
//// define
Server version：[<!-- md:samp string -->](../types/string.md)

- 特殊类型。protocol.packet.startgamepacket.server_version.descriptionFor telemetry purposes - sending your own string with your own server 'name' and version here would be useful for Mojang's telemetry.


////
//// define
Player Property Data：[<!-- md:samp CompoundTag -->](../types/compoundtag.md)

- 特殊类型。protocol.packet.startgamepacket.player_property_data.descriptionlike SyncActorPropertyPacket, specifically for minecraft:player properties


////
//// define
Server Block Type Registry Checksum：<!-- md:samp unsigned int64 -->

- 基本类型。protocol.packet.startgamepacket.server_block_type_registry_checksum.descriptionChecksum for detecting mismatches in block types between server and client.


////
//// define
World Template ID：[<!-- md:samp mce::UUID -->](../types/mce__uuid.md)

- 特殊类型。protocol.packet.startgamepacket.world_template_id.description


////
//// define
Server Enabled ClientSide Generation：<!-- md:samp bool -->

- 基本类型。protocol.packet.startgamepacket.server_enabled_clientside_generation.descriptionBiomeComponentFactory needs to know about this toggle before we start parsing BiomeComponents


////
//// define
BlockNetworkIds Are Hashes：<!-- md:samp bool -->

- 基本类型。protocol.packet.startgamepacket.blocknetworkids_are_hashes.description


////
//// define
NetworkPermissions：[<!-- md:samp NetworkPermissions -->](../types/networkpermissions.md)

- 特殊类型。protocol.packet.startgamepacket.networkpermissions.description


////

///

