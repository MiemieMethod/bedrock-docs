# <!-- md:samp BlockEventPacket -->

> 文档版本：r/20_u7<br/>协议版本：662

<!-- md:samp BlockEventPacket -->数据包，数字ID是`26`。

## 结构

```viz
digraph BlockEventPacket {
	graph [rankdir=LR];
	{
		graph [rank=max];
		2	[comment="name: \"NetworkBlockPosition\", typeName: \"\", id: 2, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=NetworkBlockPosition];
		4	[comment="name: \"varint\", typeName: \"\", id: 4, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=varint];
		6	[comment="name: \"varint\", typeName: \"\", id: 6, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=varint];
	}
	0	[comment="name: \"BlockEventPacket\", typeName: \"\", id: 0, branchId: 26, recurseId: -1, attributes: 0, notes: \"\"",
		label=BlockEventPacket];
	1	[comment="name: \"Block Position\", typeName: \"NetworkBlockPosition\", id: 1, branchId: 0, recurseId: -1, attributes: 256, notes: \"\"",
		label="Block Position"];
	0 -> 1;
	3	[comment="name: \"Event Type\", typeName: \"\", id: 3, branchId: 0, recurseId: -1, attributes: 0, notes: \"\"",
		label="Event Type"];
	0 -> 3;
	5	[comment="name: \"Event Value\", typeName: \"\", id: 5, branchId: 0, recurseId: -1, attributes: 0, notes: \"\"",
		label="Event Value"];
	0 -> 5;
	1 -> 2;
	3 -> 4;
	5 -> 6;
}

```

## 字段

/// define
BlockEventPacket

Block Position：[<!-- md:samp NetworkBlockPosition -->](refs/protocols/types/NetworkBlockPosition.md)

- 类型：NetworkBlockPosition。

Event Type：<!-- md:samp varint -->

- 类型：varint。

Event Value：<!-- md:samp varint -->

- 类型：varint。


///
