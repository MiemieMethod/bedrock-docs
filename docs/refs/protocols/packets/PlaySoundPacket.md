# <!-- md:samp PlaySoundPacket -->

> 文档版本：r/20_u7<br/>协议版本：662

<!-- md:samp PlaySoundPacket -->数据包，数字ID是`86`。

## 结构

```viz
digraph PlaySoundPacket {
	graph [rankdir=LR];
	{
		graph [rank=max];
		2	[comment="name: \"string\", typeName: \"\", id: 2, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=string];
		4	[comment="name: \"NetworkBlockPosition\", typeName: \"\", id: 4, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=NetworkBlockPosition];
		6	[comment="name: \"float\", typeName: \"\", id: 6, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=float];
		8	[comment="name: \"float\", typeName: \"\", id: 8, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=float];
	}
	0	[comment="name: \"PlaySoundPacket\", typeName: \"\", id: 0, branchId: 86, recurseId: -1, attributes: 0, notes: \"\"",
		label=PlaySoundPacket];
	1	[comment="name: \"Name\", typeName: \"\", id: 1, branchId: 0, recurseId: -1, attributes: 0, notes: \"\"",
		label=Name];
	0 -> 1;
	3	[comment="name: \"Position\", typeName: \"NetworkBlockPosition\", id: 3, branchId: 0, recurseId: -1, attributes: 256, notes: \"\"",
		label=Position];
	0 -> 3;
	5	[comment="name: \"Volume\", typeName: \"\", id: 5, branchId: 0, recurseId: -1, attributes: 0, notes: \"\"",
		label=Volume];
	0 -> 5;
	7	[comment="name: \"Pitch\", typeName: \"\", id: 7, branchId: 0, recurseId: -1, attributes: 0, notes: \"\"",
		label=Pitch];
	0 -> 7;
	1 -> 2;
	3 -> 4;
	5 -> 6;
	7 -> 8;
}

```

## 字段

/// define
PlaySoundPacket

Name：<!-- md:samp string -->

- 类型：string。

Position：[<!-- md:samp NetworkBlockPosition -->](refs/protocols/types/networkblockposition.md)

- 类型：NetworkBlockPosition。

Volume：<!-- md:samp float -->

- 类型：float。

Pitch：<!-- md:samp float -->

- 类型：float。


///
