# <!-- md:samp SerializedAbilitiesData -->

> 文档版本：r/20_u7<br/>协议版本：662

<!-- md:samp SerializedAbilitiesData -->类型。

## 结构

```viz
digraph SerializedAbilitiesData {
	graph [rankdir=LR];
	{
		graph [rank=max];
		82	[comment="name: \"int64\", typeName: \"\", id: 82, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=int64];
		84	[comment="name: \"byte\", typeName: \"\", id: 84, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=byte];
		86	[comment="name: \"byte\", typeName: \"\", id: 86, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=byte];
		89	[comment="name: \"unsigned varint\", typeName: \"\", id: 89, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label="unsigned varint"];
		103	[comment="name: \"SerializedAbilitiesData::SerializedLayer\", typeName: \"\", id: 103, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label="SerializedAbilitiesData::SerializedLayer"];
	}
	80	[comment="name: \"SerializedAbilitiesData\", typeName: \"\", id: 80, branchId: 0, recurseId: -1, attributes: 0, notes: \"\"",
		label=SerializedAbilitiesData];
	81	[comment="name: \"TargetPlayer.rawID\", typeName: \"\", id: 81, branchId: 0, recurseId: -1, attributes: 0, notes: \"\"",
		label="TargetPlayer.rawID"];
	80 -> 81;
	83	[comment="name: \"mPlayerPermissions\", typeName: \"\", id: 83, branchId: 0, recurseId: -1, attributes: 0, notes: \"enumeration: PlayerPermissionLevel\"",
		label=mPlayerPermissions];
	80 -> 83;
	85	[comment="name: \"mCommandPermissions\", typeName: \"\", id: 85, branchId: 0, recurseId: -1, attributes: 0, notes: \"enumeration: CommandPermissionLevel\"",
		label=mCommandPermissions];
	80 -> 85;
	87	[comment="name: \"Layers\", typeName: \"\", id: 87, branchId: 0, recurseId: -1, attributes: 8, notes: \"\"",
		label=Layers];
	80 -> 87;
	81 -> 82;
	83 -> 84;
	85 -> 86;
	88	[comment="name: \"Array Size\", typeName: \"\", id: 88, branchId: 0, recurseId: -1, attributes: 0, notes: \"\"",
		label="Array Size"];
	87 -> 88;
	90	[comment="name: \"example element\", typeName: \"\", id: 90, branchId: 0, recurseId: -1, attributes: 16, notes: \"\"",
		label="example element",
		style=dotted];
	87 -> 90;
	88 -> 89;
	91	[comment="name: \"layers\", typeName: \"SerializedAbilitiesData::SerializedLayer\", id: 91, branchId: 0, recurseId: -1, attributes: 256, notes: \"\"",
		label=layers];
	90 -> 91;
	91 -> 103;
}

```

## 字段

/// define
SerializedAbilitiesData

TargetPlayer.rawID：<!-- md:samp int64 -->

- 类型：int64。

mPlayerPermissions：<!-- md:samp byte -->

- 类型：byte。enumeration: PlayerPermissionLevel

mCommandPermissions：<!-- md:samp byte -->

- 类型：byte。enumeration: CommandPermissionLevel

Layers

Layers数组的大小：<!-- md:samp unsigned varint -->

- 类型：unsigned varint。

Layers的示例元素

layers：[<!-- md:samp SerializedAbilitiesData::SerializedLayer -->](refs/protocols/types/serializedabilitiesdata::serializedlayer.md)

- 类型：SerializedAbilitiesData::SerializedLayer。


///
