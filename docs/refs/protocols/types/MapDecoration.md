# <!-- md:samp MapDecoration -->

> 文档版本：r/20_u7<br/>协议版本：662

<!-- md:samp MapDecoration -->类型。

## 结构

```dot
digraph MapDecoration {
	graph [rankdir=LR];
	{
		graph [rank=max];
		62	[comment="name: \"byte\", typeName: \"\", id: 62, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=byte];
		64	[comment="name: \"byte\", typeName: \"\", id: 64, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=byte];
		66	[comment="name: \"byte\", typeName: \"\", id: 66, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=byte];
		68	[comment="name: \"byte\", typeName: \"\", id: 68, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=byte];
		70	[comment="name: \"string\", typeName: \"\", id: 70, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=string];
		72	[comment="name: \"unsigned varint\", typeName: \"\", id: 72, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label="unsigned varint"];
	}
	60	[comment="name: \"MapDecoration\", typeName: \"\", id: 60, branchId: 0, recurseId: -1, attributes: 0, notes: \"\"",
		label=MapDecoration];
	61	[comment="name: \"Map Decoration Type\", typeName: \"\", id: 61, branchId: 0, recurseId: -1, attributes: 0, notes: \"enumeration: MapDecoration::\
Type\"",
		label="Map Decoration Type"];
	60 -> 61;
	63	[comment="name: \"Rotation\", typeName: \"\", id: 63, branchId: 0, recurseId: -1, attributes: 0, notes: \"\"",
		label=Rotation];
	60 -> 63;
	65	[comment="name: \"X\", typeName: \"\", id: 65, branchId: 0, recurseId: -1, attributes: 0, notes: \"\"",
		label=X];
	60 -> 65;
	67	[comment="name: \"Y\", typeName: \"\", id: 67, branchId: 0, recurseId: -1, attributes: 0, notes: \"\"",
		label=Y];
	60 -> 67;
	69	[comment="name: \"Label\", typeName: \"\", id: 69, branchId: 0, recurseId: -1, attributes: 0, notes: \"\"",
		label=Label];
	60 -> 69;
	71	[comment="name: \"Color - ARGB\", typeName: \"\", id: 71, branchId: 0, recurseId: -1, attributes: 0, notes: \"\"",
		label="Color - ARGB"];
	60 -> 71;
	61 -> 62;
	63 -> 64;
	65 -> 66;
	67 -> 68;
	69 -> 70;
	71 -> 72;
}

```

## 字段

/// define
MapDecoration

Map Decoration Type：<!-- md:samp byte -->

- 类型：byte。enumeration: MapDecoration::Type

Rotation：<!-- md:samp byte -->

- 类型：byte。

X：<!-- md:samp byte -->

- 类型：byte。

Y：<!-- md:samp byte -->

- 类型：byte。

Label：<!-- md:samp string -->

- 类型：string。

Color - ARGB：<!-- md:samp unsigned varint -->

- 类型：unsigned varint。


///
