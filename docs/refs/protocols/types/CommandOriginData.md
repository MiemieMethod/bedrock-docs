# <!-- md:samp CommandOriginData -->

> 文档版本：r/20_u7<br/>协议版本：662

<!-- md:samp CommandOriginData -->类型。

## 结构

```viz
digraph CommandOriginData {
	graph [rankdir=LR];
	{
		graph [rank=max];
		6	[comment="name: \"unsigned varint\", typeName: \"\", id: 6, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label="unsigned varint"];
		8	[comment="name: \"mce::UUID\", typeName: \"\", id: 8, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label="mce::UUID"];
		10	[comment="name: \"string\", typeName: \"\", id: 10, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=string];
		13	[comment="name: \"[No Data]\", typeName: \"\", id: 13, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label="[No Data]"];
		15	[comment="name: \"[No Data]\", typeName: \"\", id: 15, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label="[No Data]"];
		18	[comment="name: \"varint64\", typeName: \"\", id: 18, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=varint64];
		21	[comment="name: \"varint64\", typeName: \"\", id: 21, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=varint64];
	}
	4	[comment="name: \"CommandOriginData\", typeName: \"\", id: 4, branchId: 0, recurseId: -1, attributes: 0, notes: \"\"",
		label=CommandOriginData];
	5	[comment="name: \"Command Type\", typeName: \"\", id: 5, branchId: 0, recurseId: -1, attributes: 0, notes: \"enumeration: CommandOriginType\"",
		label="Command Type"];
	4 -> 5;
	7	[comment="name: \"Command UUID\", typeName: \"mce::UUID\", id: 7, branchId: 0, recurseId: -1, attributes: 256, notes: \"Unique UUID that represents \
an instantiation of a command. Each time a command is run it should be given a UUID to represent that instance.\"",
		label="Command UUID"];
	4 -> 7;
	9	[comment="name: \"Request ID\", typeName: \"\", id: 9, branchId: 0, recurseId: -1, attributes: 0, notes: \"\"",
		label="Request ID"];
	4 -> 9;
	11	[comment="name: \"Dependency on 'Command Type'\", typeName: \"\", id: 11, branchId: 0, recurseId: -1, attributes: 2, notes: \"\"",
		label="Dependency on 'Command Type'",
		shape=note];
	4 -> 11;
	5 -> 6;
	7 -> 8;
	9 -> 10;
	12	[comment="name: \"if (0)\", typeName: \"\", id: 12, branchId: 0, recurseId: -1, attributes: 4, notes: \"\"",
		label="if (0)",
		shape=diamond];
	11 -> 12;
	14	[comment="name: \"if (5)\", typeName: \"\", id: 14, branchId: 5, recurseId: -1, attributes: 4, notes: \"\"",
		label="if (5)",
		shape=diamond];
	11 -> 14;
	16	[comment="name: \"if (4)\", typeName: \"\", id: 16, branchId: 4, recurseId: -1, attributes: 4, notes: \"\"",
		label="if (4)",
		shape=diamond];
	11 -> 16;
	19	[comment="name: \"if (3)\", typeName: \"\", id: 19, branchId: 3, recurseId: -1, attributes: 4, notes: \"\"",
		label="if (3)",
		shape=diamond];
	11 -> 19;
	12 -> 13;
	14 -> 15;
	17	[comment="name: \"Player ID\", typeName: \"\", id: 17, branchId: 0, recurseId: -1, attributes: 0, notes: \"\"",
		label="Player ID"];
	16 -> 17;
	17 -> 18;
	20	[comment="name: \"Player ID\", typeName: \"\", id: 20, branchId: 0, recurseId: -1, attributes: 0, notes: \"\"",
		label="Player ID"];
	19 -> 20;
	20 -> 21;
}

```

## 字段

/// define
CommandOriginData

Command Type：<!-- md:samp unsigned varint -->

- 类型：unsigned varint。enumeration: CommandOriginType

Command UUID：[<!-- md:samp mce::UUID -->](refs/protocols/types/mce::UUID.md)

- 类型：mce::UUID。Unique UUID that represents an instantiation of a command. Each time a command is run it should be given a UUID to represent that instance.

Request ID：<!-- md:samp string -->

- 类型：string。

Dependency on 'Command Type'

//// tab | if (0)
///// define
if (0)：<!-- md:samp [No Data] -->

- 类型：[No Data]。


/////

////

//// tab | if (5)
///// define
if (5)：<!-- md:samp [No Data] -->

- 类型：[No Data]。


/////

////

//// tab | if (4)
///// define
if (4)

Player ID：<!-- md:samp varint64 -->

- 类型：varint64。


/////

////

//// tab | if (3)
///// define
if (3)

Player ID：<!-- md:samp varint64 -->

- 类型：varint64。


/////

////



///
