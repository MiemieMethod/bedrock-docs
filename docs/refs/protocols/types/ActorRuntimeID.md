# <!-- md:samp ActorRuntimeID -->

> 文档版本：r/20_u7<br/>协议版本：662

<!-- md:samp ActorRuntimeID -->类型。

## 结构

```dot
digraph ActorRuntimeID {
	graph [rankdir=LR];
	{
		graph [rank=max];
		9	[comment="name: \"unsigned varint64\", typeName: \"\", id: 9, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label="unsigned varint64"];
	}
	7	[comment="name: \"ActorRuntimeID\", typeName: \"\", id: 7, branchId: 0, recurseId: -1, attributes: 0, notes: \"\"",
		label=ActorRuntimeID];
	8	[comment="name: \"Actor Runtime ID\", typeName: \"\", id: 8, branchId: 0, recurseId: -1, attributes: 0, notes: \"\"",
		label="Actor Runtime ID"];
	7 -> 8;
	8 -> 9;
}

```

## 字段

/// define
ActorRuntimeID

Actor Runtime ID：<!-- md:samp unsigned varint64 -->

- 类型：unsigned varint64。


///
