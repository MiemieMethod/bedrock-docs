# <!-- md:samp SetTitlePacket -->

> 文档版本：r/20_u7<br/>协议版本：662

<!-- md:samp SetTitlePacket -->数据包，数字ID是`88`。

## 结构

```dot
digraph SetTitlePacket {
	graph [rankdir=LR];
	{
		graph [rank=max];
		2	[comment="name: \"varint\", typeName: \"\", id: 2, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=varint];
		4	[comment="name: \"string\", typeName: \"\", id: 4, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=string];
		6	[comment="name: \"varint\", typeName: \"\", id: 6, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=varint];
		8	[comment="name: \"varint\", typeName: \"\", id: 8, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=varint];
		10	[comment="name: \"varint\", typeName: \"\", id: 10, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=varint];
		12	[comment="name: \"string\", typeName: \"\", id: 12, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=string];
		14	[comment="name: \"string\", typeName: \"\", id: 14, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=string];
	}
	0	[comment="name: \"SetTitlePacket\", typeName: \"\", id: 0, branchId: 88, recurseId: -1, attributes: 0, notes: \"\"",
		label=SetTitlePacket];
	1	[comment="name: \"Title Type\", typeName: \"\", id: 1, branchId: 0, recurseId: -1, attributes: 0, notes: \"enumeration: SetTitlePacket::TitleType\"",
		label="Title Type"];
	0 -> 1;
	3	[comment="name: \"Title Text\", typeName: \"\", id: 3, branchId: 0, recurseId: -1, attributes: 0, notes: \"\"",
		label="Title Text"];
	0 -> 3;
	5	[comment="name: \"Fade In Time\", typeName: \"\", id: 5, branchId: 0, recurseId: -1, attributes: 0, notes: \"\"",
		label="Fade In Time"];
	0 -> 5;
	7	[comment="name: \"Stay Time\", typeName: \"\", id: 7, branchId: 0, recurseId: -1, attributes: 0, notes: \"\"",
		label="Stay Time"];
	0 -> 7;
	9	[comment="name: \"Fade Out Time\", typeName: \"\", id: 9, branchId: 0, recurseId: -1, attributes: 0, notes: \"\"",
		label="Fade Out Time"];
	0 -> 9;
	11	[comment="name: \"Xuid\", typeName: \"\", id: 11, branchId: 0, recurseId: -1, attributes: 0, notes: \"\"",
		label=Xuid];
	0 -> 11;
	13	[comment="name: \"Platform Online Id\", typeName: \"\", id: 13, branchId: 0, recurseId: -1, attributes: 0, notes: \"\"",
		label="Platform Online Id"];
	0 -> 13;
	1 -> 2;
	3 -> 4;
	5 -> 6;
	7 -> 8;
	9 -> 10;
	11 -> 12;
	13 -> 14;
}

```

## 字段

/// define
SetTitlePacket

Title Type：<!-- md:samp varint -->

- 类型：varint。enumeration: SetTitlePacket::TitleType

Title Text：<!-- md:samp string -->

- 类型：string。

Fade In Time：<!-- md:samp varint -->

- 类型：varint。

Stay Time：<!-- md:samp varint -->

- 类型：varint。

Fade Out Time：<!-- md:samp varint -->

- 类型：varint。

Xuid：<!-- md:samp string -->

- 类型：string。

Platform Online Id：<!-- md:samp string -->

- 类型：string。


///
