# <!-- md:samp LegacyTelemetryEventPacket -->

> 文档版本：r/20_u7<br/>协议版本：662

<!-- md:samp LegacyTelemetryEventPacket -->数据包，数字ID是`65`。

## 结构

```dot
digraph LegacyTelemetryEventPacket {
	graph [rankdir=LR];
	{
		graph [rank=max];
		2	[comment="name: \"ActorUniqueID\", typeName: \"\", id: 2, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=ActorUniqueID];
		4	[comment="name: \"varint\", typeName: \"\", id: 4, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=varint];
		6	[comment="name: \"byte\", typeName: \"\", id: 6, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=byte];
		10	[comment="name: \"varint\", typeName: \"\", id: 10, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=varint];
		13	[comment="name: \"varint\", typeName: \"\", id: 13, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=varint];
		15	[comment="name: \"varint\", typeName: \"\", id: 15, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=varint];
		17	[comment="name: \"varint\", typeName: \"\", id: 17, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=varint];
		19	[comment="name: \"byte\", typeName: \"\", id: 19, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=byte];
		22	[comment="name: \"varint\", typeName: \"\", id: 22, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=varint];
		25	[comment="name: \"varint\", typeName: \"\", id: 25, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=varint];
		27	[comment="name: \"varint\", typeName: \"\", id: 27, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=varint];
		30	[comment="name: \"varint64\", typeName: \"\", id: 30, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=varint64];
		32	[comment="name: \"varint64\", typeName: \"\", id: 32, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=varint64];
		34	[comment="name: \"varint\", typeName: \"\", id: 34, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=varint];
		36	[comment="name: \"varint\", typeName: \"\", id: 36, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=varint];
		38	[comment="name: \"varint\", typeName: \"\", id: 38, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=varint];
		40	[comment="name: \"string\", typeName: \"\", id: 40, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=string];
		43	[comment="name: \"unsigned varint\", typeName: \"\", id: 43, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label="unsigned varint"];
		45	[comment="name: \"varint\", typeName: \"\", id: 45, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=varint];
		47	[comment="name: \"varint\", typeName: \"\", id: 47, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=varint];
		50	[comment="name: \"varint\", typeName: \"\", id: 50, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=varint];
		52	[comment="name: \"varint\", typeName: \"\", id: 52, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=varint];
		54	[comment="name: \"varint\", typeName: \"\", id: 54, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=varint];
		56	[comment="name: \"bool\", typeName: \"\", id: 56, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=bool];
		59	[comment="name: \"varint64\", typeName: \"\", id: 59, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=varint64];
		61	[comment="name: \"varint\", typeName: \"\", id: 61, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=varint];
		63	[comment="name: \"varint\", typeName: \"\", id: 63, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=varint];
		66	[comment="name: \"varint\", typeName: \"\", id: 66, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=varint];
		68	[comment="name: \"varint\", typeName: \"\", id: 68, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=varint];
		70	[comment="name: \"string\", typeName: \"\", id: 70, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=string];
		72	[comment="name: \"string\", typeName: \"\", id: 72, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=string];
		74	[comment="name: \"string\", typeName: \"\", id: 74, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=string];
		76	[comment="name: \"[No Data]\", typeName: \"\", id: 76, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label="[No Data]"];
		78	[comment="name: \"[No Data]\", typeName: \"\", id: 78, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label="[No Data]"];
		81	[comment="name: \"varint\", typeName: \"\", id: 81, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=varint];
		83	[comment="name: \"varint\", typeName: \"\", id: 83, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=varint];
		85	[comment="name: \"string\", typeName: \"\", id: 85, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=string];
		87	[comment="name: \"string\", typeName: \"\", id: 87, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=string];
		89	[comment="name: \"[No Data]\", typeName: \"\", id: 89, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label="[No Data]"];
		92	[comment="name: \"varint\", typeName: \"\", id: 92, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=varint];
		94	[comment="name: \"varint\", typeName: \"\", id: 94, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=varint];
		96	[comment="name: \"byte\", typeName: \"\", id: 96, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=byte];
		98	[comment="name: \"[No Data]\", typeName: \"\", id: 98, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label="[No Data]"];
		101	[comment="name: \"varint\", typeName: \"\", id: 101, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=varint];
		103	[comment="name: \"varint\", typeName: \"\", id: 103, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=varint];
		106	[comment="name: \"varint\", typeName: \"\", id: 106, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=varint];
		108	[comment="name: \"varint\", typeName: \"\", id: 108, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=varint];
		111	[comment="name: \"varint\", typeName: \"\", id: 111, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=varint];
		114	[comment="name: \"string\", typeName: \"\", id: 114, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=string];
		117	[comment="name: \"varint\", typeName: \"\", id: 117, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=varint];
		119	[comment="name: \"varint\", typeName: \"\", id: 119, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=varint];
		121	[comment="name: \"bool\", typeName: \"\", id: 121, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=bool];
		123	[comment="name: \"[No Data]\", typeName: \"\", id: 123, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label="[No Data]"];
		125	[comment="name: \"[No Data]\", typeName: \"\", id: 125, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label="[No Data]"];
		127	[comment="name: \"[No Data]\", typeName: \"\", id: 127, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label="[No Data]"];
		130	[comment="name: \"varint\", typeName: \"\", id: 130, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=varint];
		133	[comment="name: \"varint\", typeName: \"\", id: 133, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=varint];
		135	[comment="name: \"bool\", typeName: \"\", id: 135, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=bool];
		138	[comment="name: \"varint\", typeName: \"\", id: 138, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=varint];
		141	[comment="name: \"string\", typeName: \"\", id: 141, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=string];
		144	[comment="name: \"string\", typeName: \"\", id: 144, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=string];
		146	[comment="name: \"varint\", typeName: \"\", id: 146, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=varint];
		148	[comment="name: \"[No Data]\", typeName: \"\", id: 148, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label="[No Data]"];
		150	[comment="name: \"[No Data]\", typeName: \"\", id: 150, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label="[No Data]"];
		152	[comment="name: \"[No Data]\", typeName: \"\", id: 152, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label="[No Data]"];
	}
	0	[comment="name: \"LegacyTelemetryEventPacket\", typeName: \"\", id: 0, branchId: 65, recurseId: -1, attributes: 0, notes: \"\"",
		label=LegacyTelemetryEventPacket];
	1	[comment="name: \"Target Actor ID\", typeName: \"ActorUniqueID\", id: 1, branchId: 0, recurseId: -1, attributes: 256, notes: \"\"",
		label="Target Actor ID"];
	0 -> 1;
	3	[comment="name: \"Event Type\", typeName: \"\", id: 3, branchId: 0, recurseId: -1, attributes: 0, notes: \"enumeration: LegacyTelemetryEventPacket::\
Type\"",
		label="Event Type"];
	0 -> 3;
	5	[comment="name: \"Use Player ID\", typeName: \"\", id: 5, branchId: 0, recurseId: -1, attributes: 0, notes: \"\"",
		label="Use Player ID"];
	0 -> 5;
	7	[comment="name: \"Dependency on 'Event Type'\", typeName: \"\", id: 7, branchId: 0, recurseId: -1, attributes: 2, notes: \"\"",
		label="Dependency on 'Event Type'",
		shape=note];
	0 -> 7;
	1 -> 2;
	3 -> 4;
	5 -> 6;
	8	[comment="name: \"if (0)\", typeName: \"\", id: 8, branchId: 0, recurseId: -1, attributes: 4, notes: \"\"",
		label="if (0)",
		shape=diamond];
	7 -> 8;
	11	[comment="name: \"if (1)\", typeName: \"\", id: 11, branchId: 1, recurseId: -1, attributes: 4, notes: \"\"",
		label="if (1)",
		shape=diamond];
	7 -> 11;
	20	[comment="name: \"if (2)\", typeName: \"\", id: 20, branchId: 2, recurseId: -1, attributes: 4, notes: \"\"",
		label="if (2)",
		shape=diamond];
	7 -> 20;
	23	[comment="name: \"if (3)\", typeName: \"\", id: 23, branchId: 3, recurseId: -1, attributes: 4, notes: \"\"",
		label="if (3)",
		shape=diamond];
	7 -> 23;
	28	[comment="name: \"if (4)\", typeName: \"\", id: 28, branchId: 4, recurseId: -1, attributes: 4, notes: \"\"",
		label="if (4)",
		shape=diamond];
	7 -> 28;
	41	[comment="name: \"if (5)\", typeName: \"\", id: 41, branchId: 5, recurseId: -1, attributes: 4, notes: \"\"",
		label="if (5)",
		shape=diamond];
	7 -> 41;
	48	[comment="name: \"if (6)\", typeName: \"\", id: 48, branchId: 6, recurseId: -1, attributes: 4, notes: \"\"",
		label="if (6)",
		shape=diamond];
	7 -> 48;
	57	[comment="name: \"if (7)\", typeName: \"\", id: 57, branchId: 7, recurseId: -1, attributes: 4, notes: \"\"",
		label="if (7)",
		shape=diamond];
	7 -> 57;
	64	[comment="name: \"if (8)\", typeName: \"\", id: 64, branchId: 8, recurseId: -1, attributes: 4, notes: \"\"",
		label="if (8)",
		shape=diamond];
	7 -> 64;
	75	[comment="name: \"if (9)\", typeName: \"\", id: 75, branchId: 9, recurseId: -1, attributes: 4, notes: \"\"",
		label="if (9)",
		shape=diamond];
	7 -> 75;
	77	[comment="name: \"if (10)\", typeName: \"\", id: 77, branchId: 10, recurseId: -1, attributes: 4, notes: \"\"",
		label="if (10)",
		shape=diamond];
	7 -> 77;
	79	[comment="name: \"if (11)\", typeName: \"\", id: 79, branchId: 11, recurseId: -1, attributes: 4, notes: \"\"",
		label="if (11)",
		shape=diamond];
	7 -> 79;
	88	[comment="name: \"if (12)\", typeName: \"\", id: 88, branchId: 12, recurseId: -1, attributes: 4, notes: \"\"",
		label="if (12)",
		shape=diamond];
	7 -> 88;
	90	[comment="name: \"if (13)\", typeName: \"\", id: 90, branchId: 13, recurseId: -1, attributes: 4, notes: \"\"",
		label="if (13)",
		shape=diamond];
	7 -> 90;
	97	[comment="name: \"if (14)\", typeName: \"\", id: 97, branchId: 14, recurseId: -1, attributes: 4, notes: \"\"",
		label="if (14)",
		shape=diamond];
	7 -> 97;
	99	[comment="name: \"if (15)\", typeName: \"\", id: 99, branchId: 15, recurseId: -1, attributes: 4, notes: \"\"",
		label="if (15)",
		shape=diamond];
	7 -> 99;
	104	[comment="name: \"if (16)\", typeName: \"\", id: 104, branchId: 16, recurseId: -1, attributes: 4, notes: \"\"",
		label="if (16)",
		shape=diamond];
	7 -> 104;
	109	[comment="name: \"if (17)\", typeName: \"\", id: 109, branchId: 17, recurseId: -1, attributes: 4, notes: \"\"",
		label="if (17)",
		shape=diamond];
	7 -> 109;
	112	[comment="name: \"if (18)\", typeName: \"\", id: 112, branchId: 18, recurseId: -1, attributes: 4, notes: \"\"",
		label="if (18)",
		shape=diamond];
	7 -> 112;
	115	[comment="name: \"if (19)\", typeName: \"\", id: 115, branchId: 19, recurseId: -1, attributes: 4, notes: \"\"",
		label="if (19)",
		shape=diamond];
	7 -> 115;
	122	[comment="name: \"if (20)\", typeName: \"\", id: 122, branchId: 20, recurseId: -1, attributes: 4, notes: \"\"",
		label="if (20)",
		shape=diamond];
	7 -> 122;
	124	[comment="name: \"if (21)\", typeName: \"\", id: 124, branchId: 21, recurseId: -1, attributes: 4, notes: \"\"",
		label="if (21)",
		shape=diamond];
	7 -> 124;
	126	[comment="name: \"if (22)\", typeName: \"\", id: 126, branchId: 22, recurseId: -1, attributes: 4, notes: \"\"",
		label="if (22)",
		shape=diamond];
	7 -> 126;
	128	[comment="name: \"if (23)\", typeName: \"\", id: 128, branchId: 23, recurseId: -1, attributes: 4, notes: \"\"",
		label="if (23)",
		shape=diamond];
	7 -> 128;
	131	[comment="name: \"if (24)\", typeName: \"\", id: 131, branchId: 24, recurseId: -1, attributes: 4, notes: \"\"",
		label="if (24)",
		shape=diamond];
	7 -> 131;
	136	[comment="name: \"if (25)\", typeName: \"\", id: 136, branchId: 25, recurseId: -1, attributes: 4, notes: \"\"",
		label="if (25)",
		shape=diamond];
	7 -> 136;
	139	[comment="name: \"if (26)\", typeName: \"\", id: 139, branchId: 26, recurseId: -1, attributes: 4, notes: \"\"",
		label="if (26)",
		shape=diamond];
	7 -> 139;
	142	[comment="name: \"if (27)\", typeName: \"\", id: 142, branchId: 27, recurseId: -1, attributes: 4, notes: \"\"",
		label="if (27)",
		shape=diamond];
	7 -> 142;
	147	[comment="name: \"if (28)\", typeName: \"\", id: 147, branchId: 28, recurseId: -1, attributes: 4, notes: \"\"",
		label="if (28)",
		shape=diamond];
	7 -> 147;
	149	[comment="name: \"if (29)\", typeName: \"\", id: 149, branchId: 29, recurseId: -1, attributes: 4, notes: \"\"",
		label="if (29)",
		shape=diamond];
	7 -> 149;
	151	[comment="name: \"if (30)\", typeName: \"\", id: 151, branchId: 30, recurseId: -1, attributes: 4, notes: \"\"",
		label="if (30)",
		shape=diamond];
	7 -> 151;
	9	[comment="name: \"Achievement ID\", typeName: \"\", id: 9, branchId: 0, recurseId: -1, attributes: 0, notes: \"\"",
		label="Achievement ID"];
	8 -> 9;
	9 -> 10;
	12	[comment="name: \"Interaction Type\", typeName: \"\", id: 12, branchId: 0, recurseId: -1, attributes: 0, notes: \"enumeration: MinecraftEventing::\
InteractionType\"",
		label="Interaction Type"];
	11 -> 12;
	14	[comment="name: \"Interaction Actor Type\", typeName: \"\", id: 14, branchId: 0, recurseId: -1, attributes: 0, notes: \"enumeration: ActorType\"",
		label="Interaction Actor Type"];
	11 -> 14;
	16	[comment="name: \"Interaction Actor Variant\", typeName: \"\", id: 16, branchId: 0, recurseId: -1, attributes: 0, notes: \"\"",
		label="Interaction Actor Variant"];
	11 -> 16;
	18	[comment="name: \"Interaction Actor Color\", typeName: \"\", id: 18, branchId: 0, recurseId: -1, attributes: 0, notes: \"\"",
		label="Interaction Actor Color"];
	11 -> 18;
	12 -> 13;
	14 -> 15;
	16 -> 17;
	18 -> 19;
	21	[comment="name: \"Dimension ID\", typeName: \"\", id: 21, branchId: 0, recurseId: -1, attributes: 0, notes: \"Currently supported: (0 -> Overworld, \
1 -> Nether, 2 -> The End, 3 -> Undefined)\"",
		label="Dimension ID"];
	20 -> 21;
	21 -> 22;
	24	[comment="name: \"Source Dimension ID\", typeName: \"\", id: 24, branchId: 0, recurseId: -1, attributes: 0, notes: \"Currently supported: (0 -> \
Overworld, 1 -> Nether, 2 -> The End, 3 -> Undefined)\"",
		label="Source Dimension ID"];
	23 -> 24;
	26	[comment="name: \"Target Dimension ID\", typeName: \"\", id: 26, branchId: 0, recurseId: -1, attributes: 0, notes: \"Currently supported: (0 -> \
Overworld, 1 -> Nether, 2 -> The End, 3 -> Undefined)\"",
		label="Target Dimension ID"];
	23 -> 26;
	24 -> 25;
	26 -> 27;
	29	[comment="name: \"Instigator Actor ID\", typeName: \"\", id: 29, branchId: 0, recurseId: -1, attributes: 0, notes: \"\"",
		label="Instigator Actor ID"];
	28 -> 29;
	31	[comment="name: \"Target Actor ID\", typeName: \"\", id: 31, branchId: 0, recurseId: -1, attributes: 0, notes: \"\"",
		label="Target Actor ID"];
	28 -> 31;
	33	[comment="name: \"Instigator's Child Actor Type\", typeName: \"\", id: 33, branchId: 0, recurseId: -1, attributes: 0, notes: \"enumeration: ActorType\"",
		label="Instigator's Child Actor Type"];
	28 -> 33;
	35	[comment="name: \"Damage Source\", typeName: \"\", id: 35, branchId: 0, recurseId: -1, attributes: 0, notes: \"enumeration: ActorDamageCause\"",
		label="Damage Source"];
	28 -> 35;
	37	[comment="name: \"Trade Tier\", typeName: \"\", id: 37, branchId: 0, recurseId: -1, attributes: 0, notes: \"-1 if not a trading actor.\"",
		label="Trade Tier"];
	28 -> 37;
	39	[comment="name: \"Trader Name\", typeName: \"\", id: 39, branchId: 0, recurseId: -1, attributes: 0, notes: \"Empty if not a trading actor.\"",
		label="Trader Name"];
	28 -> 39;
	29 -> 30;
	31 -> 32;
	33 -> 34;
	35 -> 36;
	37 -> 38;
	39 -> 40;
	42	[comment="name: \"Contents Color\", typeName: \"\", id: 42, branchId: 0, recurseId: -1, attributes: 0, notes: \"\"",
		label="Contents Color"];
	41 -> 42;
	44	[comment="name: \"Contents Type\", typeName: \"\", id: 44, branchId: 0, recurseId: -1, attributes: 0, notes: \"\"",
		label="Contents Type"];
	41 -> 44;
	46	[comment="name: \"Fill Level\", typeName: \"\", id: 46, branchId: 0, recurseId: -1, attributes: 0, notes: \"\"",
		label="Fill Level"];
	41 -> 46;
	42 -> 43;
	44 -> 45;
	46 -> 47;
	49	[comment="name: \"Instigator Actor ID\", typeName: \"\", id: 49, branchId: 0, recurseId: -1, attributes: 0, notes: \"\"",
		label="Instigator Actor ID"];
	48 -> 49;
	51	[comment="name: \"Instigator Mob Variant\", typeName: \"\", id: 51, branchId: 0, recurseId: -1, attributes: 0, notes: \"\"",
		label="Instigator Mob Variant"];
	48 -> 51;
	53	[comment="name: \"Damage Source\", typeName: \"\", id: 53, branchId: 0, recurseId: -1, attributes: 0, notes: \"enumeration: ActorDamageCause\"",
		label="Damage Source"];
	48 -> 53;
	55	[comment="name: \"Died in Raid?\", typeName: \"\", id: 55, branchId: 0, recurseId: -1, attributes: 0, notes: \"\"",
		label="Died in Raid?"];
	48 -> 55;
	49 -> 50;
	51 -> 52;
	53 -> 54;
	55 -> 56;
	58	[comment="name: \"Boss Actor ID\", typeName: \"\", id: 58, branchId: 0, recurseId: -1, attributes: 0, notes: \"\"",
		label="Boss Actor ID"];
	57 -> 58;
	60	[comment="name: \"Party Size\", typeName: \"\", id: 60, branchId: 0, recurseId: -1, attributes: 0, notes: \"\"",
		label="Party Size"];
	57 -> 60;
	62	[comment="name: \"Boss Type\", typeName: \"\", id: 62, branchId: 0, recurseId: -1, attributes: 0, notes: \"enumeration: ActorType\"",
		label="Boss Type"];
	57 -> 62;
	58 -> 59;
	60 -> 61;
	62 -> 63;
	65	[comment="name: \"Result\", typeName: \"\", id: 65, branchId: 0, recurseId: -1, attributes: 0, notes: \"enumeration: LegacyTelemetryEventPacket::\
AgentResult\"",
		label=Result];
	64 -> 65;
	67	[comment="name: \"Result Number\", typeName: \"\", id: 67, branchId: 0, recurseId: -1, attributes: 0, notes: \"\"",
		label="Result Number"];
	64 -> 67;
	69	[comment="name: \"Command Name\", typeName: \"\", id: 69, branchId: 0, recurseId: -1, attributes: 0, notes: \"\"",
		label="Command Name"];
	64 -> 69;
	71	[comment="name: \"Result Key\", typeName: \"\", id: 71, branchId: 0, recurseId: -1, attributes: 0, notes: \"\"",
		label="Result Key"];
	64 -> 71;
	73	[comment="name: \"Result String\", typeName: \"\", id: 73, branchId: 0, recurseId: -1, attributes: 0, notes: \"\"",
		label="Result String"];
	64 -> 73;
	65 -> 66;
	67 -> 68;
	69 -> 70;
	71 -> 72;
	73 -> 74;
	75 -> 76;
	77 -> 78;
	80	[comment="name: \"Success Count\", typeName: \"\", id: 80, branchId: 0, recurseId: -1, attributes: 0, notes: \"\"",
		label="Success Count"];
	79 -> 80;
	82	[comment="name: \"Error Count\", typeName: \"\", id: 82, branchId: 0, recurseId: -1, attributes: 0, notes: \"\"",
		label="Error Count"];
	79 -> 82;
	84	[comment="name: \"Command Name\", typeName: \"\", id: 84, branchId: 0, recurseId: -1, attributes: 0, notes: \"\"",
		label="Command Name"];
	79 -> 84;
	86	[comment="name: \"Error List\", typeName: \"\", id: 86, branchId: 0, recurseId: -1, attributes: 0, notes: \"\"",
		label="Error List"];
	79 -> 86;
	80 -> 81;
	82 -> 83;
	84 -> 85;
	86 -> 87;
	88 -> 89;
	91	[comment="name: \"Born Baby: Entity Type\", typeName: \"\", id: 91, branchId: 0, recurseId: -1, attributes: 0, notes: \"\"",
		label="Born Baby: Entity Type"];
	90 -> 91;
	93	[comment="name: \"Born Baby: Entity Variant\", typeName: \"\", id: 93, branchId: 0, recurseId: -1, attributes: 0, notes: \"\"",
		label="Born Baby: Entity Variant"];
	90 -> 93;
	95	[comment="name: \"Born Baby: Color\", typeName: \"\", id: 95, branchId: 0, recurseId: -1, attributes: 0, notes: \"\"",
		label="Born Baby: Color"];
	90 -> 95;
	91 -> 92;
	93 -> 94;
	95 -> 96;
	97 -> 98;
	100	[comment="name: \"Block Interaction Type\", typeName: \"\", id: 100, branchId: 0, recurseId: -1, attributes: 0, notes: \"enumeration: MinecraftEventing::\
POIBlockInteractionType\"",
		label="Block Interaction Type"];
	99 -> 100;
	102	[comment="name: \"Item Id\", typeName: \"\", id: 102, branchId: 0, recurseId: -1, attributes: 0, notes: \"Id of the relevant item used in the interaction.\"",
		label="Item Id"];
	99 -> 102;
	100 -> 101;
	102 -> 103;
	105	[comment="name: \"Block Interaction Type\", typeName: \"\", id: 105, branchId: 0, recurseId: -1, attributes: 0, notes: \"enumeration: MinecraftEventing::\
POIBlockInteractionType\"",
		label="Block Interaction Type"];
	104 -> 105;
	107	[comment="name: \"Item Id\", typeName: \"\", id: 107, branchId: 0, recurseId: -1, attributes: 0, notes: \"Id of the relevant item used in the interaction.\"",
		label="Item Id"];
	104 -> 107;
	105 -> 106;
	107 -> 108;
	110	[comment="name: \"Item Id\", typeName: \"\", id: 110, branchId: 0, recurseId: -1, attributes: 0, notes: \"Id of the relevant item used in the interaction.\"",
		label="Item Id"];
	109 -> 110;
	110 -> 111;
	113	[comment="name: \"Event Name\", typeName: \"\", id: 113, branchId: 0, recurseId: -1, attributes: 0, notes: \"\"",
		label="Event Name"];
	112 -> 113;
	113 -> 114;
	116	[comment="name: \"Current Raid Wave\", typeName: \"\", id: 116, branchId: 0, recurseId: -1, attributes: 0, notes: \"\"",
		label="Current Raid Wave"];
	115 -> 116;
	118	[comment="name: \"Total Raid Waves\", typeName: \"\", id: 118, branchId: 0, recurseId: -1, attributes: 0, notes: \"\"",
		label="Total Raid Waves"];
	115 -> 118;
	120	[comment="name: \"Won Raid\", typeName: \"\", id: 120, branchId: 0, recurseId: -1, attributes: 0, notes: \"\"",
		label="Won Raid"];
	115 -> 120;
	116 -> 117;
	118 -> 119;
	120 -> 121;
	122 -> 123;
	124 -> 125;
	126 -> 127;
	129	[comment="name: \"Redstone Level\", typeName: \"\", id: 129, branchId: 0, recurseId: -1, attributes: 0, notes: \"\"",
		label="Redstone Level"];
	128 -> 129;
	129 -> 130;
	132	[comment="name: \"Item Id\", typeName: \"\", id: 132, branchId: 0, recurseId: -1, attributes: 0, notes: \"\"",
		label="Item Id"];
	131 -> 132;
	134	[comment="name: \"Was targeting bartering player\", typeName: \"\", id: 134, branchId: 0, recurseId: -1, attributes: 0, notes: \"\"",
		label="Was targeting bartering player"];
	131 -> 134;
	132 -> 133;
	134 -> 135;
	137	[comment="name: \"Player Waxed or Unwaxed Copper Block ID\", typeName: \"\", id: 137, branchId: 0, recurseId: -1, attributes: 0, notes: \"\"",
		label="Player Waxed or Unwaxed Copper Block ID"];
	136 -> 137;
	137 -> 138;
	140	[comment="name: \"Code builder runtime action\", typeName: \"\", id: 140, branchId: 0, recurseId: -1, attributes: 0, notes: \"\"",
		label="Code builder runtime action"];
	139 -> 140;
	140 -> 141;
	143	[comment="name: \"Objective Name\", typeName: \"\", id: 143, branchId: 0, recurseId: -1, attributes: 0, notes: \"\"",
		label="Objective Name"];
	142 -> 143;
	145	[comment="name: \"Code Builder Scoreboard Score\", typeName: \"\", id: 145, branchId: 0, recurseId: -1, attributes: 0, notes: \"\"",
		label="Code Builder Scoreboard Score"];
	142 -> 145;
	143 -> 144;
	145 -> 146;
	147 -> 148;
	149 -> 150;
	151 -> 152;
}

```

## 字段

/// define
LegacyTelemetryEventPacket

Target Actor ID：[<!-- md:samp ActorUniqueID -->](refs/protocols/types/ActorUniqueID.md)

- 类型：ActorUniqueID。

Event Type：<!-- md:samp varint -->

- 类型：varint。enumeration: LegacyTelemetryEventPacket::Type

Use Player ID：<!-- md:samp byte -->

- 类型：byte。

Dependency on 'Event Type'

//// tab | if (0)
///// define
if (0)

Achievement ID：<!-- md:samp varint -->

- 类型：varint。


/////

////

//// tab | if (1)
///// define
if (1)

Interaction Type：<!-- md:samp varint -->

- 类型：varint。enumeration: MinecraftEventing::InteractionType

Interaction Actor Type：<!-- md:samp varint -->

- 类型：varint。enumeration: ActorType

Interaction Actor Variant：<!-- md:samp varint -->

- 类型：varint。

Interaction Actor Color：<!-- md:samp byte -->

- 类型：byte。


/////

////

//// tab | if (2)
///// define
if (2)

Dimension ID：<!-- md:samp varint -->

- 类型：varint。Currently supported: (0 -> Overworld, 1 -> Nether, 2 -> The End, 3 -> Undefined)


/////

////

//// tab | if (3)
///// define
if (3)

Source Dimension ID：<!-- md:samp varint -->

- 类型：varint。Currently supported: (0 -> Overworld, 1 -> Nether, 2 -> The End, 3 -> Undefined)

Target Dimension ID：<!-- md:samp varint -->

- 类型：varint。Currently supported: (0 -> Overworld, 1 -> Nether, 2 -> The End, 3 -> Undefined)


/////

////

//// tab | if (4)
///// define
if (4)

Instigator Actor ID：<!-- md:samp varint64 -->

- 类型：varint64。

Target Actor ID：<!-- md:samp varint64 -->

- 类型：varint64。

Instigator's Child Actor Type：<!-- md:samp varint -->

- 类型：varint。enumeration: ActorType

Damage Source：<!-- md:samp varint -->

- 类型：varint。enumeration: ActorDamageCause

Trade Tier：<!-- md:samp varint -->

- 类型：varint。-1 if not a trading actor.

Trader Name：<!-- md:samp string -->

- 类型：string。Empty if not a trading actor.


/////

////

//// tab | if (5)
///// define
if (5)

Contents Color：<!-- md:samp unsigned varint -->

- 类型：unsigned varint。

Contents Type：<!-- md:samp varint -->

- 类型：varint。

Fill Level：<!-- md:samp varint -->

- 类型：varint。


/////

////

//// tab | if (6)
///// define
if (6)

Instigator Actor ID：<!-- md:samp varint -->

- 类型：varint。

Instigator Mob Variant：<!-- md:samp varint -->

- 类型：varint。

Damage Source：<!-- md:samp varint -->

- 类型：varint。enumeration: ActorDamageCause

Died in Raid?：<!-- md:samp bool -->

- 类型：bool。


/////

////

//// tab | if (7)
///// define
if (7)

Boss Actor ID：<!-- md:samp varint64 -->

- 类型：varint64。

Party Size：<!-- md:samp varint -->

- 类型：varint。

Boss Type：<!-- md:samp varint -->

- 类型：varint。enumeration: ActorType


/////

////

//// tab | if (8)
///// define
if (8)

Result：<!-- md:samp varint -->

- 类型：varint。enumeration: LegacyTelemetryEventPacket::AgentResult

Result Number：<!-- md:samp varint -->

- 类型：varint。

Command Name：<!-- md:samp string -->

- 类型：string。

Result Key：<!-- md:samp string -->

- 类型：string。

Result String：<!-- md:samp string -->

- 类型：string。


/////

////

//// tab | if (9)
///// define
if (9)：<!-- md:samp [No Data] -->

- 类型：[No Data]。


/////

////

//// tab | if (10)
///// define
if (10)：<!-- md:samp [No Data] -->

- 类型：[No Data]。


/////

////

//// tab | if (11)
///// define
if (11)

Success Count：<!-- md:samp varint -->

- 类型：varint。

Error Count：<!-- md:samp varint -->

- 类型：varint。

Command Name：<!-- md:samp string -->

- 类型：string。

Error List：<!-- md:samp string -->

- 类型：string。


/////

////

//// tab | if (12)
///// define
if (12)：<!-- md:samp [No Data] -->

- 类型：[No Data]。


/////

////

//// tab | if (13)
///// define
if (13)

Born Baby: Entity Type：<!-- md:samp varint -->

- 类型：varint。

Born Baby: Entity Variant：<!-- md:samp varint -->

- 类型：varint。

Born Baby: Color：<!-- md:samp byte -->

- 类型：byte。


/////

////

//// tab | if (14)
///// define
if (14)：<!-- md:samp [No Data] -->

- 类型：[No Data]。


/////

////

//// tab | if (15)
///// define
if (15)

Block Interaction Type：<!-- md:samp varint -->

- 类型：varint。enumeration: MinecraftEventing::POIBlockInteractionType

Item Id：<!-- md:samp varint -->

- 类型：varint。Id of the relevant item used in the interaction.


/////

////

//// tab | if (16)
///// define
if (16)

Block Interaction Type：<!-- md:samp varint -->

- 类型：varint。enumeration: MinecraftEventing::POIBlockInteractionType

Item Id：<!-- md:samp varint -->

- 类型：varint。Id of the relevant item used in the interaction.


/////

////

//// tab | if (17)
///// define
if (17)

Item Id：<!-- md:samp varint -->

- 类型：varint。Id of the relevant item used in the interaction.


/////

////

//// tab | if (18)
///// define
if (18)

Event Name：<!-- md:samp string -->

- 类型：string。


/////

////

//// tab | if (19)
///// define
if (19)

Current Raid Wave：<!-- md:samp varint -->

- 类型：varint。

Total Raid Waves：<!-- md:samp varint -->

- 类型：varint。

Won Raid：<!-- md:samp bool -->

- 类型：bool。


/////

////

//// tab | if (20)
///// define
if (20)：<!-- md:samp [No Data] -->

- 类型：[No Data]。


/////

////

//// tab | if (21)
///// define
if (21)：<!-- md:samp [No Data] -->

- 类型：[No Data]。


/////

////

//// tab | if (22)
///// define
if (22)：<!-- md:samp [No Data] -->

- 类型：[No Data]。


/////

////

//// tab | if (23)
///// define
if (23)

Redstone Level：<!-- md:samp varint -->

- 类型：varint。


/////

////

//// tab | if (24)
///// define
if (24)

Item Id：<!-- md:samp varint -->

- 类型：varint。

Was targeting bartering player：<!-- md:samp bool -->

- 类型：bool。


/////

////

//// tab | if (25)
///// define
if (25)

Player Waxed or Unwaxed Copper Block ID：<!-- md:samp varint -->

- 类型：varint。


/////

////

//// tab | if (26)
///// define
if (26)

Code builder runtime action：<!-- md:samp string -->

- 类型：string。


/////

////

//// tab | if (27)
///// define
if (27)

Objective Name：<!-- md:samp string -->

- 类型：string。

Code Builder Scoreboard Score：<!-- md:samp varint -->

- 类型：varint。


/////

////

//// tab | if (28)
///// define
if (28)：<!-- md:samp [No Data] -->

- 类型：[No Data]。


/////

////

//// tab | if (29)
///// define
if (29)：<!-- md:samp [No Data] -->

- 类型：[No Data]。


/////

////

//// tab | if (30)
///// define
if (30)：<!-- md:samp [No Data] -->

- 类型：[No Data]。


/////

////



///
