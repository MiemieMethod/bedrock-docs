# <!-- md:samp StartGamePacket -->

> 文档版本：r/20_u8<br/>协议版本：671

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
22 -> 139
0 -> 140
140 -> 141
0 -> 142
142 -> 143
0 -> 144
144 -> 145
0 -> 146
146 -> 147
0 -> 148
148 -> 156
0 -> 157
157 -> 158
0 -> 159
159 -> 160
0 -> 161
161 -> 162
162 -> 163
161 -> 164
164 -> 165
165 -> 166
164 -> 167
167 -> 168
0 -> 169
169 -> 170
170 -> 171
169 -> 172
172 -> 173
173 -> 181
0 -> 182
182 -> 183
0 -> 184
184 -> 185
0 -> 186
186 -> 187
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
198 -> 202

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
139 [label="LevelSettings",comment="name: \"LevelSettings\", typeName: \"\", id: 139, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
140 [label="Level ID",comment="name: \"Level ID\", typeName: \"\", id: 140, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
141 [label="string",comment="name: \"string\", typeName: \"\", id: 141, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
142 [label="Level Name",comment="name: \"Level Name\", typeName: \"\", id: 142, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
143 [label="string",comment="name: \"string\", typeName: \"\", id: 143, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
144 [label="Template Content Identity",comment="name: \"Template Content Identity\", typeName: \"\", id: 144, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
145 [label="string",comment="name: \"string\", typeName: \"\", id: 145, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
146 [label="Is Trial?",comment="name: \"Is Trial?\", typeName: \"\", id: 146, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
147 [label="bool",comment="name: \"bool\", typeName: \"\", id: 147, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
148 [label="Movement Settings",comment="name: \"Movement Settings\", typeName: \"SyncedPlayerMovementSettings\", id: 148, branchId: 0, recurseId: -1, attributes: 256, notes: \"\""];
156 [label="SyncedPlayerMovementSettings",comment="name: \"SyncedPlayerMovementSettings\", typeName: \"\", id: 156, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
157 [label="Current Level Time",comment="name: \"Current Level Time\", typeName: \"\", id: 157, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
158 [label="unsigned int64",comment="name: \"unsigned int64\", typeName: \"\", id: 158, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
159 [label="Enchantment Seed",comment="name: \"Enchantment Seed\", typeName: \"\", id: 159, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
160 [label="varint",comment="name: \"varint\", typeName: \"\", id: 160, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
161 [label="Block Properties",comment="name: \"Block Properties\", typeName: \"\", id: 161, branchId: 0, recurseId: -1, attributes: 8, notes: \"\""];
162 [label="Array Size",comment="name: \"Array Size\", typeName: \"\", id: 162, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
163 [label="unsigned varint",comment="name: \"unsigned varint\", typeName: \"\", id: 163, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
164 [label="example element",style=dotted,comment="name: \"example element\", typeName: \"\", id: 164, branchId: 0, recurseId: -1, attributes: 16, notes: \"\""];
165 [label="Block Name",comment="name: \"Block Name\", typeName: \"\", id: 165, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
166 [label="string",comment="name: \"string\", typeName: \"\", id: 166, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
167 [label="Block Definition",comment="name: \"Block Definition\", typeName: \"CompoundTag\", id: 167, branchId: 0, recurseId: -1, attributes: 256, notes: \"Map of block states. { key (component name):[label,value] } (Can be left empty.)\""];
168 [label="CompoundTag",comment="name: \"CompoundTag\", typeName: \"\", id: 168, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
169 [label="Item List - every vanilla item must be present",comment="name: \"Item List - every vanilla item must be present\", typeName: \"\", id: 169, branchId: 0, recurseId: -1, attributes: 8, notes: \"\""];
170 [label="Array Size",comment="name: \"Array Size\", typeName: \"\", id: 170, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
171 [label="unsigned varint",comment="name: \"unsigned varint\", typeName: \"\", id: 171, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
172 [label="example element",style=dotted,comment="name: \"example element\", typeName: \"\", id: 172, branchId: 0, recurseId: -1, attributes: 16, notes: \"\""];
173 [label="Item Info",comment="name: \"Item Info\", typeName: \"ItemData\", id: 173, branchId: 0, recurseId: -1, attributes: 256, notes: \"See: ItemData Type\""];
181 [label="ItemData",comment="name: \"ItemData\", typeName: \"\", id: 181, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
182 [label="Multiplayer Correlation Id",comment="name: \"Multiplayer Correlation Id\", typeName: \"\", id: 182, branchId: 0, recurseId: -1, attributes: 0, notes: \"A UUID to identify this multiplayer session.\""];
183 [label="string",comment="name: \"string\", typeName: \"\", id: 183, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
184 [label="Enable Item Stack Net Manager",comment="name: \"Enable Item Stack Net Manager\", typeName: \"\", id: 184, branchId: 0, recurseId: -1, attributes: 0, notes: \"Whether the new item stack net manager is enabled for server authoritative inventory. This will eventually be required.\""];
185 [label="bool",comment="name: \"bool\", typeName: \"\", id: 185, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
186 [label="Server version",comment="name: \"Server version\", typeName: \"\", id: 186, branchId: 0, recurseId: -1, attributes: 0, notes: \"For telemetry purposes - sending your own string with your own server name and version here would be useful for Mojang's telemetry.\""];
187 [label="string",comment="name: \"string\", typeName: \"\", id: 187, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
188 [label="Player Property Data",comment="name: \"Player Property Data\", typeName: \"CompoundTag\", id: 188, branchId: 0, recurseId: -1, attributes: 256, notes: \"like SyncActorPropertyPacket, specifically for minecraft:player properties\""];
189 [label="CompoundTag",comment="name: \"CompoundTag\", typeName: \"\", id: 189, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
190 [label="Server Block Type Registry Checksum",comment="name: \"Server Block Type Registry Checksum\", typeName: \"\", id: 190, branchId: 0, recurseId: -1, attributes: 0, notes: \"Checksum for detecting mismatches in block types between server and client.\""];
191 [label="unsigned int64",comment="name: \"unsigned int64\", typeName: \"\", id: 191, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
192 [label="World Template ID",comment="name: \"World Template ID\", typeName: \"mce::UUID\", id: 192, branchId: 0, recurseId: -1, attributes: 256, notes: \"\""];
193 [label="mce::UUID",comment="name: \"mce::UUID\", typeName: \"\", id: 193, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
194 [label="Server Enabled ClientSide Generation",comment="name: \"Server Enabled ClientSide Generation\", typeName: \"\", id: 194, branchId: 0, recurseId: -1, attributes: 0, notes: \"BiomeComponentFactory needs to know about this toggle before we start parsing BiomeComponents\""];
195 [label="bool",comment="name: \"bool\", typeName: \"\", id: 195, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
196 [label="BlockNetworkIds Are Hashes",comment="name: \"BlockNetworkIds Are Hashes\", typeName: \"\", id: 196, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
197 [label="bool",comment="name: \"bool\", typeName: \"\", id: 197, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
198 [label="NetworkPermissions",comment="name: \"NetworkPermissions\", typeName: \"NetworkPermissions\", id: 198, branchId: 0, recurseId: -1, attributes: 256, notes: \"\""];
202 [label="NetworkPermissions",comment="name: \"NetworkPermissions\", typeName: \"\", id: 202, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
{ rank = max;5;10;12;14;21;139;141;143;145;147;156;158;160;163;166;168;171;181;183;185;187;189;191;193;195;197;202}

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

