# <!-- md:samp StructureTemplateDataResponsePacket -->

> 文档版本：r/20_u7<br/>协议版本：662

<!-- md:samp StructureTemplateDataResponsePacket -->数据包，数字ID是`133`。

## 结构

```viz
digraph StructureTemplateDataResponsePacket {
	graph [rankdir=LR];
	{
		graph [rank=max];
		2	[comment="name: \"string\", typeName: \"\", id: 2, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=string];
		6	[comment="name: \"bool\", typeName: \"\", id: 6, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=bool];
		8	[comment="name: \"byte\", typeName: \"\", id: 8, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=byte];
		11	[comment="name: \"bool\", typeName: \"\", id: 11, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=bool];
		13	[comment="name: \"CompoundTag\", typeName: \"\", id: 13, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=CompoundTag];
		15	[comment="name: \"byte\", typeName: \"\", id: 15, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=byte];
	}
	0	[comment="name: \"StructureTemplateDataResponsePacket\", typeName: \"\", id: 0, branchId: 133, recurseId: -1, attributes: 0, notes: \"\"",
		label=StructureTemplateDataResponsePacket];
	1	[comment="name: \"Structure Name\", typeName: \"\", id: 1, branchId: 0, recurseId: -1, attributes: 0, notes: \"\"",
		label="Structure Name"];
	0 -> 1;
	3	[comment="name: \"Dependency on 'Requested structure exists?'\", typeName: \"\", id: 3, branchId: 0, recurseId: -1, attributes: 2, notes: \"\"",
		label="Dependency on 'Requested structure exists?'",
		shape=note];
	0 -> 3;
	1 -> 2;
	4	[comment="name: \"if (0)\", typeName: \"\", id: 4, branchId: 0, recurseId: -1, attributes: 4, notes: \"\"",
		label="if (0)",
		shape=diamond];
	3 -> 4;
	9	[comment="name: \"if (1)\", typeName: \"\", id: 9, branchId: 1, recurseId: -1, attributes: 4, notes: \"\"",
		label="if (1)",
		shape=diamond];
	3 -> 9;
	5	[comment="name: \"Failure\", typeName: \"\", id: 5, branchId: 0, recurseId: -1, attributes: 0, notes: \"Bool set to false, indicating the requested \
structure didn't exist.\"",
		label=Failure];
	4 -> 5;
	7	[comment="name: \"Response Type\", typeName: \"\", id: 7, branchId: 0, recurseId: -1, attributes: 0, notes: \"enumeration: StructureTemplateResponseType\"",
		label="Response Type"];
	4 -> 7;
	5 -> 6;
	7 -> 8;
	10	[comment="name: \"Success\", typeName: \"\", id: 10, branchId: 0, recurseId: -1, attributes: 0, notes: \"Bool set to true, indicating success.\"",
		label=Success];
	9 -> 10;
	12	[comment="name: \"Structure's NBT\", typeName: \"CompoundTag\", id: 12, branchId: 0, recurseId: -1, attributes: 256, notes: \"\"",
		label="Structure's NBT"];
	9 -> 12;
	14	[comment="name: \"Response Type\", typeName: \"\", id: 14, branchId: 0, recurseId: -1, attributes: 0, notes: \"enumeration: StructureTemplateResponseType\"",
		label="Response Type"];
	9 -> 14;
	10 -> 11;
	12 -> 13;
	14 -> 15;
}

```

## 字段

/// define
StructureTemplateDataResponsePacket

Structure Name：<!-- md:samp string -->

- 类型：string。

Dependency on 'Requested structure exists?'

//// tab | if (0)
///// define
if (0)

Failure：<!-- md:samp bool -->

- 类型：bool。Bool set to false, indicating the requested structure d'id'n't exist.

Response Type：<!-- md:samp byte -->

- 类型：byte。enumeration: StructureTemplateResponseType


/////

////

//// tab | if (1)
///// define
if (1)

Success：<!-- md:samp bool -->

- 类型：bool。Bool set to true, indicating success.

Structure's NBT：[<!-- md:samp CompoundTag -->](../types/compoundtag.md)

- 类型：CompoundTag。

Response Type：<!-- md:samp byte -->

- 类型：byte。enumeration: StructureTemplateResponseType


/////

////



///
