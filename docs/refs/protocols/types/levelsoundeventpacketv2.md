# <!-- md:samp LevelSoundEventPacketV2 -->

> 文档版本：r/20_u7<br/>协议版本：662

<!-- md:samp LevelSoundEventPacketV2 -->类型，数字ID是`120`。

## 结构

```viz
digraph LevelSoundEventPacketV2 {
	graph [rankdir=LR];
	{
		graph [rank=max];
		2	[comment="name: \"byte\", typeName: \"\", id: 2, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=byte];
		4	[comment="name: \"Vec3\", typeName: \"\", id: 4, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=Vec3];
		6	[comment="name: \"varint\", typeName: \"\", id: 6, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=varint];
		8	[comment="name: \"string\", typeName: \"\", id: 8, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=string];
		10	[comment="name: \"bool\", typeName: \"\", id: 10, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=bool];
		12	[comment="name: \"bool\", typeName: \"\", id: 12, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=bool];
	}
	0	[comment="name: \"LevelSoundEventPacketV2\", typeName: \"\", id: 0, branchId: 120, recurseId: -1, attributes: 0, notes: \"\"",
		label=LevelSoundEventPacketV2];
	1	[comment="name: \"Event ID\", typeName: \"\", id: 1, branchId: 0, recurseId: -1, attributes: 0, notes: \"enumeration: Puv::Legacy::LevelSoundEvent\"",
		label="Event ID"];
	0 -> 1;
	3	[comment="name: \"Position\", typeName: \"Vec3\", id: 3, branchId: 0, recurseId: -1, attributes: 256, notes: \"\"",
		label=Position];
	0 -> 3;
	5	[comment="name: \"Data\", typeName: \"\", id: 5, branchId: 0, recurseId: -1, attributes: 0, notes: \"\"",
		label=Data];
	0 -> 5;
	7	[comment="name: \"Actor Identifier\", typeName: \"\", id: 7, branchId: 0, recurseId: -1, attributes: 0, notes: \"\"",
		label="Actor Identifier"];
	0 -> 7;
	9	[comment="name: \"Baby Mob\", typeName: \"\", id: 9, branchId: 0, recurseId: -1, attributes: 0, notes: \"\"",
		label="Baby Mob"];
	0 -> 9;
	11	[comment="name: \"Global\", typeName: \"\", id: 11, branchId: 0, recurseId: -1, attributes: 0, notes: \"\"",
		label=Global];
	0 -> 11;
	1 -> 2;
	3 -> 4;
	5 -> 6;
	7 -> 8;
	9 -> 10;
	11 -> 12;
}

```

## 字段

/// define
LevelSoundEventPacketV2

Event ID：<!-- md:samp byte -->

- 类型：byte。enumeration: Puv::Legacy::LevelSoundEvent

Position：[<!-- md:samp Vec3 -->](../types/vec3.md)

- 类型：Vec3。

Data：<!-- md:samp varint -->

- 类型：varint。

Actor Identifier：<!-- md:samp string -->

- 类型：string。

Baby Mob：<!-- md:samp bool -->

- 类型：bool。

Global：<!-- md:samp bool -->

- 类型：bool。


///
