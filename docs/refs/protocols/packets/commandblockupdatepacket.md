# <!-- md:samp CommandBlockUpdatePacket -->

> 文档版本：r/20_u7<br/>协议版本：662

<!-- md:samp CommandBlockUpdatePacket -->数据包，数字ID是`78`。

## 结构

```viz
digraph CommandBlockUpdatePacket {
	graph [rankdir=LR];
	{
		graph [rank=max];
		2	[comment="name: \"bool\", typeName: \"\", id: 2, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=bool];
		6	[comment="name: \"ActorRuntimeID\", typeName: \"\", id: 6, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=ActorRuntimeID];
		9	[comment="name: \"NetworkBlockPosition\", typeName: \"\", id: 9, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=NetworkBlockPosition];
		11	[comment="name: \"unsigned varint\", typeName: \"\", id: 11, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label="unsigned varint"];
		13	[comment="name: \"bool\", typeName: \"\", id: 13, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=bool];
		15	[comment="name: \"bool\", typeName: \"\", id: 15, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=bool];
		17	[comment="name: \"string\", typeName: \"\", id: 17, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=string];
		19	[comment="name: \"string\", typeName: \"\", id: 19, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=string];
		21	[comment="name: \"string\", typeName: \"\", id: 21, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=string];
		23	[comment="name: \"bool\", typeName: \"\", id: 23, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=bool];
		25	[comment="name: \"unsigned int\", typeName: \"\", id: 25, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label="unsigned int"];
		27	[comment="name: \"bool\", typeName: \"\", id: 27, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=bool];
	}
	0	[comment="name: \"CommandBlockUpdatePacket\", typeName: \"\", id: 0, branchId: 78, recurseId: -1, attributes: 0, notes: \"\"",
		label=CommandBlockUpdatePacket];
	1	[comment="name: \"Is Block?\", typeName: \"\", id: 1, branchId: 0, recurseId: -1, attributes: 0, notes: \"\"",
		label="Is Block?"];
	0 -> 1;
	3	[comment="name: \"Dependency on 'Is Block?'\", typeName: \"\", id: 3, branchId: 0, recurseId: -1, attributes: 2, notes: \"\"",
		label="Dependency on 'Is Block?'",
		shape=note];
	0 -> 3;
	16	[comment="name: \"Command\", typeName: \"\", id: 16, branchId: 0, recurseId: -1, attributes: 0, notes: \"\"",
		label=Command];
	0 -> 16;
	18	[comment="name: \"Last Output\", typeName: \"\", id: 18, branchId: 0, recurseId: -1, attributes: 0, notes: \"\"",
		label="Last Output"];
	0 -> 18;
	20	[comment="name: \"Name\", typeName: \"\", id: 20, branchId: 0, recurseId: -1, attributes: 0, notes: \"\"",
		label=Name];
	0 -> 20;
	22	[comment="name: \"Track Output?\", typeName: \"\", id: 22, branchId: 0, recurseId: -1, attributes: 0, notes: \"\"",
		label="Track Output?"];
	0 -> 22;
	24	[comment="name: \"Tick Delay\", typeName: \"\", id: 24, branchId: 0, recurseId: -1, attributes: 0, notes: \"\"",
		label="Tick Delay"];
	0 -> 24;
	26	[comment="name: \"Should execute on first tick?\", typeName: \"\", id: 26, branchId: 0, recurseId: -1, attributes: 0, notes: \"If a delay is set \
on a repeating command block, should the command execute on first tick, or on first delay?\"",
		label="Should execute on first tick?"];
	0 -> 26;
	1 -> 2;
	4	[comment="name: \"if (0)\", typeName: \"\", id: 4, branchId: 0, recurseId: -1, attributes: 4, notes: \"\"",
		label="if (0)",
		shape=diamond];
	3 -> 4;
	7	[comment="name: \"if (1)\", typeName: \"\", id: 7, branchId: 1, recurseId: -1, attributes: 4, notes: \"\"",
		label="if (1)",
		shape=diamond];
	3 -> 7;
	5	[comment="name: \"Target Runtime ID\", typeName: \"ActorRuntimeID\", id: 5, branchId: 0, recurseId: -1, attributes: 256, notes: \"\"",
		label="Target Runtime ID"];
	4 -> 5;
	5 -> 6;
	8	[comment="name: \"Block Position\", typeName: \"NetworkBlockPosition\", id: 8, branchId: 0, recurseId: -1, attributes: 256, notes: \"\"",
		label="Block Position"];
	7 -> 8;
	10	[comment="name: \"Command Block Mode\", typeName: \"\", id: 10, branchId: 0, recurseId: -1, attributes: 0, notes: \"enumeration: CommandBlockMode\"",
		label="Command Block Mode"];
	7 -> 10;
	12	[comment="name: \"Redstone Mode\", typeName: \"\", id: 12, branchId: 0, recurseId: -1, attributes: 0, notes: \"\"",
		label="Redstone Mode"];
	7 -> 12;
	14	[comment="name: \"Is Conditional?\", typeName: \"\", id: 14, branchId: 0, recurseId: -1, attributes: 0, notes: \"\"",
		label="Is Conditional?"];
	7 -> 14;
	8 -> 9;
	10 -> 11;
	12 -> 13;
	14 -> 15;
	16 -> 17;
	18 -> 19;
	20 -> 21;
	22 -> 23;
	24 -> 25;
	26 -> 27;
}

```

## 字段

/// define
CommandBlockUpdatePacket

Is Block?：<!-- md:samp bool -->

- 类型：bool。

Dependency on 'Is Block?'

//// tab | if (0)
///// define
if (0)

Target Runtime ID：[<!-- md:samp ActorRuntimeID -->](../types/actorruntimeid.md)

- 类型：ActorRuntimeID。


/////

////

//// tab | if (1)
///// define
if (1)

Block Position：[<!-- md:samp NetworkBlockPosition -->](../types/networkblockposition.md)

- 类型：NetworkBlockPosition。

Command Block Mode：<!-- md:samp unsigned varint -->

- 类型：unsigned varint。enumeration: CommandBlockMode

Redstone Mode：<!-- md:samp bool -->

- 类型：bool。

Is Conditional?：<!-- md:samp bool -->

- 类型：bool。


/////

////


Command：<!-- md:samp string -->

- 类型：string。

Last Output：<!-- md:samp string -->

- 类型：string。

Name：<!-- md:samp string -->

- 类型：string。

Track Output?：<!-- md:samp bool -->

- 类型：bool。

Tick Delay：<!-- md:samp unsigned int -->

- 类型：unsigned int。

Should execute on first tick?：<!-- md:samp bool -->

- 类型：bool。If a delay is set on a repeating command block, should the command execute on first tick, or on first delay?


///
