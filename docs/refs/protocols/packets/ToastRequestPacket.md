# <!-- md:samp ToastRequestPacket -->

> 文档版本：r/20_u7<br/>协议版本：662

<!-- md:samp ToastRequestPacket -->数据包，数字ID是`186`。

## 结构

```dot
digraph ToastRequestPacket {
	graph [rankdir=LR];
	{
		graph [rank=max];
		2	[comment="name: \"string\", typeName: \"\", id: 2, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=string];
		4	[comment="name: \"string\", typeName: \"\", id: 4, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=string];
	}
	0	[comment="name: \"ToastRequestPacket\", typeName: \"\", id: 0, branchId: 186, recurseId: -1, attributes: 0, notes: \"\"",
		label=ToastRequestPacket];
	1	[comment="name: \"Title\", typeName: \"\", id: 1, branchId: 0, recurseId: -1, attributes: 0, notes: \"\"",
		label=Title];
	0 -> 1;
	3	[comment="name: \"Content\", typeName: \"\", id: 3, branchId: 0, recurseId: -1, attributes: 0, notes: \"\"",
		label=Content];
	0 -> 3;
	1 -> 2;
	3 -> 4;
}

```

## 字段

/// define
ToastRequestPacket

Title：<!-- md:samp string -->

- 类型：string。

Content：<!-- md:samp string -->

- 类型：string。


///
