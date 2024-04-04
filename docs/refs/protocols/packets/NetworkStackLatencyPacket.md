# <!-- md:samp NetworkStackLatencyPacket -->

> 文档版本：r/20_u7<br/>协议版本：662

<!-- md:samp NetworkStackLatencyPacket -->数据包，数字ID是`115`。

## 结构

```dot
digraph NetworkStackLatencyPacket {
	graph [rankdir=LR];
	{
		graph [rank=max];
		2	[comment="name: \"unsigned int64\", typeName: \"\", id: 2, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label="unsigned int64"];
		4	[comment="name: \"bool\", typeName: \"\", id: 4, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=bool];
	}
	0	[comment="name: \"NetworkStackLatencyPacket\", typeName: \"\", id: 0, branchId: 115, recurseId: -1, attributes: 0, notes: \"\"",
		label=NetworkStackLatencyPacket];
	1	[comment="name: \"Creation Time\", typeName: \"\", id: 1, branchId: 0, recurseId: -1, attributes: 0, notes: \"\"",
		label="Creation Time"];
	0 -> 1;
	3	[comment="name: \"Is From Server\", typeName: \"\", id: 3, branchId: 0, recurseId: -1, attributes: 0, notes: \"\"",
		label="Is From Server"];
	0 -> 3;
	1 -> 2;
	3 -> 4;
}

```

## 字段

/// define
NetworkStackLatencyPacket

Creation Time：<!-- md:samp unsigned int64 -->

- 类型：unsigned int64。

Is From Server：<!-- md:samp bool -->

- 类型：bool。


///
