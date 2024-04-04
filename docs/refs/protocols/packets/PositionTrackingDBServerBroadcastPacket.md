# <!-- md:samp PositionTrackingDBServerBroadcastPacket -->

> 文档版本：r/20_u7<br/>协议版本：662

<!-- md:samp PositionTrackingDBServerBroadcastPacket -->数据包，数字ID是`153`。

## 结构

```dot
digraph PositionTrackingDBServerBroadcastPacket {
	graph [rankdir=LR];
	{
		graph [rank=max];
		2	[comment="name: \"byte\", typeName: \"\", id: 2, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=byte];
		7	[comment="name: \"PositionTrackingId\", typeName: \"\", id: 7, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=PositionTrackingId];
		9	[comment="name: \"CompoundTag\", typeName: \"\", id: 9, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=CompoundTag];
	}
	0	[comment="name: \"PositionTrackingDBServerBroadcastPacket\", typeName: \"\", id: 0, branchId: 153, recurseId: -1, attributes: 0, notes: \"\"",
		label=PositionTrackingDBServerBroadcastPacket];
	1	[comment="name: \"Action\", typeName: \"\", id: 1, branchId: 0, recurseId: -1, attributes: 0, notes: \"enumeration: PositionTrackingDBServerBroadcastPacket::\
Action\"",
		label=Action];
	0 -> 1;
	3	[comment="name: \"Id\", typeName: \"PositionTrackingId\", id: 3, branchId: 0, recurseId: -1, attributes: 256, notes: \"\"",
		label=Id];
	0 -> 3;
	8	[comment="name: \"Position tracking data\", typeName: \"CompoundTag\", id: 8, branchId: 0, recurseId: -1, attributes: 256, notes: \"CompoundTag \
for record key:version (byte)id (string)positions (list of (int, int, int))dimension (int)status (byte, record status enum)\"",
		label="Position tracking data"];
	0 -> 8;
	1 -> 2;
	3 -> 7;
	8 -> 9;
}

```

## 字段

/// define
PositionTrackingDBServerBroadcastPacket

Action：<!-- md:samp byte -->

- 类型：byte。enumeration: PositionTrackingDBServerBroadcastPacket::Action

Id：[<!-- md:samp PositionTrackingId -->](refs/protocols/types/PositionTrackingId.md)

- 类型：PositionTrackingId。

Position tracking data：[<!-- md:samp CompoundTag -->](refs/protocols/types/CompoundTag.md)

- 类型：CompoundTag。CompoundTag for record key:version (byte)'id' (string)positions (list of (int, int, int))dimension (int)status (byte, record status enum)


///
