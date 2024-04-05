# <!-- md:samp MoveActorAbsolutePacket -->

> 文档版本：r/20_u7<br/>协议版本：662

<!-- md:samp MoveActorAbsolutePacket -->数据包，数字ID是`18`。

## 结构

```viz
digraph MoveActorAbsolutePacket {
	graph [rankdir=LR];
	{
		graph [rank=max];
		15	[comment="name: \"MoveActorAbsoluteData\", typeName: \"\", id: 15, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=MoveActorAbsoluteData];
	}
	0	[comment="name: \"MoveActorAbsolutePacket\", typeName: \"\", id: 0, branchId: 18, recurseId: -1, attributes: 0, notes: \"\"",
		label=MoveActorAbsolutePacket];
	1	[comment="name: \"Move Data\", typeName: \"MoveActorAbsoluteData\", id: 1, branchId: 0, recurseId: -1, attributes: 256, notes: \"\"",
		label="Move Data"];
	0 -> 1;
	1 -> 15;
}

```

## 字段

/// define
MoveActorAbsolutePacket

Move Data：[<!-- md:samp MoveActorAbsoluteData -->](refs/protocols/types/moveactorabsolutedata.md)

- 类型：MoveActorAbsoluteData。


///
