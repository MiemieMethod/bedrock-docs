# <!-- md:samp MapItemTrackedActor::UniqueId -->

> 文档版本：r/20_u7<br/>协议版本：662

<!-- md:samp MapItemTrackedActor::UniqueId -->类型。

## 结构

```viz
digraph "MapItemTrackedActor::UniqueId" {
	graph [rankdir=LR];
	{
		graph [rank=max];
		44	[comment="name: \"int\", typeName: \"\", id: 44, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=int];
		48	[comment="name: \"ActorUniqueID\", typeName: \"\", id: 48, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=ActorUniqueID];
		51	[comment="name: \"NetworkBlockPosition\", typeName: \"\", id: 51, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=NetworkBlockPosition];
		53	[comment="name: \"[No Data]\", typeName: \"\", id: 53, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label="[No Data]"];
	}
	42	[comment="name: \"MapItemTrackedActor::UniqueId\", typeName: \"\", id: 42, branchId: 0, recurseId: -1, attributes: 0, notes: \"\"",
		label="MapItemTrackedActor::UniqueId"];
	43	[comment="name: \"Type\", typeName: \"\", id: 43, branchId: 0, recurseId: -1, attributes: 0, notes: \"enumeration: MapItemTrackedActor::Type\"",
		label=Type];
	42 -> 43;
	45	[comment="name: \"Dependency on 'Type'\", typeName: \"\", id: 45, branchId: 0, recurseId: -1, attributes: 2, notes: \"\"",
		label="Dependency on 'Type'",
		shape=note];
	42 -> 45;
	43 -> 44;
	46	[comment="name: \"if (0)\", typeName: \"\", id: 46, branchId: 0, recurseId: -1, attributes: 4, notes: \"\"",
		label="if (0)",
		shape=diamond];
	45 -> 46;
	49	[comment="name: \"if (1)\", typeName: \"\", id: 49, branchId: 1, recurseId: -1, attributes: 4, notes: \"\"",
		label="if (1)",
		shape=diamond];
	45 -> 49;
	52	[comment="name: \"if (2)\", typeName: \"\", id: 52, branchId: 2, recurseId: -1, attributes: 4, notes: \"\"",
		label="if (2)",
		shape=diamond];
	45 -> 52;
	47	[comment="name: \"Unique ID\", typeName: \"ActorUniqueID\", id: 47, branchId: 0, recurseId: -1, attributes: 256, notes: \"\"",
		label="Unique ID"];
	46 -> 47;
	47 -> 48;
	50	[comment="name: \"Block position\", typeName: \"NetworkBlockPosition\", id: 50, branchId: 0, recurseId: -1, attributes: 256, notes: \"\"",
		label="Block position"];
	49 -> 50;
	50 -> 51;
	52 -> 53;
}

```

## 字段

/// define
MapItemTrackedActor::UniqueId

Type：<!-- md:samp int -->

- 类型：int。enumeration: MapItemTrackedActor::Type

Dependency on 'Type'

//// tab | if (0)
///// define
if (0)

Unique ID：[<!-- md:samp ActorUniqueID -->](refs/protocols/types/actoruniqueid.md)

- 类型：ActorUniqueID。


/////

////

//// tab | if (1)
///// define
if (1)

Block position：[<!-- md:samp NetworkBlockPosition -->](refs/protocols/types/networkblockposition.md)

- 类型：NetworkBlockPosition。


/////

////

//// tab | if (2)
///// define
if (2)：<!-- md:samp [No Data] -->

- 类型：[No Data]。


/////

////



///
