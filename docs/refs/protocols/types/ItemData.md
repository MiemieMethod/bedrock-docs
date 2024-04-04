# <!-- md:samp ItemData -->

> 文档版本：r/20_u7<br/>协议版本：662

<!-- md:samp ItemData -->类型。

## 结构

```dot
digraph ItemData {
	graph [rankdir=LR];
	{
		graph [rank=max];
		174	[comment="name: \"string\", typeName: \"\", id: 174, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=string];
		176	[comment="name: \"short\", typeName: \"\", id: 176, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=short];
		178	[comment="name: \"bool\", typeName: \"\", id: 178, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=bool];
	}
	172	[comment="name: \"ItemData\", typeName: \"\", id: 172, branchId: 0, recurseId: -1, attributes: 0, notes: \"\"",
		label=ItemData];
	173	[comment="name: \"Item Name\", typeName: \"\", id: 173, branchId: 0, recurseId: -1, attributes: 0, notes: \"\"",
		label="Item Name"];
	172 -> 173;
	175	[comment="name: \"Item Id\", typeName: \"\", id: 175, branchId: 0, recurseId: -1, attributes: 0, notes: \"Block id's < 256 (can be negative); Item \
id's > 257\"",
		label="Item Id"];
	172 -> 175;
	177	[comment="name: \"Is Component Based\", typeName: \"\", id: 177, branchId: 0, recurseId: -1, attributes: 0, notes: \"\"",
		label="Is Component Based"];
	172 -> 177;
	173 -> 174;
	175 -> 176;
	177 -> 178;
}

```

## 字段

/// define
ItemData

Item Name：<!-- md:samp string -->

- 类型：string。

Item Id：<!-- md:samp short -->

- 类型：short。Block 'id''s < 256 (can be negative); Item 'id''s > 257

Is Component Based：<!-- md:samp bool -->

- 类型：bool。


///
