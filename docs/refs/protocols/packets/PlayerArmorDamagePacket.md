# <!-- md:samp PlayerArmorDamagePacket -->

> 文档版本：r/20_u7<br/>协议版本：662

<!-- md:samp PlayerArmorDamagePacket -->数据包，数字ID是`149`。

## 结构

```dot
digraph PlayerArmorDamagePacket {
	graph [rankdir=LR];
	{
		graph [rank=max];
		2	[comment="name: \"byte\", typeName: \"\", id: 2, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=byte];
		4	[comment="name: \"varint\", typeName: \"\", id: 4, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=varint];
		6	[comment="name: \"varint\", typeName: \"\", id: 6, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=varint];
		8	[comment="name: \"varint\", typeName: \"\", id: 8, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=varint];
		10	[comment="name: \"varint\", typeName: \"\", id: 10, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=varint];
	}
	0	[comment="name: \"PlayerArmorDamagePacket\", typeName: \"\", id: 0, branchId: 149, recurseId: -1, attributes: 0, notes: \"\"",
		label=PlayerArmorDamagePacket];
	1	[comment="name: \"Slots Bitset\", typeName: \"\", id: 1, branchId: 0, recurseId: -1, attributes: 0, notes: \"\"",
		label="Slots Bitset"];
	0 -> 1;
	3	[comment="name: \"Damage For Slot (Only Gets Written If Bit Is Set)\", typeName: \"\", id: 3, branchId: 0, recurseId: -1, attributes: 0, notes: \"\"",
		label="Damage For Slot (Only Gets Written If Bit Is Set)"];
	0 -> 3;
	5	[comment="name: \"Damage For Slot (Only Gets Written If Bit Is Set)\", typeName: \"\", id: 5, branchId: 0, recurseId: -1, attributes: 0, notes: \"\"",
		label="Damage For Slot (Only Gets Written If Bit Is Set)"];
	0 -> 5;
	7	[comment="name: \"Damage For Slot (Only Gets Written If Bit Is Set)\", typeName: \"\", id: 7, branchId: 0, recurseId: -1, attributes: 0, notes: \"\"",
		label="Damage For Slot (Only Gets Written If Bit Is Set)"];
	0 -> 7;
	9	[comment="name: \"Damage For Slot (Only Gets Written If Bit Is Set)\", typeName: \"\", id: 9, branchId: 0, recurseId: -1, attributes: 0, notes: \"\"",
		label="Damage For Slot (Only Gets Written If Bit Is Set)"];
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
PlayerArmorDamagePacket

Slots Bitset：<!-- md:samp byte -->

- 类型：byte。

Damage For Slot (Only Gets Written If Bit Is Set)：<!-- md:samp varint -->

- 类型：varint。


///
