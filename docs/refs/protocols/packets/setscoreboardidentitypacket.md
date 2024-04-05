# <!-- md:samp SetScoreboardIdentityPacket -->

> 文档版本：r/20_u7<br/>协议版本：662

<!-- md:samp SetScoreboardIdentityPacket -->数据包，数字ID是`112`。

## 结构

```viz
digraph SetScoreboardIdentityPacket {
	graph [rankdir=LR];
	{
		graph [rank=max];
		2	[comment="name: \"byte\", typeName: \"\", id: 2, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=byte];
		5	[comment="name: \"unsigned varint\", typeName: \"\", id: 5, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label="unsigned varint"];
		8	[comment="name: \"ScoreboardId\", typeName: \"\", id: 8, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=ScoreboardId];
		11	[comment="name: \"[No Data]\", typeName: \"\", id: 11, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label="[No Data]"];
		14	[comment="name: \"varint64\", typeName: \"\", id: 14, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=varint64];
	}
	0	[comment="name: \"SetScoreboardIdentityPacket\", typeName: \"\", id: 0, branchId: 112, recurseId: -1, attributes: 0, notes: \"\"",
		label=SetScoreboardIdentityPacket];
	1	[comment="name: \"Scoreboard Identity Packet Type\", typeName: \"\", id: 1, branchId: 0, recurseId: -1, attributes: 0, notes: \"enumeration: ScoreboardIdentityPacketType\"",
		label="Scoreboard Identity Packet Type"];
	0 -> 1;
	3	[comment="name: \"Identity Info\", typeName: \"\", id: 3, branchId: 0, recurseId: -1, attributes: 8, notes: \"\"",
		label="Identity Info"];
	0 -> 3;
	1 -> 2;
	4	[comment="name: \"Array Size\", typeName: \"\", id: 4, branchId: 0, recurseId: -1, attributes: 0, notes: \"\"",
		label="Array Size"];
	3 -> 4;
	6	[comment="name: \"example element\", typeName: \"\", id: 6, branchId: 0, recurseId: -1, attributes: 16, notes: \"\"",
		label="example element",
		style=dotted];
	3 -> 6;
	4 -> 5;
	7	[comment="name: \"Scoreboard Id\", typeName: \"ScoreboardId\", id: 7, branchId: 0, recurseId: -1, attributes: 256, notes: \"\"",
		label="Scoreboard Id"];
	6 -> 7;
	9	[comment="name: \"Dependency on 'Is Update Type'\", typeName: \"\", id: 9, branchId: 0, recurseId: -1, attributes: 2, notes: \"\"",
		label="Dependency on 'Is Update Type'",
		shape=note];
	6 -> 9;
	7 -> 8;
	10	[comment="name: \"if (0)\", typeName: \"\", id: 10, branchId: 0, recurseId: -1, attributes: 4, notes: \"\"",
		label="if (0)",
		shape=diamond];
	9 -> 10;
	12	[comment="name: \"if (1)\", typeName: \"\", id: 12, branchId: 1, recurseId: -1, attributes: 4, notes: \"\"",
		label="if (1)",
		shape=diamond];
	9 -> 12;
	10 -> 11;
	13	[comment="name: \"Player Unique Id\", typeName: \"\", id: 13, branchId: 0, recurseId: -1, attributes: 0, notes: \"\"",
		label="Player Unique Id"];
	12 -> 13;
	13 -> 14;
}

```

## 字段

/// define
SetScoreboardIdentityPacket

Scoreboard Identity Packet Type：<!-- md:samp byte -->

- 类型：byte。enumeration: ScoreboardIdentityPacketType

Identity Info

//// define
Identity Info数组的大小：<!-- md:samp unsigned varint -->

- 类型：unsigned varint。


////


//// define
Identity Info的示例元素

Scoreboard Id：[<!-- md:samp ScoreboardId -->](../types/scoreboardid.md)

- 类型：ScoreboardId。

Dependency on 'Is Update Type'

///// tab | if (0)
////// define
if (0)：<!-- md:samp [No Data] -->

- 类型：[No Data]。


//////

/////

///// tab | if (1)
////// define
if (1)

Player Unique Id：<!-- md:samp varint64 -->

- 类型：varint64。


//////

/////



////



///
