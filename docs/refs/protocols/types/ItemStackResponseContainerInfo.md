# <!-- md:samp ItemStackResponseContainerInfo -->

> 文档版本：r/20_u7<br/>协议版本：662

<!-- md:samp ItemStackResponseContainerInfo -->类型。

## 结构

```viz
digraph ItemStackResponseContainerInfo {
	graph [rankdir=LR];
	{
		graph [rank=max];
		20	[comment="name: \"byte\", typeName: \"\", id: 20, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=byte];
		23	[comment="name: \"unsigned varint\", typeName: \"\", id: 23, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label="unsigned varint"];
		42	[comment="name: \"ItemStackResponseSlotInfo\", typeName: \"\", id: 42, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=ItemStackResponseSlotInfo];
	}
	18	[comment="name: \"ItemStackResponseContainerInfo\", typeName: \"\", id: 18, branchId: 0, recurseId: -1, attributes: 0, notes: \"\"",
		label=ItemStackResponseContainerInfo];
	19	[comment="name: \"Open Container Net Id\", typeName: \"\", id: 19, branchId: 0, recurseId: -1, attributes: 0, notes: \"\"",
		label="Open Container Net Id"];
	18 -> 19;
	21	[comment="name: \"Slots\", typeName: \"\", id: 21, branchId: 0, recurseId: -1, attributes: 8, notes: \"\"",
		label=Slots];
	18 -> 21;
	19 -> 20;
	22	[comment="name: \"Array Size\", typeName: \"\", id: 22, branchId: 0, recurseId: -1, attributes: 0, notes: \"\"",
		label="Array Size"];
	21 -> 22;
	24	[comment="name: \"example element\", typeName: \"\", id: 24, branchId: 0, recurseId: -1, attributes: 16, notes: \"\"",
		label="example element",
		style=dotted];
	21 -> 24;
	22 -> 23;
	25	[comment="name: \"Slot Info\", typeName: \"ItemStackResponseSlotInfo\", id: 25, branchId: 0, recurseId: -1, attributes: 256, notes: \"\"",
		label="Slot Info"];
	24 -> 25;
	25 -> 42;
}

```

## 字段

/// define
ItemStackResponseContainerInfo

Open Container Net Id：<!-- md:samp byte -->

- 类型：byte。

Slots

Slots数组的大小：<!-- md:samp unsigned varint -->

- 类型：unsigned varint。

Slots的示例元素

Slot Info：[<!-- md:samp ItemStackResponseSlotInfo -->](refs/protocols/types/ItemStackResponseSlotInfo.md)

- 类型：ItemStackResponseSlotInfo。


///
