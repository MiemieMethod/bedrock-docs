# <!-- md:samp SerializedAbilitiesData::SerializedLayer -->

> 文档版本：r/20_u7<br/>协议版本：662

<!-- md:samp SerializedAbilitiesData::SerializedLayer -->类型。

## 结构

```dot
digraph "SerializedAbilitiesData::SerializedLayer" {
	graph [rankdir=LR];
	{
		graph [rank=max];
		94	[comment="name: \"unsigned short\", typeName: \"\", id: 94, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label="unsigned short"];
		96	[comment="name: \"unsigned int\", typeName: \"\", id: 96, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label="unsigned int"];
		98	[comment="name: \"unsigned int\", typeName: \"\", id: 98, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label="unsigned int"];
		100	[comment="name: \"float\", typeName: \"\", id: 100, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=float];
		102	[comment="name: \"float\", typeName: \"\", id: 102, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=float];
	}
	92	[comment="name: \"SerializedAbilitiesData::SerializedLayer\", typeName: \"\", id: 92, branchId: 0, recurseId: -1, attributes: 0, notes: \"\"",
		label="SerializedAbilitiesData::SerializedLayer"];
	93	[comment="name: \"SerializedLayer\", typeName: \"\", id: 93, branchId: 0, recurseId: -1, attributes: 0, notes: \"enumeration: SerializedAbilitiesData::\
SerializedAbilitiesLayer\"",
		label=SerializedLayer];
	92 -> 93;
	95	[comment="name: \"AbilitiesSet\", typeName: \"\", id: 95, branchId: 0, recurseId: -1, attributes: 0, notes: \"\"",
		label=AbilitiesSet];
	92 -> 95;
	97	[comment="name: \"AbilityValues\", typeName: \"\", id: 97, branchId: 0, recurseId: -1, attributes: 0, notes: \"\"",
		label=AbilityValues];
	92 -> 97;
	99	[comment="name: \"FlySpeed\", typeName: \"\", id: 99, branchId: 0, recurseId: -1, attributes: 0, notes: \"\"",
		label=FlySpeed];
	92 -> 99;
	101	[comment="name: \"WalkSpeed\", typeName: \"\", id: 101, branchId: 0, recurseId: -1, attributes: 0, notes: \"\"",
		label=WalkSpeed];
	92 -> 101;
	93 -> 94;
	95 -> 96;
	97 -> 98;
	99 -> 100;
	101 -> 102;
}

```

## 字段

/// define
SerializedAbilitiesData::SerializedLayer

SerializedLayer：<!-- md:samp unsigned short -->

- 类型：unsigned short。enumeration: SerializedAbilitiesData::SerializedAbilitiesLayer

AbilitiesSet：<!-- md:samp unsigned int -->

- 类型：unsigned int。

AbilityValues：<!-- md:samp unsigned int -->

- 类型：unsigned int。

FlySpeed：<!-- md:samp float -->

- 类型：float。

WalkSpeed：<!-- md:samp float -->

- 类型：float。


///
