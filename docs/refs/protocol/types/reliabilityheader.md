# <!-- md:samp Reliability Header -->

> 文档版本：r/20_u7<br/>协议版本：662

<!-- md:samp Reliability Header -->类型。

## 结构

```viz
digraph "Reliability Header" {
	graph [rankdir=LR];
	{
		graph [rank=max];
		2	[comment="name: \"byte\", typeName: \"\", id: 2, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=byte];
		4	[comment="name: \"unsigned short\", typeName: \"\", id: 4, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label="unsigned short"];
		7	[comment="name: \"[No Data]\", typeName: \"\", id: 7, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label="[No Data]"];
		10	[comment="name: \"unsigned int24\", typeName: \"\", id: 10, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label="unsigned int24"];
		12	[comment="name: \"unsigned int24\", typeName: \"\", id: 12, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label="unsigned int24"];
		14	[comment="name: \"byte\", typeName: \"\", id: 14, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=byte];
		17	[comment="name: \"unsigned int24\", typeName: \"\", id: 17, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label="unsigned int24"];
		20	[comment="name: \"unsigned int24\", typeName: \"\", id: 20, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label="unsigned int24"];
		22	[comment="name: \"unsigned int24\", typeName: \"\", id: 22, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label="unsigned int24"];
		24	[comment="name: \"byte\", typeName: \"\", id: 24, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=byte];
		27	[comment="name: \"unsigned int24\", typeName: \"\", id: 27, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label="unsigned int24"];
		29	[comment="name: \"unsigned int24\", typeName: \"\", id: 29, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label="unsigned int24"];
		31	[comment="name: \"unsigned int24\", typeName: \"\", id: 31, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label="unsigned int24"];
		33	[comment="name: \"byte\", typeName: \"\", id: 33, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=byte];
		36	[comment="name: \"[No Data]\", typeName: \"\", id: 36, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label="[No Data]"];
		39	[comment="name: \"unsigned int\", typeName: \"\", id: 39, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label="unsigned int"];
		41	[comment="name: \"unsigned short\", typeName: \"\", id: 41, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label="unsigned short"];
		43	[comment="name: \"unsigned int\", typeName: \"\", id: 43, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label="unsigned int"];
	}
	0	[comment="name: \"Reliability Header\", typeName: \"\", id: 0, branchId: 0, recurseId: -1, attributes: 0, notes: \"\"",
		label="Reliability Header"];
	1	[comment="name: \"Reliability Type (3 bits), is packet split? (1 bit)\", typeName: \"\", id: 1, branchId: 0, recurseId: -1, attributes: 0, notes: \"\"",
		label="Reliability Type (3 bits), is packet split? (1 bit)"];
	0 -> 1;
	3	[comment="name: \"Payload Bit Length\", typeName: \"\", id: 3, branchId: 0, recurseId: -1, attributes: 0, notes: \"\"",
		label="Payload Bit Length"];
	0 -> 3;
	5	[comment="name: \"Dependency on 'Reliability Type'\", typeName: \"\", id: 5, branchId: 0, recurseId: -1, attributes: 2, notes: \"\"",
		label="Dependency on 'Reliability Type'",
		shape=note];
	0 -> 5;
	34	[comment="name: \"Dependency on 'Is Packet Split?'\", typeName: \"\", id: 34, branchId: 0, recurseId: -1, attributes: 2, notes: \"\"",
		label="Dependency on 'Is Packet Split?'",
		shape=note];
	0 -> 34;
	1 -> 2;
	3 -> 4;
	6	[comment="name: \"if (0)\", typeName: \"\", id: 6, branchId: 0, recurseId: -1, attributes: 4, notes: \"\"",
		label="if (0)",
		shape=diamond];
	5 -> 6;
	8	[comment="name: \"if (1)\", typeName: \"\", id: 8, branchId: 1, recurseId: -1, attributes: 4, notes: \"\"",
		label="if (1)",
		shape=diamond];
	5 -> 8;
	15	[comment="name: \"if (2)\", typeName: \"\", id: 15, branchId: 2, recurseId: -1, attributes: 4, notes: \"\"",
		label="if (2)",
		shape=diamond];
	5 -> 15;
	18	[comment="name: \"if (3)\", typeName: \"\", id: 18, branchId: 3, recurseId: -1, attributes: 4, notes: \"\"",
		label="if (3)",
		shape=diamond];
	5 -> 18;
	25	[comment="name: \"if (4)\", typeName: \"\", id: 25, branchId: 4, recurseId: -1, attributes: 4, notes: \"\"",
		label="if (4)",
		shape=diamond];
	5 -> 25;
	6 -> 7;
	9	[comment="name: \"Sequenced Index\", typeName: \"\", id: 9, branchId: 0, recurseId: -1, attributes: 0, notes: \"\"",
		label="Sequenced Index"];
	8 -> 9;
	11	[comment="name: \"Ordering Index\", typeName: \"\", id: 11, branchId: 0, recurseId: -1, attributes: 0, notes: \"\"",
		label="Ordering Index"];
	8 -> 11;
	13	[comment="name: \"Ordering Channel\", typeName: \"\", id: 13, branchId: 0, recurseId: -1, attributes: 0, notes: \"\"",
		label="Ordering Channel"];
	8 -> 13;
	9 -> 10;
	11 -> 12;
	13 -> 14;
	16	[comment="name: \"Reliable Message\", typeName: \"\", id: 16, branchId: 0, recurseId: -1, attributes: 0, notes: \"\"",
		label="Reliable Message"];
	15 -> 16;
	16 -> 17;
	19	[comment="name: \"Reliable Message\", typeName: \"\", id: 19, branchId: 0, recurseId: -1, attributes: 0, notes: \"\"",
		label="Reliable Message"];
	18 -> 19;
	21	[comment="name: \"Ordering Index\", typeName: \"\", id: 21, branchId: 0, recurseId: -1, attributes: 0, notes: \"\"",
		label="Ordering Index"];
	18 -> 21;
	23	[comment="name: \"Ordering Channel\", typeName: \"\", id: 23, branchId: 0, recurseId: -1, attributes: 0, notes: \"\"",
		label="Ordering Channel"];
	18 -> 23;
	19 -> 20;
	21 -> 22;
	23 -> 24;
	26	[comment="name: \"Reliable Message\", typeName: \"\", id: 26, branchId: 0, recurseId: -1, attributes: 0, notes: \"\"",
		label="Reliable Message"];
	25 -> 26;
	28	[comment="name: \"Sequenced Index\", typeName: \"\", id: 28, branchId: 0, recurseId: -1, attributes: 0, notes: \"\"",
		label="Sequenced Index"];
	25 -> 28;
	30	[comment="name: \"Ordering Index\", typeName: \"\", id: 30, branchId: 0, recurseId: -1, attributes: 0, notes: \"\"",
		label="Ordering Index"];
	25 -> 30;
	32	[comment="name: \"Ordering Channel\", typeName: \"\", id: 32, branchId: 0, recurseId: -1, attributes: 0, notes: \"\"",
		label="Ordering Channel"];
	25 -> 32;
	26 -> 27;
	28 -> 29;
	30 -> 31;
	32 -> 33;
	35	[comment="name: \"if (0)\", typeName: \"\", id: 35, branchId: 0, recurseId: -1, attributes: 4, notes: \"\"",
		label="if (0)",
		shape=diamond];
	34 -> 35;
	37	[comment="name: \"if (1)\", typeName: \"\", id: 37, branchId: 1, recurseId: -1, attributes: 4, notes: \"\"",
		label="if (1)",
		shape=diamond];
	34 -> 37;
	35 -> 36;
	38	[comment="name: \"Split Packet Count\", typeName: \"\", id: 38, branchId: 0, recurseId: -1, attributes: 0, notes: \"\"",
		label="Split Packet Count"];
	37 -> 38;
	40	[comment="name: \"Split Packet Id\", typeName: \"\", id: 40, branchId: 0, recurseId: -1, attributes: 0, notes: \"\"",
		label="Split Packet Id"];
	37 -> 40;
	42	[comment="name: \"Split Packet Index\", typeName: \"\", id: 42, branchId: 0, recurseId: -1, attributes: 0, notes: \"\"",
		label="Split Packet Index"];
	37 -> 42;
	38 -> 39;
	40 -> 41;
	42 -> 43;
}

```

## 字段

/// define
Reliability Header

Reliability Type (3 bits), is packet split? (1 bit)：<!-- md:samp byte -->

- 类型：byte。

Payload Bit Length：<!-- md:samp unsigned short -->

- 类型：unsigned short。

Dependency on 'Reliability Type'

//// tab | if (0)
///// define
if (0)：<!-- md:samp [No Data] -->

- 类型：[No Data]。


/////

////

//// tab | if (1)
///// define
if (1)

Sequenced Index：<!-- md:samp unsigned int24 -->

- 类型：unsigned int24。

Ordering Index：<!-- md:samp unsigned int24 -->

- 类型：unsigned int24。

Ordering Channel：<!-- md:samp byte -->

- 类型：byte。


/////

////

//// tab | if (2)
///// define
if (2)

Reliable Message：<!-- md:samp unsigned int24 -->

- 类型：unsigned int24。


/////

////

//// tab | if (3)
///// define
if (3)

Reliable Message：<!-- md:samp unsigned int24 -->

- 类型：unsigned int24。

Ordering Index：<!-- md:samp unsigned int24 -->

- 类型：unsigned int24。

Ordering Channel：<!-- md:samp byte -->

- 类型：byte。


/////

////

//// tab | if (4)
///// define
if (4)

Reliable Message：<!-- md:samp unsigned int24 -->

- 类型：unsigned int24。

Sequenced Index：<!-- md:samp unsigned int24 -->

- 类型：unsigned int24。

Ordering Index：<!-- md:samp unsigned int24 -->

- 类型：unsigned int24。

Ordering Channel：<!-- md:samp byte -->

- 类型：byte。


/////

////


Dependency on 'Is Packet Split?'

//// tab | if (0)
///// define
if (0)：<!-- md:samp [No Data] -->

- 类型：[No Data]。


/////

////

//// tab | if (1)
///// define
if (1)

Split Packet Count：<!-- md:samp unsigned int -->

- 类型：unsigned int。

Split Packet Id：<!-- md:samp unsigned short -->

- 类型：unsigned short。

Split Packet Index：<!-- md:samp unsigned int -->

- 类型：unsigned int。


/////

////



///
