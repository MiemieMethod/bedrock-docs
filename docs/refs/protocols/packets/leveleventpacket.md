# <!-- md:samp LevelEventPacket -->

> 文档版本：r/20_u7<br/>协议版本：662

<!-- md:samp LevelEventPacket -->数据包，数字ID是`25`。

## 结构

```viz
digraph LevelEventPacket {
	graph [rankdir=LR];
	{
		graph [rank=max];
		2	[comment="name: \"varint\", typeName: \"\", id: 2, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=varint];
		4	[comment="name: \"Vec3\", typeName: \"\", id: 4, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=Vec3];
		6	[comment="name: \"varint\", typeName: \"\", id: 6, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=varint];
	}
	0	[comment="name: \"LevelEventPacket\", typeName: \"\", id: 0, branchId: 25, recurseId: -1, attributes: 0, notes: \"\"",
		label=LevelEventPacket];
	1	[comment="name: \"Event ID\", typeName: \"\", id: 1, branchId: 0, recurseId: -1, attributes: 0, notes: \"enumeration: LevelEvent\"",
		label="Event ID"];
	0 -> 1;
	3	[comment="name: \"Position\", typeName: \"Vec3\", id: 3, branchId: 0, recurseId: -1, attributes: 256, notes: \"Note about Event ID: Legacy particles \
use the @enums.html#Particle Type@  enum |ed with ParticleLegacyEvent(0x4000)\"",
		label=Position];
	0 -> 3;
	5	[comment="name: \"Data\", typeName: \"\", id: 5, branchId: 0, recurseId: -1, attributes: 0, notes: \"\"",
		label=Data];
	0 -> 5;
	1 -> 2;
	3 -> 4;
	5 -> 6;
}

```

## 字段

/// define
LevelEventPacket

Event ID：<!-- md:samp varint -->

- 类型：varint。enumeration: LevelEvent

Position：[<!-- md:samp Vec3 -->](../types/vec3.md)

- 类型：Vec3。Note about Event ID: Legacy particles use the @enums.html#Particle Type@  enum |ed with ParticleLegacyEvent(0x4000)

Data：<!-- md:samp varint -->

- 类型：varint。


///
