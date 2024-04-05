# <!-- md:samp DataItem -->

> 文档版本：r/20_u7<br/>协议版本：662

<!-- md:samp DataItem -->类型。

## 结构

```viz
digraph DataItem {
	graph [rankdir=LR];
	{
		graph [rank=max];
		3	[comment="name: \"unsigned varint\", typeName: \"\", id: 3, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label="unsigned varint"];
		5	[comment="name: \"byte\", typeName: \"\", id: 5, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=byte];
		9	[comment="name: \"byte\", typeName: \"\", id: 9, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=byte];
		12	[comment="name: \"short\", typeName: \"\", id: 12, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=short];
		15	[comment="name: \"varint\", typeName: \"\", id: 15, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=varint];
		18	[comment="name: \"float\", typeName: \"\", id: 18, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=float];
		21	[comment="name: \"string\", typeName: \"\", id: 21, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=string];
		24	[comment="name: \"CompoundTag\", typeName: \"\", id: 24, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=CompoundTag];
		27	[comment="name: \"BlockPos\", typeName: \"\", id: 27, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=BlockPos];
		30	[comment="name: \"varint64\", typeName: \"\", id: 30, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=varint64];
		33	[comment="name: \"Vec3\", typeName: \"\", id: 33, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=Vec3];
	}
	1	[comment="name: \"DataItem\", typeName: \"\", id: 1, branchId: 0, recurseId: -1, attributes: 0, notes: \"\"",
		label=DataItem];
	2	[comment="name: \"ID\", typeName: \"\", id: 2, branchId: 0, recurseId: -1, attributes: 0, notes: \"\"",
		label=ID];
	1 -> 2;
	4	[comment="name: \"Type\", typeName: \"\", id: 4, branchId: 0, recurseId: -1, attributes: 0, notes: \"enumeration: DataItemType\"",
		label=Type];
	1 -> 4;
	6	[comment="name: \"Dependency on 'Type'\", typeName: \"\", id: 6, branchId: 0, recurseId: -1, attributes: 2, notes: \"\"",
		label="Dependency on 'Type'",
		shape=note];
	1 -> 6;
	2 -> 3;
	4 -> 5;
	7	[comment="name: \"if (0)\", typeName: \"\", id: 7, branchId: 0, recurseId: -1, attributes: 4, notes: \"\"",
		label="if (0)",
		shape=diamond];
	6 -> 7;
	10	[comment="name: \"if (1)\", typeName: \"\", id: 10, branchId: 1, recurseId: -1, attributes: 4, notes: \"\"",
		label="if (1)",
		shape=diamond];
	6 -> 10;
	13	[comment="name: \"if (2)\", typeName: \"\", id: 13, branchId: 2, recurseId: -1, attributes: 4, notes: \"\"",
		label="if (2)",
		shape=diamond];
	6 -> 13;
	16	[comment="name: \"if (3)\", typeName: \"\", id: 16, branchId: 3, recurseId: -1, attributes: 4, notes: \"\"",
		label="if (3)",
		shape=diamond];
	6 -> 16;
	19	[comment="name: \"if (4)\", typeName: \"\", id: 19, branchId: 4, recurseId: -1, attributes: 4, notes: \"\"",
		label="if (4)",
		shape=diamond];
	6 -> 19;
	22	[comment="name: \"if (5)\", typeName: \"\", id: 22, branchId: 5, recurseId: -1, attributes: 4, notes: \"\"",
		label="if (5)",
		shape=diamond];
	6 -> 22;
	25	[comment="name: \"if (6)\", typeName: \"\", id: 25, branchId: 6, recurseId: -1, attributes: 4, notes: \"\"",
		label="if (6)",
		shape=diamond];
	6 -> 25;
	28	[comment="name: \"if (7)\", typeName: \"\", id: 28, branchId: 7, recurseId: -1, attributes: 4, notes: \"\"",
		label="if (7)",
		shape=diamond];
	6 -> 28;
	31	[comment="name: \"if (8)\", typeName: \"\", id: 31, branchId: 8, recurseId: -1, attributes: 4, notes: \"\"",
		label="if (8)",
		shape=diamond];
	6 -> 31;
	8	[comment="name: \"Value\", typeName: \"\", id: 8, branchId: 0, recurseId: -1, attributes: 0, notes: \"\"",
		label=Value];
	7 -> 8;
	8 -> 9;
	11	[comment="name: \"Value\", typeName: \"\", id: 11, branchId: 0, recurseId: -1, attributes: 0, notes: \"\"",
		label=Value];
	10 -> 11;
	11 -> 12;
	14	[comment="name: \"Value\", typeName: \"\", id: 14, branchId: 0, recurseId: -1, attributes: 0, notes: \"\"",
		label=Value];
	13 -> 14;
	14 -> 15;
	17	[comment="name: \"Value\", typeName: \"\", id: 17, branchId: 0, recurseId: -1, attributes: 0, notes: \"\"",
		label=Value];
	16 -> 17;
	17 -> 18;
	20	[comment="name: \"Value\", typeName: \"\", id: 20, branchId: 0, recurseId: -1, attributes: 0, notes: \"\"",
		label=Value];
	19 -> 20;
	20 -> 21;
	23	[comment="name: \"Value\", typeName: \"\", id: 23, branchId: 0, recurseId: -1, attributes: 256, notes: \"\"",
		label=Value];
	22 -> 23;
	23 -> 24;
	26	[comment="name: \"Value\", typeName: \"\", id: 26, branchId: 0, recurseId: -1, attributes: 256, notes: \"\"",
		label=Value];
	25 -> 26;
	26 -> 27;
	29	[comment="name: \"Value\", typeName: \"\", id: 29, branchId: 0, recurseId: -1, attributes: 0, notes: \"\"",
		label=Value];
	28 -> 29;
	29 -> 30;
	32	[comment="name: \"Value\", typeName: \"\", id: 32, branchId: 0, recurseId: -1, attributes: 256, notes: \"\"",
		label=Value];
	31 -> 32;
	32 -> 33;
}

```

## 字段

/// define
DataItem

ID：<!-- md:samp unsigned varint -->

- 类型：unsigned varint。

Type：<!-- md:samp byte -->

- 类型：byte。enumeration: DataItemType

Dependency on 'Type'

//// tab | if (0)
///// define
if (0)

Value：<!-- md:samp byte -->

- 类型：byte。


/////

////

//// tab | if (1)
///// define
if (1)

Value：<!-- md:samp short -->

- 类型：short。


/////

////

//// tab | if (2)
///// define
if (2)

Value：<!-- md:samp varint -->

- 类型：varint。


/////

////

//// tab | if (3)
///// define
if (3)

Value：<!-- md:samp float -->

- 类型：float。


/////

////

//// tab | if (4)
///// define
if (4)

Value：<!-- md:samp string -->

- 类型：string。


/////

////

//// tab | if (5)
///// define
if (5)

Value：[<!-- md:samp CompoundTag -->](refs/protocols/types/compoundtag.md)

- 类型：CompoundTag。


/////

////

//// tab | if (6)
///// define
if (6)

Value：[<!-- md:samp BlockPos -->](refs/protocols/types/blockpos.md)

- 类型：BlockPos。


/////

////

//// tab | if (7)
///// define
if (7)

Value：<!-- md:samp varint64 -->

- 类型：varint64。


/////

////

//// tab | if (8)
///// define
if (8)

Value：[<!-- md:samp Vec3 -->](refs/protocols/types/vec3.md)

- 类型：Vec3。


/////

////



///
