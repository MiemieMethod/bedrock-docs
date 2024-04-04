# <!-- md:samp ChangeMobPropertyPacket -->

> 文档版本：r/20_u7<br/>协议版本：662

<!-- md:samp ChangeMobPropertyPacket -->数据包，数字ID是`182`。

## 结构

```viz
digraph ChangeMobPropertyPacket {
	graph [rankdir=LR];
	{
		graph [rank=max];
		2	[comment="name: \"ActorUniqueID\", typeName: \"\", id: 2, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=ActorUniqueID];
		4	[comment="name: \"string\", typeName: \"\", id: 4, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=string];
		6	[comment="name: \"bool\", typeName: \"\", id: 6, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=bool];
		8	[comment="name: \"string\", typeName: \"\", id: 8, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=string];
		10	[comment="name: \"varint\", typeName: \"\", id: 10, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=varint];
		12	[comment="name: \"float\", typeName: \"\", id: 12, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=float];
	}
	0	[comment="name: \"ChangeMobPropertyPacket\", typeName: \"\", id: 0, branchId: 182, recurseId: -1, attributes: 0, notes: \"\"",
		label=ChangeMobPropertyPacket];
	1	[comment="name: \"Actor Id\", typeName: \"ActorUniqueID\", id: 1, branchId: 0, recurseId: -1, attributes: 256, notes: \"\"",
		label="Actor Id"];
	0 -> 1;
	3	[comment="name: \"Property Name\", typeName: \"\", id: 3, branchId: 0, recurseId: -1, attributes: 0, notes: \"\"",
		label="Property Name"];
	0 -> 3;
	5	[comment="name: \"BoolComponent Value\", typeName: \"\", id: 5, branchId: 0, recurseId: -1, attributes: 0, notes: \"\"",
		label="BoolComponent Value"];
	0 -> 5;
	7	[comment="name: \"StringComponent Value\", typeName: \"\", id: 7, branchId: 0, recurseId: -1, attributes: 0, notes: \"\"",
		label="StringComponent Value"];
	0 -> 7;
	9	[comment="name: \"IntComponent Value\", typeName: \"\", id: 9, branchId: 0, recurseId: -1, attributes: 0, notes: \"\"",
		label="IntComponent Value"];
	0 -> 9;
	11	[comment="name: \"FloatComponent Value\", typeName: \"\", id: 11, branchId: 0, recurseId: -1, attributes: 0, notes: \"\"",
		label="FloatComponent Value"];
	0 -> 11;
	1 -> 2;
	3 -> 4;
	5 -> 6;
	7 -> 8;
	9 -> 10;
	11 -> 12;
}

```

## 字段

/// define
ChangeMobPropertyPacket

Actor Id：[<!-- md:samp ActorUniqueID -->](refs/protocols/types/ActorUniqueID.md)

- 类型：ActorUniqueID。

Property Name：<!-- md:samp string -->

- 类型：string。

BoolComponent Value：<!-- md:samp bool -->

- 类型：bool。

StringComponent Value：<!-- md:samp string -->

- 类型：string。

IntComponent Value：<!-- md:samp varint -->

- 类型：varint。

FloatComponent Value：<!-- md:samp float -->

- 类型：float。


///
