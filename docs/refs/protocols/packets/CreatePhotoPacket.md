# <!-- md:samp CreatePhotoPacket -->

> 文档版本：r/20_u7<br/>协议版本：662

<!-- md:samp CreatePhotoPacket -->数据包，数字ID是`171`。

## 结构

```dot
digraph CreatePhotoPacket {
	graph [rankdir=LR];
	{
		graph [rank=max];
		2	[comment="name: \"unsigned int64\", typeName: \"\", id: 2, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label="unsigned int64"];
		4	[comment="name: \"string\", typeName: \"\", id: 4, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=string];
		6	[comment="name: \"string\", typeName: \"\", id: 6, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=string];
	}
	0	[comment="name: \"CreatePhotoPacket\", typeName: \"\", id: 0, branchId: 171, recurseId: -1, attributes: 0, notes: \"\"",
		label=CreatePhotoPacket];
	1	[comment="name: \"Raw ID\", typeName: \"\", id: 1, branchId: 0, recurseId: -1, attributes: 0, notes: \"\"",
		label="Raw ID"];
	0 -> 1;
	3	[comment="name: \"Photo Name\", typeName: \"\", id: 3, branchId: 0, recurseId: -1, attributes: 0, notes: \"\"",
		label="Photo Name"];
	0 -> 3;
	5	[comment="name: \"Photo Item Name\", typeName: \"\", id: 5, branchId: 0, recurseId: -1, attributes: 0, notes: \"\"",
		label="Photo Item Name"];
	0 -> 5;
	1 -> 2;
	3 -> 4;
	5 -> 6;
}

```

## 字段

/// define
CreatePhotoPacket

Raw ID：<!-- md:samp unsigned int64 -->

- 类型：unsigned int64。

Photo Name：<!-- md:samp string -->

- 类型：string。

Photo Item Name：<!-- md:samp string -->

- 类型：string。


///
