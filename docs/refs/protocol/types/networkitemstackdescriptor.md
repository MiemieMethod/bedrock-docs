# <!-- md:samp NetworkItemStackDescriptor -->

> 文档版本：r/20_u7<br/>协议版本：662

<!-- md:samp NetworkItemStackDescriptor -->类型。

## 结构

```viz
digraph NetworkItemStackDescriptor {
	graph [rankdir=LR];
	{
		graph [rank=max];
		22	[comment="name: \"varint\", typeName: \"\", id: 22, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=varint];
		25	[comment="name: \"varint\", typeName: \"\", id: 25, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=varint];
		27	[comment="name: \"unsigned short\", typeName: \"\", id: 27, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label="unsigned short"];
		29	[comment="name: \"unsigned varint\", typeName: \"\", id: 29, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label="unsigned varint"];
		31	[comment="name: \"bool\", typeName: \"\", id: 31, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=bool];
		34	[comment="name: \"[No Data]\", typeName: \"\", id: 34, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label="[No Data]"];
		40	[comment="name: \"ItemStackNetIdVariant\", typeName: \"\", id: 40, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=ItemStackNetIdVariant];
		42	[comment="name: \"varint\", typeName: \"\", id: 42, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=varint];
		44	[comment="name: \"string\", typeName: \"\", id: 44, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=string];
	}
	18	[comment="name: \"NetworkItemStackDescriptor\", typeName: \"\", id: 18, branchId: 0, recurseId: -1, attributes: 0, notes: \"\"",
		label=NetworkItemStackDescriptor];
	19	[comment="name: \"Dependency on 'Valid item'\", typeName: \"\", id: 19, branchId: 0, recurseId: -1, attributes: 2, notes: \"\"",
		label="Dependency on 'Valid item'",
		shape=note];
	18 -> 19;
	20	[comment="name: \"if (0)\", typeName: \"\", id: 20, branchId: 0, recurseId: -1, attributes: 4, notes: \"\"",
		label="if (0)",
		shape=diamond];
	19 -> 20;
	23	[comment="name: \"if (1)\", typeName: \"\", id: 23, branchId: 1, recurseId: -1, attributes: 4, notes: \"\"",
		label="if (1)",
		shape=diamond];
	19 -> 23;
	21	[comment="name: \"Id\", typeName: \"\", id: 21, branchId: 0, recurseId: -1, attributes: 0, notes: \"Send fixed Id of 0 for invalid item\"",
		label=Id];
	20 -> 21;
	21 -> 22;
	24	[comment="name: \"Id\", typeName: \"\", id: 24, branchId: 0, recurseId: -1, attributes: 0, notes: \"\"",
		label=Id];
	23 -> 24;
	26	[comment="name: \"Stack size\", typeName: \"\", id: 26, branchId: 0, recurseId: -1, attributes: 0, notes: \"\"",
		label="Stack size"];
	23 -> 26;
	28	[comment="name: \"Aux value\", typeName: \"\", id: 28, branchId: 0, recurseId: -1, attributes: 0, notes: \"\"",
		label="Aux value"];
	23 -> 28;
	30	[comment="name: \"Include Net Id\", typeName: \"\", id: 30, branchId: 0, recurseId: -1, attributes: 0, notes: \"\"",
		label="Include Net Id"];
	23 -> 30;
	32	[comment="name: \"Dependency on 'Include Net Id'\", typeName: \"\", id: 32, branchId: 0, recurseId: -1, attributes: 2, notes: \"\"",
		label="Dependency on 'Include Net Id'",
		shape=note];
	23 -> 32;
	41	[comment="name: \"Block Runtime Id\", typeName: \"\", id: 41, branchId: 0, recurseId: -1, attributes: 0, notes: \"\"",
		label="Block Runtime Id"];
	23 -> 41;
	43	[comment="name: \"User Data Buffer\", typeName: \"\", id: 43, branchId: 0, recurseId: -1, attributes: 0, notes: \"The @ItemInstanceUserData.html#\
ItemInstanceUserData@  binary blob encoded as a String, so it's unsigned varint length prefixed. Get all your nbt+property bytes, \
calculate the length, write that length, THEN write the data.\"",
		label="User Data Buffer"];
	23 -> 43;
	24 -> 25;
	26 -> 27;
	28 -> 29;
	30 -> 31;
	33	[comment="name: \"if (0)\", typeName: \"\", id: 33, branchId: 0, recurseId: -1, attributes: 4, notes: \"\"",
		label="if (0)",
		shape=diamond];
	32 -> 33;
	35	[comment="name: \"if (1)\", typeName: \"\", id: 35, branchId: 1, recurseId: -1, attributes: 4, notes: \"\"",
		label="if (1)",
		shape=diamond];
	32 -> 35;
	33 -> 34;
	36	[comment="name: \"Net Id Variant\", typeName: \"ItemStackNetIdVariant\", id: 36, branchId: 0, recurseId: -1, attributes: 256, notes: \"\"",
		label="Net Id Variant"];
	35 -> 36;
	36 -> 40;
	41 -> 42;
	43 -> 44;
}

```

## 字段

/// define
NetworkItemStackDescriptor

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

Include Net Id：<!-- md:samp bool -->

- 类型：bool。

Dependency on 'Include Net Id'

////// tab | if (0)
/////// define
if (0)：<!-- md:samp [No Data] -->

- 类型：[No Data]。


///////

//////

////// tab | if (1)
/////// define
if (1)

Net Id Variant：[<!-- md:samp ItemStackNetIdVariant -->](refs/protocols/types/itemstacknetidvariant.md)

- 类型：ItemStackNetIdVariant。


///////

//////


Block Runtime Id：<!-- md:samp varint -->

- 类型：varint。

User Data Buffer：<!-- md:samp string -->

- 类型：string。The @ItemInstanceUserData.html#ItemInstanceUserData@  binary blob encoded as a String, so it's unsigned varint length prefixed. Get all your nbt+property bytes, calculate the length, write that length, THEN write the data.


/////

////



///
