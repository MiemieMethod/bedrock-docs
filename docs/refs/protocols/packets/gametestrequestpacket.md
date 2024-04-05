# <!-- md:samp GameTestRequestPacket -->

> 文档版本：r/20_u7<br/>协议版本：662

<!-- md:samp GameTestRequestPacket -->数据包，数字ID是`194`。

## 结构

```viz
digraph GameTestRequestPacket {
	graph [rankdir=LR];
	{
		graph [rank=max];
		2	[comment="name: \"varint\", typeName: \"\", id: 2, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=varint];
		4	[comment="name: \"varint\", typeName: \"\", id: 4, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=varint];
		6	[comment="name: \"byte\", typeName: \"\", id: 6, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=byte];
		8	[comment="name: \"bool\", typeName: \"\", id: 8, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=bool];
		10	[comment="name: \"BlockPos\", typeName: \"\", id: 10, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=BlockPos];
		12	[comment="name: \"varint\", typeName: \"\", id: 12, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=varint];
		14	[comment="name: \"string\", typeName: \"\", id: 14, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=string];
	}
	0	[comment="name: \"GameTestRequestPacket\", typeName: \"\", id: 0, branchId: 194, recurseId: -1, attributes: 0, notes: \"\"",
		label=GameTestRequestPacket];
	1	[comment="name: \"MaxTestsPerBatch\", typeName: \"\", id: 1, branchId: 0, recurseId: -1, attributes: 0, notes: \"\"",
		label=MaxTestsPerBatch];
	0 -> 1;
	3	[comment="name: \"RepeatCount\", typeName: \"\", id: 3, branchId: 0, recurseId: -1, attributes: 0, notes: \"\"",
		label=RepeatCount];
	0 -> 3;
	5	[comment="name: \"Rotation\", typeName: \"\", id: 5, branchId: 0, recurseId: -1, attributes: 0, notes: \"enumeration: Rotation\"",
		label=Rotation];
	0 -> 5;
	7	[comment="name: \"StopOnFailure\", typeName: \"\", id: 7, branchId: 0, recurseId: -1, attributes: 0, notes: \"\"",
		label=StopOnFailure];
	0 -> 7;
	9	[comment="name: \"TestPos\", typeName: \"BlockPos\", id: 9, branchId: 0, recurseId: -1, attributes: 256, notes: \"\"",
		label=TestPos];
	0 -> 9;
	11	[comment="name: \"TestsPerRow\", typeName: \"\", id: 11, branchId: 0, recurseId: -1, attributes: 0, notes: \"\"",
		label=TestsPerRow];
	0 -> 11;
	13	[comment="name: \"TestName\", typeName: \"\", id: 13, branchId: 0, recurseId: -1, attributes: 0, notes: \"\"",
		label=TestName];
	0 -> 13;
	1 -> 2;
	3 -> 4;
	5 -> 6;
	7 -> 8;
	9 -> 10;
	11 -> 12;
	13 -> 14;
}

```

## 字段

/// define
GameTestRequestPacket

MaxTestsPerBatch：<!-- md:samp varint -->

- 类型：varint。

RepeatCount：<!-- md:samp varint -->

- 类型：varint。

Rotation：<!-- md:samp byte -->

- 类型：byte。enumeration: Rotation

StopOnFailure：<!-- md:samp bool -->

- 类型：bool。

TestPos：[<!-- md:samp BlockPos -->](refs/protocols/types/blockpos.md)

- 类型：BlockPos。

TestsPerRow：<!-- md:samp varint -->

- 类型：varint。

TestName：<!-- md:samp string -->

- 类型：string。


///
