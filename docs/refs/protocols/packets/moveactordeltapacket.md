# <!-- md:samp MoveActorDeltaPacket -->

> 文档版本：r/20_u7<br/>协议版本：662

<!-- md:samp MoveActorDeltaPacket -->数据包，数字ID是`111`。

## 结构

```viz
digraph MoveActorDeltaPacket {
	graph [rankdir=LR];
	{
		graph [rank=max];
		19	[comment="name: \"MoveActorDeltaData\", typeName: \"\", id: 19, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=MoveActorDeltaData];
	}
	0	[comment="name: \"MoveActorDeltaPacket\", typeName: \"\", id: 0, branchId: 111, recurseId: -1, attributes: 0, notes: \"\"",
		label=MoveActorDeltaPacket];
	1	[comment="name: \"Move Data\", typeName: \"MoveActorDeltaData\", id: 1, branchId: 0, recurseId: -1, attributes: 256, notes: \"\"",
		label="Move Data"];
	0 -> 1;
	1 -> 19;
}

```

## 字段

/// define
MoveActorDeltaPacket

Move Data：[<!-- md:samp MoveActorDeltaData -->](../types/moveactordeltadata.md)

- 类型：MoveActorDeltaData。


///
