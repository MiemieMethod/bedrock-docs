# <!-- md:samp PlayerListPacket -->

> 文档版本：r/20_u7<br/>协议版本：662

<!-- md:samp PlayerListPacket -->数据包，数字ID是`63`。

## 结构

```viz
digraph PlayerListPacket {
	graph [rankdir=LR];
	{
		graph [rank=max];
		2	[comment="name: \"byte\", typeName: \"\", id: 2, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=byte];
		7	[comment="name: \"unsigned varint\", typeName: \"\", id: 7, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label="unsigned varint"];
		10	[comment="name: \"mce::UUID\", typeName: \"\", id: 10, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label="mce::UUID"];
		12	[comment="name: \"ActorUniqueID\", typeName: \"\", id: 12, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=ActorUniqueID];
		14	[comment="name: \"string\", typeName: \"\", id: 14, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=string];
		16	[comment="name: \"string\", typeName: \"\", id: 16, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=string];
		18	[comment="name: \"string\", typeName: \"\", id: 18, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=string];
		20	[comment="name: \"int\", typeName: \"\", id: 20, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=int];
		113	[comment="name: \"SerializedSkin\", typeName: \"\", id: 113, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=SerializedSkin];
		115	[comment="name: \"bool\", typeName: \"\", id: 115, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=bool];
		117	[comment="name: \"bool\", typeName: \"\", id: 117, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=bool];
		119	[comment="name: \"bool\", typeName: \"\", id: 119, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=bool];
		121	[comment="name: \"bool\", typeName: \"\", id: 121, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=bool];
		125	[comment="name: \"unsigned varint\", typeName: \"\", id: 125, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label="unsigned varint"];
		128	[comment="name: \"mce::UUID\", typeName: \"\", id: 128, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label="mce::UUID"];
	}
	0	[comment="name: \"PlayerListPacket\", typeName: \"\", id: 0, branchId: 63, recurseId: -1, attributes: 0, notes: \"\"",
		label=PlayerListPacket];
	1	[comment="name: \"Action\", typeName: \"\", id: 1, branchId: 0, recurseId: -1, attributes: 0, notes: \"enumeration: PlayerListPacketType\"",
		label=Action];
	0 -> 1;
	3	[comment="name: \"Dependency on 'Action'\", typeName: \"\", id: 3, branchId: 0, recurseId: -1, attributes: 2, notes: \"\"",
		label="Dependency on 'Action'",
		shape=note];
	0 -> 3;
	1 -> 2;
	4	[comment="name: \"if (0)\", typeName: \"\", id: 4, branchId: 0, recurseId: -1, attributes: 4, notes: \"\"",
		label="if (0)",
		shape=diamond];
	3 -> 4;
	122	[comment="name: \"if (1)\", typeName: \"\", id: 122, branchId: 1, recurseId: -1, attributes: 4, notes: \"\"",
		label="if (1)",
		shape=diamond];
	3 -> 122;
	5	[comment="name: \"Add Player List\", typeName: \"\", id: 5, branchId: 0, recurseId: -1, attributes: 8, notes: \"\"",
		label="Add Player List"];
	4 -> 5;
	120	[comment="name: \"Is trusted skin\", typeName: \"\", id: 120, branchId: 0, recurseId: -1, attributes: 0, notes: \"\"",
		label="Is trusted skin"];
	4 -> 120;
	6	[comment="name: \"Array Size\", typeName: \"\", id: 6, branchId: 0, recurseId: -1, attributes: 0, notes: \"\"",
		label="Array Size"];
	5 -> 6;
	8	[comment="name: \"example element\", typeName: \"\", id: 8, branchId: 0, recurseId: -1, attributes: 16, notes: \"\"",
		label="example element",
		style=dotted];
	5 -> 8;
	6 -> 7;
	9	[comment="name: \"UUID\", typeName: \"mce::UUID\", id: 9, branchId: 0, recurseId: -1, attributes: 256, notes: \"\"",
		label=UUID];
	8 -> 9;
	11	[comment="name: \"Target Actor ID\", typeName: \"ActorUniqueID\", id: 11, branchId: 0, recurseId: -1, attributes: 256, notes: \"\"",
		label="Target Actor ID"];
	8 -> 11;
	13	[comment="name: \"Player Name\", typeName: \"\", id: 13, branchId: 0, recurseId: -1, attributes: 0, notes: \"\"",
		label="Player Name"];
	8 -> 13;
	15	[comment="name: \"XBL XUID\", typeName: \"\", id: 15, branchId: 0, recurseId: -1, attributes: 0, notes: \"\"",
		label="XBL XUID"];
	8 -> 15;
	17	[comment="name: \"Platform Chat Id\", typeName: \"\", id: 17, branchId: 0, recurseId: -1, attributes: 0, notes: \"\"",
		label="Platform Chat Id"];
	8 -> 17;
	19	[comment="name: \"Build Platform\", typeName: \"\", id: 19, branchId: 0, recurseId: -1, attributes: 0, notes: \"enumeration: BuildPlatform\"",
		label="Build Platform"];
	8 -> 19;
	21	[comment="name: \"Serialized Skin\", typeName: \"SerializedSkin\", id: 21, branchId: 0, recurseId: -1, attributes: 256, notes: \"\"",
		label="Serialized Skin"];
	8 -> 21;
	114	[comment="name: \"Is Teacher?\", typeName: \"\", id: 114, branchId: 0, recurseId: -1, attributes: 0, notes: \"\"",
		label="Is Teacher?"];
	8 -> 114;
	116	[comment="name: \"Is Host?\", typeName: \"\", id: 116, branchId: 0, recurseId: -1, attributes: 0, notes: \"\"",
		label="Is Host?"];
	8 -> 116;
	118	[comment="name: \"Is SubClient\", typeName: \"\", id: 118, branchId: 0, recurseId: -1, attributes: 0, notes: \"\"",
		label="Is SubClient"];
	8 -> 118;
	9 -> 10;
	11 -> 12;
	13 -> 14;
	15 -> 16;
	17 -> 18;
	19 -> 20;
	21 -> 113;
	114 -> 115;
	116 -> 117;
	118 -> 119;
	120 -> 121;
	123	[comment="name: \"Remove Player List\", typeName: \"\", id: 123, branchId: 0, recurseId: -1, attributes: 8, notes: \"\"",
		label="Remove Player List"];
	122 -> 123;
	124	[comment="name: \"Array Size\", typeName: \"\", id: 124, branchId: 0, recurseId: -1, attributes: 0, notes: \"\"",
		label="Array Size"];
	123 -> 124;
	126	[comment="name: \"example element\", typeName: \"\", id: 126, branchId: 0, recurseId: -1, attributes: 16, notes: \"\"",
		label="example element",
		style=dotted];
	123 -> 126;
	124 -> 125;
	127	[comment="name: \"UUID\", typeName: \"mce::UUID\", id: 127, branchId: 0, recurseId: -1, attributes: 256, notes: \"\"",
		label=UUID];
	126 -> 127;
	127 -> 128;
}

```

## 字段

/// define
PlayerListPacket

Action：<!-- md:samp byte -->

- 类型：byte。enumeration: PlayerListPacketType

Dependency on 'Action'

//// tab | if (0)
///// define
if (0)

Add Player List

Add Player List数组的大小：<!-- md:samp unsigned varint -->

- 类型：unsigned varint。

Add Player List的示例元素

UUID：[<!-- md:samp mce::UUID -->](refs/protocols/types/mce::UUID.md)

- 类型：mce::UUID。

Target Actor ID：[<!-- md:samp ActorUniqueID -->](refs/protocols/types/ActorUniqueID.md)

- 类型：ActorUniqueID。

Player Name：<!-- md:samp string -->

- 类型：string。

XBL XUID：<!-- md:samp string -->

- 类型：string。

Platform Chat Id：<!-- md:samp string -->

- 类型：string。

Build Platform：<!-- md:samp int -->

- 类型：int。enumeration: BuildPlatform

Serialized Skin：[<!-- md:samp SerializedSkin -->](refs/protocols/types/SerializedSkin.md)

- 类型：SerializedSkin。

Is Teacher?：<!-- md:samp bool -->

- 类型：bool。

Is Host?：<!-- md:samp bool -->

- 类型：bool。

Is SubClient：<!-- md:samp bool -->

- 类型：bool。

Is trusted skin：<!-- md:samp bool -->

- 类型：bool。


/////

////

//// tab | if (1)
///// define
if (1)

Remove Player List

Remove Player List数组的大小：<!-- md:samp unsigned varint -->

- 类型：unsigned varint。

Remove Player List的示例元素

UUID：[<!-- md:samp mce::UUID -->](refs/protocols/types/mce::UUID.md)

- 类型：mce::UUID。


/////

////



///
