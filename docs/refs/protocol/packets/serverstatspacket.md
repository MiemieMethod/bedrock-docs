# <!-- md:samp ServerStatsPacket -->

> 文档版本：r/20_u7<br/>协议版本：662

<!-- md:samp ServerStatsPacket -->数据包，数字ID是`192`。

## 结构

```viz
digraph ServerStatsPacket {
	graph [rankdir=LR];
	{
		graph [rank=max];
		2	[comment="name: \"float\", typeName: \"\", id: 2, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=float];
		4	[comment="name: \"float\", typeName: \"\", id: 4, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=float];
	}
	0	[comment="name: \"ServerStatsPacket\", typeName: \"\", id: 0, branchId: 192, recurseId: -1, attributes: 0, notes: \"\"",
		label=ServerStatsPacket];
	1	[comment="name: \"ServerTime\", typeName: \"\", id: 1, branchId: 0, recurseId: -1, attributes: 0, notes: \"\"",
		label=ServerTime];
	0 -> 1;
	3	[comment="name: \"NetworkTime\", typeName: \"\", id: 3, branchId: 0, recurseId: -1, attributes: 0, notes: \"\"",
		label=NetworkTime];
	0 -> 3;
	1 -> 2;
	3 -> 4;
}

```

## 字段

/// define
ServerStatsPacket

ServerTime：<!-- md:samp float -->

- 类型：float。

NetworkTime：<!-- md:samp float -->

- 类型：float。


///
