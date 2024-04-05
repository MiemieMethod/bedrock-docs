# <!-- md:samp PositionTrackingId -->

> 文档版本：r/20_u7<br/>协议版本：662

<!-- md:samp PositionTrackingId -->类型。

## 结构

```viz
digraph PositionTrackingId {
	graph [rankdir=LR];
	{
		graph [rank=max];
		6	[comment="name: \"varint\", typeName: \"\", id: 6, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=varint];
	}
	4	[comment="name: \"PositionTrackingId\", typeName: \"\", id: 4, branchId: 0, recurseId: -1, attributes: 0, notes: \"\"",
		label=PositionTrackingId];
	5	[comment="name: \"Value\", typeName: \"\", id: 5, branchId: 0, recurseId: -1, attributes: 0, notes: \"\"",
		label=Value];
	4 -> 5;
	5 -> 6;
}

```

## 字段

/// define
PositionTrackingId

Value：<!-- md:samp varint -->

- 类型：varint。


///
