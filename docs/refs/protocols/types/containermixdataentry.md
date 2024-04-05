# <!-- md:samp ContainerMixDataEntry -->

> 文档版本：r/20_u7<br/>协议版本：662

<!-- md:samp ContainerMixDataEntry -->类型。

## 结构

```viz
digraph ContainerMixDataEntry {
	graph [rankdir=LR];
	{
		graph [rank=max];
		33	[comment="name: \"varint\", typeName: \"\", id: 33, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=varint];
		35	[comment="name: \"varint\", typeName: \"\", id: 35, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=varint];
		37	[comment="name: \"varint\", typeName: \"\", id: 37, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=varint];
	}
	31	[comment="name: \"ContainerMixDataEntry\", typeName: \"\", id: 31, branchId: 0, recurseId: -1, attributes: 0, notes: \"\"",
		label=ContainerMixDataEntry];
	32	[comment="name: \"From Item (Id): Input\", typeName: \"\", id: 32, branchId: 0, recurseId: -1, attributes: 0, notes: \"\"",
		label="From Item (Id): Input"];
	31 -> 32;
	34	[comment="name: \"Re-agent Item Id\", typeName: \"\", id: 34, branchId: 0, recurseId: -1, attributes: 0, notes: \"\"",
		label="Re-agent Item Id"];
	31 -> 34;
	36	[comment="name: \"To Item (Id): Output\", typeName: \"\", id: 36, branchId: 0, recurseId: -1, attributes: 0, notes: \"\"",
		label="To Item (Id): Output"];
	31 -> 36;
	32 -> 33;
	34 -> 35;
	36 -> 37;
}

```

## 字段

/// define
ContainerMixDataEntry

From Item (Id): Input：<!-- md:samp varint -->

- 类型：varint。

Re-agent Item Id：<!-- md:samp varint -->

- 类型：varint。

To Item (Id): Output：<!-- md:samp varint -->

- 类型：varint。


///
