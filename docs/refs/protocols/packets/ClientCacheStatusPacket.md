# <!-- md:samp ClientCacheStatusPacket -->

> 文档版本：r/20_u7<br/>协议版本：662

<!-- md:samp ClientCacheStatusPacket -->数据包，数字ID是`129`。

## 结构

```viz
digraph ClientCacheStatusPacket {
	graph [rankdir=LR];
	{
		graph [rank=max];
		2	[comment="name: \"bool\", typeName: \"\", id: 2, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=bool];
	}
	0	[comment="name: \"ClientCacheStatusPacket\", typeName: \"\", id: 0, branchId: 129, recurseId: -1, attributes: 0, notes: \"\"",
		label=ClientCacheStatusPacket];
	1	[comment="name: \"Is cache supported?\", typeName: \"\", id: 1, branchId: 0, recurseId: -1, attributes: 0, notes: \"\"",
		label="Is cache supported?"];
	0 -> 1;
	1 -> 2;
}

```

## 字段

/// define
ClientCacheStatusPacket

Is cache supported?：<!-- md:samp bool -->

- 类型：bool。


///
