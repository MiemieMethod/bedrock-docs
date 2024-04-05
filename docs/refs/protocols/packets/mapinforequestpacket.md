# <!-- md:samp MapInfoRequestPacket -->

> 文档版本：r/20_u7<br/>协议版本：662

<!-- md:samp MapInfoRequestPacket -->数据包，数字ID是`68`。

## 结构

```viz
digraph MapInfoRequestPacket {
	graph [rankdir=LR];
	{
		graph [rank=max];
		2	[comment="name: \"ActorUniqueID\", typeName: \"\", id: 2, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=ActorUniqueID];
		4	[comment="name: \"unsigned int\", typeName: \"\", id: 4, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label="unsigned int"];
		7	[comment="name: \"[No Data]\", typeName: \"\", id: 7, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label="[No Data]"];
		12	[comment="name: \"unsigned int\", typeName: \"\", id: 12, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label="unsigned int"];
		14	[comment="name: \"unsigned short\", typeName: \"\", id: 14, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label="unsigned short"];
	}
	0	[comment="name: \"MapInfoRequestPacket\", typeName: \"\", id: 0, branchId: 68, recurseId: -1, attributes: 0, notes: \"\"",
		label=MapInfoRequestPacket];
	1	[comment="name: \"Map Unique ID\", typeName: \"ActorUniqueID\", id: 1, branchId: 0, recurseId: -1, attributes: 256, notes: \"\"",
		label="Map Unique ID"];
	0 -> 1;
	3	[comment="name: \"Client Pixels List Size\", typeName: \"\", id: 3, branchId: 0, recurseId: -1, attributes: 0, notes: \"\"",
		label="Client Pixels List Size"];
	0 -> 3;
	5	[comment="name: \"Dependency on 'mClientPixels.size() > 0 ?'\", typeName: \"\", id: 5, branchId: 0, recurseId: -1, attributes: 2, notes: \"\"",
		label="Dependency on 'mClientPixels.size() > 0 ?'",
		shape=note];
	0 -> 5;
	1 -> 2;
	3 -> 4;
	6	[comment="name: \"if (0)\", typeName: \"\", id: 6, branchId: 0, recurseId: -1, attributes: 4, notes: \"\"",
		label="if (0)",
		shape=diamond];
	5 -> 6;
	8	[comment="name: \"if (1)\", typeName: \"\", id: 8, branchId: 1, recurseId: -1, attributes: 4, notes: \"\"",
		label="if (1)",
		shape=diamond];
	5 -> 8;
	6 -> 7;
	9	[comment="name: \"Client Pixels List\", typeName: \"\", id: 9, branchId: 0, recurseId: -1, attributes: 8, notes: \"These are sent from the client \
to tell the Server map about terrain pixels it doesn't know about\"",
		label="Client Pixels List"];
	8 -> 9;
	10	[comment="name: \"example element\", typeName: \"\", id: 10, branchId: 0, recurseId: -1, attributes: 16, notes: \"\"",
		label="example element",
		style=dotted];
	9 -> 10;
	11	[comment="name: \"pixel\", typeName: \"\", id: 11, branchId: 0, recurseId: -1, attributes: 0, notes: \"\"",
		label=pixel];
	10 -> 11;
	13	[comment="name: \"index\", typeName: \"\", id: 13, branchId: 0, recurseId: -1, attributes: 0, notes: \"\"",
		label=index];
	10 -> 13;
	11 -> 12;
	13 -> 14;
}

```

## 字段

/// define
MapInfoRequestPacket

Map Unique ID：[<!-- md:samp ActorUniqueID -->](../types/actoruniqueid.md)

- 类型：ActorUniqueID。

Client Pixels List Size：<!-- md:samp unsigned int -->

- 类型：unsigned int。

Dependency on 'mClientPixels.size() > 0 ?'

//// tab | if (0)
///// define
if (0)：<!-- md:samp [No Data] -->

- 类型：[No Data]。


/////

////

//// tab | if (1)
///// define
if (1)

Client Pixels List

////// define
Client Pixels List的示例元素

pixel：<!-- md:samp unsigned int -->

- 类型：unsigned int。

index：<!-- md:samp unsigned short -->

- 类型：unsigned short。


//////



/////

////



///
