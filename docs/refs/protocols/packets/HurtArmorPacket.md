# <!-- md:samp HurtArmorPacket -->

> 文档版本：r/20_u7<br/>协议版本：662

<!-- md:samp HurtArmorPacket -->数据包，数字ID是`38`。

## 结构

```viz
digraph HurtArmorPacket {
	graph [rankdir=LR];
	{
		graph [rank=max];
		2	[comment="name: \"varint\", typeName: \"\", id: 2, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=varint];
		4	[comment="name: \"varint\", typeName: \"\", id: 4, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=varint];
		6	[comment="name: \"unsigned varint64\", typeName: \"\", id: 6, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label="unsigned varint64"];
	}
	0	[comment="name: \"HurtArmorPacket\", typeName: \"\", id: 0, branchId: 38, recurseId: -1, attributes: 0, notes: \"\"",
		label=HurtArmorPacket];
	1	[comment="name: \"Cause\", typeName: \"\", id: 1, branchId: 0, recurseId: -1, attributes: 0, notes: \"\"",
		label=Cause];
	0 -> 1;
	3	[comment="name: \"Damage\", typeName: \"\", id: 3, branchId: 0, recurseId: -1, attributes: 0, notes: \"\"",
		label=Damage];
	0 -> 3;
	5	[comment="name: \"Armor Slots\", typeName: \"\", id: 5, branchId: 0, recurseId: -1, attributes: 0, notes: \"Bitset\"",
		label="Armor Slots"];
	0 -> 5;
	1 -> 2;
	3 -> 4;
	5 -> 6;
}

```

## 字段

/// define
HurtArmorPacket

Cause：<!-- md:samp varint -->

- 类型：varint。

Damage：<!-- md:samp varint -->

- 类型：varint。

Armor Slots：<!-- md:samp unsigned varint64 -->

- 类型：unsigned varint64。Bitset


///
