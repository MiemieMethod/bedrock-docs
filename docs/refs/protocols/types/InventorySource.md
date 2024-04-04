# <!-- md:samp InventorySource -->

> 文档版本：r/20_u7<br/>协议版本：662

<!-- md:samp InventorySource -->类型。

## 结构

```dot
digraph InventorySource {
	graph [rankdir=LR];
	{
		graph [rank=max];
		32	[comment="name: \"unsigned varint\", typeName: \"\", id: 32, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label="unsigned varint"];
		36	[comment="name: \"varint\", typeName: \"\", id: 36, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=varint];
		38	[comment="name: \"[No Data]\", typeName: \"\", id: 38, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label="[No Data]"];
		41	[comment="name: \"unsigned varint\", typeName: \"\", id: 41, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label="unsigned varint"];
		43	[comment="name: \"[No Data]\", typeName: \"\", id: 43, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label="[No Data]"];
	}
	30	[comment="name: \"InventorySource\", typeName: \"\", id: 30, branchId: 0, recurseId: -1, attributes: 0, notes: \"\"",
		label=InventorySource];
	31	[comment="name: \"Source Type\", typeName: \"\", id: 31, branchId: 0, recurseId: -1, attributes: 0, notes: \"enumeration: InventorySourceType\"",
		label="Source Type"];
	30 -> 31;
	33	[comment="name: \"Dependency on 'Source Type'\", typeName: \"\", id: 33, branchId: 0, recurseId: -1, attributes: 2, notes: \"\"",
		label="Dependency on 'Source Type'",
		shape=note];
	30 -> 33;
	31 -> 32;
	34	[comment="name: \"if (0)\", typeName: \"\", id: 34, branchId: 0, recurseId: -1, attributes: 4, notes: \"\"",
		label="if (0)",
		shape=diamond];
	33 -> 34;
	37	[comment="name: \"if (1)\", typeName: \"\", id: 37, branchId: 1, recurseId: -1, attributes: 4, notes: \"\"",
		label="if (1)",
		shape=diamond];
	33 -> 37;
	39	[comment="name: \"if (2)\", typeName: \"\", id: 39, branchId: 2, recurseId: -1, attributes: 4, notes: \"\"",
		label="if (2)",
		shape=diamond];
	33 -> 39;
	42	[comment="name: \"if (3)\", typeName: \"\", id: 42, branchId: 3, recurseId: -1, attributes: 4, notes: \"\"",
		label="if (3)",
		shape=diamond];
	33 -> 42;
	35	[comment="name: \"Container ID\", typeName: \"\", id: 35, branchId: 0, recurseId: -1, attributes: 0, notes: \"enumeration: ContainerID\"",
		label="Container ID"];
	34 -> 35;
	35 -> 36;
	37 -> 38;
	40	[comment="name: \"Bit Flags\", typeName: \"\", id: 40, branchId: 0, recurseId: -1, attributes: 0, notes: \"enumeration: InventorySource::InventorySourceFlags\"",
		label="Bit Flags"];
	39 -> 40;
	40 -> 41;
	42 -> 43;
}

```

## 字段

/// define
InventorySource

Source Type：<!-- md:samp unsigned varint -->

- 类型：unsigned varint。enumeration: InventorySourceType

Dependency on 'Source Type'

//// tab | if (0)
///// define
if (0)

Container ID：<!-- md:samp varint -->

- 类型：varint。enumeration: ContainerID


/////

////

//// tab | if (1)
///// define
if (1)：<!-- md:samp [No Data] -->

- 类型：[No Data]。


/////

////

//// tab | if (2)
///// define
if (2)

Bit Flags：<!-- md:samp unsigned varint -->

- 类型：unsigned varint。enumeration: InventorySource::InventorySourceFlags


/////

////

//// tab | if (3)
///// define
if (3)：<!-- md:samp [No Data] -->

- 类型：[No Data]。


/////

////



///
