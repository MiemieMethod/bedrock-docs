# <!-- md:samp SetTimePacket -->

> 文档版本：r/20_u7<br/>协议版本：662

<!-- md:samp SetTimePacket -->数据包，数字ID是`10`。

## 结构

```dot
digraph SetTimePacket {
	graph [rankdir=LR];
	{
		graph [rank=max];
		2	[comment="name: \"varint\", typeName: \"\", id: 2, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=varint];
	}
	0	[comment="name: \"SetTimePacket\", typeName: \"\", id: 0, branchId: 10, recurseId: -1, attributes: 0, notes: \"\"",
		label=SetTimePacket];
	1	[comment="name: \"Time\", typeName: \"\", id: 1, branchId: 0, recurseId: -1, attributes: 0, notes: \"\"",
		label=Time];
	0 -> 1;
	1 -> 2;
}

```

## 字段

/// define
SetTimePacket

Time：<!-- md:samp varint -->

- 类型：varint。


///
