# <!-- md:samp PlayStatusPacket -->

> 文档版本：r/20_u7<br/>协议版本：662

<!-- md:samp PlayStatusPacket -->数据包，数字ID是`2`。

## 结构

```dot
digraph PlayStatusPacket {
	graph [rankdir=LR];
	{
		graph [rank=max];
		2	[comment="name: \"big endian int\", typeName: \"\", id: 2, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label="big endian int"];
	}
	0	[comment="name: \"PlayStatusPacket\", typeName: \"\", id: 0, branchId: 2, recurseId: -1, attributes: 0, notes: \"\"",
		label=PlayStatusPacket];
	1	[comment="name: \"Status\", typeName: \"\", id: 1, branchId: 0, recurseId: -1, attributes: 0, notes: \"enumeration: PlayStatus\"",
		label=Status];
	0 -> 1;
	1 -> 2;
}

```

## 字段

/// define
PlayStatusPacket

Status：<!-- md:samp big endian int -->

- 类型：big endian int。enumeration: PlayStatus


///
