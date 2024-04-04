# <!-- md:samp AddVolumeEntityPacket -->

> 文档版本：r/20_u7<br/>协议版本：662

<!-- md:samp AddVolumeEntityPacket -->数据包，数字ID是`166`。

## 结构

```viz
digraph AddVolumeEntityPacket {
	graph [rankdir=LR];
	{
		graph [rank=max];
		5	[comment="name: \"EntityNetId\", typeName: \"\", id: 5, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=EntityNetId];
		7	[comment="name: \"CompoundTag\", typeName: \"\", id: 7, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=CompoundTag];
		9	[comment="name: \"string\", typeName: \"\", id: 9, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=string];
		11	[comment="name: \"string\", typeName: \"\", id: 11, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=string];
		13	[comment="name: \"NetworkBlockPosition\", typeName: \"\", id: 13, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=NetworkBlockPosition];
		15	[comment="name: \"NetworkBlockPosition\", typeName: \"\", id: 15, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=NetworkBlockPosition];
		17	[comment="name: \"varint\", typeName: \"\", id: 17, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=varint];
		19	[comment="name: \"string\", typeName: \"\", id: 19, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=string];
	}
	0	[comment="name: \"AddVolumeEntityPacket\", typeName: \"\", id: 0, branchId: 166, recurseId: -1, attributes: 0, notes: \"\"",
		label=AddVolumeEntityPacket];
	1	[comment="name: \"Entity Network Id\", typeName: \"EntityNetId\", id: 1, branchId: 0, recurseId: -1, attributes: 256, notes: \"\"",
		label="Entity Network Id"];
	0 -> 1;
	6	[comment="name: \"Components\", typeName: \"CompoundTag\", id: 6, branchId: 0, recurseId: -1, attributes: 256, notes: \"\"",
		label=Components];
	0 -> 6;
	8	[comment="name: \"JSON Identifier\", typeName: \"\", id: 8, branchId: 0, recurseId: -1, attributes: 0, notes: \"\"",
		label="JSON Identifier"];
	0 -> 8;
	10	[comment="name: \"Instance Name\", typeName: \"\", id: 10, branchId: 0, recurseId: -1, attributes: 0, notes: \"\"",
		label="Instance Name"];
	0 -> 10;
	12	[comment="name: \"Min Bounds\", typeName: \"NetworkBlockPosition\", id: 12, branchId: 0, recurseId: -1, attributes: 256, notes: \"\"",
		label="Min Bounds"];
	0 -> 12;
	14	[comment="name: \"Max Bounds\", typeName: \"NetworkBlockPosition\", id: 14, branchId: 0, recurseId: -1, attributes: 256, notes: \"\"",
		label="Max Bounds"];
	0 -> 14;
	16	[comment="name: \"Dimension Type\", typeName: \"\", id: 16, branchId: 0, recurseId: -1, attributes: 0, notes: \"\"",
		label="Dimension Type"];
	0 -> 16;
	18	[comment="name: \"Engine Version\", typeName: \"\", id: 18, branchId: 0, recurseId: -1, attributes: 0, notes: \"Semantic version string\"",
		label="Engine Version"];
	0 -> 18;
	1 -> 5;
	6 -> 7;
	8 -> 9;
	10 -> 11;
	12 -> 13;
	14 -> 15;
	16 -> 17;
	18 -> 19;
}

```

## 字段

/// define
AddVolumeEntityPacket

Entity Network Id：[<!-- md:samp EntityNetId -->](refs/protocols/types/EntityNetId.md)

- 类型：EntityNetId。

Components：[<!-- md:samp CompoundTag -->](refs/protocols/types/CompoundTag.md)

- 类型：CompoundTag。

JSON Identifier：<!-- md:samp string -->

- 类型：string。

Instance Name：<!-- md:samp string -->

- 类型：string。

Min Bounds：[<!-- md:samp NetworkBlockPosition -->](refs/protocols/types/NetworkBlockPosition.md)

- 类型：NetworkBlockPosition。

Max Bounds：[<!-- md:samp NetworkBlockPosition -->](refs/protocols/types/NetworkBlockPosition.md)

- 类型：NetworkBlockPosition。

Dimension Type：<!-- md:samp varint -->

- 类型：varint。

Engine Version：<!-- md:samp string -->

- 类型：string。Semantic version string


///
