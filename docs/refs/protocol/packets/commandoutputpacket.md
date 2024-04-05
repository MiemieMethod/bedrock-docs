# <!-- md:samp CommandOutputPacket -->

> 文档版本：r/20_u7<br/>协议版本：662

<!-- md:samp CommandOutputPacket -->数据包，数字ID是`79`。

## 结构

```viz
digraph CommandOutputPacket {
	graph [rankdir=LR];
	{
		graph [rank=max];
		2	[comment="name: \"CommandOriginData\", typeName: \"\", id: 2, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=CommandOriginData];
		4	[comment="name: \"byte\", typeName: \"\", id: 4, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=byte];
		6	[comment="name: \"unsigned varint\", typeName: \"\", id: 6, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label="unsigned varint"];
		9	[comment="name: \"unsigned varint\", typeName: \"\", id: 9, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label="unsigned varint"];
		12	[comment="name: \"bool\", typeName: \"\", id: 12, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=bool];
		14	[comment="name: \"string\", typeName: \"\", id: 14, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=string];
		17	[comment="name: \"unsigned varint\", typeName: \"\", id: 17, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label="unsigned varint"];
		20	[comment="name: \"string\", typeName: \"\", id: 20, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=string];
		23	[comment="name: \"[No Data]\", typeName: \"\", id: 23, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label="[No Data]"];
		26	[comment="name: \"string\", typeName: \"\", id: 26, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=string];
	}
	0	[comment="name: \"CommandOutputPacket\", typeName: \"\", id: 0, branchId: 79, recurseId: -1, attributes: 0, notes: \"\"",
		label=CommandOutputPacket];
	1	[comment="name: \"Origin Data\", typeName: \"CommandOriginData\", id: 1, branchId: 0, recurseId: -1, attributes: 256, notes: \"\"",
		label="Origin Data"];
	0 -> 1;
	3	[comment="name: \"Output Type\", typeName: \"\", id: 3, branchId: 0, recurseId: -1, attributes: 0, notes: \"enumeration: CommandOutputType\"",
		label="Output Type"];
	0 -> 3;
	5	[comment="name: \"Success Count\", typeName: \"\", id: 5, branchId: 0, recurseId: -1, attributes: 0, notes: \"\"",
		label="Success Count"];
	0 -> 5;
	7	[comment="name: \"Output Messages\", typeName: \"\", id: 7, branchId: 0, recurseId: -1, attributes: 8, notes: \"\"",
		label="Output Messages"];
	0 -> 7;
	21	[comment="name: \"Dependency on 'Output Type == DataSet'\", typeName: \"\", id: 21, branchId: 0, recurseId: -1, attributes: 2, notes: \"\"",
		label="Dependency on 'Output Type == DataSet'",
		shape=note];
	0 -> 21;
	1 -> 2;
	3 -> 4;
	5 -> 6;
	8	[comment="name: \"Array Size\", typeName: \"\", id: 8, branchId: 0, recurseId: -1, attributes: 0, notes: \"\"",
		label="Array Size"];
	7 -> 8;
	10	[comment="name: \"example element\", typeName: \"\", id: 10, branchId: 0, recurseId: -1, attributes: 16, notes: \"\"",
		label="example element",
		style=dotted];
	7 -> 10;
	8 -> 9;
	11	[comment="name: \"Successful?\", typeName: \"\", id: 11, branchId: 0, recurseId: -1, attributes: 0, notes: \"\"",
		label="Successful?"];
	10 -> 11;
	13	[comment="name: \"Message ID\", typeName: \"\", id: 13, branchId: 0, recurseId: -1, attributes: 0, notes: \"\"",
		label="Message ID"];
	10 -> 13;
	15	[comment="name: \"Parameters\", typeName: \"\", id: 15, branchId: 0, recurseId: -1, attributes: 8, notes: \"\"",
		label=Parameters];
	10 -> 15;
	11 -> 12;
	13 -> 14;
	16	[comment="name: \"Array Size\", typeName: \"\", id: 16, branchId: 0, recurseId: -1, attributes: 0, notes: \"\"",
		label="Array Size"];
	15 -> 16;
	18	[comment="name: \"example element\", typeName: \"\", id: 18, branchId: 0, recurseId: -1, attributes: 16, notes: \"\"",
		label="example element",
		style=dotted];
	15 -> 18;
	16 -> 17;
	19	[comment="name: \"Param\", typeName: \"\", id: 19, branchId: 0, recurseId: -1, attributes: 0, notes: \"\"",
		label=Param];
	18 -> 19;
	19 -> 20;
	22	[comment="name: \"if (0)\", typeName: \"\", id: 22, branchId: 0, recurseId: -1, attributes: 4, notes: \"\"",
		label="if (0)",
		shape=diamond];
	21 -> 22;
	24	[comment="name: \"if (1)\", typeName: \"\", id: 24, branchId: 1, recurseId: -1, attributes: 4, notes: \"\"",
		label="if (1)",
		shape=diamond];
	21 -> 24;
	22 -> 23;
	25	[comment="name: \"Data Set\", typeName: \"\", id: 25, branchId: 0, recurseId: -1, attributes: 0, notes: \"\"",
		label="Data Set"];
	24 -> 25;
	25 -> 26;
}

```

## 字段

/// define
CommandOutputPacket

Origin Data：[<!-- md:samp CommandOriginData -->](refs/protocols/types/commandorigindata.md)

- 类型：CommandOriginData。

Output Type：<!-- md:samp byte -->

- 类型：byte。enumeration: CommandOutputType

Success Count：<!-- md:samp unsigned varint -->

- 类型：unsigned varint。

Output Messages

Output Messages数组的大小：<!-- md:samp unsigned varint -->

- 类型：unsigned varint。

Output Messages的示例元素

Successful?：<!-- md:samp bool -->

- 类型：bool。

Message ID：<!-- md:samp string -->

- 类型：string。

Parameters

Parameters数组的大小：<!-- md:samp unsigned varint -->

- 类型：unsigned varint。

Parameters的示例元素

Param：<!-- md:samp string -->

- 类型：string。

Dependency on 'Output Type == DataSet'

//// tab | if (0)
///// define
if (0)：<!-- md:samp [No Data] -->

- 类型：[No Data]。


/////

////

//// tab | if (1)
///// define
if (1)

Data Set：<!-- md:samp string -->

- 类型：string。


/////

////



///
