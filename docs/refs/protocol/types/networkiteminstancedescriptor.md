# <!-- md:samp NetworkItemInstanceDescriptor -->

> 文档版本：r/20_u7<br/>协议版本：662

<!-- md:samp NetworkItemInstanceDescriptor -->类型。

## 结构

```viz
digraph NetworkItemInstanceDescriptor {
	graph [rankdir=LR];
	{
		graph [rank=max];
		29	[comment="name: \"varint\", typeName: \"\", id: 29, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=varint];
		32	[comment="name: \"varint\", typeName: \"\", id: 32, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=varint];
		34	[comment="name: \"unsigned short\", typeName: \"\", id: 34, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label="unsigned short"];
		36	[comment="name: \"unsigned varint\", typeName: \"\", id: 36, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label="unsigned varint"];
		38	[comment="name: \"varint\", typeName: \"\", id: 38, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=varint];
		40	[comment="name: \"string\", typeName: \"\", id: 40, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=string];
	}
	25	[comment="name: \"NetworkItemInstanceDescriptor\", typeName: \"\", id: 25, branchId: 0, recurseId: -1, attributes: 0, notes: \"\"",
		label=NetworkItemInstanceDescriptor];
	26	[comment="name: \"Dependency on 'Valid item'\", typeName: \"\", id: 26, branchId: 0, recurseId: -1, attributes: 2, notes: \"\"",
		label="Dependency on 'Valid item'",
		shape=note];
	25 -> 26;
	27	[comment="name: \"if (0)\", typeName: \"\", id: 27, branchId: 0, recurseId: -1, attributes: 4, notes: \"\"",
		label="if (0)",
		shape=diamond];
	26 -> 27;
	30	[comment="name: \"if (1)\", typeName: \"\", id: 30, branchId: 1, recurseId: -1, attributes: 4, notes: \"\"",
		label="if (1)",
		shape=diamond];
	26 -> 30;
	28	[comment="name: \"Id\", typeName: \"\", id: 28, branchId: 0, recurseId: -1, attributes: 0, notes: \"Send fixed Id of 0 for invalid item\"",
		label=Id];
	27 -> 28;
	28 -> 29;
	31	[comment="name: \"Id\", typeName: \"\", id: 31, branchId: 0, recurseId: -1, attributes: 0, notes: \"\"",
		label=Id];
	30 -> 31;
	33	[comment="name: \"Stack size\", typeName: \"\", id: 33, branchId: 0, recurseId: -1, attributes: 0, notes: \"\"",
		label="Stack size"];
	30 -> 33;
	35	[comment="name: \"Aux value\", typeName: \"\", id: 35, branchId: 0, recurseId: -1, attributes: 0, notes: \"\"",
		label="Aux value"];
	30 -> 35;
	37	[comment="name: \"Block Runtime Id\", typeName: \"\", id: 37, branchId: 0, recurseId: -1, attributes: 0, notes: \"\"",
		label="Block Runtime Id"];
	30 -> 37;
	39	[comment="name: \"User Data Buffer\", typeName: \"\", id: 39, branchId: 0, recurseId: -1, attributes: 0, notes: \"The @ItemInstanceUserData.html#\
ItemInstanceUserData@  binary blob encoded as a String, so it's unsigned varint length prefixed. Get all your nbt+property bytes, \
calculate the length, write that length, THEN write the data.\"",
		label="User Data Buffer"];
	30 -> 39;
	31 -> 32;
	33 -> 34;
	35 -> 36;
	37 -> 38;
	39 -> 40;
}

```

## 字段

/// define
NetworkItemInstanceDescriptor

Dependency on 'Valid item'

//// tab | if (0)
///// define
if (0)

Id：<!-- md:samp varint -->

- 类型：varint。Send fixed Id of 0 for inval'id' item


/////

////

//// tab | if (1)
///// define
if (1)

Id：<!-- md:samp varint -->

- 类型：varint。

Stack size：<!-- md:samp unsigned short -->

- 类型：unsigned short。

Aux value：<!-- md:samp unsigned varint -->

- 类型：unsigned varint。

Block Runtime Id：<!-- md:samp varint -->

- 类型：varint。

User Data Buffer：<!-- md:samp string -->

- 类型：string。The @ItemInstanceUserData.html#ItemInstanceUserData@  binary blob encoded as a String, so it's unsigned varint length prefixed. Get all your nbt+property bytes, calculate the length, write that length, THEN write the data.


/////

////



///
