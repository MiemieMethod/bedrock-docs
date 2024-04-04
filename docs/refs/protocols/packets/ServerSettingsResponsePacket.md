# <!-- md:samp ServerSettingsResponsePacket -->

> 文档版本：r/20_u7<br/>协议版本：662

<!-- md:samp ServerSettingsResponsePacket -->数据包，数字ID是`103`。

## 结构

```dot
digraph ServerSettingsResponsePacket {
	graph [rankdir=LR];
	{
		graph [rank=max];
		2	[comment="name: \"unsigned varint\", typeName: \"\", id: 2, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label="unsigned varint"];
		4	[comment="name: \"string\", typeName: \"\", id: 4, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=string];
	}
	0	[comment="name: \"ServerSettingsResponsePacket\", typeName: \"\", id: 0, branchId: 103, recurseId: -1, attributes: 0, notes: \"\"",
		label=ServerSettingsResponsePacket];
	1	[comment="name: \"Form ID\", typeName: \"\", id: 1, branchId: 0, recurseId: -1, attributes: 0, notes: \"\"",
		label="Form ID"];
	0 -> 1;
	3	[comment="name: \"Form UI JSON\", typeName: \"\", id: 3, branchId: 0, recurseId: -1, attributes: 0, notes: \"\"",
		label="Form UI JSON"];
	0 -> 3;
	1 -> 2;
	3 -> 4;
}

```

## 字段

/// define
ServerSettingsResponsePacket

Form ID：<!-- md:samp unsigned varint -->

- 类型：unsigned varint。

Form UI JSON：<!-- md:samp string -->

- 类型：string。


///
