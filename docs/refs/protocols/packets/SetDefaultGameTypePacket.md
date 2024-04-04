# <!-- md:samp SetDefaultGameTypePacket -->

> 文档版本：r/20_u7<br/>协议版本：662

<!-- md:samp SetDefaultGameTypePacket -->数据包，数字ID是`105`。

## 结构

```dot
digraph SetDefaultGameTypePacket {
	graph [rankdir=LR];
	{
		graph [rank=max];
		2	[comment="name: \"varint\", typeName: \"\", id: 2, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=varint];
	}
	0	[comment="name: \"SetDefaultGameTypePacket\", typeName: \"\", id: 0, branchId: 105, recurseId: -1, attributes: 0, notes: \"\"",
		label=SetDefaultGameTypePacket];
	1	[comment="name: \"Default Game Type\", typeName: \"\", id: 1, branchId: 0, recurseId: -1, attributes: 0, notes: \"enumeration: GameType\"",
		label="Default Game Type"];
	0 -> 1;
	1 -> 2;
}

```

## 字段

/// define
SetDefaultGameTypePacket

Default Game Type：<!-- md:samp varint -->

- 类型：varint。enumeration: GameType


///
