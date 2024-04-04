# <!-- md:samp RequestAbilityPacket -->

> 文档版本：r/20_u7<br/>协议版本：662

<!-- md:samp RequestAbilityPacket -->数据包，数字ID是`184`。

## 结构

```dot
digraph RequestAbilityPacket {
	graph [rankdir=LR];
	{
		graph [rank=max];
		2	[comment="name: \"byte\", typeName: \"\", id: 2, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=byte];
		4	[comment="name: \"byte\", typeName: \"\", id: 4, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=byte];
		8	[comment="name: \"bool\", typeName: \"\", id: 8, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=bool];
		10	[comment="name: \"float\", typeName: \"\", id: 10, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=float];
		13	[comment="name: \"bool\", typeName: \"\", id: 13, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=bool];
		15	[comment="name: \"float\", typeName: \"\", id: 15, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=float];
	}
	0	[comment="name: \"RequestAbilityPacket\", typeName: \"\", id: 0, branchId: 184, recurseId: -1, attributes: 0, notes: \"\"",
		label=RequestAbilityPacket];
	1	[comment="name: \"Ability\", typeName: \"\", id: 1, branchId: 0, recurseId: -1, attributes: 0, notes: \"enumeration: AbilitiesIndex\"",
		label=Ability];
	0 -> 1;
	3	[comment="name: \"Value Type\", typeName: \"\", id: 3, branchId: 0, recurseId: -1, attributes: 0, notes: \"enumeration: RequestAbilityPacket::Type\"",
		label="Value Type"];
	0 -> 3;
	5	[comment="name: \"Dependency on 'Value Type'\", typeName: \"\", id: 5, branchId: 0, recurseId: -1, attributes: 2, notes: \"\"",
		label="Dependency on 'Value Type'",
		shape=note];
	0 -> 5;
	1 -> 2;
	3 -> 4;
	6	[comment="name: \"if (1)\", typeName: \"\", id: 6, branchId: 1, recurseId: -1, attributes: 4, notes: \"\"",
		label="if (1)",
		shape=diamond];
	5 -> 6;
	11	[comment="name: \"if (2)\", typeName: \"\", id: 11, branchId: 2, recurseId: -1, attributes: 4, notes: \"\"",
		label="if (2)",
		shape=diamond];
	5 -> 11;
	7	[comment="name: \"Varible Value\", typeName: \"\", id: 7, branchId: 0, recurseId: -1, attributes: 0, notes: \"\"",
		label="Varible Value"];
	6 -> 7;
	9	[comment="name: \"Default Value = 0.0\", typeName: \"\", id: 9, branchId: 0, recurseId: -1, attributes: 0, notes: \"\"",
		label="Default Value = 0.0"];
	6 -> 9;
	7 -> 8;
	9 -> 10;
	12	[comment="name: \"Default Value = false\", typeName: \"\", id: 12, branchId: 0, recurseId: -1, attributes: 0, notes: \"\"",
		label="Default Value = false"];
	11 -> 12;
	14	[comment="name: \"Varible Value\", typeName: \"\", id: 14, branchId: 0, recurseId: -1, attributes: 0, notes: \"\"",
		label="Varible Value"];
	11 -> 14;
	12 -> 13;
	14 -> 15;
}

```

## 字段

/// define
RequestAbilityPacket

Ability：<!-- md:samp byte -->

- 类型：byte。enumeration: AbilitiesIndex

Value Type：<!-- md:samp byte -->

- 类型：byte。enumeration: RequestAbilityPacket::Type

Dependency on 'Value Type'

//// tab | if (1)
///// define
if (1)

Varible Value：<!-- md:samp bool -->

- 类型：bool。

Default Value = 0.0：<!-- md:samp float -->

- 类型：float。


/////

////

//// tab | if (2)
///// define
if (2)

Default Value = false：<!-- md:samp bool -->

- 类型：bool。

Varible Value：<!-- md:samp float -->

- 类型：float。


/////

////



///
