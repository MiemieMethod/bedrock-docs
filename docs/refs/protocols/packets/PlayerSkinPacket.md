# <!-- md:samp PlayerSkinPacket -->

> 文档版本：r/20_u7<br/>协议版本：662

<!-- md:samp PlayerSkinPacket -->数据包，数字ID是`93`。

## 结构

```dot
digraph PlayerSkinPacket {
	graph [rankdir=LR];
	{
		graph [rank=max];
		2	[comment="name: \"mce::UUID\", typeName: \"\", id: 2, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label="mce::UUID"];
		4	[comment="name: \"SerializedSkin\", typeName: \"\", id: 4, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=SerializedSkin];
		6	[comment="name: \"string\", typeName: \"\", id: 6, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=string];
		8	[comment="name: \"string\", typeName: \"\", id: 8, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=string];
		10	[comment="name: \"bool\", typeName: \"\", id: 10, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=bool];
	}
	0	[comment="name: \"PlayerSkinPacket\", typeName: \"\", id: 0, branchId: 93, recurseId: -1, attributes: 0, notes: \"\"",
		label=PlayerSkinPacket];
	1	[comment="name: \"UUID\", typeName: \"mce::UUID\", id: 1, branchId: 0, recurseId: -1, attributes: 256, notes: \"\"",
		label=UUID];
	0 -> 1;
	3	[comment="name: \"Serialized Skin\", typeName: \"SerializedSkin\", id: 3, branchId: 0, recurseId: -1, attributes: 256, notes: \"\"",
		label="Serialized Skin"];
	0 -> 3;
	5	[comment="name: \"New Skin Name\", typeName: \"\", id: 5, branchId: 0, recurseId: -1, attributes: 0, notes: \"\"",
		label="New Skin Name"];
	0 -> 5;
	7	[comment="name: \"Old Skin Name\", typeName: \"\", id: 7, branchId: 0, recurseId: -1, attributes: 0, notes: \"\"",
		label="Old Skin Name"];
	0 -> 7;
	9	[comment="name: \"Whether skin is trusted marketplace content\", typeName: \"\", id: 9, branchId: 0, recurseId: -1, attributes: 0, notes: \"\"",
		label="Whether skin is trusted marketplace content"];
	0 -> 9;
	1 -> 2;
	3 -> 4;
	5 -> 6;
	7 -> 8;
	9 -> 10;
}

```

## 字段

/// define
PlayerSkinPacket

UUID：[<!-- md:samp mce::UUID -->](refs/protocols/types/mce::UUID.md)

- 类型：mce::UUID。

Serialized Skin：[<!-- md:samp SerializedSkin -->](refs/protocols/types/SerializedSkin.md)

- 类型：SerializedSkin。

New Skin Name：<!-- md:samp string -->

- 类型：string。

Old Skin Name：<!-- md:samp string -->

- 类型：string。

Whether skin is trusted marketplace content：<!-- md:samp bool -->

- 类型：bool。


///
