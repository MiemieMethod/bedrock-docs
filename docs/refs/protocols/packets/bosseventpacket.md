# <!-- md:samp BossEventPacket -->

> 文档版本：r/20_u7<br/>协议版本：662

<!-- md:samp BossEventPacket -->数据包，数字ID是`74`。

## 结构

```viz
digraph BossEventPacket {
	graph [rankdir=LR];
	{
		graph [rank=max];
		2	[comment="name: \"ActorUniqueID\", typeName: \"\", id: 2, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=ActorUniqueID];
		4	[comment="name: \"int\", typeName: \"\", id: 4, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=int];
		8	[comment="name: \"string\", typeName: \"\", id: 8, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=string];
		10	[comment="name: \"float\", typeName: \"\", id: 10, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=float];
		12	[comment="name: \"unsigned short\", typeName: \"\", id: 12, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label="unsigned short"];
		14	[comment="name: \"unsigned varint\", typeName: \"\", id: 14, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label="unsigned varint"];
		16	[comment="name: \"unsigned varint\", typeName: \"\", id: 16, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label="unsigned varint"];
		19	[comment="name: \"ActorUniqueID\", typeName: \"\", id: 19, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=ActorUniqueID];
		21	[comment="name: \"[No Data]\", typeName: \"\", id: 21, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label="[No Data]"];
		24	[comment="name: \"ActorUniqueID\", typeName: \"\", id: 24, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=ActorUniqueID];
		27	[comment="name: \"float\", typeName: \"\", id: 27, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=float];
		30	[comment="name: \"string\", typeName: \"\", id: 30, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=string];
		33	[comment="name: \"unsigned short\", typeName: \"\", id: 33, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label="unsigned short"];
		35	[comment="name: \"unsigned varint\", typeName: \"\", id: 35, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label="unsigned varint"];
		37	[comment="name: \"unsigned varint\", typeName: \"\", id: 37, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label="unsigned varint"];
		40	[comment="name: \"unsigned varint\", typeName: \"\", id: 40, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label="unsigned varint"];
		42	[comment="name: \"unsigned varint\", typeName: \"\", id: 42, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label="unsigned varint"];
		45	[comment="name: \"ActorUniqueID\", typeName: \"\", id: 45, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=ActorUniqueID];
	}
	0	[comment="name: \"BossEventPacket\", typeName: \"\", id: 0, branchId: 74, recurseId: -1, attributes: 0, notes: \"\"",
		label=BossEventPacket];
	1	[comment="name: \"Target Actor ID\", typeName: \"ActorUniqueID\", id: 1, branchId: 0, recurseId: -1, attributes: 256, notes: \"\"",
		label="Target Actor ID"];
	0 -> 1;
	3	[comment="name: \"Event Type\", typeName: \"\", id: 3, branchId: 0, recurseId: -1, attributes: 0, notes: \"enumeration: BossEventUpdateType\"",
		label="Event Type"];
	0 -> 3;
	5	[comment="name: \"Dependency on 'Event Type'\", typeName: \"\", id: 5, branchId: 0, recurseId: -1, attributes: 2, notes: \"\"",
		label="Dependency on 'Event Type'",
		shape=note];
	0 -> 5;
	1 -> 2;
	3 -> 4;
	6	[comment="name: \"if (0)\", typeName: \"\", id: 6, branchId: 0, recurseId: -1, attributes: 4, notes: \"\"",
		label="if (0)",
		shape=diamond];
	5 -> 6;
	17	[comment="name: \"if (1)\", typeName: \"\", id: 17, branchId: 1, recurseId: -1, attributes: 4, notes: \"\"",
		label="if (1)",
		shape=diamond];
	5 -> 17;
	20	[comment="name: \"if (2)\", typeName: \"\", id: 20, branchId: 2, recurseId: -1, attributes: 4, notes: \"\"",
		label="if (2)",
		shape=diamond];
	5 -> 20;
	22	[comment="name: \"if (3)\", typeName: \"\", id: 22, branchId: 3, recurseId: -1, attributes: 4, notes: \"\"",
		label="if (3)",
		shape=diamond];
	5 -> 22;
	25	[comment="name: \"if (4)\", typeName: \"\", id: 25, branchId: 4, recurseId: -1, attributes: 4, notes: \"\"",
		label="if (4)",
		shape=diamond];
	5 -> 25;
	28	[comment="name: \"if (5)\", typeName: \"\", id: 28, branchId: 5, recurseId: -1, attributes: 4, notes: \"\"",
		label="if (5)",
		shape=diamond];
	5 -> 28;
	31	[comment="name: \"if (6)\", typeName: \"\", id: 31, branchId: 6, recurseId: -1, attributes: 4, notes: \"\"",
		label="if (6)",
		shape=diamond];
	5 -> 31;
	38	[comment="name: \"if (7)\", typeName: \"\", id: 38, branchId: 7, recurseId: -1, attributes: 4, notes: \"\"",
		label="if (7)",
		shape=diamond];
	5 -> 38;
	43	[comment="name: \"if (8)\", typeName: \"\", id: 43, branchId: 8, recurseId: -1, attributes: 4, notes: \"\"",
		label="if (8)",
		shape=diamond];
	5 -> 43;
	7	[comment="name: \"Name\", typeName: \"\", id: 7, branchId: 0, recurseId: -1, attributes: 0, notes: \"Name of the boss to add\"",
		label=Name];
	6 -> 7;
	9	[comment="name: \"Health Percent\", typeName: \"\", id: 9, branchId: 0, recurseId: -1, attributes: 0, notes: \"Health value of the boss\"",
		label="Health Percent"];
	6 -> 9;
	11	[comment="name: \"Darken Screen\", typeName: \"\", id: 11, branchId: 0, recurseId: -1, attributes: 0, notes: \"A boolean value for whether or not \
we should darken the screen (has a 0 or 1 value)\"",
		label="Darken Screen"];
	6 -> 11;
	13	[comment="name: \"Color\", typeName: \"\", id: 13, branchId: 0, recurseId: -1, attributes: 0, notes: \"color for the boss bar, listed in an enumeration\"",
		label=Color];
	6 -> 13;
	15	[comment="name: \"Overlay\", typeName: \"\", id: 15, branchId: 0, recurseId: -1, attributes: 0, notes: \"overlay for the boss bar, listed in an \
enumeration\"",
		label=Overlay];
	6 -> 15;
	7 -> 8;
	9 -> 10;
	11 -> 12;
	13 -> 14;
	15 -> 16;
	18	[comment="name: \"Player ID\", typeName: \"ActorUniqueID\", id: 18, branchId: 0, recurseId: -1, attributes: 256, notes: \"\"",
		label="Player ID"];
	17 -> 18;
	18 -> 19;
	20 -> 21;
	23	[comment="name: \"Player ID\", typeName: \"ActorUniqueID\", id: 23, branchId: 0, recurseId: -1, attributes: 256, notes: \"\"",
		label="Player ID"];
	22 -> 23;
	23 -> 24;
	26	[comment="name: \"Health Percent\", typeName: \"\", id: 26, branchId: 0, recurseId: -1, attributes: 0, notes: \"\"",
		label="Health Percent"];
	25 -> 26;
	26 -> 27;
	29	[comment="name: \"Name\", typeName: \"\", id: 29, branchId: 0, recurseId: -1, attributes: 0, notes: \"\"",
		label=Name];
	28 -> 29;
	29 -> 30;
	32	[comment="name: \"Darken Screen\", typeName: \"\", id: 32, branchId: 0, recurseId: -1, attributes: 0, notes: \"\"",
		label="Darken Screen"];
	31 -> 32;
	34	[comment="name: \"Color\", typeName: \"\", id: 34, branchId: 0, recurseId: -1, attributes: 0, notes: \"\"",
		label=Color];
	31 -> 34;
	36	[comment="name: \"Overlay\", typeName: \"\", id: 36, branchId: 0, recurseId: -1, attributes: 0, notes: \"\"",
		label=Overlay];
	31 -> 36;
	32 -> 33;
	34 -> 35;
	36 -> 37;
	39	[comment="name: \"Color\", typeName: \"\", id: 39, branchId: 0, recurseId: -1, attributes: 0, notes: \"\"",
		label=Color];
	38 -> 39;
	41	[comment="name: \"Overlay\", typeName: \"\", id: 41, branchId: 0, recurseId: -1, attributes: 0, notes: \"\"",
		label=Overlay];
	38 -> 41;
	39 -> 40;
	41 -> 42;
	44	[comment="name: \"Player ID\", typeName: \"ActorUniqueID\", id: 44, branchId: 0, recurseId: -1, attributes: 256, notes: \"\"",
		label="Player ID"];
	43 -> 44;
	44 -> 45;
}

```

## 字段

/// define
BossEventPacket

Target Actor ID：[<!-- md:samp ActorUniqueID -->](../types/actoruniqueid.md)

- 类型：ActorUniqueID。

Event Type：<!-- md:samp int -->

- 类型：int。enumeration: BossEventUpdateType

Dependency on 'Event Type'

//// tab | if (0)
///// define
if (0)

Name：<!-- md:samp string -->

- 类型：string。Name of the boss to add

Health Percent：<!-- md:samp float -->

- 类型：float。Health value of the boss

Darken Screen：<!-- md:samp unsigned short -->

- 类型：unsigned short。A boolean value for whether or not we should darken the screen (has a 0 or 1 value)

Color：<!-- md:samp unsigned varint -->

- 类型：unsigned varint。color for the boss bar, listed in an enumeration

Overlay：<!-- md:samp unsigned varint -->

- 类型：unsigned varint。overlay for the boss bar, listed in an enumeration


/////

////

//// tab | if (1)
///// define
if (1)

Player ID：[<!-- md:samp ActorUniqueID -->](../types/actoruniqueid.md)

- 类型：ActorUniqueID。


/////

////

//// tab | if (2)
///// define
if (2)：<!-- md:samp [No Data] -->

- 类型：[No Data]。


/////

////

//// tab | if (3)
///// define
if (3)

Player ID：[<!-- md:samp ActorUniqueID -->](../types/actoruniqueid.md)

- 类型：ActorUniqueID。


/////

////

//// tab | if (4)
///// define
if (4)

Health Percent：<!-- md:samp float -->

- 类型：float。


/////

////

//// tab | if (5)
///// define
if (5)

Name：<!-- md:samp string -->

- 类型：string。


/////

////

//// tab | if (6)
///// define
if (6)

Darken Screen：<!-- md:samp unsigned short -->

- 类型：unsigned short。

Color：<!-- md:samp unsigned varint -->

- 类型：unsigned varint。

Overlay：<!-- md:samp unsigned varint -->

- 类型：unsigned varint。


/////

////

//// tab | if (7)
///// define
if (7)

Color：<!-- md:samp unsigned varint -->

- 类型：unsigned varint。

Overlay：<!-- md:samp unsigned varint -->

- 类型：unsigned varint。


/////

////

//// tab | if (8)
///// define
if (8)

Player ID：[<!-- md:samp ActorUniqueID -->](../types/actoruniqueid.md)

- 类型：ActorUniqueID。


/////

////



///
