# <!-- md:samp StructureEditorData -->

> 文档版本：r/20_u7<br/>协议版本：662

<!-- md:samp StructureEditorData -->类型。

## 结构

```viz
digraph StructureEditorData {
	graph [rankdir=LR];
	{
		graph [rank=max];
		6	[comment="name: \"string\", typeName: \"\", id: 6, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=string];
		8	[comment="name: \"string\", typeName: \"\", id: 8, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=string];
		10	[comment="name: \"bool\", typeName: \"\", id: 10, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=bool];
		12	[comment="name: \"bool\", typeName: \"\", id: 12, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=bool];
		14	[comment="name: \"varint\", typeName: \"\", id: 14, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=varint];
		45	[comment="name: \"StructureSettings\", typeName: \"\", id: 45, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=StructureSettings];
		47	[comment="name: \"varint\", typeName: \"\", id: 47, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=varint];
	}
	4	[comment="name: \"StructureEditorData\", typeName: \"\", id: 4, branchId: 0, recurseId: -1, attributes: 0, notes: \"\"",
		label=StructureEditorData];
	5	[comment="name: \"Structure Name\", typeName: \"\", id: 5, branchId: 0, recurseId: -1, attributes: 0, notes: \"\"",
		label="Structure Name"];
	4 -> 5;
	7	[comment="name: \"Data Field\", typeName: \"\", id: 7, branchId: 0, recurseId: -1, attributes: 0, notes: \"Used for structure blocks in data mode.\"",
		label="Data Field"];
	4 -> 7;
	9	[comment="name: \"Should players be included?\", typeName: \"\", id: 9, branchId: 0, recurseId: -1, attributes: 0, notes: \"\"",
		label="Should players be included?"];
	4 -> 9;
	11	[comment="name: \"Should show bounding box?\", typeName: \"\", id: 11, branchId: 0, recurseId: -1, attributes: 0, notes: \"\"",
		label="Should show bounding box?"];
	4 -> 11;
	13	[comment="name: \"Structure Block Type\", typeName: \"\", id: 13, branchId: 0, recurseId: -1, attributes: 0, notes: \"enumeration: StructureBlockType\"",
		label="Structure Block Type"];
	4 -> 13;
	15	[comment="name: \"Structure Settings\", typeName: \"StructureSettings\", id: 15, branchId: 0, recurseId: -1, attributes: 256, notes: \"\"",
		label="Structure Settings"];
	4 -> 15;
	46	[comment="name: \"Redstone Save Mode\", typeName: \"\", id: 46, branchId: 0, recurseId: -1, attributes: 0, notes: \"enumeration: StructureRedstoneSaveMode\"",
		label="Redstone Save Mode"];
	4 -> 46;
	5 -> 6;
	7 -> 8;
	9 -> 10;
	11 -> 12;
	13 -> 14;
	15 -> 45;
	46 -> 47;
}

```

## 字段

/// define
StructureEditorData

Structure Name：<!-- md:samp string -->

- 类型：string。

Data Field：<!-- md:samp string -->

- 类型：string。Used for structure blocks in data mode.

Should players be included?：<!-- md:samp bool -->

- 类型：bool。

Should show bounding box?：<!-- md:samp bool -->

- 类型：bool。

Structure Block Type：<!-- md:samp varint -->

- 类型：varint。enumeration: StructureBlockType

Structure Settings：[<!-- md:samp StructureSettings -->](../types/structuresettings.md)

- 类型：StructureSettings。

Redstone Save Mode：<!-- md:samp varint -->

- 类型：varint。enumeration: StructureRedstoneSaveMode


///
