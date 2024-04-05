# <!-- md:samp BookEditPacket -->

> 文档版本：r/20_u7<br/>协议版本：662

<!-- md:samp BookEditPacket -->数据包，数字ID是`97`。

## 结构

```viz
digraph BookEditPacket {
	graph [rankdir=LR];
	{
		graph [rank=max];
		2	[comment="name: \"byte\", typeName: \"\", id: 2, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=byte];
		4	[comment="name: \"byte\", typeName: \"\", id: 4, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=byte];
		8	[comment="name: \"byte\", typeName: \"\", id: 8, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=byte];
		10	[comment="name: \"string\", typeName: \"\", id: 10, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=string];
		12	[comment="name: \"string\", typeName: \"\", id: 12, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=string];
		15	[comment="name: \"byte\", typeName: \"\", id: 15, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=byte];
		17	[comment="name: \"string\", typeName: \"\", id: 17, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=string];
		19	[comment="name: \"string\", typeName: \"\", id: 19, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=string];
		22	[comment="name: \"byte\", typeName: \"\", id: 22, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=byte];
		25	[comment="name: \"byte\", typeName: \"\", id: 25, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=byte];
		27	[comment="name: \"byte\", typeName: \"\", id: 27, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=byte];
		30	[comment="name: \"string\", typeName: \"\", id: 30, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=string];
		32	[comment="name: \"string\", typeName: \"\", id: 32, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=string];
		34	[comment="name: \"string\", typeName: \"\", id: 34, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=string];
	}
	0	[comment="name: \"BookEditPacket\", typeName: \"\", id: 0, branchId: 97, recurseId: -1, attributes: 0, notes: \"\"",
		label=BookEditPacket];
	1	[comment="name: \"Action\", typeName: \"\", id: 1, branchId: 0, recurseId: -1, attributes: 0, notes: \"enumeration: BookEditAction\"",
		label=Action];
	0 -> 1;
	3	[comment="name: \"Book Slot\", typeName: \"\", id: 3, branchId: 0, recurseId: -1, attributes: 0, notes: \"\"",
		label="Book Slot"];
	0 -> 3;
	5	[comment="name: \"Dependency on 'Action'\", typeName: \"\", id: 5, branchId: 0, recurseId: -1, attributes: 2, notes: \"\"",
		label="Dependency on 'Action'",
		shape=note];
	0 -> 5;
	1 -> 2;
	3 -> 4;
	6	[comment="name: \"if (0)\", typeName: \"\", id: 6, branchId: 0, recurseId: -1, attributes: 4, notes: \"\"",
		label="if (0)",
		shape=diamond];
	5 -> 6;
	13	[comment="name: \"if (1)\", typeName: \"\", id: 13, branchId: 1, recurseId: -1, attributes: 4, notes: \"\"",
		label="if (1)",
		shape=diamond];
	5 -> 13;
	20	[comment="name: \"if (2)\", typeName: \"\", id: 20, branchId: 2, recurseId: -1, attributes: 4, notes: \"\"",
		label="if (2)",
		shape=diamond];
	5 -> 20;
	23	[comment="name: \"if (3)\", typeName: \"\", id: 23, branchId: 3, recurseId: -1, attributes: 4, notes: \"\"",
		label="if (3)",
		shape=diamond];
	5 -> 23;
	28	[comment="name: \"if (4)\", typeName: \"\", id: 28, branchId: 4, recurseId: -1, attributes: 4, notes: \"\"",
		label="if (4)",
		shape=diamond];
	5 -> 28;
	7	[comment="name: \"Page Index\", typeName: \"\", id: 7, branchId: 0, recurseId: -1, attributes: 0, notes: \"\"",
		label="Page Index"];
	6 -> 7;
	9	[comment="name: \"Text A\", typeName: \"\", id: 9, branchId: 0, recurseId: -1, attributes: 0, notes: \"\"",
		label="Text A"];
	6 -> 9;
	11	[comment="name: \"Text B\", typeName: \"\", id: 11, branchId: 0, recurseId: -1, attributes: 0, notes: \"\"",
		label="Text B"];
	6 -> 11;
	7 -> 8;
	9 -> 10;
	11 -> 12;
	14	[comment="name: \"Page Index\", typeName: \"\", id: 14, branchId: 0, recurseId: -1, attributes: 0, notes: \"\"",
		label="Page Index"];
	13 -> 14;
	16	[comment="name: \"Text A\", typeName: \"\", id: 16, branchId: 0, recurseId: -1, attributes: 0, notes: \"\"",
		label="Text A"];
	13 -> 16;
	18	[comment="name: \"Text B\", typeName: \"\", id: 18, branchId: 0, recurseId: -1, attributes: 0, notes: \"\"",
		label="Text B"];
	13 -> 18;
	14 -> 15;
	16 -> 17;
	18 -> 19;
	21	[comment="name: \"Page Index\", typeName: \"\", id: 21, branchId: 0, recurseId: -1, attributes: 0, notes: \"\"",
		label="Page Index"];
	20 -> 21;
	21 -> 22;
	24	[comment="name: \"Page Index A\", typeName: \"\", id: 24, branchId: 0, recurseId: -1, attributes: 0, notes: \"\"",
		label="Page Index A"];
	23 -> 24;
	26	[comment="name: \"Page Index B\", typeName: \"\", id: 26, branchId: 0, recurseId: -1, attributes: 0, notes: \"\"",
		label="Page Index B"];
	23 -> 26;
	24 -> 25;
	26 -> 27;
	29	[comment="name: \"Text A\", typeName: \"\", id: 29, branchId: 0, recurseId: -1, attributes: 0, notes: \"\"",
		label="Text A"];
	28 -> 29;
	31	[comment="name: \"Text B\", typeName: \"\", id: 31, branchId: 0, recurseId: -1, attributes: 0, notes: \"\"",
		label="Text B"];
	28 -> 31;
	33	[comment="name: \"XUID\", typeName: \"\", id: 33, branchId: 0, recurseId: -1, attributes: 0, notes: \"\"",
		label=XUID];
	28 -> 33;
	29 -> 30;
	31 -> 32;
	33 -> 34;
}

```

## 字段

/// define
BookEditPacket

Action：<!-- md:samp byte -->

- 类型：byte。enumeration: BookEditAction

Book Slot：<!-- md:samp byte -->

- 类型：byte。

Dependency on 'Action'

//// tab | if (0)
///// define
if (0)

Page Index：<!-- md:samp byte -->

- 类型：byte。

Text A：<!-- md:samp string -->

- 类型：string。

Text B：<!-- md:samp string -->

- 类型：string。


/////

////

//// tab | if (1)
///// define
if (1)

Page Index：<!-- md:samp byte -->

- 类型：byte。

Text A：<!-- md:samp string -->

- 类型：string。

Text B：<!-- md:samp string -->

- 类型：string。


/////

////

//// tab | if (2)
///// define
if (2)

Page Index：<!-- md:samp byte -->

- 类型：byte。


/////

////

//// tab | if (3)
///// define
if (3)

Page Index A：<!-- md:samp byte -->

- 类型：byte。

Page Index B：<!-- md:samp byte -->

- 类型：byte。


/////

////

//// tab | if (4)
///// define
if (4)

Text A：<!-- md:samp string -->

- 类型：string。

Text B：<!-- md:samp string -->

- 类型：string。

XUID：<!-- md:samp string -->

- 类型：string。


/////

////



///
