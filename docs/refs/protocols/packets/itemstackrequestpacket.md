# <!-- md:samp ItemStackRequestPacket -->

> 文档版本：r/20_u7<br/>协议版本：662

<!-- md:samp ItemStackRequestPacket -->数据包，数字ID是`147`。

## 结构

```viz
digraph ItemStackRequestPacket {
	graph [rankdir=LR];
	{
		graph [rank=max];
		3	[comment="name: \"unsigned varint\", typeName: \"\", id: 3, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label="unsigned varint"];
		6	[comment="name: \"TypedClientNetId<struct ItemStackRequestIdTag,int,0>\", typeName: \"\", id: 6, branchId: 0, recurseId: -1, attributes: 512, \
notes: \"\"",
			label="TypedClientNetId<struct ItemStackRequestIdTag,int,0>"];
		9	[comment="name: \"unsigned varint\", typeName: \"\", id: 9, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label="unsigned varint"];
		12	[comment="name: \"byte\", typeName: \"\", id: 12, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=byte];
		14	[comment="name: \"byte\", typeName: \"\", id: 14, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=byte];
		16	[comment="name: \"ItemStackRequestSlotInfo\", typeName: \"\", id: 16, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=ItemStackRequestSlotInfo];
		18	[comment="name: \"ItemStackRequestSlotInfo\", typeName: \"\", id: 18, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=ItemStackRequestSlotInfo];
		21	[comment="name: \"unsigned varint\", typeName: \"\", id: 21, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label="unsigned varint"];
		24	[comment="name: \"string\", typeName: \"\", id: 24, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=string];
		26	[comment="name: \"int\", typeName: \"\", id: 26, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=int];
	}
	0	[comment="name: \"ItemStackRequestPacket\", typeName: \"\", id: 0, branchId: 147, recurseId: -1, attributes: 0, notes: \"\"",
		label=ItemStackRequestPacket];
	1	[comment="name: \"Requests\", typeName: \"\", id: 1, branchId: 0, recurseId: -1, attributes: 8, notes: \"\"",
		label=Requests];
	0 -> 1;
	2	[comment="name: \"Array Size\", typeName: \"\", id: 2, branchId: 0, recurseId: -1, attributes: 0, notes: \"\"",
		label="Array Size"];
	1 -> 2;
	4	[comment="name: \"example element\", typeName: \"\", id: 4, branchId: 0, recurseId: -1, attributes: 16, notes: \"\"",
		label="example element",
		style=dotted];
	1 -> 4;
	2 -> 3;
	5	[comment="name: \"Client Request Id\", typeName: \"TypedClientNetId<struct ItemStackRequestIdTag,int,0>\", id: 5, branchId: 0, recurseId: -1, \
attributes: 256, notes: \"\"",
		label="Client Request Id"];
	4 -> 5;
	7	[comment="name: \"Actions\", typeName: \"\", id: 7, branchId: 0, recurseId: -1, attributes: 8, notes: \"There are a variety of possible actions \
each with their own schema; this (Take) is just one example. Refer to the Item Stack Net Manager documentation.\"",
		label=Actions];
	4 -> 7;
	19	[comment="name: \"Strings To Filter\", typeName: \"\", id: 19, branchId: 0, recurseId: -1, attributes: 8, notes: \"Array of strings to submit to \
profanity filtering service\"",
		label="Strings To Filter"];
	4 -> 19;
	25	[comment="name: \"StringsToFilterOrigin\", typeName: \"\", id: 25, branchId: 0, recurseId: -1, attributes: 0, notes: \"enumeration: TextProcessingEventOrigin\"",
		label=StringsToFilterOrigin];
	4 -> 25;
	5 -> 6;
	8	[comment="name: \"Array Size\", typeName: \"\", id: 8, branchId: 0, recurseId: -1, attributes: 0, notes: \"\"",
		label="Array Size"];
	7 -> 8;
	10	[comment="name: \"example element\", typeName: \"\", id: 10, branchId: 0, recurseId: -1, attributes: 16, notes: \"\"",
		label="example element",
		style=dotted];
	7 -> 10;
	8 -> 9;
	11	[comment="name: \"Action type\", typeName: \"\", id: 11, branchId: 0, recurseId: -1, attributes: 0, notes: \"enumeration: ItemStackRequestActionType\"",
		label="Action type"];
	10 -> 11;
	13	[comment="name: \"Amount\", typeName: \"\", id: 13, branchId: 0, recurseId: -1, attributes: 0, notes: \"\"",
		label=Amount];
	10 -> 13;
	15	[comment="name: \"Source\", typeName: \"ItemStackRequestSlotInfo\", id: 15, branchId: 0, recurseId: -1, attributes: 256, notes: \"\"",
		label=Source];
	10 -> 15;
	17	[comment="name: \"Destination\", typeName: \"ItemStackRequestSlotInfo\", id: 17, branchId: 0, recurseId: -1, attributes: 256, notes: \"\"",
		label=Destination];
	10 -> 17;
	11 -> 12;
	13 -> 14;
	15 -> 16;
	17 -> 18;
	20	[comment="name: \"Array Size\", typeName: \"\", id: 20, branchId: 0, recurseId: -1, attributes: 0, notes: \"\"",
		label="Array Size"];
	19 -> 20;
	22	[comment="name: \"example element\", typeName: \"\", id: 22, branchId: 0, recurseId: -1, attributes: 16, notes: \"\"",
		label="example element",
		style=dotted];
	19 -> 22;
	20 -> 21;
	23	[comment="name: \"String To Filter\", typeName: \"\", id: 23, branchId: 0, recurseId: -1, attributes: 0, notes: \"Indivdiual string that needs \
checking\"",
		label="String To Filter"];
	22 -> 23;
	23 -> 24;
	25 -> 26;
}

```

## 字段

/// define
ItemStackRequestPacket

Requests

Requests数组的大小：<!-- md:samp unsigned varint -->

- 类型：unsigned varint。

Requests的示例元素

Client Request Id：[<!-- md:samp TypedClientNetId<struct ItemStackRequestIdTag,int,0> -->](refs/protocols/types/typedclientnetid<struct_itemstackrequestidtag,int,0>.md)

- 类型：TypedClientNetId<struct ItemStackRequestIdTag,int,0>。

Actions

Actions数组的大小：<!-- md:samp unsigned varint -->

- 类型：unsigned varint。

Actions的示例元素

Action type：<!-- md:samp byte -->

- 类型：byte。enumeration: ItemStackRequestActionType

Amount：<!-- md:samp byte -->

- 类型：byte。

Source：[<!-- md:samp ItemStackRequestSlotInfo -->](refs/protocols/types/itemstackrequestslotinfo.md)

- 类型：ItemStackRequestSlotInfo。

Destination：[<!-- md:samp ItemStackRequestSlotInfo -->](refs/protocols/types/itemstackrequestslotinfo.md)

- 类型：ItemStackRequestSlotInfo。

Strings To Filter

Strings To Filter数组的大小：<!-- md:samp unsigned varint -->

- 类型：unsigned varint。

Strings To Filter的示例元素

String To Filter：<!-- md:samp string -->

- 类型：string。Indivdiual string that needs checking

StringsToFilterOrigin：<!-- md:samp int -->

- 类型：int。enumeration: TextProcessingEventOrigin


///
