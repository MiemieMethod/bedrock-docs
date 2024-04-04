# <!-- md:samp StructureTemplateDataRequestPacket -->

> 文档版本：r/20_u7<br/>协议版本：662

<!-- md:samp StructureTemplateDataRequestPacket -->数据包，数字ID是`132`。

## 结构

```dot
digraph StructureTemplateDataRequestPacket {
	graph [rankdir=LR];
	{
		graph [rank=max];
		2	[comment="name: \"string\", typeName: \"\", id: 2, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=string];
		4	[comment="name: \"NetworkBlockPosition\", typeName: \"\", id: 4, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=NetworkBlockPosition];
		6	[comment="name: \"StructureSettings\", typeName: \"\", id: 6, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=StructureSettings];
		8	[comment="name: \"byte\", typeName: \"\", id: 8, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=byte];
	}
	0	[comment="name: \"StructureTemplateDataRequestPacket\", typeName: \"\", id: 0, branchId: 132, recurseId: -1, attributes: 0, notes: \"\"",
		label=StructureTemplateDataRequestPacket];
	1	[comment="name: \"Structure Name\", typeName: \"\", id: 1, branchId: 0, recurseId: -1, attributes: 0, notes: \"\"",
		label="Structure Name"];
	0 -> 1;
	3	[comment="name: \"Structure Position\", typeName: \"NetworkBlockPosition\", id: 3, branchId: 0, recurseId: -1, attributes: 256, notes: \"\"",
		label="Structure Position"];
	0 -> 3;
	5	[comment="name: \"Structure Settings\", typeName: \"StructureSettings\", id: 5, branchId: 0, recurseId: -1, attributes: 256, notes: \"\"",
		label="Structure Settings"];
	0 -> 5;
	7	[comment="name: \"Requested Operation\", typeName: \"\", id: 7, branchId: 0, recurseId: -1, attributes: 0, notes: \"enumeration: StructureTemplateRequestOperation\"",
		label="Requested Operation"];
	0 -> 7;
	1 -> 2;
	3 -> 4;
	5 -> 6;
	7 -> 8;
}

```

## 字段

/// define
StructureTemplateDataRequestPacket

Structure Name：<!-- md:samp string -->

- 类型：string。

Structure Position：[<!-- md:samp NetworkBlockPosition -->](refs/protocols/types/NetworkBlockPosition.md)

- 类型：NetworkBlockPosition。

Structure Settings：[<!-- md:samp StructureSettings -->](refs/protocols/types/StructureSettings.md)

- 类型：StructureSettings。

Requested Operation：<!-- md:samp byte -->

- 类型：byte。enumeration: StructureTemplateRequestOperation


///
