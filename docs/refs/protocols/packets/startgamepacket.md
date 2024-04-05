# <!-- md:samp StartGamePacket -->

> 文档版本：r/20_u7<br/>协议版本：662

<!-- md:samp StartGamePacket -->数据包，数字ID是`11`。

## 结构

```viz
digraph StartGamePacket {
	graph [rankdir=LR];
	{
		graph [rank=max];
		5	[comment="name: \"ActorUniqueID\", typeName: \"\", id: 5, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=ActorUniqueID];
		10	[comment="name: \"ActorRuntimeID\", typeName: \"\", id: 10, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=ActorRuntimeID];
		12	[comment="name: \"varint\", typeName: \"\", id: 12, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=varint];
		14	[comment="name: \"Vec3\", typeName: \"\", id: 14, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=Vec3];
		21	[comment="name: \"Vec2\", typeName: \"\", id: 21, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=Vec2];
		137	[comment="name: \"LevelSettings\", typeName: \"\", id: 137, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=LevelSettings];
		139	[comment="name: \"string\", typeName: \"\", id: 139, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=string];
		141	[comment="name: \"string\", typeName: \"\", id: 141, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=string];
		143	[comment="name: \"string\", typeName: \"\", id: 143, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=string];
		145	[comment="name: \"bool\", typeName: \"\", id: 145, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=bool];
		154	[comment="name: \"SyncedPlayerMovementSettings\", typeName: \"\", id: 154, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=SyncedPlayerMovementSettings];
		156	[comment="name: \"unsigned int64\", typeName: \"\", id: 156, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label="unsigned int64"];
		158	[comment="name: \"varint\", typeName: \"\", id: 158, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=varint];
		161	[comment="name: \"unsigned varint\", typeName: \"\", id: 161, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label="unsigned varint"];
		164	[comment="name: \"string\", typeName: \"\", id: 164, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=string];
		166	[comment="name: \"CompoundTag\", typeName: \"\", id: 166, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=CompoundTag];
		169	[comment="name: \"unsigned varint\", typeName: \"\", id: 169, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label="unsigned varint"];
		179	[comment="name: \"ItemData\", typeName: \"\", id: 179, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=ItemData];
		181	[comment="name: \"string\", typeName: \"\", id: 181, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=string];
		183	[comment="name: \"bool\", typeName: \"\", id: 183, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=bool];
		185	[comment="name: \"string\", typeName: \"\", id: 185, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=string];
		187	[comment="name: \"CompoundTag\", typeName: \"\", id: 187, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=CompoundTag];
		189	[comment="name: \"unsigned int64\", typeName: \"\", id: 189, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label="unsigned int64"];
		191	[comment="name: \"mce::UUID\", typeName: \"\", id: 191, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label="mce::UUID"];
		193	[comment="name: \"bool\", typeName: \"\", id: 193, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=bool];
		195	[comment="name: \"bool\", typeName: \"\", id: 195, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=bool];
		200	[comment="name: \"NetworkPermissions\", typeName: \"\", id: 200, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=NetworkPermissions];
	}
	0	[comment="name: \"StartGamePacket\", typeName: \"\", id: 0, branchId: 11, recurseId: -1, attributes: 0, notes: \"\"",
		label=StartGamePacket];
	1	[comment="name: \"Target Actor ID\", typeName: \"ActorUniqueID\", id: 1, branchId: 0, recurseId: -1, attributes: 256, notes: \"\"",
		label="Target Actor ID"];
	0 -> 1;
	6	[comment="name: \"Target Runtime ID\", typeName: \"ActorRuntimeID\", id: 6, branchId: 0, recurseId: -1, attributes: 256, notes: \"\"",
		label="Target Runtime ID"];
	0 -> 6;
	11	[comment="name: \"Actor Game Type\", typeName: \"\", id: 11, branchId: 0, recurseId: -1, attributes: 0, notes: \"enumeration: GameType\"",
		label="Actor Game Type"];
	0 -> 11;
	13	[comment="name: \"Position\", typeName: \"Vec3\", id: 13, branchId: 0, recurseId: -1, attributes: 256, notes: \"\"",
		label=Position];
	0 -> 13;
	15	[comment="name: \"Rotation\", typeName: \"Vec2\", id: 15, branchId: 0, recurseId: -1, attributes: 256, notes: \"\"",
		label=Rotation];
	0 -> 15;
	22	[comment="name: \"Settings\", typeName: \"LevelSettings\", id: 22, branchId: 0, recurseId: -1, attributes: 256, notes: \"\"",
		label=Settings];
	0 -> 22;
	138	[comment="name: \"Level ID\", typeName: \"\", id: 138, branchId: 0, recurseId: -1, attributes: 0, notes: \"\"",
		label="Level ID"];
	0 -> 138;
	140	[comment="name: \"Level Name\", typeName: \"\", id: 140, branchId: 0, recurseId: -1, attributes: 0, notes: \"\"",
		label="Level Name"];
	0 -> 140;
	142	[comment="name: \"Template Content Identity\", typeName: \"\", id: 142, branchId: 0, recurseId: -1, attributes: 0, notes: \"\"",
		label="Template Content Identity"];
	0 -> 142;
	144	[comment="name: \"Is Trial?\", typeName: \"\", id: 144, branchId: 0, recurseId: -1, attributes: 0, notes: \"\"",
		label="Is Trial?"];
	0 -> 144;
	146	[comment="name: \"Movement Settings\", typeName: \"SyncedPlayerMovementSettings\", id: 146, branchId: 0, recurseId: -1, attributes: 256, notes: \"\"",
		label="Movement Settings"];
	0 -> 146;
	155	[comment="name: \"Current Level Time\", typeName: \"\", id: 155, branchId: 0, recurseId: -1, attributes: 0, notes: \"\"",
		label="Current Level Time"];
	0 -> 155;
	157	[comment="name: \"Enchantment Seed\", typeName: \"\", id: 157, branchId: 0, recurseId: -1, attributes: 0, notes: \"\"",
		label="Enchantment Seed"];
	0 -> 157;
	159	[comment="name: \"Block Properties\", typeName: \"\", id: 159, branchId: 0, recurseId: -1, attributes: 8, notes: \"\"",
		label="Block Properties"];
	0 -> 159;
	167	[comment="name: \"Item List - every vanilla item must be present\", typeName: \"\", id: 167, branchId: 0, recurseId: -1, attributes: 8, notes: \"\"",
		label="Item List - every vanilla item must be present"];
	0 -> 167;
	180	[comment="name: \"Multiplayer Correlation Id\", typeName: \"\", id: 180, branchId: 0, recurseId: -1, attributes: 0, notes: \"A UUID to identify \
this multiplayer session.\"",
		label="Multiplayer Correlation Id"];
	0 -> 180;
	182	[comment="name: \"Enable Item Stack Net Manager\", typeName: \"\", id: 182, branchId: 0, recurseId: -1, attributes: 0, notes: \"Whether the new \
item stack net manager is enabled for server authoritative inventory. This will eventually be required.\"",
		label="Enable Item Stack Net Manager"];
	0 -> 182;
	184	[comment="name: \"Server version\", typeName: \"\", id: 184, branchId: 0, recurseId: -1, attributes: 0, notes: \"For telemetry purposes - sending \
your own string with your own server name and version here would be useful for Mojang's telemetry.\"",
		label="Server version"];
	0 -> 184;
	186	[comment="name: \"Player Property Data\", typeName: \"CompoundTag\", id: 186, branchId: 0, recurseId: -1, attributes: 256, notes: \"like SyncActorPropertyPacket, \
specifically for minecraft:player properties\"",
		label="Player Property Data"];
	0 -> 186;
	188	[comment="name: \"Server Block Type Registry Checksum\", typeName: \"\", id: 188, branchId: 0, recurseId: -1, attributes: 0, notes: \"Checksum \
for detecting mismatches in block types between server and client.\"",
		label="Server Block Type Registry Checksum"];
	0 -> 188;
	190	[comment="name: \"World Template ID\", typeName: \"mce::UUID\", id: 190, branchId: 0, recurseId: -1, attributes: 256, notes: \"\"",
		label="World Template ID"];
	0 -> 190;
	192	[comment="name: \"Server Enabled ClientSide Generation\", typeName: \"\", id: 192, branchId: 0, recurseId: -1, attributes: 0, notes: \"BiomeComponentFactory \
needs to know about this toggle before we start parsing BiomeComponents\"",
		label="Server Enabled ClientSide Generation"];
	0 -> 192;
	194	[comment="name: \"BlockNetworkIds Are Hashes\", typeName: \"\", id: 194, branchId: 0, recurseId: -1, attributes: 0, notes: \"\"",
		label="BlockNetworkIds Are Hashes"];
	0 -> 194;
	196	[comment="name: \"NetworkPermissions\", typeName: \"NetworkPermissions\", id: 196, branchId: 0, recurseId: -1, attributes: 256, notes: \"\"",
		label=NetworkPermissions];
	0 -> 196;
	1 -> 5;
	6 -> 10;
	11 -> 12;
	13 -> 14;
	15 -> 21;
	22 -> 137;
	138 -> 139;
	140 -> 141;
	142 -> 143;
	144 -> 145;
	146 -> 154;
	155 -> 156;
	157 -> 158;
	160	[comment="name: \"Array Size\", typeName: \"\", id: 160, branchId: 0, recurseId: -1, attributes: 0, notes: \"\"",
		label="Array Size"];
	159 -> 160;
	162	[comment="name: \"example element\", typeName: \"\", id: 162, branchId: 0, recurseId: -1, attributes: 16, notes: \"\"",
		label="example element",
		style=dotted];
	159 -> 162;
	160 -> 161;
	163	[comment="name: \"Block Name\", typeName: \"\", id: 163, branchId: 0, recurseId: -1, attributes: 0, notes: \"\"",
		label="Block Name"];
	162 -> 163;
	165	[comment="name: \"Block Definition\", typeName: \"CompoundTag\", id: 165, branchId: 0, recurseId: -1, attributes: 256, notes: \"Map of block states. { \
key (component name):[label,value] } (Can be left empty.)\"",
		label="Block Definition"];
	162 -> 165;
	163 -> 164;
	165 -> 166;
	168	[comment="name: \"Array Size\", typeName: \"\", id: 168, branchId: 0, recurseId: -1, attributes: 0, notes: \"\"",
		label="Array Size"];
	167 -> 168;
	170	[comment="name: \"example element\", typeName: \"\", id: 170, branchId: 0, recurseId: -1, attributes: 16, notes: \"\"",
		label="example element",
		style=dotted];
	167 -> 170;
	168 -> 169;
	171	[comment="name: \"Item Info\", typeName: \"ItemData\", id: 171, branchId: 0, recurseId: -1, attributes: 256, notes: \"See: ItemData Type\"",
		label="Item Info"];
	170 -> 171;
	171 -> 179;
	180 -> 181;
	182 -> 183;
	184 -> 185;
	186 -> 187;
	188 -> 189;
	190 -> 191;
	192 -> 193;
	194 -> 195;
	196 -> 200;
}

```

## 字段

/// define
StartGamePacket

Target Actor ID：[<!-- md:samp ActorUniqueID -->](refs/protocols/types/actoruniqueid.md)

- 类型：ActorUniqueID。

Target Runtime ID：[<!-- md:samp ActorRuntimeID -->](refs/protocols/types/actorruntimeid.md)

- 类型：ActorRuntimeID。

Actor Game Type：<!-- md:samp varint -->

- 类型：varint。enumeration: GameType

Position：[<!-- md:samp Vec3 -->](refs/protocols/types/vec3.md)

- 类型：Vec3。

Rotation：[<!-- md:samp Vec2 -->](refs/protocols/types/vec2.md)

- 类型：Vec2。

Settings：[<!-- md:samp LevelSettings -->](refs/protocols/types/levelsettings.md)

- 类型：LevelSettings。

Level ID：<!-- md:samp string -->

- 类型：string。

Level Name：<!-- md:samp string -->

- 类型：string。

Template Content Identity：<!-- md:samp string -->

- 类型：string。

Is Trial?：<!-- md:samp bool -->

- 类型：bool。

Movement Settings：[<!-- md:samp SyncedPlayerMovementSettings -->](refs/protocols/types/syncedplayermovementsettings.md)

- 类型：SyncedPlayerMovementSettings。

Current Level Time：<!-- md:samp unsigned int64 -->

- 类型：unsigned int64。

Enchantment Seed：<!-- md:samp varint -->

- 类型：varint。

Block Properties

Block Properties数组的大小：<!-- md:samp unsigned varint -->

- 类型：unsigned varint。

Block Properties的示例元素

Block Name：<!-- md:samp string -->

- 类型：string。

Block Definition：[<!-- md:samp CompoundTag -->](refs/protocols/types/compoundtag.md)

- 类型：CompoundTag。Map of block states. { key (component 'name'):[label,value] } (Can be left empty.)

Item List - every vanilla item must be present

Item List - every vanilla item must be present数组的大小：<!-- md:samp unsigned varint -->

- 类型：unsigned varint。

Item List - every vanilla item must be present的示例元素

Item Info：[<!-- md:samp ItemData -->](refs/protocols/types/itemdata.md)

- 类型：ItemData。See: ItemData Type

Multiplayer Correlation Id：<!-- md:samp string -->

- 类型：string。A UUID to 'id'entify this multiplayer session.

Enable Item Stack Net Manager：<!-- md:samp bool -->

- 类型：bool。Whether the new item stack net manager is enabled for server authoritative inventory. This will eventually be required.

Server version：<!-- md:samp string -->

- 类型：string。For telemetry purposes - sending your own string with your own server 'name' and version here would be useful for Mojang's telemetry.

Player Property Data：[<!-- md:samp CompoundTag -->](refs/protocols/types/compoundtag.md)

- 类型：CompoundTag。like SyncActorPropertyPacket, specifically for minecraft:player properties

Server Block Type Registry Checksum：<!-- md:samp unsigned int64 -->

- 类型：unsigned int64。Checksum for detecting mismatches in block types between server and client.

World Template ID：[<!-- md:samp mce::UUID -->](refs/protocols/types/mce::uuid.md)

- 类型：mce::UUID。

Server Enabled ClientSide Generation：<!-- md:samp bool -->

- 类型：bool。BiomeComponentFactory needs to know about this toggle before we start parsing BiomeComponents

BlockNetworkIds Are Hashes：<!-- md:samp bool -->

- 类型：bool。

NetworkPermissions：[<!-- md:samp NetworkPermissions -->](refs/protocols/types/networkpermissions.md)

- 类型：NetworkPermissions。


///
