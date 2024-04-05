# <!-- md:samp StructureBlockUpdatePacket -->

> 文档版本：r/20_u7<br/>协议版本：662

<!-- md:samp StructureBlockUpdatePacket -->数据包，数字ID是`90`。

## 结构

```viz
digraph StructureBlockUpdatePacket {
	graph [rankdir=LR];
	{
		graph [rank=max];
		2	[comment="name: \"NetworkBlockPosition\", typeName: \"\", id: 2, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=NetworkBlockPosition];
		48	[comment="name: \"StructureEditorData\", typeName: \"\", id: 48, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=StructureEditorData];
		50	[comment="name: \"bool\", typeName: \"\", id: 50, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=bool];
		52	[comment="name: \"bool\", typeName: \"\", id: 52, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=bool];
	}
	0	[comment="name: \"StructureBlockUpdatePacket\", typeName: \"\", id: 0, branchId: 90, recurseId: -1, attributes: 0, notes: \"\"",
		label=StructureBlockUpdatePacket];
	1	[comment="name: \"Block Position\", typeName: \"NetworkBlockPosition\", id: 1, branchId: 0, recurseId: -1, attributes: 256, notes: \"\"",
		label="Block Position"];
	0 -> 1;
	3	[comment="name: \"Structure Data\", typeName: \"StructureEditorData\", id: 3, branchId: 0, recurseId: -1, attributes: 256, notes: \"\"",
		label="Structure Data"];
	0 -> 3;
	49	[comment="name: \"Trigger?\", typeName: \"\", id: 49, branchId: 0, recurseId: -1, attributes: 0, notes: \"\"",
		label="Trigger?"];
	0 -> 49;
	51	[comment="name: \"IsWaterlogged\", typeName: \"\", id: 51, branchId: 0, recurseId: -1, attributes: 0, notes: \"\"",
		label=IsWaterlogged];
	0 -> 51;
	1 -> 2;
	3 -> 48;
	49 -> 50;
	51 -> 52;
}

```

## 字段

/// define
StructureBlockUpdatePacket

Block Position：[<!-- md:samp NetworkBlockPosition -->](refs/protocols/types/networkblockposition.md)

- 类型：NetworkBlockPosition。

Structure Data：[<!-- md:samp StructureEditorData -->](refs/protocols/types/structureeditordata.md)

- 类型：StructureEditorData。

Trigger?：<!-- md:samp bool -->

- 类型：bool。

IsWaterlogged：<!-- md:samp bool -->

- 类型：bool。


///
