# <!-- md:samp ItemStackResponseInfo -->

> 文档版本：r/20_u7<br/>协议版本：662

<!-- md:samp ItemStackResponseInfo -->类型。

## 结构

```viz
digraph ItemStackResponseInfo {
	graph [rankdir=LR];
	{
		graph [rank=max];
		8	[comment="name: \"byte\", typeName: \"\", id: 8, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=byte];
		10	[comment="name: \"TypedClientNetId<struct ItemStackRequestIdTag,int,0>\", typeName: \"\", id: 10, branchId: 0, recurseId: -1, attributes: 512, \
notes: \"\"",
			label="TypedClientNetId<struct ItemStackRequestIdTag,int,0>"];
		15	[comment="name: \"unsigned varint\", typeName: \"\", id: 15, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label="unsigned varint"];
		43	[comment="name: \"ItemStackResponseContainerInfo\", typeName: \"\", id: 43, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=ItemStackResponseContainerInfo];
		45	[comment="name: \"[No Data]\", typeName: \"\", id: 45, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label="[No Data]"];
	}
	6	[comment="name: \"ItemStackResponseInfo\", typeName: \"\", id: 6, branchId: 0, recurseId: -1, attributes: 0, notes: \"\"",
		label=ItemStackResponseInfo];
	7	[comment="name: \"Result\", typeName: \"\", id: 7, branchId: 0, recurseId: -1, attributes: 0, notes: \"enumeration: ItemStackNetResult\"",
		label=Result];
	6 -> 7;
	9	[comment="name: \"Client Request Id\", typeName: \"TypedClientNetId<struct ItemStackRequestIdTag,int,0>\", id: 9, branchId: 0, recurseId: -1, \
attributes: 256, notes: \"\"",
		label="Client Request Id"];
	6 -> 9;
	11	[comment="name: \"Dependency on 'ItemStackNetResult'\", typeName: \"\", id: 11, branchId: 0, recurseId: -1, attributes: 2, notes: \"\"",
		label="Dependency on 'ItemStackNetResult'",
		shape=note];
	6 -> 11;
	7 -> 8;
	9 -> 10;
	12	[comment="name: \"if (0)\", typeName: \"\", id: 12, branchId: 0, recurseId: -1, attributes: 4, notes: \"\"",
		label="if (0)",
		shape=diamond];
	11 -> 12;
	44	[comment="name: \"if (1)\", typeName: \"\", id: 44, branchId: 1, recurseId: -1, attributes: 4, notes: \"\"",
		label="if (1)",
		shape=diamond];
	11 -> 44;
	13	[comment="name: \"Containers\", typeName: \"\", id: 13, branchId: 0, recurseId: -1, attributes: 8, notes: \"\"",
		label=Containers];
	12 -> 13;
	14	[comment="name: \"Array Size\", typeName: \"\", id: 14, branchId: 0, recurseId: -1, attributes: 0, notes: \"\"",
		label="Array Size"];
	13 -> 14;
	16	[comment="name: \"example element\", typeName: \"\", id: 16, branchId: 0, recurseId: -1, attributes: 16, notes: \"\"",
		label="example element",
		style=dotted];
	13 -> 16;
	14 -> 15;
	17	[comment="name: \"Container Info\", typeName: \"ItemStackResponseContainerInfo\", id: 17, branchId: 0, recurseId: -1, attributes: 256, notes: \"\"",
		label="Container Info"];
	16 -> 17;
	17 -> 43;
	44 -> 45;
}

```

## 字段

/// define
ItemStackResponseInfo

Result：<!-- md:samp byte -->

- 类型：byte。enumeration: ItemStackNetResult

Client Request Id：[<!-- md:samp TypedClientNetId<struct ItemStackRequestIdTag,int,0> -->](refs/protocols/types/typedclientnetid<struct_itemstackrequestidtag,int,0>.md)

- 类型：TypedClientNetId<struct ItemStackRequestIdTag,int,0>。

Dependency on 'ItemStackNetResult'

//// tab | if (0)
///// define
if (0)

Containers

Containers数组的大小：<!-- md:samp unsigned varint -->

- 类型：unsigned varint。

Containers的示例元素

Container Info：[<!-- md:samp ItemStackResponseContainerInfo -->](refs/protocols/types/itemstackresponsecontainerinfo.md)

- 类型：ItemStackResponseContainerInfo。


/////

////

//// tab | if (1)
///// define
if (1)：<!-- md:samp [No Data] -->

- 类型：[No Data]。


/////

////



///
