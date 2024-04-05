# <!-- md:samp TextPacket -->

> 文档版本：r/20_u7<br/>协议版本：662

<!-- md:samp TextPacket -->数据包，数字ID是`9`。

## 结构

```viz
digraph TextPacket {
	graph [rankdir=LR];
	{
		graph [rank=max];
		2	[comment="name: \"byte\", typeName: \"\", id: 2, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=byte];
		4	[comment="name: \"bool\", typeName: \"\", id: 4, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=bool];
		8	[comment="name: \"string\", typeName: \"\", id: 8, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=string];
		11	[comment="name: \"string\", typeName: \"\", id: 11, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=string];
		13	[comment="name: \"string\", typeName: \"\", id: 13, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=string];
		16	[comment="name: \"string\", typeName: \"\", id: 16, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=string];
		19	[comment="name: \"unsigned varint\", typeName: \"\", id: 19, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label="unsigned varint"];
		22	[comment="name: \"string\", typeName: \"\", id: 22, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=string];
		25	[comment="name: \"string\", typeName: \"\", id: 25, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=string];
		28	[comment="name: \"unsigned varint\", typeName: \"\", id: 28, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label="unsigned varint"];
		31	[comment="name: \"string\", typeName: \"\", id: 31, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=string];
		34	[comment="name: \"string\", typeName: \"\", id: 34, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=string];
		37	[comment="name: \"unsigned varint\", typeName: \"\", id: 37, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label="unsigned varint"];
		40	[comment="name: \"string\", typeName: \"\", id: 40, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=string];
		43	[comment="name: \"string\", typeName: \"\", id: 43, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=string];
		46	[comment="name: \"string\", typeName: \"\", id: 46, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=string];
		49	[comment="name: \"string\", typeName: \"\", id: 49, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=string];
		51	[comment="name: \"string\", typeName: \"\", id: 51, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=string];
		54	[comment="name: \"string\", typeName: \"\", id: 54, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=string];
		56	[comment="name: \"string\", typeName: \"\", id: 56, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=string];
		59	[comment="name: \"string\", typeName: \"\", id: 59, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=string];
		62	[comment="name: \"string\", typeName: \"\", id: 62, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=string];
		65	[comment="name: \"string\", typeName: \"\", id: 65, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=string];
		67	[comment="name: \"string\", typeName: \"\", id: 67, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=string];
		69	[comment="name: \"string\", typeName: \"\", id: 69, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=string];
	}
	0	[comment="name: \"TextPacket\", typeName: \"\", id: 0, branchId: 9, recurseId: -1, attributes: 0, notes: \"\"",
		label=TextPacket];
	1	[comment="name: \"Message Type\", typeName: \"\", id: 1, branchId: 0, recurseId: -1, attributes: 0, notes: \"enumeration: TextPacketType\"",
		label="Message Type"];
	0 -> 1;
	3	[comment="name: \"Localize?\", typeName: \"\", id: 3, branchId: 0, recurseId: -1, attributes: 0, notes: \"\"",
		label="Localize?"];
	0 -> 3;
	5	[comment="name: \"Dependency on 'Message Type'\", typeName: \"\", id: 5, branchId: 0, recurseId: -1, attributes: 2, notes: \"\"",
		label="Dependency on 'Message Type'",
		shape=note];
	0 -> 5;
	66	[comment="name: \"Sender's XUID\", typeName: \"\", id: 66, branchId: 0, recurseId: -1, attributes: 0, notes: \"\"",
		label="Sender's XUID"];
	0 -> 66;
	68	[comment="name: \"Platform Id\", typeName: \"\", id: 68, branchId: 0, recurseId: -1, attributes: 0, notes: \"\"",
		label="Platform Id"];
	0 -> 68;
	1 -> 2;
	3 -> 4;
	6	[comment="name: \"if (0)\", typeName: \"\", id: 6, branchId: 0, recurseId: -1, attributes: 4, notes: \"\"",
		label="if (0)",
		shape=diamond];
	5 -> 6;
	9	[comment="name: \"if (1)\", typeName: \"\", id: 9, branchId: 1, recurseId: -1, attributes: 4, notes: \"\"",
		label="if (1)",
		shape=diamond];
	5 -> 9;
	14	[comment="name: \"if (2)\", typeName: \"\", id: 14, branchId: 2, recurseId: -1, attributes: 4, notes: \"\"",
		label="if (2)",
		shape=diamond];
	5 -> 14;
	23	[comment="name: \"if (3)\", typeName: \"\", id: 23, branchId: 3, recurseId: -1, attributes: 4, notes: \"\"",
		label="if (3)",
		shape=diamond];
	5 -> 23;
	32	[comment="name: \"if (4)\", typeName: \"\", id: 32, branchId: 4, recurseId: -1, attributes: 4, notes: \"\"",
		label="if (4)",
		shape=diamond];
	5 -> 32;
	41	[comment="name: \"if (5)\", typeName: \"\", id: 41, branchId: 5, recurseId: -1, attributes: 4, notes: \"\"",
		label="if (5)",
		shape=diamond];
	5 -> 41;
	44	[comment="name: \"if (6)\", typeName: \"\", id: 44, branchId: 6, recurseId: -1, attributes: 4, notes: \"\"",
		label="if (6)",
		shape=diamond];
	5 -> 44;
	47	[comment="name: \"if (7)\", typeName: \"\", id: 47, branchId: 7, recurseId: -1, attributes: 4, notes: \"\"",
		label="if (7)",
		shape=diamond];
	5 -> 47;
	52	[comment="name: \"if (8)\", typeName: \"\", id: 52, branchId: 8, recurseId: -1, attributes: 4, notes: \"\"",
		label="if (8)",
		shape=diamond];
	5 -> 52;
	57	[comment="name: \"if (9)\", typeName: \"\", id: 57, branchId: 9, recurseId: -1, attributes: 4, notes: \"\"",
		label="if (9)",
		shape=diamond];
	5 -> 57;
	60	[comment="name: \"if (10)\", typeName: \"\", id: 60, branchId: 10, recurseId: -1, attributes: 4, notes: \"\"",
		label="if (10)",
		shape=diamond];
	5 -> 60;
	63	[comment="name: \"if (11)\", typeName: \"\", id: 63, branchId: 11, recurseId: -1, attributes: 4, notes: \"\"",
		label="if (11)",
		shape=diamond];
	5 -> 63;
	7	[comment="name: \"Message\", typeName: \"\", id: 7, branchId: 0, recurseId: -1, attributes: 0, notes: \"\"",
		label=Message];
	6 -> 7;
	7 -> 8;
	10	[comment="name: \"Player Name\", typeName: \"\", id: 10, branchId: 0, recurseId: -1, attributes: 0, notes: \"\"",
		label="Player Name"];
	9 -> 10;
	12	[comment="name: \"Message\", typeName: \"\", id: 12, branchId: 0, recurseId: -1, attributes: 0, notes: \"\"",
		label=Message];
	9 -> 12;
	10 -> 11;
	12 -> 13;
	15	[comment="name: \"Message\", typeName: \"\", id: 15, branchId: 0, recurseId: -1, attributes: 0, notes: \"\"",
		label=Message];
	14 -> 15;
	17	[comment="name: \"Parameter List\", typeName: \"\", id: 17, branchId: 0, recurseId: -1, attributes: 8, notes: \"\"",
		label="Parameter List"];
	14 -> 17;
	15 -> 16;
	18	[comment="name: \"Array Size\", typeName: \"\", id: 18, branchId: 0, recurseId: -1, attributes: 0, notes: \"\"",
		label="Array Size"];
	17 -> 18;
	20	[comment="name: \"example element\", typeName: \"\", id: 20, branchId: 0, recurseId: -1, attributes: 16, notes: \"\"",
		label="example element",
		style=dotted];
	17 -> 20;
	18 -> 19;
	21	[comment="name: \"Parameter\", typeName: \"\", id: 21, branchId: 0, recurseId: -1, attributes: 0, notes: \"\"",
		label=Parameter];
	20 -> 21;
	21 -> 22;
	24	[comment="name: \"Message\", typeName: \"\", id: 24, branchId: 0, recurseId: -1, attributes: 0, notes: \"\"",
		label=Message];
	23 -> 24;
	26	[comment="name: \"Parameter List\", typeName: \"\", id: 26, branchId: 0, recurseId: -1, attributes: 8, notes: \"\"",
		label="Parameter List"];
	23 -> 26;
	24 -> 25;
	27	[comment="name: \"Array Size\", typeName: \"\", id: 27, branchId: 0, recurseId: -1, attributes: 0, notes: \"\"",
		label="Array Size"];
	26 -> 27;
	29	[comment="name: \"example element\", typeName: \"\", id: 29, branchId: 0, recurseId: -1, attributes: 16, notes: \"\"",
		label="example element",
		style=dotted];
	26 -> 29;
	27 -> 28;
	30	[comment="name: \"Parameter\", typeName: \"\", id: 30, branchId: 0, recurseId: -1, attributes: 0, notes: \"\"",
		label=Parameter];
	29 -> 30;
	30 -> 31;
	33	[comment="name: \"Message\", typeName: \"\", id: 33, branchId: 0, recurseId: -1, attributes: 0, notes: \"\"",
		label=Message];
	32 -> 33;
	35	[comment="name: \"Parameter List\", typeName: \"\", id: 35, branchId: 0, recurseId: -1, attributes: 8, notes: \"\"",
		label="Parameter List"];
	32 -> 35;
	33 -> 34;
	36	[comment="name: \"Array Size\", typeName: \"\", id: 36, branchId: 0, recurseId: -1, attributes: 0, notes: \"\"",
		label="Array Size"];
	35 -> 36;
	38	[comment="name: \"example element\", typeName: \"\", id: 38, branchId: 0, recurseId: -1, attributes: 16, notes: \"\"",
		label="example element",
		style=dotted];
	35 -> 38;
	36 -> 37;
	39	[comment="name: \"Parameter\", typeName: \"\", id: 39, branchId: 0, recurseId: -1, attributes: 0, notes: \"\"",
		label=Parameter];
	38 -> 39;
	39 -> 40;
	42	[comment="name: \"Message\", typeName: \"\", id: 42, branchId: 0, recurseId: -1, attributes: 0, notes: \"\"",
		label=Message];
	41 -> 42;
	42 -> 43;
	45	[comment="name: \"Message\", typeName: \"\", id: 45, branchId: 0, recurseId: -1, attributes: 0, notes: \"\"",
		label=Message];
	44 -> 45;
	45 -> 46;
	48	[comment="name: \"Player Name\", typeName: \"\", id: 48, branchId: 0, recurseId: -1, attributes: 0, notes: \"\"",
		label="Player Name"];
	47 -> 48;
	50	[comment="name: \"Message\", typeName: \"\", id: 50, branchId: 0, recurseId: -1, attributes: 0, notes: \"\"",
		label=Message];
	47 -> 50;
	48 -> 49;
	50 -> 51;
	53	[comment="name: \"Player Name\", typeName: \"\", id: 53, branchId: 0, recurseId: -1, attributes: 0, notes: \"\"",
		label="Player Name"];
	52 -> 53;
	55	[comment="name: \"Message\", typeName: \"\", id: 55, branchId: 0, recurseId: -1, attributes: 0, notes: \"\"",
		label=Message];
	52 -> 55;
	53 -> 54;
	55 -> 56;
	58	[comment="name: \"Message\", typeName: \"\", id: 58, branchId: 0, recurseId: -1, attributes: 0, notes: \"\"",
		label=Message];
	57 -> 58;
	58 -> 59;
	61	[comment="name: \"Message\", typeName: \"\", id: 61, branchId: 0, recurseId: -1, attributes: 0, notes: \"\"",
		label=Message];
	60 -> 61;
	61 -> 62;
	64	[comment="name: \"Message\", typeName: \"\", id: 64, branchId: 0, recurseId: -1, attributes: 0, notes: \"\"",
		label=Message];
	63 -> 64;
	64 -> 65;
	66 -> 67;
	68 -> 69;
}

```

## 字段

/// define
TextPacket

Message Type：<!-- md:samp byte -->

- 类型：byte。enumeration: TextPacketType

Localize?：<!-- md:samp bool -->

- 类型：bool。

Dependency on 'Message Type'

//// tab | if (0)
///// define
if (0)

Message：<!-- md:samp string -->

- 类型：string。


/////

////

//// tab | if (1)
///// define
if (1)

Player Name：<!-- md:samp string -->

- 类型：string。

Message：<!-- md:samp string -->

- 类型：string。


/////

////

//// tab | if (2)
///// define
if (2)

Message：<!-- md:samp string -->

- 类型：string。

Parameter List

Parameter List数组的大小：<!-- md:samp unsigned varint -->

- 类型：unsigned varint。

Parameter List的示例元素

Parameter：<!-- md:samp string -->

- 类型：string。


/////

////

//// tab | if (3)
///// define
if (3)

Message：<!-- md:samp string -->

- 类型：string。

Parameter List

Parameter List数组的大小：<!-- md:samp unsigned varint -->

- 类型：unsigned varint。

Parameter List的示例元素

Parameter：<!-- md:samp string -->

- 类型：string。


/////

////

//// tab | if (4)
///// define
if (4)

Message：<!-- md:samp string -->

- 类型：string。

Parameter List

Parameter List数组的大小：<!-- md:samp unsigned varint -->

- 类型：unsigned varint。

Parameter List的示例元素

Parameter：<!-- md:samp string -->

- 类型：string。


/////

////

//// tab | if (5)
///// define
if (5)

Message：<!-- md:samp string -->

- 类型：string。


/////

////

//// tab | if (6)
///// define
if (6)

Message：<!-- md:samp string -->

- 类型：string。


/////

////

//// tab | if (7)
///// define
if (7)

Player Name：<!-- md:samp string -->

- 类型：string。

Message：<!-- md:samp string -->

- 类型：string。


/////

////

//// tab | if (8)
///// define
if (8)

Player Name：<!-- md:samp string -->

- 类型：string。

Message：<!-- md:samp string -->

- 类型：string。


/////

////

//// tab | if (9)
///// define
if (9)

Message：<!-- md:samp string -->

- 类型：string。


/////

////

//// tab | if (10)
///// define
if (10)

Message：<!-- md:samp string -->

- 类型：string。


/////

////

//// tab | if (11)
///// define
if (11)

Message：<!-- md:samp string -->

- 类型：string。


/////

////


Sender's XUID：<!-- md:samp string -->

- 类型：string。

Platform Id：<!-- md:samp string -->

- 类型：string。


///
