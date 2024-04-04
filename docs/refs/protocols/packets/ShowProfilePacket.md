# <!-- md:samp ShowProfilePacket -->

> 文档版本：r/20_u7<br/>协议版本：662

<!-- md:samp ShowProfilePacket -->数据包，数字ID是`104`。

## 结构

```dot
digraph ShowProfilePacket {
	graph [rankdir=LR];
	{
		graph [rank=max];
		2	[comment="name: \"string\", typeName: \"\", id: 2, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=string];
	}
	0	[comment="name: \"ShowProfilePacket\", typeName: \"\", id: 0, branchId: 104, recurseId: -1, attributes: 0, notes: \"\"",
		label=ShowProfilePacket];
	1	[comment="name: \"Player XUID\", typeName: \"\", id: 1, branchId: 0, recurseId: -1, attributes: 0, notes: \"\"",
		label="Player XUID"];
	0 -> 1;
	1 -> 2;
}

```

## 字段

/// define
ShowProfilePacket

Player XUID：<!-- md:samp string -->

- 类型：string。


///
