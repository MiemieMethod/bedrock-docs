# <!-- md:samp FilterTextPacket -->

> 文档版本：r/20_u7<br/>协议版本：662

<!-- md:samp FilterTextPacket -->数据包，数字ID是`163`。

## 结构

```dot
digraph FilterTextPacket {
	graph [rankdir=LR];
	{
		graph [rank=max];
		2	[comment="name: \"string\", typeName: \"\", id: 2, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=string];
		4	[comment="name: \"bool\", typeName: \"\", id: 4, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=bool];
	}
	0	[comment="name: \"FilterTextPacket\", typeName: \"\", id: 0, branchId: 163, recurseId: -1, attributes: 0, notes: \"\"",
		label=FilterTextPacket];
	1	[comment="name: \"Text\", typeName: \"\", id: 1, branchId: 0, recurseId: -1, attributes: 0, notes: \"\"",
		label=Text];
	0 -> 1;
	3	[comment="name: \"From Server\", typeName: \"\", id: 3, branchId: 0, recurseId: -1, attributes: 0, notes: \"Whether this message is a filtered \
string from the server or a string in need of filtering from the client\"",
		label="From Server"];
	0 -> 3;
	1 -> 2;
	3 -> 4;
}

```

## 字段

/// define
FilterTextPacket

Text：<!-- md:samp string -->

- 类型：string。

From Server：<!-- md:samp bool -->

- 类型：bool。Whether this message is a filtered string from the server or a string in need of filtering from the client


///
