# <!-- md:samp ResourcePackStackPacket -->

> 文档版本：r/20_u7<br/>协议版本：662

<!-- md:samp ResourcePackStackPacket -->数据包，数字ID是`7`。

## 结构

```dot
digraph ResourcePackStackPacket {
	graph [rankdir=LR];
	{
		graph [rank=max];
		2	[comment="name: \"bool\", typeName: \"\", id: 2, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=bool];
		5	[comment="name: \"unsigned varint\", typeName: \"\", id: 5, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label="unsigned varint"];
		8	[comment="name: \"string\", typeName: \"\", id: 8, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=string];
		10	[comment="name: \"string\", typeName: \"\", id: 10, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=string];
		12	[comment="name: \"string\", typeName: \"\", id: 12, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=string];
		15	[comment="name: \"unsigned varint\", typeName: \"\", id: 15, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label="unsigned varint"];
		18	[comment="name: \"string\", typeName: \"\", id: 18, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=string];
		20	[comment="name: \"string\", typeName: \"\", id: 20, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=string];
		22	[comment="name: \"string\", typeName: \"\", id: 22, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=string];
		27	[comment="name: \"BaseGameVersion\", typeName: \"\", id: 27, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=BaseGameVersion];
		44	[comment="name: \"Experiments\", typeName: \"\", id: 44, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=Experiments];
	}
	0	[comment="name: \"ResourcePackStackPacket\", typeName: \"\", id: 0, branchId: 7, recurseId: -1, attributes: 0, notes: \"\"",
		label=ResourcePackStackPacket];
	1	[comment="name: \"Texture Pack Required\", typeName: \"\", id: 1, branchId: 0, recurseId: -1, attributes: 0, notes: \"\"",
		label="Texture Pack Required"];
	0 -> 1;
	3	[comment="name: \"Add-On List\", typeName: \"\", id: 3, branchId: 0, recurseId: -1, attributes: 8, notes: \"\"",
		label="Add-On List"];
	0 -> 3;
	13	[comment="name: \"Texture Pack List\", typeName: \"\", id: 13, branchId: 0, recurseId: -1, attributes: 8, notes: \"\"",
		label="Texture Pack List"];
	0 -> 13;
	23	[comment="name: \"Base Game Version\", typeName: \"BaseGameVersion\", id: 23, branchId: 0, recurseId: -1, attributes: 256, notes: \"For clients \
to be able to set their stack to the right version.\"",
		label="Base Game Version"];
	0 -> 23;
	28	[comment="name: \"Experiments\", typeName: \"Experiments\", id: 28, branchId: 0, recurseId: -1, attributes: 256, notes: \"Refer to the Experiments \
type for how to serialize\"",
		label=Experiments];
	0 -> 28;
	1 -> 2;
	4	[comment="name: \"Array Size\", typeName: \"\", id: 4, branchId: 0, recurseId: -1, attributes: 0, notes: \"\"",
		label="Array Size"];
	3 -> 4;
	6	[comment="name: \"example element\", typeName: \"\", id: 6, branchId: 0, recurseId: -1, attributes: 16, notes: \"\"",
		label="example element",
		style=dotted];
	3 -> 6;
	4 -> 5;
	7	[comment="name: \"ID\", typeName: \"\", id: 7, branchId: 0, recurseId: -1, attributes: 0, notes: \"\"",
		label=ID];
	6 -> 7;
	9	[comment="name: \"Version\", typeName: \"\", id: 9, branchId: 0, recurseId: -1, attributes: 0, notes: \"\"",
		label=Version];
	6 -> 9;
	11	[comment="name: \"Sub Pack Name\", typeName: \"\", id: 11, branchId: 0, recurseId: -1, attributes: 0, notes: \"\"",
		label="Sub Pack Name"];
	6 -> 11;
	7 -> 8;
	9 -> 10;
	11 -> 12;
	14	[comment="name: \"Array Size\", typeName: \"\", id: 14, branchId: 0, recurseId: -1, attributes: 0, notes: \"\"",
		label="Array Size"];
	13 -> 14;
	16	[comment="name: \"example element\", typeName: \"\", id: 16, branchId: 0, recurseId: -1, attributes: 16, notes: \"\"",
		label="example element",
		style=dotted];
	13 -> 16;
	14 -> 15;
	17	[comment="name: \"ID\", typeName: \"\", id: 17, branchId: 0, recurseId: -1, attributes: 0, notes: \"\"",
		label=ID];
	16 -> 17;
	19	[comment="name: \"Version\", typeName: \"\", id: 19, branchId: 0, recurseId: -1, attributes: 0, notes: \"\"",
		label=Version];
	16 -> 19;
	21	[comment="name: \"Sub Pack Name\", typeName: \"\", id: 21, branchId: 0, recurseId: -1, attributes: 0, notes: \"\"",
		label="Sub Pack Name"];
	16 -> 21;
	17 -> 18;
	19 -> 20;
	21 -> 22;
	23 -> 27;
	28 -> 44;
}

```

## 字段

/// define
ResourcePackStackPacket

Texture Pack Required：<!-- md:samp bool -->

- 类型：bool。

Add-On List

Add-On List数组的大小：<!-- md:samp unsigned varint -->

- 类型：unsigned varint。

Add-On List的示例元素

ID：<!-- md:samp string -->

- 类型：string。

Version：<!-- md:samp string -->

- 类型：string。

Sub Pack Name：<!-- md:samp string -->

- 类型：string。

Texture Pack List

Texture Pack List数组的大小：<!-- md:samp unsigned varint -->

- 类型：unsigned varint。

Texture Pack List的示例元素

Base Game Version：[<!-- md:samp BaseGameVersion -->](refs/protocols/types/BaseGameVersion.md)

- 类型：BaseGameVersion。For clients to be able to set their stack to the right version.

Experiments：[<!-- md:samp Experiments -->](refs/protocols/types/Experiments.md)

- 类型：Experiments。Refer to the Experiments type for how to serialize


///
