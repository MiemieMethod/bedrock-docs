# <!-- md:samp CodeBuilderPacket -->

> 文档版本：r/20_u7<br/>协议版本：662

<!-- md:samp CodeBuilderPacket -->数据包，数字ID是`150`。

## 结构

```viz
digraph CodeBuilderPacket {
	graph [rankdir=LR];
	{
		graph [rank=max];
		2	[comment="name: \"string\", typeName: \"\", id: 2, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=string];
		4	[comment="name: \"bool\", typeName: \"\", id: 4, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=bool];
	}
	0	[comment="name: \"CodeBuilderPacket\", typeName: \"\", id: 0, branchId: 150, recurseId: -1, attributes: 0, notes: \"\"",
		label=CodeBuilderPacket];
	1	[comment="name: \"URL\", typeName: \"\", id: 1, branchId: 0, recurseId: -1, attributes: 0, notes: \"\"",
		label=URL];
	0 -> 1;
	3	[comment="name: \"Should open code builder\", typeName: \"\", id: 3, branchId: 0, recurseId: -1, attributes: 0, notes: \"\"",
		label="Should open code builder"];
	0 -> 3;
	1 -> 2;
	3 -> 4;
}

```

## 字段

/// define
CodeBuilderPacket

URL：<!-- md:samp string -->

- 类型：string。

Should open code builder：<!-- md:samp bool -->

- 类型：bool。


///
