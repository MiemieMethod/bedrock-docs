# <!-- md:samp AvailableCommandsPacket -->

> 文档版本：r/20_u7<br/>协议版本：662

<!-- md:samp AvailableCommandsPacket -->数据包，数字ID是`76`。

## 结构

```viz
digraph AvailableCommandsPacket {
	graph [rankdir=LR];
	{
		graph [rank=max];
		3	[comment="name: \"unsigned varint\", typeName: \"\", id: 3, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label="unsigned varint"];
		6	[comment="name: \"string\", typeName: \"\", id: 6, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=string];
		9	[comment="name: \"unsigned varint\", typeName: \"\", id: 9, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label="unsigned varint"];
		12	[comment="name: \"string\", typeName: \"\", id: 12, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=string];
		15	[comment="name: \"unsigned varint\", typeName: \"\", id: 15, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label="unsigned varint"];
		18	[comment="name: \"string\", typeName: \"\", id: 18, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=string];
		21	[comment="name: \"unsigned varint\", typeName: \"\", id: 21, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label="unsigned varint"];
		24	[comment="name: \"string\", typeName: \"\", id: 24, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=string];
		27	[comment="name: \"unsigned varint\", typeName: \"\", id: 27, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label="unsigned varint"];
		34	[comment="name: \"unsigned int\", typeName: \"\", id: 34, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label="unsigned int"];
		37	[comment="name: \"unsigned short\", typeName: \"\", id: 37, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label="unsigned short"];
		40	[comment="name: \"byte\", typeName: \"\", id: 40, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=byte];
		43	[comment="name: \"unsigned varint\", typeName: \"\", id: 43, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label="unsigned varint"];
		46	[comment="name: \"string\", typeName: \"\", id: 46, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=string];
		49	[comment="name: \"unsigned varint\", typeName: \"\", id: 49, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label="unsigned varint"];
		52	[comment="name: \"unsigned short\", typeName: \"\", id: 52, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label="unsigned short"];
		54	[comment="name: \"unsigned short\", typeName: \"\", id: 54, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label="unsigned short"];
		57	[comment="name: \"unsigned varint\", typeName: \"\", id: 57, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label="unsigned varint"];
		60	[comment="name: \"string\", typeName: \"\", id: 60, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=string];
		62	[comment="name: \"string\", typeName: \"\", id: 62, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=string];
		64	[comment="name: \"unsigned short\", typeName: \"\", id: 64, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label="unsigned short"];
		66	[comment="name: \"byte\", typeName: \"\", id: 66, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=byte];
		68	[comment="name: \"int\", typeName: \"\", id: 68, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=int];
		71	[comment="name: \"unsigned varint\", typeName: \"\", id: 71, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label="unsigned varint"];
		74	[comment="name: \"unsigned short\", typeName: \"\", id: 74, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label="unsigned short"];
		77	[comment="name: \"unsigned varint\", typeName: \"\", id: 77, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label="unsigned varint"];
		80	[comment="name: \"bool\", typeName: \"\", id: 80, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=bool];
		83	[comment="name: \"unsigned varint\", typeName: \"\", id: 83, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label="unsigned varint"];
		86	[comment="name: \"string\", typeName: \"\", id: 86, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=string];
		88	[comment="name: \"unsigned int\", typeName: \"\", id: 88, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label="unsigned int"];
		90	[comment="name: \"bool\", typeName: \"\", id: 90, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=bool];
		92	[comment="name: \"byte\", typeName: \"\", id: 92, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=byte];
		95	[comment="name: \"unsigned varint\", typeName: \"\", id: 95, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label="unsigned varint"];
		98	[comment="name: \"string\", typeName: \"\", id: 98, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=string];
		101	[comment="name: \"unsigned varint\", typeName: \"\", id: 101, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label="unsigned varint"];
		104	[comment="name: \"string\", typeName: \"\", id: 104, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=string];
		107	[comment="name: \"unsigned varint\", typeName: \"\", id: 107, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label="unsigned varint"];
		110	[comment="name: \"unsigned int\", typeName: \"\", id: 110, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label="unsigned int"];
		112	[comment="name: \"unsigned int\", typeName: \"\", id: 112, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label="unsigned int"];
		115	[comment="name: \"unsigned varint\", typeName: \"\", id: 115, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label="unsigned varint"];
		118	[comment="name: \"byte\", typeName: \"\", id: 118, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=byte];
	}
	0	[comment="name: \"AvailableCommandsPacket\", typeName: \"\", id: 0, branchId: 76, recurseId: -1, attributes: 0, notes: \"\"",
		label=AvailableCommandsPacket];
	1	[comment="name: \"Enum Values\", typeName: \"\", id: 1, branchId: 0, recurseId: -1, attributes: 8, notes: \"\"",
		label="Enum Values"];
	0 -> 1;
	7	[comment="name: \"Enum Values\", typeName: \"\", id: 7, branchId: 0, recurseId: -1, attributes: 8, notes: \"\"",
		label="Enum Values"];
	0 -> 7;
	13	[comment="name: \"Post Fixes\", typeName: \"\", id: 13, branchId: 0, recurseId: -1, attributes: 8, notes: \"\"",
		label="Post Fixes"];
	0 -> 13;
	19	[comment="name: \"Enum Data\", typeName: \"\", id: 19, branchId: 0, recurseId: -1, attributes: 8, notes: \"\"",
		label="Enum Data"];
	0 -> 19;
	41	[comment="name: \"Chained Subcommand Data\", typeName: \"\", id: 41, branchId: 0, recurseId: -1, attributes: 8, notes: \"\"",
		label="Chained Subcommand Data"];
	0 -> 41;
	55	[comment="name: \"Commands\", typeName: \"\", id: 55, branchId: 0, recurseId: -1, attributes: 8, notes: \"\"",
		label=Commands];
	0 -> 55;
	93	[comment="name: \"Soft Enums\", typeName: \"\", id: 93, branchId: 0, recurseId: -1, attributes: 8, notes: \"\"",
		label="Soft Enums"];
	0 -> 93;
	105	[comment="name: \"Constraints\", typeName: \"\", id: 105, branchId: 0, recurseId: -1, attributes: 8, notes: \"\"",
		label=Constraints];
	0 -> 105;
	2	[comment="name: \"Array Size\", typeName: \"\", id: 2, branchId: 0, recurseId: -1, attributes: 0, notes: \"\"",
		label="Array Size"];
	1 -> 2;
	4	[comment="name: \"example element\", typeName: \"\", id: 4, branchId: 0, recurseId: -1, attributes: 16, notes: \"\"",
		label="example element",
		style=dotted];
	1 -> 4;
	2 -> 3;
	5	[comment="name: \"Value\", typeName: \"\", id: 5, branchId: 0, recurseId: -1, attributes: 0, notes: \"\"",
		label=Value];
	4 -> 5;
	5 -> 6;
	8	[comment="name: \"Array Size\", typeName: \"\", id: 8, branchId: 0, recurseId: -1, attributes: 0, notes: \"\"",
		label="Array Size"];
	7 -> 8;
	10	[comment="name: \"example element\", typeName: \"\", id: 10, branchId: 0, recurseId: -1, attributes: 16, notes: \"\"",
		label="example element",
		style=dotted];
	7 -> 10;
	8 -> 9;
	11	[comment="name: \"Chained Subcommand Values\", typeName: \"\", id: 11, branchId: 0, recurseId: -1, attributes: 0, notes: \"\"",
		label="Chained Subcommand Values"];
	10 -> 11;
	11 -> 12;
	14	[comment="name: \"Array Size\", typeName: \"\", id: 14, branchId: 0, recurseId: -1, attributes: 0, notes: \"\"",
		label="Array Size"];
	13 -> 14;
	16	[comment="name: \"example element\", typeName: \"\", id: 16, branchId: 0, recurseId: -1, attributes: 16, notes: \"\"",
		label="example element",
		style=dotted];
	13 -> 16;
	14 -> 15;
	17	[comment="name: \"Post Fix\", typeName: \"\", id: 17, branchId: 0, recurseId: -1, attributes: 0, notes: \"\"",
		label="Post Fix"];
	16 -> 17;
	17 -> 18;
	20	[comment="name: \"Array Size\", typeName: \"\", id: 20, branchId: 0, recurseId: -1, attributes: 0, notes: \"\"",
		label="Array Size"];
	19 -> 20;
	22	[comment="name: \"example element\", typeName: \"\", id: 22, branchId: 0, recurseId: -1, attributes: 16, notes: \"\"",
		label="example element",
		style=dotted];
	19 -> 22;
	20 -> 21;
	23	[comment="name: \"Name\", typeName: \"\", id: 23, branchId: 0, recurseId: -1, attributes: 0, notes: \"\"",
		label=Name];
	22 -> 23;
	25	[comment="name: \"Values\", typeName: \"\", id: 25, branchId: 0, recurseId: -1, attributes: 8, notes: \"\"",
		label=Values];
	22 -> 25;
	23 -> 24;
	26	[comment="name: \"Array Size\", typeName: \"\", id: 26, branchId: 0, recurseId: -1, attributes: 0, notes: \"\"",
		label="Array Size"];
	25 -> 26;
	28	[comment="name: \"example element\", typeName: \"\", id: 28, branchId: 0, recurseId: -1, attributes: 16, notes: \"\"",
		label="example element",
		style=dotted];
	25 -> 28;
	26 -> 27;
	29	[comment="name: \"Dependency on 'Enum Values Size <= 256'\", typeName: \"\", id: 29, branchId: 0, recurseId: -1, attributes: 2, notes: \"\"",
		label="Dependency on 'Enum Values Size <= 256'",
		shape=note];
	28 -> 29;
	30	[comment="name: \"if (0)\", typeName: \"\", id: 30, branchId: 0, recurseId: -1, attributes: 4, notes: \"\"",
		label="if (0)",
		shape=diamond];
	29 -> 30;
	38	[comment="name: \"if (1)\", typeName: \"\", id: 38, branchId: 1, recurseId: -1, attributes: 4, notes: \"\"",
		label="if (1)",
		shape=diamond];
	29 -> 38;
	31	[comment="name: \"Dependency on 'Enum Values Size <= 65536'\", typeName: \"\", id: 31, branchId: 0, recurseId: -1, attributes: 2, notes: \"\"",
		label="Dependency on 'Enum Values Size <= 65536'",
		shape=note];
	30 -> 31;
	32	[comment="name: \"if (0)\", typeName: \"\", id: 32, branchId: 0, recurseId: -1, attributes: 4, notes: \"\"",
		label="if (0)",
		shape=diamond];
	31 -> 32;
	35	[comment="name: \"if (1)\", typeName: \"\", id: 35, branchId: 1, recurseId: -1, attributes: 4, notes: \"\"",
		label="if (1)",
		shape=diamond];
	31 -> 35;
	33	[comment="name: \"Enum Value\", typeName: \"\", id: 33, branchId: 0, recurseId: -1, attributes: 0, notes: \"\"",
		label="Enum Value"];
	32 -> 33;
	33 -> 34;
	36	[comment="name: \"Enum Value\", typeName: \"\", id: 36, branchId: 0, recurseId: -1, attributes: 0, notes: \"\"",
		label="Enum Value"];
	35 -> 36;
	36 -> 37;
	39	[comment="name: \"Enum Value\", typeName: \"\", id: 39, branchId: 0, recurseId: -1, attributes: 0, notes: \"\"",
		label="Enum Value"];
	38 -> 39;
	39 -> 40;
	42	[comment="name: \"Array Size\", typeName: \"\", id: 42, branchId: 0, recurseId: -1, attributes: 0, notes: \"\"",
		label="Array Size"];
	41 -> 42;
	44	[comment="name: \"example element\", typeName: \"\", id: 44, branchId: 0, recurseId: -1, attributes: 16, notes: \"\"",
		label="example element",
		style=dotted];
	41 -> 44;
	42 -> 43;
	45	[comment="name: \"SubCommand Name\", typeName: \"\", id: 45, branchId: 0, recurseId: -1, attributes: 0, notes: \"\"",
		label="SubCommand Name"];
	44 -> 45;
	47	[comment="name: \"SubCommand values\", typeName: \"\", id: 47, branchId: 0, recurseId: -1, attributes: 8, notes: \"\"",
		label="SubCommand values"];
	44 -> 47;
	45 -> 46;
	48	[comment="name: \"Array Size\", typeName: \"\", id: 48, branchId: 0, recurseId: -1, attributes: 0, notes: \"\"",
		label="Array Size"];
	47 -> 48;
	50	[comment="name: \"example element\", typeName: \"\", id: 50, branchId: 0, recurseId: -1, attributes: 16, notes: \"\"",
		label="example element",
		style=dotted];
	47 -> 50;
	48 -> 49;
	51	[comment="name: \"SubCommand First Value\", typeName: \"\", id: 51, branchId: 0, recurseId: -1, attributes: 0, notes: \"\"",
		label="SubCommand First Value"];
	50 -> 51;
	53	[comment="name: \"SubCommand Second Value\", typeName: \"\", id: 53, branchId: 0, recurseId: -1, attributes: 0, notes: \"\"",
		label="SubCommand Second Value"];
	50 -> 53;
	51 -> 52;
	53 -> 54;
	56	[comment="name: \"Array Size\", typeName: \"\", id: 56, branchId: 0, recurseId: -1, attributes: 0, notes: \"\"",
		label="Array Size"];
	55 -> 56;
	58	[comment="name: \"example element\", typeName: \"\", id: 58, branchId: 0, recurseId: -1, attributes: 16, notes: \"\"",
		label="example element",
		style=dotted];
	55 -> 58;
	56 -> 57;
	59	[comment="name: \"Name\", typeName: \"\", id: 59, branchId: 0, recurseId: -1, attributes: 0, notes: \"\"",
		label=Name];
	58 -> 59;
	61	[comment="name: \"Description\", typeName: \"\", id: 61, branchId: 0, recurseId: -1, attributes: 0, notes: \"\"",
		label=Description];
	58 -> 61;
	63	[comment="name: \"Flags\", typeName: \"\", id: 63, branchId: 0, recurseId: -1, attributes: 0, notes: \"\"",
		label=Flags];
	58 -> 63;
	65	[comment="name: \"Permission Level\", typeName: \"\", id: 65, branchId: 0, recurseId: -1, attributes: 0, notes: \"enumeration: CommandPermissionLevel\"",
		label="Permission Level"];
	58 -> 65;
	67	[comment="name: \"Alias Enum\", typeName: \"\", id: 67, branchId: 0, recurseId: -1, attributes: 0, notes: \"\"",
		label="Alias Enum"];
	58 -> 67;
	69	[comment="name: \"CommandData Chained Subcommand Indexes\", typeName: \"\", id: 69, branchId: 0, recurseId: -1, attributes: 8, notes: \"\"",
		label="CommandData Chained Subcommand Indexes"];
	58 -> 69;
	75	[comment="name: \"Overloads\", typeName: \"\", id: 75, branchId: 0, recurseId: -1, attributes: 8, notes: \"\"",
		label=Overloads];
	58 -> 75;
	59 -> 60;
	61 -> 62;
	63 -> 64;
	65 -> 66;
	67 -> 68;
	70	[comment="name: \"Array Size\", typeName: \"\", id: 70, branchId: 0, recurseId: -1, attributes: 0, notes: \"\"",
		label="Array Size"];
	69 -> 70;
	72	[comment="name: \"example element\", typeName: \"\", id: 72, branchId: 0, recurseId: -1, attributes: 16, notes: \"\"",
		label="example element",
		style=dotted];
	69 -> 72;
	70 -> 71;
	73	[comment="name: \"Index\", typeName: \"\", id: 73, branchId: 0, recurseId: -1, attributes: 0, notes: \"\"",
		label=Index];
	72 -> 73;
	73 -> 74;
	76	[comment="name: \"Array Size\", typeName: \"\", id: 76, branchId: 0, recurseId: -1, attributes: 0, notes: \"\"",
		label="Array Size"];
	75 -> 76;
	78	[comment="name: \"example element\", typeName: \"\", id: 78, branchId: 0, recurseId: -1, attributes: 16, notes: \"\"",
		label="example element",
		style=dotted];
	75 -> 78;
	76 -> 77;
	79	[comment="name: \"isChaining\", typeName: \"\", id: 79, branchId: 0, recurseId: -1, attributes: 0, notes: \"\"",
		label=isChaining];
	78 -> 79;
	81	[comment="name: \"Parameter Data\", typeName: \"\", id: 81, branchId: 0, recurseId: -1, attributes: 8, notes: \"\"",
		label="Parameter Data"];
	78 -> 81;
	79 -> 80;
	82	[comment="name: \"Array Size\", typeName: \"\", id: 82, branchId: 0, recurseId: -1, attributes: 0, notes: \"\"",
		label="Array Size"];
	81 -> 82;
	84	[comment="name: \"example element\", typeName: \"\", id: 84, branchId: 0, recurseId: -1, attributes: 16, notes: \"\"",
		label="example element",
		style=dotted];
	81 -> 84;
	82 -> 83;
	85	[comment="name: \"Name\", typeName: \"\", id: 85, branchId: 0, recurseId: -1, attributes: 0, notes: \"\"",
		label=Name];
	84 -> 85;
	87	[comment="name: \"Parse Symbol\", typeName: \"\", id: 87, branchId: 0, recurseId: -1, attributes: 0, notes: \"\"",
		label="Parse Symbol"];
	84 -> 87;
	89	[comment="name: \"Is Optional?\", typeName: \"\", id: 89, branchId: 0, recurseId: -1, attributes: 0, notes: \"\"",
		label="Is Optional?"];
	84 -> 89;
	91	[comment="name: \"Options\", typeName: \"\", id: 91, branchId: 0, recurseId: -1, attributes: 0, notes: \"\"",
		label=Options];
	84 -> 91;
	85 -> 86;
	87 -> 88;
	89 -> 90;
	91 -> 92;
	94	[comment="name: \"Array Size\", typeName: \"\", id: 94, branchId: 0, recurseId: -1, attributes: 0, notes: \"\"",
		label="Array Size"];
	93 -> 94;
	96	[comment="name: \"example element\", typeName: \"\", id: 96, branchId: 0, recurseId: -1, attributes: 16, notes: \"\"",
		label="example element",
		style=dotted];
	93 -> 96;
	94 -> 95;
	97	[comment="name: \"Enum Name\", typeName: \"\", id: 97, branchId: 0, recurseId: -1, attributes: 0, notes: \"\"",
		label="Enum Name"];
	96 -> 97;
	99	[comment="name: \"Enum Options\", typeName: \"\", id: 99, branchId: 0, recurseId: -1, attributes: 8, notes: \"\"",
		label="Enum Options"];
	96 -> 99;
	97 -> 98;
	100	[comment="name: \"Array Size\", typeName: \"\", id: 100, branchId: 0, recurseId: -1, attributes: 0, notes: \"\"",
		label="Array Size"];
	99 -> 100;
	102	[comment="name: \"example element\", typeName: \"\", id: 102, branchId: 0, recurseId: -1, attributes: 16, notes: \"\"",
		label="example element",
		style=dotted];
	99 -> 102;
	100 -> 101;
	103	[comment="name: \"Value\", typeName: \"\", id: 103, branchId: 0, recurseId: -1, attributes: 0, notes: \"\"",
		label=Value];
	102 -> 103;
	103 -> 104;
	106	[comment="name: \"Array Size\", typeName: \"\", id: 106, branchId: 0, recurseId: -1, attributes: 0, notes: \"\"",
		label="Array Size"];
	105 -> 106;
	108	[comment="name: \"example element\", typeName: \"\", id: 108, branchId: 0, recurseId: -1, attributes: 16, notes: \"\"",
		label="example element",
		style=dotted];
	105 -> 108;
	106 -> 107;
	109	[comment="name: \"Enum Value Symbol\", typeName: \"\", id: 109, branchId: 0, recurseId: -1, attributes: 0, notes: \"Symbol in the command parser \
representing this enum's value.\"",
		label="Enum Value Symbol"];
	108 -> 109;
	111	[comment="name: \"Enum Symbol\", typeName: \"\", id: 111, branchId: 0, recurseId: -1, attributes: 0, notes: \"Symbol in the command parser representing \
this enum.\"",
		label="Enum Symbol"];
	108 -> 111;
	113	[comment="name: \"Constraint Indices\", typeName: \"\", id: 113, branchId: 0, recurseId: -1, attributes: 8, notes: \"\"",
		label="Constraint Indices"];
	108 -> 113;
	109 -> 110;
	111 -> 112;
	114	[comment="name: \"Array Size\", typeName: \"\", id: 114, branchId: 0, recurseId: -1, attributes: 0, notes: \"\"",
		label="Array Size"];
	113 -> 114;
	116	[comment="name: \"example element\", typeName: \"\", id: 116, branchId: 0, recurseId: -1, attributes: 16, notes: \"\"",
		label="example element",
		style=dotted];
	113 -> 116;
	114 -> 115;
	117	[comment="name: \"Semantic Constraint Index\", typeName: \"\", id: 117, branchId: 0, recurseId: -1, attributes: 0, notes: \"Index of the semantic \
constraint within the command parser.\"",
		label="Semantic Constraint Index"];
	116 -> 117;
	117 -> 118;
}

```

## 字段

/// define
AvailableCommandsPacket

Enum Values

//// define
Enum Values数组的大小：<!-- md:samp unsigned varint -->

- 类型：unsigned varint。


////


//// define
Enum Values的示例元素

Value：<!-- md:samp string -->

- 类型：string。


////


//// define
Enum Values的示例元素

Chained Subcommand Values：<!-- md:samp string -->

- 类型：string。


////


Post Fixes

//// define
Post Fixes数组的大小：<!-- md:samp unsigned varint -->

- 类型：unsigned varint。


////


//// define
Post Fixes的示例元素

Post Fix：<!-- md:samp string -->

- 类型：string。


////


Enum Data

//// define
Enum Data数组的大小：<!-- md:samp unsigned varint -->

- 类型：unsigned varint。


////


//// define
Enum Data的示例元素

Name：<!-- md:samp string -->

- 类型：string。

Values

///// define
Values数组的大小：<!-- md:samp unsigned varint -->

- 类型：unsigned varint。


/////


///// define
Values的示例元素

Dependency on 'Enum Values Size <= 256'

////// tab | if (0)
/////// define
if (0)

Dependency on 'Enum Values Size <= 65536'

//////// tab | if (0)
///////// define
if (0)

Enum Value：<!-- md:samp unsigned int -->

- 类型：unsigned int。


/////////

////////

//////// tab | if (1)
///////// define
if (1)

Enum Value：<!-- md:samp unsigned short -->

- 类型：unsigned short。


/////////

////////



///////

//////

////// tab | if (1)
/////// define
if (1)

Enum Value：<!-- md:samp byte -->

- 类型：byte。


///////

//////



/////



////


Chained Subcommand Data

//// define
Chained Subcommand Data数组的大小：<!-- md:samp unsigned varint -->

- 类型：unsigned varint。


////


//// define
Chained Subcommand Data的示例元素

SubCommand Name：<!-- md:samp string -->

- 类型：string。

SubCommand values

///// define
SubCommand values数组的大小：<!-- md:samp unsigned varint -->

- 类型：unsigned varint。


/////


///// define
SubCommand values的示例元素

SubCommand First Value：<!-- md:samp unsigned short -->

- 类型：unsigned short。

SubCommand Second Value：<!-- md:samp unsigned short -->

- 类型：unsigned short。


/////



////


Commands

//// define
Commands数组的大小：<!-- md:samp unsigned varint -->

- 类型：unsigned varint。


////


//// define
Commands的示例元素

Name：<!-- md:samp string -->

- 类型：string。

Description：<!-- md:samp string -->

- 类型：string。

Flags：<!-- md:samp unsigned short -->

- 类型：unsigned short。

Permission Level：<!-- md:samp byte -->

- 类型：byte。enumeration: CommandPermissionLevel

Alias Enum：<!-- md:samp int -->

- 类型：int。

CommandData Chained Subcommand Indexes

///// define
CommandData Chained Subcommand Indexes数组的大小：<!-- md:samp unsigned varint -->

- 类型：unsigned varint。


/////


///// define
CommandData Chained Subcommand Indexes的示例元素

Index：<!-- md:samp unsigned short -->

- 类型：unsigned short。


/////


Overloads

///// define
Overloads数组的大小：<!-- md:samp unsigned varint -->

- 类型：unsigned varint。


/////


///// define
Overloads的示例元素

isChaining：<!-- md:samp bool -->

- 类型：bool。

Parameter Data

////// define
Parameter Data数组的大小：<!-- md:samp unsigned varint -->

- 类型：unsigned varint。


//////


////// define
Parameter Data的示例元素

Name：<!-- md:samp string -->

- 类型：string。

Parse Symbol：<!-- md:samp unsigned int -->

- 类型：unsigned int。

Is Optional?：<!-- md:samp bool -->

- 类型：bool。

Options：<!-- md:samp byte -->

- 类型：byte。


//////



/////



////


Soft Enums

//// define
Soft Enums数组的大小：<!-- md:samp unsigned varint -->

- 类型：unsigned varint。


////


//// define
Soft Enums的示例元素

Enum Name：<!-- md:samp string -->

- 类型：string。

Enum Options

///// define
Enum Options数组的大小：<!-- md:samp unsigned varint -->

- 类型：unsigned varint。


/////


///// define
Enum Options的示例元素

Value：<!-- md:samp string -->

- 类型：string。


/////



////


Constraints

//// define
Constraints数组的大小：<!-- md:samp unsigned varint -->

- 类型：unsigned varint。


////


//// define
Constraints的示例元素

Enum Value Symbol：<!-- md:samp unsigned int -->

- 类型：unsigned int。Symbol in the command parser representing this enum's value.

Enum Symbol：<!-- md:samp unsigned int -->

- 类型：unsigned int。Symbol in the command parser representing this enum.

Constraint Indices

///// define
Constraint Indices数组的大小：<!-- md:samp unsigned varint -->

- 类型：unsigned varint。


/////


///// define
Constraint Indices的示例元素

Semantic Constraint Index：<!-- md:samp byte -->

- 类型：byte。Index of the semantic constraint within the command parser.


/////



////



///
