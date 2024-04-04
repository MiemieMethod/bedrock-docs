# <!-- md:samp TickSyncPacket -->

> 文档版本：r/20_u7<br/>协议版本：662

<!-- md:samp TickSyncPacket -->数据包，数字ID是`23`。

## 结构

```dot
digraph TickSyncPacket {
	graph [rankdir=LR];
	{
		graph [rank=max];
		2	[comment="name: \"int64\", typeName: \"\", id: 2, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=int64];
		4	[comment="name: \"int64\", typeName: \"\", id: 4, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=int64];
	}
	0	[comment="name: \"TickSyncPacket\", typeName: \"\", id: 0, branchId: 23, recurseId: -1, attributes: 0, notes: \"\"",
		label=TickSyncPacket];
	1	[comment="name: \"Client Request Timestamp\", typeName: \"\", id: 1, branchId: 0, recurseId: -1, attributes: 0, notes: \"\"",
		label="Client Request Timestamp"];
	0 -> 1;
	3	[comment="name: \"Server Reception Response Timestamp\", typeName: \"\", id: 3, branchId: 0, recurseId: -1, attributes: 0, notes: \"\"",
		label="Server Reception Response Timestamp"];
	0 -> 3;
	1 -> 2;
	3 -> 4;
}

```

## 字段

/// define
TickSyncPacket

Client Request Timestamp：<!-- md:samp int64 -->

- 类型：int64。

Server Reception Response Timestamp：<!-- md:samp int64 -->

- 类型：int64。


///
