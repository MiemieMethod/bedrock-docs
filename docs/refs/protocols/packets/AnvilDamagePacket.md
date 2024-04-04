# <!-- md:samp AnvilDamagePacket -->

> 文档版本：r/20_u7<br/>协议版本：662

<!-- md:samp AnvilDamagePacket -->数据包，数字ID是`141`。

## 结构

```viz
digraph AnvilDamagePacket {
	graph [rankdir=LR];
	{
		graph [rank=max];
		2	[comment="name: \"byte\", typeName: \"\", id: 2, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=byte];
		4	[comment="name: \"NetworkBlockPosition\", typeName: \"\", id: 4, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=NetworkBlockPosition];
	}
	0	[comment="name: \"AnvilDamagePacket\", typeName: \"\", id: 0, branchId: 141, recurseId: -1, attributes: 0, notes: \"\"",
		label=AnvilDamagePacket];
	1	[comment="name: \"Damage Amount\", typeName: \"\", id: 1, branchId: 0, recurseId: -1, attributes: 0, notes: \"\"",
		label="Damage Amount"];
	0 -> 1;
	3	[comment="name: \"Block Position\", typeName: \"NetworkBlockPosition\", id: 3, branchId: 0, recurseId: -1, attributes: 256, notes: \"\"",
		label="Block Position"];
	0 -> 3;
	1 -> 2;
	3 -> 4;
}

```

## 字段

/// define
AnvilDamagePacket

Damage Amount：<!-- md:samp byte -->

- 类型：byte。

Block Position：[<!-- md:samp NetworkBlockPosition -->](refs/protocols/types/NetworkBlockPosition.md)

- 类型：NetworkBlockPosition。


///
