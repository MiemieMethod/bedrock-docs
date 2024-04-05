# <!-- md:samp LevelEventGenericPacket -->

> 文档版本：r/20_u7<br/>协议版本：662

<!-- md:samp LevelEventGenericPacket -->数据包，数字ID是`124`。

## 结构

```viz
digraph LevelEventGenericPacket {
	graph [rankdir=LR];
	{
		graph [rank=max];
		2	[comment="name: \"varint\", typeName: \"\", id: 2, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=varint];
		4	[comment="name: \"CompoundTag\", typeName: \"\", id: 4, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=CompoundTag];
	}
	0	[comment="name: \"LevelEventGenericPacket\", typeName: \"\", id: 0, branchId: 124, recurseId: -1, attributes: 0, notes: \"\"",
		label=LevelEventGenericPacket];
	1	[comment="name: \"Event ID\", typeName: \"\", id: 1, branchId: 0, recurseId: -1, attributes: 0, notes: \"enumeration: LevelEvent\"",
		label="Event ID"];
	0 -> 1;
	3	[comment="name: \"Event Data\", typeName: \"CompoundTag\", id: 3, branchId: 0, recurseId: -1, attributes: 256, notes: \"Note about Event ID: Legacy \
particles use the @enums.html#Particle Type@  enum |ed with ParticleLegacyEvent(0x4000)\"",
		label="Event Data"];
	0 -> 3;
	1 -> 2;
	3 -> 4;
}

```

## 字段

/// define
LevelEventGenericPacket

Event ID：<!-- md:samp varint -->

- 类型：varint。enumeration: LevelEvent

Event Data：[<!-- md:samp CompoundTag -->](../types/compoundtag.md)

- 类型：CompoundTag。Note about Event ID: Legacy particles use the @enums.html#Particle Type@  enum |ed with ParticleLegacyEvent(0x4000)


///
