# <!-- md:samp OpenSignPacket -->

> 文档版本：r/20_u7<br/>协议版本：662

<!-- md:samp OpenSignPacket -->数据包，数字ID是`303`。

## 结构

```dot
digraph OpenSignPacket {
	graph [rankdir=LR];
	{
		graph [rank=max];
		2	[comment="name: \"NetworkBlockPosition\", typeName: \"\", id: 2, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=NetworkBlockPosition];
		4	[comment="name: \"bool\", typeName: \"\", id: 4, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=bool];
	}
	0	[comment="name: \"OpenSignPacket\", typeName: \"\", id: 0, branchId: 303, recurseId: -1, attributes: 0, notes: \"\"",
		label=OpenSignPacket];
	1	[comment="name: \"Pos\", typeName: \"NetworkBlockPosition\", id: 1, branchId: 0, recurseId: -1, attributes: 256, notes: \"\"",
		label=Pos];
	0 -> 1;
	3	[comment="name: \"Is Front Side\", typeName: \"\", id: 3, branchId: 0, recurseId: -1, attributes: 0, notes: \"\"",
		label="Is Front Side"];
	0 -> 3;
	1 -> 2;
	3 -> 4;
}

```

## 字段

/// define
OpenSignPacket

Pos：[<!-- md:samp NetworkBlockPosition -->](refs/protocols/types/NetworkBlockPosition.md)

- 类型：NetworkBlockPosition。

Is Front Side：<!-- md:samp bool -->

- 类型：bool。


///
