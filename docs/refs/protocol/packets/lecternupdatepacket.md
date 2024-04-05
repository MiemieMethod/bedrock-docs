# <!-- md:samp LecternUpdatePacket -->

> 文档版本：r/20_u7<br/>协议版本：662

<!-- md:samp LecternUpdatePacket -->数据包，数字ID是`125`。

## 结构

```viz
digraph LecternUpdatePacket {
	graph [rankdir=LR];
	{
		graph [rank=max];
		2	[comment="name: \"byte\", typeName: \"\", id: 2, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=byte];
		4	[comment="name: \"byte\", typeName: \"\", id: 4, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=byte];
		6	[comment="name: \"NetworkBlockPosition\", typeName: \"\", id: 6, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=NetworkBlockPosition];
	}
	0	[comment="name: \"LecternUpdatePacket\", typeName: \"\", id: 0, branchId: 125, recurseId: -1, attributes: 0, notes: \"\"",
		label=LecternUpdatePacket];
	1	[comment="name: \"New page to show\", typeName: \"\", id: 1, branchId: 0, recurseId: -1, attributes: 0, notes: \"\"",
		label="New page to show"];
	0 -> 1;
	3	[comment="name: \"Total Pages\", typeName: \"\", id: 3, branchId: 0, recurseId: -1, attributes: 0, notes: \"\"",
		label="Total Pages"];
	0 -> 3;
	5	[comment="name: \"Position of Lectern to update\", typeName: \"NetworkBlockPosition\", id: 5, branchId: 0, recurseId: -1, attributes: 256, notes: \"\"",
		label="Position of Lectern to update"];
	0 -> 5;
	1 -> 2;
	3 -> 4;
	5 -> 6;
}

```

## 字段

/// define
LecternUpdatePacket

New page to show：<!-- md:samp byte -->

- 类型：byte。

Total Pages：<!-- md:samp byte -->

- 类型：byte。

Position of Lectern to update：[<!-- md:samp NetworkBlockPosition -->](refs/protocols/types/networkblockposition.md)

- 类型：NetworkBlockPosition。


///
