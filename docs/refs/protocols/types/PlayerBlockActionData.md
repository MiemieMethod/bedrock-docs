# <!-- md:samp PlayerBlockActionData -->

> 文档版本：r/20_u7<br/>协议版本：662

<!-- md:samp PlayerBlockActionData -->类型。

## 结构

```viz
digraph PlayerBlockActionData {
	graph [rankdir=LR];
	{
		graph [rank=max];
		126	[comment="name: \"varint\", typeName: \"\", id: 126, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=varint];
		130	[comment="name: \"BlockPos\", typeName: \"\", id: 130, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=BlockPos];
		132	[comment="name: \"varint\", typeName: \"\", id: 132, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=varint];
		135	[comment="name: \"BlockPos\", typeName: \"\", id: 135, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=BlockPos];
		137	[comment="name: \"varint\", typeName: \"\", id: 137, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=varint];
		140	[comment="name: \"BlockPos\", typeName: \"\", id: 140, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=BlockPos];
		142	[comment="name: \"varint\", typeName: \"\", id: 142, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=varint];
		145	[comment="name: \"BlockPos\", typeName: \"\", id: 145, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=BlockPos];
		147	[comment="name: \"varint\", typeName: \"\", id: 147, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=varint];
		150	[comment="name: \"BlockPos\", typeName: \"\", id: 150, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=BlockPos];
		152	[comment="name: \"varint\", typeName: \"\", id: 152, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=varint];
		155	[comment="name: \"BlockPos\", typeName: \"\", id: 155, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=BlockPos];
		157	[comment="name: \"varint\", typeName: \"\", id: 157, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=varint];
	}
	124	[comment="name: \"PlayerBlockActionData\", typeName: \"\", id: 124, branchId: 0, recurseId: -1, attributes: 0, notes: \"\"",
		label=PlayerBlockActionData];
	125	[comment="name: \"Player Action Type\", typeName: \"\", id: 125, branchId: 0, recurseId: -1, attributes: 0, notes: \"\"",
		label="Player Action Type"];
	124 -> 125;
	127	[comment="name: \"Dependency on 'Player Action Type'\", typeName: \"\", id: 127, branchId: 0, recurseId: -1, attributes: 2, notes: \"\"",
		label="Dependency on 'Player Action Type'",
		shape=note];
	124 -> 127;
	125 -> 126;
	128	[comment="name: \"if (26)\", typeName: \"\", id: 128, branchId: 26, recurseId: -1, attributes: 4, notes: \"\"",
		label="if (26)",
		shape=diamond];
	127 -> 128;
	133	[comment="name: \"if (0)\", typeName: \"\", id: 133, branchId: 0, recurseId: -1, attributes: 4, notes: \"\"",
		label="if (0)",
		shape=diamond];
	127 -> 133;
	138	[comment="name: \"if (1)\", typeName: \"\", id: 138, branchId: 1, recurseId: -1, attributes: 4, notes: \"\"",
		label="if (1)",
		shape=diamond];
	127 -> 138;
	143	[comment="name: \"if (18)\", typeName: \"\", id: 143, branchId: 18, recurseId: -1, attributes: 4, notes: \"\"",
		label="if (18)",
		shape=diamond];
	127 -> 143;
	148	[comment="name: \"if (27)\", typeName: \"\", id: 148, branchId: 27, recurseId: -1, attributes: 4, notes: \"\"",
		label="if (27)",
		shape=diamond];
	127 -> 148;
	153	[comment="name: \"if (2)\", typeName: \"\", id: 153, branchId: 2, recurseId: -1, attributes: 4, notes: \"\"",
		label="if (2)",
		shape=diamond];
	127 -> 153;
	129	[comment="name: \"Position\", typeName: \"BlockPos\", id: 129, branchId: 0, recurseId: -1, attributes: 256, notes: \"\"",
		label=Position];
	128 -> 129;
	131	[comment="name: \"Facing\", typeName: \"\", id: 131, branchId: 0, recurseId: -1, attributes: 0, notes: \"\"",
		label=Facing];
	128 -> 131;
	129 -> 130;
	131 -> 132;
	134	[comment="name: \"Position\", typeName: \"BlockPos\", id: 134, branchId: 0, recurseId: -1, attributes: 256, notes: \"\"",
		label=Position];
	133 -> 134;
	136	[comment="name: \"Facing\", typeName: \"\", id: 136, branchId: 0, recurseId: -1, attributes: 0, notes: \"\"",
		label=Facing];
	133 -> 136;
	134 -> 135;
	136 -> 137;
	139	[comment="name: \"Position\", typeName: \"BlockPos\", id: 139, branchId: 0, recurseId: -1, attributes: 256, notes: \"\"",
		label=Position];
	138 -> 139;
	141	[comment="name: \"Facing\", typeName: \"\", id: 141, branchId: 0, recurseId: -1, attributes: 0, notes: \"\"",
		label=Facing];
	138 -> 141;
	139 -> 140;
	141 -> 142;
	144	[comment="name: \"Position\", typeName: \"BlockPos\", id: 144, branchId: 0, recurseId: -1, attributes: 256, notes: \"\"",
		label=Position];
	143 -> 144;
	146	[comment="name: \"Facing\", typeName: \"\", id: 146, branchId: 0, recurseId: -1, attributes: 0, notes: \"\"",
		label=Facing];
	143 -> 146;
	144 -> 145;
	146 -> 147;
	149	[comment="name: \"Position\", typeName: \"BlockPos\", id: 149, branchId: 0, recurseId: -1, attributes: 256, notes: \"\"",
		label=Position];
	148 -> 149;
	151	[comment="name: \"Facing\", typeName: \"\", id: 151, branchId: 0, recurseId: -1, attributes: 0, notes: \"\"",
		label=Facing];
	148 -> 151;
	149 -> 150;
	151 -> 152;
	154	[comment="name: \"Position\", typeName: \"BlockPos\", id: 154, branchId: 0, recurseId: -1, attributes: 256, notes: \"\"",
		label=Position];
	153 -> 154;
	156	[comment="name: \"Facing\", typeName: \"\", id: 156, branchId: 0, recurseId: -1, attributes: 0, notes: \"\"",
		label=Facing];
	153 -> 156;
	154 -> 155;
	156 -> 157;
}

```

## 字段

/// define
PlayerBlockActionData

Player Action Type：<!-- md:samp varint -->

- 类型：varint。

Dependency on 'Player Action Type'

//// tab | if (26)
///// define
if (26)

Position：[<!-- md:samp BlockPos -->](refs/protocols/types/BlockPos.md)

- 类型：BlockPos。

Facing：<!-- md:samp varint -->

- 类型：varint。


/////

////

//// tab | if (0)
///// define
if (0)

Position：[<!-- md:samp BlockPos -->](refs/protocols/types/BlockPos.md)

- 类型：BlockPos。

Facing：<!-- md:samp varint -->

- 类型：varint。


/////

////

//// tab | if (1)
///// define
if (1)

Position：[<!-- md:samp BlockPos -->](refs/protocols/types/BlockPos.md)

- 类型：BlockPos。

Facing：<!-- md:samp varint -->

- 类型：varint。


/////

////

//// tab | if (18)
///// define
if (18)

Position：[<!-- md:samp BlockPos -->](refs/protocols/types/BlockPos.md)

- 类型：BlockPos。

Facing：<!-- md:samp varint -->

- 类型：varint。


/////

////

//// tab | if (27)
///// define
if (27)

Position：[<!-- md:samp BlockPos -->](refs/protocols/types/BlockPos.md)

- 类型：BlockPos。

Facing：<!-- md:samp varint -->

- 类型：varint。


/////

////

//// tab | if (2)
///// define
if (2)

Position：[<!-- md:samp BlockPos -->](refs/protocols/types/BlockPos.md)

- 类型：BlockPos。

Facing：<!-- md:samp varint -->

- 类型：varint。


/////

////



///
