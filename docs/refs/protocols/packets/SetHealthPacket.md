# <!-- md:samp SetHealthPacket -->

> 文档版本：r/20_u7<br/>协议版本：662

<!-- md:samp SetHealthPacket -->数据包，数字ID是`42`。

## 结构

```dot
digraph SetHealthPacket {
	graph [rankdir=LR];
	{
		graph [rank=max];
		2	[comment="name: \"varint\", typeName: \"\", id: 2, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=varint];
	}
	0	[comment="name: \"SetHealthPacket\", typeName: \"\", id: 0, branchId: 42, recurseId: -1, attributes: 0, notes: \"\"",
		label=SetHealthPacket];
	1	[comment="name: \"Health\", typeName: \"\", id: 1, branchId: 0, recurseId: -1, attributes: 0, notes: \"\"",
		label=Health];
	0 -> 1;
	1 -> 2;
}

```

## 字段

/// define
SetHealthPacket

Health：<!-- md:samp varint -->

- 类型：varint。


///
