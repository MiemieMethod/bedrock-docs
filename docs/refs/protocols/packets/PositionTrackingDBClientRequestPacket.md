# <!-- md:samp PositionTrackingDBClientRequestPacket -->

> 文档版本：r/20_u7<br/>协议版本：662

<!-- md:samp PositionTrackingDBClientRequestPacket -->数据包，数字ID是`154`。

## 结构

```dot
digraph PositionTrackingDBClientRequestPacket {
	graph [rankdir=LR];
	{
		graph [rank=max];
		2	[comment="name: \"byte\", typeName: \"\", id: 2, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=byte];
		4	[comment="name: \"PositionTrackingId\", typeName: \"\", id: 4, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=PositionTrackingId];
	}
	0	[comment="name: \"PositionTrackingDBClientRequestPacket\", typeName: \"\", id: 0, branchId: 154, recurseId: -1, attributes: 0, notes: \"\"",
		label=PositionTrackingDBClientRequestPacket];
	1	[comment="name: \"Action\", typeName: \"\", id: 1, branchId: 0, recurseId: -1, attributes: 0, notes: \"enumeration: PositionTrackingDBClientRequestPacket::\
Action\"",
		label=Action];
	0 -> 1;
	3	[comment="name: \"Id\", typeName: \"PositionTrackingId\", id: 3, branchId: 0, recurseId: -1, attributes: 256, notes: \"\"",
		label=Id];
	0 -> 3;
	1 -> 2;
	3 -> 4;
}

```

## 字段

/// define
PositionTrackingDBClientRequestPacket

Action：<!-- md:samp byte -->

- 类型：byte。enumeration: PositionTrackingDBClientRequestPacket::Action

Id：[<!-- md:samp PositionTrackingId -->](refs/protocols/types/PositionTrackingId.md)

- 类型：PositionTrackingId。


///
