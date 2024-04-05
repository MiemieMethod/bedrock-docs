# <!-- md:samp BaseDescription -->

> 文档版本：r/20_u7<br/>协议版本：662

<!-- md:samp BaseDescription -->类型。

## 结构

```viz
digraph BaseDescription {
	graph [rankdir=LR];
	{
		graph [rank=max];
		4	[comment="name: \"string\", typeName: \"\", id: 4, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=string];
		6	[comment="name: \"unsigned short\", typeName: \"\", id: 6, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label="unsigned short"];
		9	[comment="name: \"string\", typeName: \"\", id: 9, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=string];
		11	[comment="name: \"byte\", typeName: \"\", id: 11, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=byte];
		14	[comment="name: \"string\", typeName: \"\", id: 14, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=string];
		17	[comment="name: \"string\", typeName: \"\", id: 17, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=string];
		19	[comment="name: \"unsigned short\", typeName: \"\", id: 19, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label="unsigned short"];
	}
	1	[comment="name: \"BaseDescription\", typeName: \"\", id: 1, branchId: 0, recurseId: -1, attributes: 0, notes: \"\"",
		label=BaseDescription];
	2	[comment="name: \"Internal ItemDescriptor\", typeName: \"\", id: 2, branchId: 0, recurseId: -1, attributes: 0, notes: \"\"",
		label="Internal ItemDescriptor"];
	1 -> 2;
	7	[comment="name: \"Molang Descriptor\", typeName: \"\", id: 7, branchId: 0, recurseId: -1, attributes: 0, notes: \"\"",
		label="Molang Descriptor"];
	1 -> 7;
	12	[comment="name: \"ItemTag Descriptor\", typeName: \"\", id: 12, branchId: 0, recurseId: -1, attributes: 0, notes: \"\"",
		label="ItemTag Descriptor"];
	1 -> 12;
	15	[comment="name: \"Deferred Descriptor\", typeName: \"\", id: 15, branchId: 0, recurseId: -1, attributes: 0, notes: \"\"",
		label="Deferred Descriptor"];
	1 -> 15;
	3	[comment="name: \"Full Name\", typeName: \"\", id: 3, branchId: 0, recurseId: -1, attributes: 0, notes: \"\"",
		label="Full Name"];
	2 -> 3;
	5	[comment="name: \"Aux Value\", typeName: \"\", id: 5, branchId: 0, recurseId: -1, attributes: 0, notes: \"\"",
		label="Aux Value"];
	2 -> 5;
	3 -> 4;
	5 -> 6;
	8	[comment="name: \"Full Name\", typeName: \"\", id: 8, branchId: 0, recurseId: -1, attributes: 0, notes: \"\"",
		label="Full Name"];
	7 -> 8;
	10	[comment="name: \"Molang Version\", typeName: \"\", id: 10, branchId: 0, recurseId: -1, attributes: 0, notes: \"enumeration: MolangVersion\"",
		label="Molang Version"];
	7 -> 10;
	8 -> 9;
	10 -> 11;
	13	[comment="name: \"Item Tag\", typeName: \"\", id: 13, branchId: 0, recurseId: -1, attributes: 0, notes: \"\"",
		label="Item Tag"];
	12 -> 13;
	13 -> 14;
	16	[comment="name: \"Full Name\", typeName: \"\", id: 16, branchId: 0, recurseId: -1, attributes: 0, notes: \"\"",
		label="Full Name"];
	15 -> 16;
	18	[comment="name: \"Aux Value\", typeName: \"\", id: 18, branchId: 0, recurseId: -1, attributes: 0, notes: \"\"",
		label="Aux Value"];
	15 -> 18;
	16 -> 17;
	18 -> 19;
}

```

## 字段

/// define
BaseDescription

Internal ItemDescriptor

Full Name：<!-- md:samp string -->

- 类型：string。

Aux Value：<!-- md:samp unsigned short -->

- 类型：unsigned short。

Molang Descriptor

Molang Version：<!-- md:samp byte -->

- 类型：byte。enumeration: MolangVersion

ItemTag Descriptor

Item Tag：<!-- md:samp string -->

- 类型：string。

Deferred Descriptor


///
